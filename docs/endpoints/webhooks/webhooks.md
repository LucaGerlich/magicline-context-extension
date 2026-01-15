# General Information

### What are webhooks

Webhooks enable  to push real-time notifications to your application.
We use HTTPS to send these notifications to a URL you specify.
You can then use these notifications to call specific endpoint on the  Open API.

### Use cases

You can use webhook event notifications to alert your app to certain events.

**Use Case 1 - Customer Checkin Event**

The customer check in event notifies your application once a customer has physically checked-in to a facility.

**Use Case 2 - Customer Created Event**

The customer created event notifies your application of any newly created customers within the  for facilities that have activated a third party integration.

### How to enable webhooks

Setting up your  webhooks requires just a few steps:

**Prerequisites**

- Join the  Partner Program to start using  Open API
- The studio that you would like to interact with must have your integration activated
- You have received a webhook API key as well as a  Open API key for each studio individually


#### 1. Serve webhook endpoint

Implement webhook endpoint according to our [definition](../webhooks/webhooks#operation/webhook). Serve this endpoint so that it can be accessed by us without additional configuration and/or VPNs.
Only HTTPS endpoints with valid SSL certificates are allowed. Timeout for requests to your endpoint is 5 seconds, after that requests will be treated as unsuccessful.

Information
For any unsuccessful webhook deliveries there is no retry.

#### 2. Register webhook endpoint URL

Specify your webhook endpoint URL (e.g. https://your.domain.com/webhook) at **@magicline.com**. By default we will send all webhook events to the provided URL. You can limit the amount of events you receive by specifying a set of event types. It is also possible to have different URLs per event type.

#### 3. Receive events

After we register your endpoint you will start receiving events. Validate webhook API key with the one provided during the  Open API integrations partner setup.

### Headers

The webhook request contains the following headers:

| Header | Description |
|  --- | --- |
| x-api-key | API key received by our team. Validate it and match with studio. |


### Delivery notifications

We expect that your Webhook endpoint will respond in max. **5000ms**. After that time we will cancel our request and treat it as undelivered.
In case of any error, Webhook request will be resend after **10 minutes**. We will try to send that request for a total of
**3 repeats**.

###How to work with our webhooks
The  webhooks are setup as notifiers without explicit payload data and require you to access the respective endpoints on the  Open API to get the most up to date information regarding the webhook event.

Sample JSON of a webhook call:


```json
{
  "entityId": 7893459,
  "uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
  "payload": [
    {
      "timestamp": 1642779144176,
      "type": "CUSTOMER_CREATED"
    }
  ]
}
```

Every webhook request has an `entityId` field which corresponds to the `type`.
Example: for the `CUSTOMER_CHECKIN` event, the entityId field will correspond to the `customerId`.
You can find the details of every `type` and the corresponding `entityId` field under the section .

Important
Please ignore any unknown properties in request body, as we might add them in next versions

Sequence diagram for `CUSTOMER_CREATED` event:

Important
As layed out in the diagram above, please do not make any requests to  OpenAPI during processing of the webhook.
Processing of webhooks must be **asynchronous**.