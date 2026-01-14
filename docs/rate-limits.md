# Rate Limits

Magicline APIs enforce rate limits to protect service stability.
Rate limits can differ between Open-API and Connect API and may vary per tenant.

Clients must implement backoff and retry handling for `429` responses.

---

### How Rate Limiting Works

When the limit is exceeded, the API responds with:

- **HTTP 429** `Too Many Requests`
- An error envelope with an appropriate error code (commonly `RATE_LIMITED`)

Example:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests"
  }
}
```

---

### Rate Limit Headers
Magicline may include rate limit metadata via response headers:
| Header                  | Description                                |
| ----------------------- | ------------------------------------------ |
| `X-RateLimit-Limit`     | Maximum requests per window                |
| `X-RateLimit-Remaining` | Requests left in current window            |
| `X-RateLimit-Reset`     | Timestamp (seconds) when the window resets |
| `Retry-After`           | Seconds to wait before retrying            |
Not all endpoints return all headers.
If Retry-After is present, it must be treated as authoritative.

---

### Client Strategy
1) Respect Retry-After

If the server returns Retry-After, wait at least that many seconds before retrying.

2) Exponential Backoff

If no Retry-After header exists, use exponential backoff:

- attempt 1: 500ms
- attempt 2: 1000ms
- attempt 3: 2000ms
- stop after 3 retries.

3) Jitter

Add small random jitter (±10–20%) to avoid thundering-herd issues in parallel clients.

---

### Recommended Defaults
| Property       | Value                   |
| -------------- | ----------------------- |
| Max retries    | 3                       |
| Initial delay  | 500ms                   |
| Backoff factor | 2x                      |
| Max delay      | 5s                      |
| Parallelism    | keep low (avoid bursts) |

---

### Example Retry Logic (TypeScript)
```typescript
function sleep(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

function jitter(ms: number) {
  const delta = ms * 0.2;
  return ms - delta + Math.random() * delta * 2;
}

export async function withRetries<T>(fn: () => Promise<T>): Promise<T> {
  let delay = 500;

  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      return await fn();
    } catch (err: any) {
      const status = err?.status ?? err?.response?.status;
      const retryAfterHeader = err?.response?.headers?.["retry-after"];

      const retryable = status === 429 || (status >= 500 && status <= 599);
      if (!retryable || attempt === 3) throw err;

      if (retryAfterHeader) {
        const seconds = Number(retryAfterHeader);
        if (!Number.isNaN(seconds) && seconds > 0) {
          await sleep(seconds * 1000);
          continue;
        }
      }

      await sleep(jitter(delay));
      delay = Math.min(delay * 2, 5000);
    }
  }

  // unreachable
  throw new Error("Retry loop failed unexpectedly");
}

```

---
### Frontend Considerations (Connect API)
Because the Connect API is public and can be called from browsers:

- Expect stricter limits per IP
- Avoid polling
- Prefer caching and debounced queries
- Batch requests where possible