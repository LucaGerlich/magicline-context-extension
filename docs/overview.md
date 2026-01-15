# API Overview

Magicline exposes two independent API surfaces:

- **Open-API** – secured backend API (API-key protected)
- **Connect API** – public, auth-free frontend API

They differ in authentication, data sensitivity, and intended usage.  
Never assume that conventions from one automatically apply to the other.

## Base URLs

| API         | Base URL |
| ----------- | -------- |
| Open-API    | https://{tenantname}.open-api.{environment}.magicline.com |
| Connect API | https://{tenantname}.api.{environment}.magicline.com |

---

## Environments

Magicline is provided in separate environments. Base URLs are environment-specific.

| Environment | Open-API Base URL | Connect API Base URL |
|-------------|-------------------|----------------------|
| Production  | See Magicline tenant config | See Magicline tenant config |
| Staging     | See Magicline tenant config | See Magicline tenant config |
| Development | See Magicline tenant config | See Magicline tenant config |

Base URLs are tenant-bound and must be provided by Magicline.

---

## API Versioning

Magicline APIs are versioned via the URL path:

/v1/
/v2/

Versioning is global and applies to both Open-API and Connect API.

Once an integration targets a version, it must not assume backward compatibility when upgrading.

---

## Transport

| Property | Value |
|--------|------|
| Protocol | HTTPS only |
| Encoding | UTF-8 |
| Content-Type | `application/json` |
| Timezone | UTC |
| Date format | ISO-8601 (`YYYY-MM-DDTHH:mm:ssZ`) |

---

## Common Request Headers

### Open-API

| Header | Required | Description |
|------|---------|-------------|
| `X-API-KEY` | Yes | Static API key |
| `Content-Type` | Yes | `application/json` |
| `Accept` | Recommended | `application/json` |

### Connect API

| Header | Required | Description |
|------|---------|-------------|
| `Content-Type` | Yes | `application/json` |
| `Accept` | Recommended | `application/json` |

---

## Response Envelope

All endpoints return JSON.  
Most endpoints use a common envelope pattern:

```json
{
  "success": true,
  "data": {},
  "error": null
}
{
  "success": false,
  "data": null,
  "error": {
    "code": "STRING_CODE",
    "message": "Human readable message"
  }
}
```

### HTTP Status Codes
| Code | Meaning                    |
| ---- | -------------------------- |
| 200  | Success                    |
| 201  | Resource created           |
| 400  | Validation error           |
| 401  | Unauthorized               |
| 403  | Forbidden                  |
| 404  | Not found                  |
| 409  | Conflict                   |
| 422  | Semantic validation failed |
| 429  | Rate limit exceeded        |
| 500  | Server error               |

---

### Idempotency

For endpoints that create or modify state, Magicline may support idempotent requests via an idempotency key header:
Idempotency-Key: <uuid>
If supported by the endpoint, repeated requests with the same key will not create duplicate resources.

Endpoint support must be verified in the endpoint documentation.

---

### Timeouts & Retries

| Property       | Recommendation              |
| -------------- | --------------------------- |
| Client timeout | 10–15 seconds               |
| Retry on       | 429, 5xx                    |
| Retry backoff  | Exponential, start at 500ms |
| Max retries    | 3                           |

---

### Data Sensitivity

| API         | Contains PII | Usage                   |
| ----------- | ------------ | ----------------------- |
| Open-API    | Yes          | Backend only            |
| Connect API | No           | Public frontend allowed |

Never expose Open-API responses directly to clients.