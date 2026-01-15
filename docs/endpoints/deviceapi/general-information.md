# General Information

The  Device API allows Third Party applications to access our data in a common and standardized manner.
You can use this API to get access to devices in .
We use OpenAPI 3.0. specifications for all our endpoints.

### Authentication

The  Device API uses persistent token authentication, separate for every device in .
Tokens are generated automatically when a studio owner creates a device in .
To receive the token you will have to

* Get started with [Open-API](../openapi/general-information)
  * This is necessary in further steps
* Register [webhooks](../webhooks/general-information)
  * Subscribe to websocket event type [DEVICE_CREATED](../webhooks/event-types) which will be executed every time
a new device is created in the
  * Map the  `deviceId` from the webhook to your corresponding, concrete device. Most likely in cooperation with the studio owner
* Call [activate](../openapi/openapi#operation/activateDevice) to activate device and receive the token
* If you want to check the state of devices you can call [getDevices](../openapi/openapi/devices#getDevices) to get
all devices


### API requests

All API requests must be made over HTTPS. The   URL is the request base
URL.
The complete URL varies depending on the accessed resource.

For example, to identify use on a device, you must make an HTTP POST request to
the   URL.

The `<tenant_name>` information is already mentioned [here](../openapi/general-information#api-requests).

## Access

In , each device requires configuration, which must be set up by studio operator.
There are multiple ways they can configure their devices, and this configuration has an
impact on the identification results. The identification process consists of two parts:
checks and actions. If there are no issues during the check part, the actions are executed.

### Checks

Checks are always executed when you call the identification endpoint.
This is the section where we check whether the customer is allowed to access the studio,
parking lot, rooms or use equipment. Multiple different checks are performed here
and if the customer is not allowed, you will receive an error with the description.

### Actions

Actions are executed only when the `shouldExecuteAction` variable is set to `true` upon calling the [identification endpoint](../deviceapi/deviceapi#cardReaderIdentification).
This is the section where the actual action is performed, for example the member is checked-in, the number of open slots on the parking lot is updated, contingents for access to rooms or equipments is booked, etc.

## Vending

In , each device requires configuration, which must be set up by studio operator.
There are multiple ways they can configure their devices, and this configuration has an
impact on the vending process. The vending process consists of two parts:
checks and actions. If there are no issues during the check part, the actions are executed.

Warning
Vending devices need concurrency control to prevent abuse. Therefore, when calling the
[identification endpoint](../deviceapi/deviceapi/vending#vendingIdentification) a `transactionId` needs to be provided which is
then used to lock the customer, so only the device with this `transactionId` is able to do any further operations for
this customer until the lock is released. The lock is released when either of the following happens:

* the [sale endpoint](../deviceapi/deviceapi#vendingSale) is called with `shouldExecuteAction` variable set to `true` which actually completes the vending process and the current transaction
* when the [timeout](#timeouts) of the device is reached
The `transactionId` needs to be provided for every vending endpoint as a UUID in 8-4-4-4-12 format, for example
`4671fde7-bb07-4fe5-aa0e-947d9ccb842f`


### Checks

This is the section where we check whether the customer is allowed to use vending devices in studio.
Multiple different checks are performed here and if the customer is not allowed, you will receive
an error with the description.

Checks are executed in two steps [identification](../deviceapi/deviceapi/vending#vendingIdentification) and [sale](../deviceapi/deviceapi#vendingSale).

#### Identification

This is the endpoint where we check whether the customer is allowed to use the vending device.
Multiple different checks are performed here and if the customer is not allowed, you will receive
an error with the description.

#### Sale

This is the endpoint where we check whether the customer is allowed to buy a specific product if dry-run (`shouldExecuteAction` is false) is active.
Multiple different checks are performed like payment option, product price.

### Actions

Actions are executed only when the `shouldExecuteAction` variable is set to `true` upon calling the [sale endpoint](../deviceapi/deviceapi#vendingSale).
This is the section where the actual action takes place. For instance, if a milkshake is sold, the customer is subsequently charged.

### Timeouts

There are two timeouts in place for vending process which should take care of stopping the transaction if customer does not finish the sale.
Both timeouts can be configured in  for every device.

Warning
Note that it's important to communicate with the studio operator regarding the desired duration of timeouts for your device.

#### Idle timeout

This timeout commences following [identification](../deviceapi/deviceapi/vending#vendingIdentification). For example, a user initiates vending by identifying themselves
on the reader and should subsequently proceed with product selection. However, should they walk away without completing the process,
the transaction will automatically be canceled after 15(configurable value) seconds. Following this period, the user can then use another device.

#### Product draw timeout

This timeout begins once the [sale endpoint](../deviceapi/deviceapi#vendingSale) is reached, with the `shouldExecuteAction` variable set to `false`.
For example, a user initiates vending by identifying themselves on the reader, following which they select a
product and confirm their selection. If the time between calling [sale endpoint](../deviceapi/deviceapi#vendingSale)
with the `shouldExecuteAction` variable set to `false`and [sale endpoint](../deviceapi/deviceapi#vendingSale) with
the `shouldExecuteAction` variable set to `true` takes longer than the configured
product draw timeout, the user is able to use another device. Once the sale is completed by calling the [sale endpoint](../deviceapi/deviceapi#vendingSale)
with `shouldExecuteAction` set to `true`, the transaction concludes, enabling the user to use a different device.

## Time

In , each device requires configuration, which must be set up by the studio operator.
There are multiple ways they can configure their devices, and this configuration has an
impact on the process. The process consists of two parts:
checks and actions. If there are no issues during the check part, the actions are executed.

### Checks

This is the section where we check whether the customer is allowed to use time devices in studio.
Multiple different checks are performed here and if the customer is not allowed, you will receive
an error with the description.

Checks are executed in two steps [identification](../deviceapi/deviceapi/vending#vendingIdentification) and [usage](../deviceapi/deviceapi#vendingUsage).

#### Identification

This is the endpoint where we check whether the customer is allowed to use the time device.
Multiple different checks are performed here and if the customer is not allowed, you will receive
an error with the description.

#### Usage

This is the endpoint where we check whether the customer is allowed to use a specific benefit if dry-run (`shouldExecuteAction` is false) is active.

### Actions

Actions are executed only when the `shouldExecuteAction` variable is set to `true` upon calling the [usage endpoint](../deviceapi/deviceapi#timeUsage).
This is the section where the actual action takes place. For instance, if a solarium turns on, the benefit of customer is booked or customer is changed if the benefit is not contingent.

## Database transaction timeout

A database transaction timeout occurs if there is a long-running database task. In that case, the task will be cancelled, and the request returns an HTTP code 503 (Service Unavailable).
If such an event happens, it is safe to retry later. This could arise due to the database processing an excessive amount of data at the moment.
An example of this involves tasks that adjust a customer's financial status. If these are in progress, it's often not possible to initiate a new transaction.
Therefore, you may sometimes have to wait a few minutes. To avoid waiting and blocking the system with the request, we cancel it, and you can retry later.

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