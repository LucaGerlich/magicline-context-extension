# Errors

Magicline APIs return structured error responses using a common error envelope.
Clients must not rely solely on HTTP status codes; the error object must always be evaluated.

---

## Error Envelope

All error responses follow this structure:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "STRING_CODE",
    "message": "Human readable description"
  }
}
```

---

## Error Codes
| Code                  | HTTP      | Meaning                          |
| --------------------- | --------- | -------------------------------- |
| `UNAUTHORIZED`        | 401       | Missing or invalid API key       |
| `FORBIDDEN`           | 403       | API key does not have permission |
| `NOT_FOUND`           | 404       | Resource not found               |
| `VALIDATION_FAILED`   | 400 / 422 | Request validation error         |
| `CONFLICT`            | 409       | State conflict                   |
| `RATE_LIMITED`        | 429       | Too many requests                |
| `INTERNAL_ERROR`      | 500       | Internal server error            |
| `SERVICE_UNAVAILABLE` | 503       | Temporary service outage         |

### Validation Errors
For validation failures, the error object may include a structured field list:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "One or more fields are invalid",
    "fields": [
      { "field": "email", "reason": "Invalid format" },
      { "field": "startDate", "reason": "Must be in the future" }
    ]
  }
}
```

### Client Behavior
| Error                   | Action                  |
| ----------------------- | ----------------------- |
| 400 / VALIDATION_FAILED | Fix payload and retry   |
| 401                     | Refresh / fix API key   |
| 403                     | Verify permissions      |
| 404                     | Verify IDs and routing  |
| 409                     | Re-read state and retry |
| 429                     | Retry with backoff      |
| 5xx                     | Retry with backoff      |

---

### Retry Policy
| Property      | Value       |
| ------------- | ----------- |
| Retry on      | 429, 5xx    |
| Backoff       | Exponential |
| Initial delay | 500 ms      |
| Max retries   | 3           |

---

### Logging Rules

- Never log full request bodies containing PII
- Log only error code, HTTP status, and correlation ID if present
- Redact all personal data