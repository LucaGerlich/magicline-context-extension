# Event call

Endpoint: POST /webhook
Security: ApiKeyAuth

## Request fields (application/json):

  - `entityId` (integer, required)
    Entity Id bounded to event
    Example: 7893459

  - `uuid` (string, required)
    Unique Event UUID

  - `payload` (array, required)
    Currently single element

  - `payload.timestamp` (integer, required)
    Milliseconds since Unix Epoch
    Example: 1642779144176

  - `payload.type` (string, required)
    Event type. See [event types](../../event-types) for details
    Example: "CUSTOMER_CREATED"

  - `payload.content` (object)
    Additional data specific for event. Currently placeholder for future more complex events. More information in [Event types](../../event-types) section.
    Example: {"field":"value"}
