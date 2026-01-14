# Magicline API Context

You are assisting with integrating against the Magicline API.
Local docs live in ./docs. Treat them as source of truth.

## Operating rules
- Do not invent endpoints, fields, auth headers, query params, or enums.
- If something is not explicitly stated in ./docs:
  - say "not found in local docs"
  - propose what to verify next (which doc file to check / what detail is missing)
- Always keep outputs implementation-ready (examples + payload shapes).

## What to output (default)
When asked to implement a feature, output in this order:
1) Get Context what you need to implement the feature and which data is needed to implement it.
2) Endpoint plan
   - endpoint(s)
   - method(s)
   - required headers
   - query/body parameters
   - pagination + filtering approach
3) Data contracts
   - TS types / interfaces for request + response
4) Example requests
   - curl example
   - Node.js/TypeScript example (fetch/axios)
5) Edge cases
   - error codes + retries/backoff
   - idempotency (if applicable)
   - rate limits (if defined)

## Conventions
- Base URL(s), environments: see docs/overview.md
- Auth scheme, token handling: see docs/auth.md
- Pagination: see docs/pagination.md
- Errors: see docs/errors.md
- Rate limits: see docs/rate-limits.md
- Naming conventions and common fields: see docs/conventions.md

## Security
- Never print real tokens or secrets.
- Use placeholders and environment variables in code examples.
- Avoid logging PII; redact user/member data in examples.

## Assumptions (only if docs are missing)
If local docs do not cover the topic, you may:
- describe multiple plausible options and explicitly label them as assumptions
- ask for the missing excerpt or file to be added to ./docs