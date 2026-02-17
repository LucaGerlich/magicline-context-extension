#!/usr/bin/env python3
"""
Sync Magicline Markdown documentation from the "View as Markdown" endpoints.

Features:
- Full sync of all reachable .md pages from one or more start URLs
- Refresh changed pages (ETag / Last-Modified + content hash tracking)
- Add new pages automatically
- Prune deleted/removed pages locally (files not present anymore or returning 404)
- Optional "changelog gate": only run full sync when changelog changed

By default this script writes into:
  references/vendor/magicline/

This directory is treated as FULLY MANAGED by this script.
Safe to prune there; do not place custom files in it.

Usage:
  pip install requests
  python scripts/sync_magicline_markdown.py

Common:
  python scripts/sync_magicline_markdown.py --check-changelog

Open API only:
  python scripts/sync_magicline_markdown.py --start https://developer.sportalliance.com/apis/magicline/openapi/openapi
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from collections import deque
from dataclasses import dataclass
from typing import Iterable, Optional
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_OUT_DIR = os.path.join("references", "vendor", "magicline")

DEFAULT_START_URLS = [
    "https://developer.sportalliance.com/apis/magicline/openapi/openapi",
    "https://developer.sportalliance.com/apis/magicline/connectapi/connectapi",
    "https://developer.sportalliance.com/apis/magicline/deviceapi/deviceapi",
]

ALLOWED_HOSTS_DEFAULT = {
    "redocly.sportalliance.com",
    "developer.sportalliance.com",
}

STATE_FILE_NAME = "_state.json"
MANIFEST_FILE_NAME = "_manifest.json"

# Markdown link patterns
# Inline: [text](target)
MD_INLINE_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# Reference def: [id]: target
MD_REF_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*([^\s]+)\s*$", re.MULTILINE)
# Raw URLs in text
RAW_URL_RE = re.compile(r"https?://[^\s)>\"]+")


@dataclass(frozen=True)
class PageResult:
    url: str
    status: str  # "saved" | "unchanged" | "missing" | "error"
    path: Optional[str] = None
    discovered: int = 0
    http_status: Optional[int] = None


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def normalize_url(url: str) -> str:
    """Drop query + fragment."""
    p = urlparse(url)
    return urlunparse((p.scheme, p.netloc, p.path, "", "", ""))


def to_markdown_url(url: str) -> str:
    """
    Convert developer.sportalliance.com HTML docs into redocly markdown endpoint.
    If already .md, return normalized.
    """
    url = normalize_url(url)
    p = urlparse(url)

    if not p.scheme:
        # Relative -> keep as-is; caller will urljoin with base
        return url

    # already markdown
    if p.path.lower().endswith(".md"):
        return url

    # dev portal -> redocly + append .md
    if p.netloc == "developer.sportalliance.com":
        new_path = p.path.rstrip("/") + ".md"
        return urlunparse((p.scheme, "redocly.sportalliance.com", new_path, "", "", ""))

    # redocly without .md -> append
    if p.netloc == "redocly.sportalliance.com":
        new_path = p.path.rstrip("/") + ".md"
        return urlunparse((p.scheme, p.netloc, new_path, "", "", ""))

    # best-effort
    new_path = p.path.rstrip("/") + ".md"
    return urlunparse((p.scheme, p.netloc, new_path, "", "", ""))


def is_probably_doc_link(target: str) -> bool:
    """
    Decide whether a markdown link target should be treated as a doc page.
    We want:
      - relative paths (no scheme) that look like docs
      - absolute http(s) links
    We skip:
      - mailto:, tel:, javascript:
      - images / assets (png, jpg, svg, etc.)
      - non-doc file types (yaml, json, etc.) unless you explicitly want them
    """
    t = target.strip()
    if not t:
        return False
    lower = t.lower()

    if lower.startswith(("mailto:", "tel:", "javascript:")):
        return False

    # Skip common assets
    if any(lower.endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf")):
        return False

    return True


def extract_links(markdown_text: str, base_url: str) -> set[str]:
    """
    Extract candidate doc links, normalize to markdown URLs when possible.
    """
    links: set[str] = set()

    def add_target(t: str) -> None:
        t = t.strip()
        if not is_probably_doc_link(t):
            return

        # remove surrounding <> if present
        if t.startswith("<") and t.endswith(">"):
            t = t[1:-1].strip()

        # strip fragment/query for crawling
        abs_url = t
        if not urlparse(t).scheme:
            abs_url = urljoin(base_url, t)

        abs_url = normalize_url(abs_url)

        # Convert to .md if it looks like a docs page
        if abs_url.endswith(".md"):
            links.add(abs_url)
        else:
            # Heuristic: treat same-doc pages without extension as markdown pages
            links.add(to_markdown_url(abs_url))

    for m in MD_INLINE_LINK_RE.findall(markdown_text):
        add_target(m)

    for m in MD_REF_DEF_RE.findall(markdown_text):
        add_target(m)

    for m in RAW_URL_RE.findall(markdown_text):
        add_target(m)

    return links


def build_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(
        {
            "User-Agent": "magicline-md-sync/1.0",
            "Accept": "text/markdown,text/plain;q=0.9,*/*;q=0.8",
        }
    )
    return session


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def load_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, obj: dict) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def url_to_local_path(out_dir: str, url: str) -> str:
    """
    Map URL path to local path under out_dir.

    Example:
      https://redocly.sportalliance.com/apis/magicline/openapi/openapi.md
    becomes:
      references/vendor/magicline/apis/magicline/openapi/openapi.md
    """
    p = urlparse(url)
    rel = p.path.lstrip("/")
    if not rel.endswith(".md"):
        rel = rel.rstrip("/") + ".md"
    return os.path.join(out_dir, rel)


def should_skip_by_changelog(
    session: requests.Session,
    state: dict,
    changelog_url: str,
    allowed_hosts: set[str],
    timeout: int,
) -> bool:
    """
    Fetch changelog and decide if sync can be skipped.
    Uses ETag / Last-Modified if available, plus content hash fallback.
    """
    changelog_url = to_markdown_url(changelog_url)
    p = urlparse(changelog_url)
    if p.netloc not in allowed_hosts:
        raise ValueError(f"Changelog host not allowed: {p.netloc}")

    headers = {}
    prev = (state.get("changelog") or {}).get(changelog_url) or {}
    if prev.get("etag"):
        headers["If-None-Match"] = prev["etag"]
    if prev.get("last_modified"):
        headers["If-Modified-Since"] = prev["last_modified"]

    resp = session.get(changelog_url, headers=headers, timeout=timeout)
    if resp.status_code == 304:
        return True

    if resp.status_code >= 400:
        # If changelog fails, do not skip; run full sync.
        return False

    text = resp.text
    new_hash = sha256_text(text)

    # store metadata
    state.setdefault("changelog", {})
    state["changelog"][changelog_url] = {
        "etag": resp.headers.get("ETag"),
        "last_modified": resp.headers.get("Last-Modified"),
        "sha256": new_hash,
        "checked_at": int(time.time()),
    }

    old_hash = prev.get("sha256")
    return old_hash == new_hash


def sync(
    start_urls: Iterable[str],
    out_dir: str,
    allowed_hosts: set[str],
    delay_s: float,
    timeout: int,
    max_pages: int,
    prune: bool,
    check_changelog: bool,
    changelog_url: Optional[str],
    dry_run: bool,
) -> list[PageResult]:
    ensure_dir(out_dir)

    state_path = os.path.join(out_dir, STATE_FILE_NAME)
    manifest_path = os.path.join(out_dir, MANIFEST_FILE_NAME)

    state = load_json(state_path)
    session = build_session()

    # Optional changelog gating
    if check_changelog and changelog_url:
        if should_skip_by_changelog(session, state, changelog_url, allowed_hosts, timeout):
            save_json(state_path, state)
            print("[SKIP] Changelog unchanged; skipping full sync.")
            return []

    queue = deque()
    for u in start_urls:
        mu = to_markdown_url(u)
        queue.append(mu)

    seen: set[str] = set()
    expected_files: set[str] = set()
    results: list[PageResult] = []

    # URL metadata cache in state
    state.setdefault("pages", {})

    while queue and len(seen) < max_pages:
        url = normalize_url(queue.popleft())
        if url in seen:
            continue

        p = urlparse(url)
        if p.netloc not in allowed_hosts:
            continue

        seen.add(url)

        # Conditional GET headers
        meta = state["pages"].get(url, {})
        headers = {}
        if meta.get("etag"):
            headers["If-None-Match"] = meta["etag"]
        if meta.get("last_modified"):
            headers["If-Modified-Since"] = meta["last_modified"]

        local_path = url_to_local_path(out_dir, url)
        expected_files.add(local_path)

        # Fetch
        try:
            resp = session.get(url, headers=headers, timeout=timeout)
        except Exception as e:
            results.append(PageResult(url=url, status="error", http_status=None))
            print(f"[ERR] {url}: {e}")
            continue

        if resp.status_code == 304:
            # unchanged; read local content for link extraction
            if os.path.exists(local_path):
                with open(local_path, "r", encoding="utf-8") as f:
                    text = f.read()
            else:
                # No local file but 304: treat as fetch needed
                resp = session.get(url, timeout=timeout)
                if resp.status_code >= 400:
                    results.append(PageResult(url=url, status="error", http_status=resp.status_code))
                    print(f"[ERR] {url}: HTTP {resp.status_code}")
                    continue
                text = resp.text

            links = extract_links(text, url)
            added = 0
            for link in links:
                lp = urlparse(link)
                if lp.netloc in allowed_hosts and link not in seen:
                    queue.append(link)
                    added += 1

            results.append(PageResult(url=url, status="unchanged", path=local_path, discovered=added, http_status=304))
            if delay_s:
                time.sleep(delay_s)
            continue

        if resp.status_code == 404:
            # If removed, delete local file
            if os.path.exists(local_path) and not dry_run:
                os.remove(local_path)
            results.append(PageResult(url=url, status="missing", path=local_path, discovered=0, http_status=404))
            # Remove from state
            state["pages"].pop(url, None)
            if delay_s:
                time.sleep(delay_s)
            continue

        if resp.status_code >= 400:
            results.append(PageResult(url=url, status="error", path=local_path, discovered=0, http_status=resp.status_code))
            print(f"[ERR] {url}: HTTP {resp.status_code}")
            if delay_s:
                time.sleep(delay_s)
            continue

        text = resp.text
        new_hash = sha256_text(text)

        old_hash = meta.get("sha256")
        changed = old_hash != new_hash or not os.path.exists(local_path)

        if changed and not dry_run:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, "w", encoding="utf-8") as f:
                f.write(text)

        # Update state meta
        state["pages"][url] = {
            "etag": resp.headers.get("ETag"),
            "last_modified": resp.headers.get("Last-Modified"),
            "sha256": new_hash,
            "saved_path": os.path.relpath(local_path, out_dir),
            "last_sync": int(time.time()),
        }

        links = extract_links(text, url)
        added = 0
        for link in links:
            lp = urlparse(link)
            if lp.netloc in allowed_hosts and link not in seen:
                queue.append(link)
                added += 1

        results.append(PageResult(url=url, status="saved" if changed else "unchanged", path=local_path, discovered=added, http_status=resp.status_code))
        print(f"[OK] {url} -> {local_path} ({'updated' if changed else 'no change'}, +{added})")

        if delay_s:
            time.sleep(delay_s)

    # Prune local files not in expected set
    if prune:
        removed = 0
        for root, _, files in os.walk(out_dir):
            for fn in files:
                if fn in (STATE_FILE_NAME, MANIFEST_FILE_NAME):
                    continue
                if not fn.lower().endswith(".md"):
                    continue
                path = os.path.join(root, fn)
                if path not in expected_files:
                    removed += 1
                    if not dry_run:
                        os.remove(path)

        if removed:
            print(f"[PRUNE] Removed {removed} stale markdown files.")

    # Write manifest for inspection/debugging
    manifest = {
        "synced_at": int(time.time()),
        "start_urls": [to_markdown_url(u) for u in start_urls],
        "pages_count": len(state.get("pages", {})),
        "notes": "This folder is managed by sync_magicline_markdown.py",
    }
    if not dry_run:
        save_json(state_path, state)
        save_json(manifest_path, manifest)

    return results


def main() -> None:
    ap = argparse.ArgumentParser(description="Sync Magicline Markdown docs (update/add/prune).")
    ap.add_argument("--out", default=DEFAULT_OUT_DIR, help=f"Managed output dir (default: {DEFAULT_OUT_DIR})")
    ap.add_argument("--start", nargs="*", default=DEFAULT_START_URLS, help="Start URLs (HTML or .md).")
    ap.add_argument("--hosts", nargs="*", default=list(ALLOWED_HOSTS_DEFAULT), help="Allowed hosts.")
    ap.add_argument("--delay", type=float, default=0.15, help="Delay between requests (seconds).")
    ap.add_argument("--timeout", type=int, default=25, help="HTTP timeout per request (seconds).")
    ap.add_argument("--max-pages", type=int, default=20000, help="Safety cap for number of pages.")
    ap.add_argument("--no-prune", action="store_true", help="Do not delete stale local files.")
    ap.add_argument("--dry-run", action="store_true", help="Do not write/delete files; only report actions.")

    ap.add_argument(
        "--check-changelog",
        action="store_true",
        help="If --changelog is provided: skip full sync when changelog is unchanged.",
    )
    ap.add_argument("--changelog", default=None, help="Changelog URL (HTML or .md).")

    args = ap.parse_args()

    results = sync(
        start_urls=args.start,
        out_dir=args.out,
        allowed_hosts=set(args.hosts),
        delay_s=args.delay,
        timeout=args.timeout,
        max_pages=args.max_pages,
        prune=not args.no_prune,
        check_changelog=args.check_changelog,
        changelog_url=args.changelog,
        dry_run=args.dry_run,
    )

    if not results:
        return

    # Summary
    saved = sum(1 for r in results if r.status == "saved")
    unchanged = sum(1 for r in results if r.status == "unchanged")
    missing = sum(1 for r in results if r.status == "missing")
    error = sum(1 for r in results if r.status == "error")
    print(f"\nSummary: updated={saved}, unchanged={unchanged}, missing={missing}, errors={error}")


if __name__ == "__main__":
    main()
