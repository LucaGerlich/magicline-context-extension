# General Information

The  Open API allows Third Party applications to access our data in a common and standardized manner.
You can use this API to get customers, contracts and other information.
We use OpenAPI 3.0. specifications for all our endpoints.

### Authentication

The  Open API uses persistent key authentication, separate for every studio in .
Keys are generated automatically when a studio owner requests an integration with your App.
Upon activation, you will receive an email with OpenAPI studio keys and the base URL.
In order to authenticate properly you have to send the OpenAPI key in `x-api-key` header.
We will validate the key and check whether it is valid and matches the current studio.

Information
If you have requested access to the  Open API and webhook functionality we will send two API Keys upon activation of your integration.
The API Keys are used for inbound requests to our endpoints and outbound requests of our webhook events.

#### HEAD requests

All `HEAD` requests are used solely to verify the validity of the provided `x-api-key`. They do not trigger any business logic and do not check the existence of the requested resource.
If the API key is valid, the response will be `200 OK`. If the API key is invalid or missing, the response will be `401 Unauthorized`.

### API requests

All API requests must be made over HTTPS. The   URL is the request base URL.
The complete URL varies depending on the accessed resource.

For example, to get a list of customers from a specific facility, you must make an HTTP GET request to
the   URL.

The base URL, including the `<tenant_name>`, is part of the activation email and must always match the corresponding `x-api-key`.
If you have registered webhooks you must look up the base URL by the [`x-api-key` header](../webhooks/general-information/#headers) you receive with every webhook event.

### Image handling

Please take into consideration that all URLs with an image to download will expire after a specified time. The exact expiration time can be found documented in the endpoint response field.

### Rate limit

All Open API endpoints have a rate limit.
Every endpoint has a separate request counter.
The default rate limit is 1000 requests per minute.
After exceeding the limit, every request for the next minute will be denied with a 429 response code.

### Service availability

The  Open API implements an adaptive query throttling mechanism to ensure system stability during periods of high database load.
When the database is under heavy load, certain endpoints may temporarily return a `503 Service Unavailable` response.
This is a protective measure to maintain overall system performance and data integrity.

If you receive a 503 response, we recommend implementing a retry strategy with exponential backoff.
The system will automatically recover once the database load decreases.

### Data chunking

Certain GET calls, especially bulk requests, may return a large number of records.
To make handling large payloads easier, we provide a way to control the maximum number of responses through data chunking.
There are two different ways this is achieved, explained below. But in short:
If you use the returned `offset` value from the response in your next request, you should always get continuous results.

In the first example, the`offset` reflects the exact `id` where the next chunk should start from. To fetch the next chunk use returned `offset` in succeeding request.
Last chunk is indicated by `hasNext: false` property value.
Example response:


```json
{
  "result": [
    {
      "id": 1210206595,
      "firstName": "Eduardo",
      "lastName": "Thomas"
    },
    {
      "id": 1210206596,
      "firstName": "Terrence",
      "lastName": "Hernandez"
    }
  ],
  "offset": "1210206596",
  "hasNext": true
}
```

In this example, the next chunk would be requested by calling `GET /endpoint?offset=1210206596`

The`offset` parameter can also be calculated as sum of the given`sliceSize` value and the last given `offset`,
reflecting an actual paginating of the results.
For example, if your request contains the `offset` `0` and a `sliceSize` of `2`, the returned `offset` will be `2`.
You may take this value for the next request (`offset` `2`, `sliceSize` `2`) to get the next chunk of results, with a returned offset of `4`, and so on.
Last chunk is indicated by `hasNext: false` property value.
Example for the first chunk with a `sliceSize` of `2`:


```json
{
  "result": [
    {
      "firstName": "Eduardo",
      "lastName": "Thomas"
    },
    {
      "firstName": "Terrence",
      "lastName": "Hernandez"
    }
  ],
  "offset": "2",
  "hasNext": true
}
```

In this example, the next chunk would be requested by calling `GET /endpoint?offset=2`

### Error Handling

The  Open API uses HTTP Status codes to reflect a successful or unsuccessful request.
2XX status codes represent a successful request, 4XX/5XX status codes represent an error.
If you receive an error status code, check the body for an error code and message.
Table of error codes:

| Http Code | Reason |
|  --- | --- |
| 400 | Validation of the request failed, check request with specification. |
| 401 | Authentication failed. Probably wrong or missing OpenAPI key. |
| 403 | Permission denied. The caller has no permission for the requested resource. |
| 404 | Requested entity not found. |
| 429 | Access denied - rate limit is exceeded. |
| 500 | Unexpected system error - internal problem. |


### Multipart/form-data requests

Some endpoints require a `multipart/form-data` request, meaning that the request body is a combination of json and binary data.
In this case, the content type of the request must be set to `multipart/form-data` and the json data request part must be of type `application/json`.
The binary data must be sent as a separate part of the request.
Here is a curl example of a `multipart/form-data` request (In this example the json data request part is called 'data' and the binary data request part is called `document`):

## Headers

### Header Accept-Language

The [Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language) header can be used to define the language that will be used for any (error-) messages in the responses. Currently these languages are supported by the :

- `cs` (Czech)
- `de` (German)
- `en` (English)
- `es` (Spanish)
- `fr` (French)
- `hu` (Hungarian)
- `it` (Italian)
- `nb` (Norwegian)
- `nl` (Dutch)
- `pl` (Polish)
- `ro` (Romanian)
- `ru` (Russian)
- `sl` (Slovenian)
- `sv` (Swedish)
- `tr` (Turkish)


Any other language not listed above, that are provided by the client using this header, will fall back to `en` (English). If this header is not provided at all by the client, the language of the studio configured in the  will be used. For some of the languages mentioned above the  has country specific variants:

- `de-CH` (Switzerland)
- `de-LI` (Liechtenstein)
- `en-CA` (Canada)
- `en-GB` (United Kingdom)
- `en-US` (USA)
- `fr-LU` (Luxembourg)


Any other country specific variants not listed above, that are provided by the client using this header, will fall back to the language. For example `de-LU` will result in `de` (German).