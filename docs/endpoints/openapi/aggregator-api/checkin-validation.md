# Checkin validation

## How to enable the check-in validation

To allow check-ins of gym-goers that don’t have a direct membership at a studio,  offers the possibility for
aggregators to register a HTTP endpoint that is being called to validate so-called guest check-ins.

This HTTP endpoint is being called during a regular check-in at a studio and must reply synchronously if the affected
gym-goer is allowed to enter the studio.

Find all details regarding on how to register the endpoint and all its details and prerequisites below here.

### Prerequisites

- Join the  Partner Program to start using  Open API
- The studio that you would like to interact with must have your integration activated
- Receive one API key for every studio you integrate with


### Check-in validation HTTP endpoint

#### Implement a check-in validation endpoint on your side

Implement a simple HTTP endpoint that is publicly available and only allows HTTPS (TLS 1.2 or higher).
 will call this endpoint for all studios that you have integrations with.

Every request from  to this endpoint will send an additional HTTP header named `X-API-Key`, which contains a
unique token for every studio you integrated with.

The endpoint must only accept `POST` and respond with HTTP status code `200` if a requested member is allowed to checkin.
In case the requested member is not allowed to check-in respond with `403`.

Information
We expect that check-in validation endpoint will respond in max. **750ms**. After that time we will cancel our request and treat it as undelivered

All requests from  are sent with the request header `Content-Type: application/json; charset=utf-8`. The
payload is sent via `POST` with the `json` in the body:


```json
{
  "aggregatorId": "<your-id>",
  "customerId": 293123213
}
```

Information
`customerId` is the unique  customer ID.

### Register your check-in validation endpoint

Send your endpoint URL (e.g. (https://api.aggregator.example.com/checkin-validation)) to .

### Receive check-in events

After we registered your endpoint you will start receiving events. Validate API key with the one provided during the
 Open API integrations partner setup.