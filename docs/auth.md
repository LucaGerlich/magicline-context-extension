# Authentication

Magicline provides two different API surfaces with different authentication models:

- **Open-API** (secured, API-key based, for member / contract / check-in / admin data)
- **Connect API** (auth-free, public, used for widget-style integrations and pre-login flows)

These APIs must be treated as separate security domains.

---

## Open-API (API-Key secured)

### Purpose

The Open-API is used for all authenticated, backend-to-backend integrations and provides access to sensitive business and member data.

Examples:
- Members
- Contracts
- Check-ins
- Bookings
- Invoices
- Payments
- Access logs

This API **requires an API key** on every request.

---

### Base URL

Defined per environment in `overview.md`.

---

### Authentication Method

Authentication is done via a static API key transmitted in an HTTP header.


This header must be present on **every Open-API request**.

---

### Example

```bash
curl -X GET https://api.magicline.example/v1/members/12345 \
  -H "X-API-KEY: $MAGICLINE_API_KEY"
```

### Key Properties

| Property      | Value                         |
| ------------- | ----------------------------- |
| Type          | Static API key                |
| Scope         | All Open-API endpoints        |
| Transport     | HTTP header `X-API-KEY`       |
| Rotation      | Manual (via Magicline admin)  |
| Expiry        | Does not expire automatically |
| Rate limiting | See `rate-limits.md`          |

### Security Rules

- Never embed the API key in frontend code
- Never expose the key in logs, URLs, or client-side bundles
- Always load from environment variables or secret managers
- Rotate immediately if leakage is suspected

---

## Connect API (Auth-free / Public)

### Purpose

The Connect API is designed for public and pre-login integrations where no Magicline authentication context exists yet.

Examples:
- Public club data
- Course schedules
- Trial signup widgets
- Pre-registration flows
- Public availability queries

These endpoints are intentionally unauthenticated and must be considered public internet APIs.

### Authentication Method

No authentication headers are required.

Requests are made directly without any credentials:

```bash
curl https://{{tenantname}}.api.magicline.com/connect/v1/courses
```

### Security Model

| Property      | Value                         |
| ------------- | ----------------------------- |
| Authentication	| None                          |
| Visibility	| Public internet               |
| Data sensitivity	| Non-personal, pre-login data only |
| Rate limiting	| See rate-limits.md            |

### Usage Rules

- Do not send personal or contract-bound data via Connect API
- Do not rely on Connect API for authorization decisions
- Use Connect API only for public discovery, not transactional operations

### Mixing APIs

| Use case                      | API         |
| ----------------------------- | ----------- |
| Fetch member profile          | Open-API    |
| Public course schedule        | Connect API |
| Check-in creation             | Open-API    |
| Trial signup page             | Connect API |
| Contract / billing operations | Open-API    |

Never mix authentication assumptions between the two.

### Implementation Checklist

- Backend uses Open-API with X-API-KEY
- Frontend uses Connect API without credentials
- Secrets stored in environment variables
- Public APIs treated as untrusted inputs

---

Next recommended file: `overview.md` (base URLs, environments, versioning, response envelope, global headers).
