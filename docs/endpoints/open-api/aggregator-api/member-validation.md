# Member validation

## How to enable the member validation

To enable studio operators to add aggregator members to the  customer base,  offers two distinct possibilities:

1. Aggregators can register a HTTP endpoint that handles validation of aggregator members. This HTTP endpoint is called during the creation of a new  customer and is necessary to be able to assign an RFID medium to the aggregator member.
2. Aggregators can make a HTTP request to an OpenAPI endpoint that checks whether a customer has already been created with a specific aggregator Id. If not, we will create a light-weight aggregator customer profile in the  which can be found by studio personnel on the initial visit to assign the RFID medium to the customer.


Which ever one of these two options you choose, they are used to make sure that studio personnel only adds valid aggregator members to the  studios and that the chance for human error is limited.

Find all details regarding the two possible approaches and all its details and prerequisites below.

### Prerequisites

- Join the  Partner Program to start using  Open API
- The studio that you would like to interact with must have your integration activated
- Receive one API key for every studio you integrate with


### 1. Member validation HTTP endpoint

#### Implement a member validation endpoint on your side

Implement a simple HTTP endpoint that is publicly available and only allows HTTPS (TLS 1.2 or higher).  will call this endpoint for all studios that you have integrations with.

Every request from  to this endpoint will send an additional HTTP header named `X-API-Key`, which contains a unique token for every studio you integrated with.

The endpoint must only accept `POST` and respond with HTTP status code `200` if a requested member is allowed to register. In case the requested member is not allowed to register respond with `404`.

Information
We expect that member validation endpoint will respond in max. **750ms**. After that time we will cancel our request and treat it as undelivered

All requests from  are sent with the request header `Content-Type: application/json; charset=utf-8`. The payload is sent via `POST` with the `Json` in the body:


```json
{
  "aggregatorId": "<your-id>" 
}
```

If the aggregator member is validated on your system,  requires basic member data in the `200` response. In case you use time limited identifiers to validate your members, you can pass a more permanent `aggregatorId` in the `200` response.

Please keep in mind that this `aggregatorId` will be used for all checkin validation calls from the .

Sample `200` response:


```json
{
  "aggregatorId": "<your-id>",
  "firstName": "Edgar",
  "lastName": "Bullock",
  "dateOfBirth": "1952-05-04",
  "email": "example@email.com",
  "gender": "MALE",
  "street": "Am Bahnhof",
  "houseNumber": "89",
  "zipCode": "12133",
  "city": "Angermünde",
  "country": "DE",
  "phonePrivate": "+4930901820",
  "phonePrivateMobile": "+4915223433333",
  "phoneBusiness": "+4930901820",
  "phoneBusinessMobile": "+4915223433333"
}
```

### Register your member validation endpoint

Send your endpoint URL (e.g. (https://api.aggregator.example.com/member-validation)) to .

### 2. Endpoint for automatic aggregator customer creation via HTTP request

If you have the functionality of enforcing check-in or booking events in your own application, you can opt for a more automatized approach to creating an aggregator customer profile in the .
The creation flow will then look as follows:

- your members check-in or book attendance in your application
- this event is used as a trigger to POST their member profile to the POST [aggregators/members endpoint](aggregator/other/createaggregatormember)
- this endpoint will check whether this member profile already exists as a customer in the . If it does not, we will create a lightweight customer profile that studio personnel can easily find upon the initial visit and assign a RFID medium if necessary


You can find details of this POST endpoint [here](aggregator/other/createaggregatormember).