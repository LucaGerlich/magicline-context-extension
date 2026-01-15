#!/usr/bin/env python3
"""
Download all Magicline API docs as Markdown by crawling the Redocly “View as Markdown” pages.

Works best when you start from the API root Markdown pages, e.g.
- https://redocly.sportalliance.com/apis/magicline/openapi/openapi.md
- https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi.md
- https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi.md

But you can also pass the normal HTML doc URLs from developer.sportalliance.com
and the script will convert them to the matching .md URL automatically.

Usage:
  pip install requests
  python download_magicline_markdown.py --out magicline-docs
"""

from __future__ import annotations

import argparse
import os
import re
import time
from collections import deque
from dataclasses import dataclass
from typing import Iterable
from urllib.parse import urljoin, urlparse, urlunparse

import requests


ALLOWED_HOSTS_DEFAULT = {
    "redocly.sportalliance.com",
    "developer.sportalliance.com",
}


MD_URL_RE = re.compile(r"https?://[^\s)]+?\.md(?:#[^\s)]*)?", re.IGNORECASE)
MD_REL_LINK_RE = re.compile(r"\(([^)]+?\.md(?:#[^)]+)?)\)", re.IGNORECASE)


@dataclass(frozen=True)
class CrawlResult:
    url: str
    saved_path: str
    discovered_links: int


def normalize_url(url: str) -> str:
    """Strip query/hash and normalize."""
    p = urlparse(url)
    # remove fragment + query
    return urlunparse((p.scheme, p.netloc, p.path, "", "", ""))


def to_markdown_url(url: str) -> str:
    """
    Convert developer.sportalliance.com HTML docs into the redocly markdown endpoint.
    If already .md, return normalized.
    """
    url = normalize_url(url)
    p = urlparse(url)

    # already markdown
    if p.path.lower().endswith(".md") and p.netloc:
        return url

    # If it's the dev portal, map to redocly host and append .md
    if p.netloc == "developer.sportalliance.com":
        new_path = p.path
        if not new_path.lower().endswith(".md"):
            new_path = new_path.rstrip("/") + ".md"
        return urlunparse((p.scheme, "redocly.sportalliance.com", new_path, "", "", ""))

    # If it's already redocly but missing .md, append it
    if p.netloc == "redocly.sportalliance.com" and not p.path.lower().endswith(".md"):
        new_path = p.path.rstrip("/") + ".md"
        return urlunparse((p.scheme, p.netloc, new_path, "", "", ""))

    # Default: if no extension, append .md (best-effort)
    if not p.path.lower().endswith(".md"):
        new_path = p.path.rstrip("/") + ".md"
        return urlunparse((p.scheme, p.netloc, new_path, "", "", ""))

    return url


def safe_local_path(out_dir: str, url: str) -> str:
    """
    Save files mirroring host + path:
      out_dir/redocly.sportalliance.com/apis/magicline/openapi/openapi.md
    """
    p = urlparse(url)
    rel = os.path.join(p.netloc, p.path.lstrip("/"))
    # avoid empty filenames
    if rel.endswith(os.sep) or rel.endswith("/"):
        rel = os.path.join(rel, "index.md")
    full = os.path.join(out_dir, rel)
    return full


def extract_markdown_links(markdown_text: str, base_url: str) -> set[str]:
    """
    Extract absolute + relative links to .md pages.
    """
    found: set[str] = set()

    # absolute URLs
    for m in MD_URL_RE.findall(markdown_text):
        found.add(normalize_url(m))

    # relative links inside ( ... )
    for m in MD_REL_LINK_RE.findall(markdown_text):
        abs_url = urljoin(base_url, m)
        found.add(normalize_url(abs_url))

    # normalize -> markdown urls (some might be html links without .md)
    normalized: set[str] = set()
    for u in found:
        normalized.add(to_markdown_url(u))

    return normalized


def ensure_dir_for_file(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)


def fetch(session: requests.Session, url: str, timeout: int = 20) -> str:
    r = session.get(url, timeout=timeout)
    r.raise_for_status()
    return r.text


def crawl(
    start_urls: Iterable[str],
    out_dir: str,
    allowed_hosts: set[str],
    delay_s: float = 0.2,
    max_pages: int = 20_000,
) -> list[CrawlResult]:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "magicline-md-downloader/1.0 (+local-docs-crawler)",
            "Accept": "text/plain,text/markdown,text/*;q=0.9,*/*;q=0.8",
        }
    )

    queue = deque(to_markdown_url(u) for u in start_urls)
    seen: set[str] = set()
    results: list[CrawlResult] = []

    while queue and len(seen) < max_pages:
        url = normalize_url(queue.popleft())
        if url in seen:
            continue

        p = urlparse(url)
        if p.netloc and p.netloc not in allowed_hosts:
            continue

        seen.add(url)

        try:
            text = fetch(session, url)
        except Exception as e:
            print(f"[WARN] Failed: {url} ({e})")
            continue

        local_path = safe_local_path(out_dir, url)
        ensure_dir_for_file(local_path)

        # Save
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(text)

        # Discover more .md links
        links = extract_markdown_links(text, url)
        added = 0
        for link in links:
            lp = urlparse(link)
            if lp.netloc and lp.netloc in allowed_hosts and link not in seen:
                queue.append(link)
                added += 1

        results.append(CrawlResult(url=url, saved_path=local_path, discovered_links=added))
        print(f"[OK] {url} -> {local_path} (+{added} links)")

        if delay_s > 0:
            time.sleep(delay_s)

    print(f"\nDone. Pages saved: {len(results)}")
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Download Magicline docs as Markdown by crawling Redocly .md pages.")
    parser.add_argument(
        "--out",
        default="magicline-docs",
        help="Output directory (default: magicline-docs)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="Delay between requests in seconds (default: 0.2)",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=20000,
        help="Safety cap for number of pages (default: 20000)",
    )
    parser.add_argument(
        "--start",
        nargs="*",
        default=[
            "https://developer.sportalliance.com/apis/magicline/openapi/openapi",
            "https://developer.sportalliance.com/apis/magicline/connectapi/connectapi",
            "https://developer.sportalliance.com/apis/magicline/deviceapi/deviceapi",
        ],
        help="Start URLs (HTML or .md). Defaults to the Magicline API roots.",
    )
    parser.add_argument(
        "--hosts",
        nargs="*",
        default=list(ALLOWED_HOSTS_DEFAULT),
        help="Allowed hosts to crawl (default: redocly.sportalliance.com developer.sportalliance.com)",
    )

    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)
    allowed_hosts = set(args.hosts)

    crawl(
        start_urls=args.start,
        out_dir=args.out,
        allowed_hosts=allowed_hosts,
        delay_s=args.delay,
        max_pages=args.max_pages,
    )


if __name__ == "__main__":
    main()

