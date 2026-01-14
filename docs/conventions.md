# Conventions

This file defines shared conventions across Magicline APIs so integrations stay consistent and predictable.

These conventions apply to both **Open-API** and **Connect API** unless an endpoint explicitly overrides them.

---

## Naming

### JSON field naming
Fields use **camelCase**:

- `firstName`
- `lastName`
- `createdAt`
- `magiclineId`

### IDs
IDs are typically represented as strings or numbers depending on the endpoint.
Do not assume UUIDs unless explicitly documented.

Recommended handling:
- treat all IDs as opaque strings in frontend + DTOs
- only cast to number if the endpoint explicitly guarantees numeric IDs

---

## Dates & Time

### Format
All timestamps are ISO-8601:

- `2026-01-14T21:30:00Z`

### Timezone
Timestamps must be interpreted as **UTC** unless documented otherwise.

### Date-only fields
When only a date is needed, it may appear as:

- `YYYY-MM-DD`

---

## Boolean fields

Booleans are returned as JSON booleans:

- `true` / `false`

Never assume `0/1` encoding.

---

## Sorting & Filtering

Collection endpoints commonly support:

- `sort`
- `order`
- filter query params (domain-specific)

Example pattern:

```http
GET /v1/members?sort=createdAt&order=desc
```

Rules:

- Do not assume filter param names; verify per endpoint.
- Prefer server-side filtering when available to avoid pulling large datasets.

---

## Pagination

Pagination is defined in pagination.md.

Always follow:

- page (1-based)
- limit

---

## Partial responses / includes

Some endpoints support including related entities via an include parameter.
Example pattern:

```http
GET /v1/members/{id}?include=contracts,tags
```

Rules:

- Only request includes you actually need.
- Treat included objects as optional in type definitions.

---

## Common Metadata Fields

Many resources include standard metadata:

| Field       | Meaning                          |
| ----------- | -------------------------------- |
| `createdAt` | Creation timestamp               |
| `updatedAt` | Last update timestamp            |
| `deletedAt` | Soft delete timestamp (nullable) |

If a field is nullable, represent it explicitly:

deletedAt: string | null;

---

## Success / Error Envelope

Responses use the standard envelope described in overview.md.

Rules:

Always check success === true before trusting data

On errors, data may be null

---

## Client-Side Caching

Recommended:

- Cache read-heavy endpoints (Connect API especially)
- Use a short TTL for public queries (e.g. 30–120 seconds)
- In backend integrations, cache static reference data (studios, categories) for minutes/hours

--- 

## Security & PII Handling

### PII fields

Member-related endpoints may include sensitive data such as:

- names
- email addresses
- phone numbers
- addresses
- birth dates

### Rules

- never log PII
- never store PII client-side unless required
- redact in debug output

---

## Error Handling

Error structure and retry guidance is documented in errors.md and rate-limits.md.

Rules:

- retry only on 429 and 5xx
- never retry validation errors without changing input

---

## Recommended TypeScript DTO Pattern

Define DTOs that mirror API payloads and keep domain models separate.

Example:

```typescript
export type ApiEnvelope<T> = {
  success: boolean;
  data: T | null;
  error: { code: string; message: string } | null;
};
```

---

## Defaults for Examples

Unless the user specifies otherwise:

- Use Node.js + TypeScript examples
- Use fetch (or undici) for HTTP calls
- Load X-API-KEY from process.env.MAGICLINE_API_KEY

