# Online contracts

## Online contract conclusion

First, it is important to understand that an offer (RateBundle) bundles several attributes. Among other things, an offer
contains several `terms`, from which the customer chooses one (Send as `rateBundleTermId`). An offer can contain e.g. a
6-month term and a 12-month term which differ in price and other features.

### Modules

Furthermore, it contains modules, e.g. a Drink-Flatrate, which are subdivided into 3 groups:

* Inclusive modules (`modules`): Free modules that are always part of the offer (no matter what term is concluded).
* Selectable modules (`selectableModules`): Free modules from which the customer may choose only a maximum
number (`maximumNumberOfSelectableModules`).
* Optional modules (`terms.optionalModules`): Paid modules that can be different per term and the customer can choose
freely.


Since offers can be configured freely, not all modules must always occur. But every offer must have at least one term.

### Flow

The flow is usually:

1. [Fetch the studio information](/apis/magicline/connectapi/connectapi#operation/getStudioList)
`GET /connect/v2/studio`
2. [Fetch rate bundles](/apis/magicline/connectapi/connectapi#operation/getRateBundleList)
`GET /connect/v1/rate-bundle`
3. Display the rate bundle information (Presentation attributes, terms, modules), as well as contract text blocks (see
below) to the customer
4. Submit member and contract data to
the [preview endpoint](/apis/magicline/connectapi/connectapi#operation/getPreview) to get
contract specific preview information
`POST /connect/v1/preview`
5. [Send contract and new member data](/apis/magicline/connectapi/connectapi#operation/createCustomerAndContract)
`POST /connect/v1/rate-bundle`


## Contract preview

The preview endpoint at

`POST /connect/v1/preview`

provides information that depends on information specific to the member and selected contract. Currently, the returned
DTO contains the following information:

- The contract's pre-use fee
- Information for the voucher to be redeemed, if a voucher code has been provided
- The age-adjusted price dependent on the customer's age, if age-based prices are configured for the rate
- Information on the contract volume.
See [Total and average prices for online sales](#total-and-average-prices-for-online-sales) for more information


### Voucher codes

When you want to allow your customers to enter a voucher code, you can use the preview endpoint to fetch information on
the voucher, how it changes the prices and to validate the voucher. The returned DTO contains the voucher's properties,
which should then be used to visualize the price changes to the customer. If the voucher code is invalid or the voucher
cannot be redeemed for another reason, the endpoint sends a `400 Bad Request` response.

In the returned DTO, the field `voucherType` specifies the voucher's type. The types of vouchers that can be redeemed
via the Connect API are `DISCOUNT` and `CREDIT`.

- If the voucher is a discount voucher, the fields `discountValue`, `discountType`, `discountedBasePrice`,
`discountedPreviewCharge` and `omitStarterPackage` are set. The `discountValue` describes the amount or percentage
that is deducted from the rate bundle term's base price. The field `discountType` can either be `AMOUNT`
or `PERCENTAGE` and determines how the `discountValue` should be interpreted. The field `discountedBasePrice` is the
base price of the specified rate bundle term after the discount has been applied. The field `discountedPreviewCharge`
is the price of the pre-use charge after the discount has been applied. The field `omitStarterPackage` specifies
whether the discount voucher is configured to fully discount the price of the rate bundle term's starter package.
- If the voucher is a credit voucher, the field `creditValue` is set. This field specifies the amount that is credited
to the member's account after its creation.


The returned DTO can also contain the properties `voucherRemarks` and `voucherTextBlocks`, regardless of the voucher
type. The `voucherRemarks` is a custom text defined in the voucher's configuration. The `voucherTextBlocks` is a list
of `ConnectApiSignableTextBlockDto`s. These text blocks are configured in the contract document used by the rate bundle
term. However, the `voucherTextBlocks` list does **exclusively** contain text blocks that are configured to be shown
only when a voucher is being redeemed. The list of all other text blocks can be found in the `contractTextBlocks`
property in the [rate bundle](/apis/magicline/connectapi/connectapi#operation/getRateBundleList)

To actually redeem the voucher on contract submission, add the voucher code to the `voucherCode` field in
the [contract creation request](/apis/magicline/connectapi/connectapi#operation/createCustomerAndContract).
Only set this field if you know that the voucher code is valid. Otherwise, contract creation will fail.

## Total and average prices for online sales

If configured, the endpoints `GET /connect/v1/rate-bundle` and `POST /connect/v1/preview` also return information on the
total and average prices during the contract's minimum runtime in the `contractVolumeInformation` field. This can be
configured under `Settings -> Membership signing -> Membership signing settings -> Other settings`.

For the endpoint `GET /connect/v1/rate-bundle`, the field is contained in each rate bundle term. For the
endpoint `POST /connect/v1/preview`, the field is present at the top-level. The DTO contains the following information:

- **Total contract volume**: This is defined as the sum of all payments that are to be performed by the customer during
the initial contract runtime. This includes the rate price, the starter package, flat fees, selected modules and the
pre-use fee. For example: Assume a contract with a runtime of **4 weeks** and a payment frequency of **10 € / week**.
Assume a starter package of **50 €**. This will result in a total contract volume
of `((10 €) / week) * 4 weeks + 50 € = 90 €`.
- **Average payment volume per month**: This is calculated as
follows: `(totalContractVolume / initialContractRuntimeInDays) * DAYS_PER_MONTH`. We define `1 month = 30 days`,
therefore `DAYS_PER_MONTH = 30`. See below for an example.
- **Average payment volume per payment frequency term**: This is calculated as
follows: `(totalContractVolume / initialContractRuntimeInDays) * paymentFrequencyTermInDays`. We
define `1 month = 30 days` and `1 year = 365 days` when converting the payment frequency term to days.
Therefore, `paymentFrequencyTermInDays = 365` for a payment frequency term of **1 year**
and `paymentFrequencyTermInDays = 30` for a payment frequency term of **1 month**. See below for an example. If the
payment frequency is **1 month**, this is the same as the **average payment volume per month**.


**Please note:**

- The assumption that `1 month = 30 days` causes the following behavior for the average payment volume per month: Assume
a contract with a runtime of **1 month**. Assume a total contract volume of **10 €**. Also assume that the current
month (when calling one of the two endpoints that return the contract volume information) has **31 days**. The
contract volume information calculations always assume that the contract is concluded at the current date. This yields
the following payment volume per month: `(10 € / 31 days) * 30 days ≈ 9.68 €`. However, if the current month has only
**30 days**, the average payment volume per month is `(10 € / 30 days) * 30 days = 10 €`.
- Similar behavior can occur for the average payment volume per payment frequency term, due to the assumption
that `1 year = 365 days`. For example: Assume a contract with a runtime of **1 year** (during a leapyear) and a
payment frequency term of **1 year**. Assume a total contract volume of **100 €**. This yields an average payment
volume per payment frequency term of `(100 € / 366 days) * 365 days ≈ 99.73 €`.
- If there is a pre-use fee, the pre-use period will be added to the contract runtime for the average payment volume
calculations. For example: Assume a contract runtime of **2 weeks** and a pre-use period of **1 week**. Assume that
the total contract volume (including pre-use fee) is **15 €**. This yields an average payment volume per month
of `(15 € / 21 days) * 30 days ≈ 21.43 €`.
- The contract volume information does not take into account any discounts that may be applied due to the redemption of
a voucher.


## Detailed communication preferences for new customers

When creating a new customer with

`POST /connect/v1/rate-bundle`

you can specify the customer's detailed communication preferences using the `communicationPreferences` array inside
the `customer` DTO. This array is expected to contain an entry for each message category. Therefore, you need to fetch
all message categories first. You can achieve this
by [fetching](/apis/magicline/connectapi/connectapi#operation/getDefaultCommunicationConfiguration) a studio's default
communication settings:

`GET /connect/v1/studio/{studioId}/communication-settings`

The list contains an entry for each existing message category. You need to decide for which categories you want to ask
the customer for consent. For example, you can match each category by its name.

## Text Blocks

The rate bundle data eventually contains additional text block information
in [contractTextBlocks](/apis/magicline/connectapi/connectapi#operation/getRateBundleList),
such as special conditions, house rules or privacy information.

You are advised to display these information to the customer and eventually present him a checkbox for confirmation or a
signature:

- `isConfirmationRequired:true, hasSignature:false`
  - This textblock must be accepted by the user so a mandatory checkbox should be presented.
- `isConfirmationRequired:true, hasSignature:true`
  - This textblock must be signed by the user so a mandatory signature field should be presented. The signature must
be sent back with the id of the textblock
in [textBlockSignatures](/apis/magicline/connectapi/connectapi#operation/createCustomerAndContract)
- `isConfirmationRequired:false, hasSignature:true`
  - This textblock **can** be signed by the user so a optional signature field should be presented. The signature must
be sent back with the id of the textblock
in [textBlockSignatures](/apis/magicline/connectapi/connectapi#operation/createCustomerAndContract)


## Signatures

The API supports digital signatures. They will be automatically rendered to the contract document.

If you wish to send them, you have to set them as SVG document in Base 64 Format. The Prefix (data:
image/svg+xml;base64,) is optional. Example:


```
    data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIiB3aWR0aD0iNTMwIiBoZWlnaHQ9IjI0MiIgdmlld0JveD0iMCAwIDUzMCAyNDIiPjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIxcHgiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgZD0iTSAzNC42NzE4NzUgMTMgTCAzNC42NzE4NzUgMTMgTCAzMy42NzE4NzUgMTMgTCAzMy42NzE4NzUgMTMgTCAzMi42NzE4NzUgMTMgTCAzMi42NzE4NzUgMTQgTCAzMS42NzE4NzUgMTUgTCAyOS42NzE4NzUgMTUgTCAyOC42NzE4NzUgMTYgTCAyNy42NzE4NzUgMTcgTCAyNy42NzE4NzUgMTcgTCAyNi42NzE4NzUgMTcgTCAyNi42NzE4NzUgMTggTCAyNi42NzE4NzUgMTggTCAyNS42NzE4NzUgMTggTCAyNC42NzE4NzUgMTkgTCAyNC42NzE4NzUgMTkgTCAyMy42NzE4NzUgMjAgTCAyMi42NzE4NzUgMjAgTCAyMi42NzE4NzUgMjEgTCAyMS42NzE4NzUgMjEgTCAyMS42NzE4NzUgMjEgTCAyMS42NzE4NzUgMjEgTCAyMS42NzE4NzUgMjEiPjwvcGF0aD48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAiIHN0cm9rZS13aWR0aD0iMXB4IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2UtbGluZWNhcD0icm91bmQiIGQ9Ik0gMTkuNjcxODc1IDEwIEwgMTkuNjcxODc1IDEwIEwgMjAuNjcxODc1IDEwIEwgMjAuNjcxODc1IDExIEwgMjAuNjcxODc1IDExIEwgMjAuNjcxODc1IDEyIEwgMjAuNjcxODc1IDEyIEwgMjEuNjcxODc1IDEyIEwgMjEuNjcxODc1IDEyIEwgMjEuNjcxODc1IDEzIEwgMjEuNjcxODc1IDEzIEwgMjEuNjcxODc1IDEzIEwgMjEuNjcxODc1IDEzIEwgMjEuNjcxODc1IDEzIEwgMjEuNjcxODc1IDE0IEwgMjIuNjcxODc1IDE0IEwgMjIuNjcxODc1IDE0IEwgMjIuNjcxODc1IDE1IEwgMjIuNjcxODc1IDE1IEwgMjMuNjcxODc1IDE2IEwgMjMuNjcxODc1IDE2IEwgMjMuNjcxODc1IDE3IEwgMjQuNjcxODc1IDE3IEwgMjQuNjcxODc1IDE3IEwgMjQuNjcxODc1IDE4IEwgMjUuNjcxODc1IDE4IEwgMjUuNjcxODc1IDE5IEwgMjUuNjcxODc1IDE5IEwgMjYuNjcxODc1IDE5IEwgMjYuNjcxODc1IDIwIEwgMjYuNjcxODc1IDIwIEwgMjcuNjcxODc1IDIwIEwgMjcuNjcxODc1IDIxIEwgMjcuNjcxODc1IDIxIEwgMjcuNjcxODc1IDIxIEwgMjguNjcxODc1IDIxIEwgMjguNjcxODc1IDIyIEwgMjguNjcxODc1IDIyIEwgMjguNjcxODc1IDIyIEwgMjkuNjcxODc1IDIyIEwgMjkuNjcxODc1IDIyIj48L3BhdGg+PC9zdmc+
```

## Proof of identity

The field `documentIdentification` is a combination of a `documentType` and a `documentNumber`. It is a flexible way to
store a specific number, e.g. an identification card number.

**Following types are available:**

* ID_CARD
* PASSPORT
* DRIVERS_LICENSE
* RESIDENCE_PERMIT
* NATIONAL_ID_NUMBER (e.g. for the turkish TC Kimlik number)


There is an automatic validation:

* Both, the `documentType` and the `documentNumber` must be filled
* For NATIONAL_ID_NUMBER in Turkey there is a validation for the T.C. Kimlik number


## Member picture

The API supports that the user can send a picture which will be used as member-picture in the final customer data. **You
are advised to use this only for this purpose and no other uploads (like documents etc.) as the image will end up as
member picture in the Magicline customer.**

1. [Fetch](/apis/magicline/connectapi/connectapi#operation/generatePreSignedUrlForPreUpload) the uploading URL
`GET /connect/v1/prospectimage/uploadurl`
2. Upload the image you got from the User. This must be implemented by your website code, e.g. access the webcam or
provide a file upload. Upload
**must** be a PUT request with the **binary data
** (not JSON, base64 or anything else) of the file, like
described [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Sending_and_Receiving_Binary_Data),
against the provided UploadUrl.
3. Send the
`objectKey`
, you fetch together with the uploadUrl, as
`imageObjectKey`
in the final
`POST /connect/v1/rate-bundle`
4. During the process of member creation the given
`imageObjectKey`
will be checked and the corresponding data which should be accessible behind it load and used as member picture. If
something fails a 500 response will be returned with

```json
     {
       "message": "Invalid image format",
       "errorCodes": [
         "VALIDATION_FAILED"
       ]
     }
```
**You must make sure that the upload request has finished before you send the final POST request otherwise it would
fail because the file cannot be copied!**


## Online contract cancellation

In some countries there is a legal obligation to allow contract cancellations online without the customer having to log
in.

### Whitelabel solution

We provide a whitelabel solution for that so that you just need to add a link to your page with a URL of this pattern:

`https://public.magicline.com/#/contractTermination?tenant=<tenant_name>&studio=<studio_id>`

Both parameters are mandatory and need to be set. The tenant name value is the same one you need to access the API. The
studio ID needs to be set to preload specific information of that studio and preselect it in the studio select box. The
URL leads to a page where a member can search for their contract(s) and submit the cancellation.

### Custom implementation

If you want to use your own page instead of the whitelabel one, you can do so by implementing
an [invisible reCAPTCHA](https://developers.google.com/recaptcha/docs/invisible?hl=en)
challenge on your site. Please contact customer support first, so we can activate your domain for reCAPTCHA. The site
key required to set up reCAPTCHA is `6Ld5qKcgAAAAAMoywArOgIrC0lQ7NpYUTsF92PIC`. Generate a token and set the query
parameter `recaptchaToken` where required.

*Note: A token is only valid for two minutes. Make sure the challenge is not invoked too early.*

Example:

1. First, fetch [all studios](/apis/magicline/connectapi/connectapi#operation/getActiveStudiosInGermanyV2) with their basic
information.
`GET /connect/v1/contracts/studios`
2. Retrieve all [active contracts](/apis/magicline/connectapi/connectapi#operation/getActiveContracts) for a member. If a member
forgot their customer number, skip to step 5.
`POST /connect/v1/contracts`
3. Fetch [studios cancellation information](/apis/magicline/connectapi/connectapi#operation/getStudioInfo) for the member's studio
to get possible cancellation reasons. The member's studio ID can be found in the response of the previous step's
request. The response is a list of contracts and each contract has a field containing the member's studio's ID. The
ID is the same for each contract, so you can just use the studio's ID from the first element in the list.
`GET /connect/v1/contracts/studios/{studioId}`
4. Submit the cancellation for the contract the member wishes
to [cancel](/apis/magicline/connectapi/connectapi#operation/cancelContract).
`POST /connect/v1/contracts/cancel`
5. If the member forgot their customer number, you can let them submit a manual cancellation request. Therefore, let the
member select a studio from the fetched list in step 1. Then load
the `cancellation reasons (deprecated)` for that studio.
`GET /connect/v1/contracts/studios/{studioId}/cancellation-reasons`
Finally, submit the [manual cancellation request](/apis/magicline/connectapi/connectapi#operation/cancelContractManual).
`POST /connect/v1/contracts/cancel-request`
Instead of immediately cancelling a contract, the manual cancellation request will create a task in the Magicline for
the studio that has been selected by the customer.


# Support credit card for online contract conclusion

If a gym has credit card set up as payment method for an offer, the following process must be implemented to allow a
member to use his credit card.

## Adyen WebComponent

To store credit cards, you need to embed a WebComponent, provided by our payment service provider Adyen. This
WebComponent contains input fields, where the User will need to enter his credit card information. The credit card
information (also CVC) will be encrypted securely by the WebComponent, and then passed to the Website via callback
function, when the User hits the Submit-Button. It is then your task to deliver the encrypted data to the Magicline
Connect API and perform the Process, as documented in the next section. Note that the encrypted credit card data can
only be read by our PSP Adyen, it is not possible for Magicline to obtain the credit card number or CVC.

To load the WebComponent via `script` use the following snippet:


```html
<script src="https://checkoutshopper-test.adyen.com/checkoutshopper/sdk/4.5.0/adyen.js"
        integrity="sha384-Co94gRjtPsf3110lIIB8CaogV5Khwg8lcSh4fK5r1gzfWZHxaqpBXwEFjaFGcLaj"
        crossorigin="anonymous"></script>
<link rel="stylesheet"
      href="https://checkoutshopper-test.adyen.com/checkoutshopper/sdk/4.5.0/adyen.css"
      integrity="sha384-8EGo5meqBqlQ4MFf3nbQYD/onCuTfclYfNl3a5uQ1swwv0XXcTkda75dvjlYbZI8"
      crossorigin="anonymous">
```

When switching to the live environment use the following script/stylesheet:


```html
<script src="https://checkoutshopper-live.adyen.com/checkoutshopper/sdk/4.5.0/adyen.js"
        integrity="sha384-Co94gRjtPsf3110lIIB8CaogV5Khwg8lcSh4fK5r1gzfWZHxaqpBXwEFjaFGcLaj"
        crossorigin="anonymous"></script>

<link rel="stylesheet"
      href="https://checkoutshopper-live.adyen.com/checkoutshopper/sdk/4.5.0/adyen.css"
      integrity="sha384-8EGo5meqBqlQ4MFf3nbQYD/onCuTfclYfNl3a5uQ1swwv0XXcTkda75dvjlYbZI8"
      crossorigin="anonymous">
```

To read more about loading the WebComponent, like using alternative ways like `NPM`, you might take a look at
the [Adyen documentation](https://docs.adyen.com/online-payments/components-web?tab=script_2#step-2-add-components).

### Process

The process of storing the needed credit card information (called "Tokenization") includes multiple steps. Depending on
the type of authorization (3DS1, 3DS2) the user might get redirected to a website by his bank, where he needs to
authenticate himself. The user is then redirected back to your site, so you need to provide a returnUrl, where the User
should be redirected back to continue his registration. Make sure to store required information, before the user leaves
your site, so you can restore it after the redirect back.

### Load WebComponent data

Your first step is to load data that is required by the Adyen WebComponent, to display the proper input fields for
credit cards. You do so by calling:

`GET /connect/v2/creditcard/tokenization/payment-methods`

The response contains a serialized object, which needs to be deserialized. Together with the payment methods response,
and additional configuration parameters, you need to initialize the Adyen WebComponent. Make sure to check configuration
parameters like **locale**, to set the appropriate locale for your User. Also make sure to use an `amount` of 0 (Zero).

Ask your Magicline contact about the `clientKey` to use for our `sandbox` and `prod` environment.


```javascript
function handlePaymentMethodsResponse(response) {
    const configuration = {
        paymentMethodsResponse: JSON.parse(response.paymentMethodsJson),
        clientKey,
        locale: "de_DE",
        environment: "live",
        showPayButton: true,
        paymentMethodsConfiguration: {
            ideal: {
                showImage: true,
            },
            card: {
                hasHolderName: true,
                holderNameRequired: true,
                name: "Credit or debit card",
                amount: {
                    value: 0,
                    currency: "EUR",
                },
            }
        },
        onSubmit: (state, component) => {
            submit(state, component);
        },
        onAdditionalDetails: (state, component) => {
            additionalDetails(state, component);
        },
    };
    const checkout = new AdyenCheckout(configuration);
    checkout.create("card").mount("#component-container");
}
```

The code example shows an example configuration, and the creation of the Adyen WebComponent, which is mounted to an HTML
element with id
**component-container**. It will display a Form where the user can enter his credit card number, expiry, cvc, and so on.

### Initiate Tokenization

In the code snippet from "Load WebComponent data" you might have noticed a callback function **onSubmit
**. This callback is invoked by the WebComponent, when the user hits the submit button. Create a submit function, that
sends the data obtained by the WebComponent to the Connect API initiate endpoint:

`POST /connect/v2/creditcard/tokenization/initiate`

Apart from the WebComponent data this endpoint requires additional information, e.g. a returnUrl, where the user is
redirected back in case of a redirect to his banking page. If a redirect takes place depends on the authentication
method and might or might not occur.

**Please note:** our services will add request params to the `returnUrl`:

1. the Magicline will add a reference to the tokenization process in form of a UUID
2. the Bank will append an authorization result


Make sure to test that your webserver and website can handle those properly. There are certain test credit card numbers
that will enforce a redirect authentication.


```javascript
function submit(state, component) {
    if (state.isValid) {
        const postData = {
            paymentMethod: JSON.stringify(state.data.paymentMethod),
            browserInfo: JSON.stringify(state.data.browserInfo),
            studioId: 12345,
            returnUrl: "https://my-company.com/checkout",
            origin: window.location.origin
        }
        post("/connect/v2/creditcard/tokenization/initiate", postData, function (data, status) {
            handleInitiateResponse(data, status, component);
        });
    }
}
```

### Handle initiate response

Apart from a `resultCode`, the initiate response contains 2 values: a `reference` which is an identifier for this
tokenization process (in the following sections this is referred to as `tokenizationReference`). It must be submitted
for subsequent requests to pick up the tokenization process. If the `action` value is set, this value must be parsed
(it is again a serialized JSON object) and passed to the `handleAction` method of the WebComponent. The action
determines the type of authentication process, if this is a redirect, make sure to store the current state of the form
so the user can continue with his registration where he left (e.g. in `window.localStorage`).


```javascript
function handleInitiateResponse(data, status, component) {
    tokenizationReference = data.reference;
    if (data.action) {
        if (response.action.type === "redirect") {
            storeCurrentState();
        }
        component.handleAction(JSON.parse(data.action));
    }
}
```

### Submit additional details

To complete the tokenization you must send additional details to the Connect API. To do this you need to handle one of
two ways:

1. if the User authenticated on the current site (3DS2), the WebComponent will invoke the `onAdditionalDetails`
callback, passing an object that contains the result.
2. If the User has been redirected to the bank website, and is redirected back to your site, the return url will contain
a request param with the additional data.


In both cases you need to send the additional data back to the Connect API via the endpoint.

`POST /connect/v2/creditcard/tokenization/{tokenizationReference}/complete`

While in the 1st case you need to know the `tokenizationReference` by yourself (you have received it in the `initiate`
response), in the 2nd case the `tokenizationReference` is also appended to the returnUrl.


```javascript
function additionalDetails(data, component) {
    // Depending on the authentication:
    // fill threeDSResult (authentication took place on your site)
    // or fill redirectResult (authentication via redirect)
    const postData = {
        threeDSResult: data.data.details.threeDSResult,
        redirectResult: null
    };
    post("/connect/v2/creditcard/tokenization/" + tokenizationReference + "/complete", postData, function (response, status) {
        handleCompleteResponse();
    });
}
```

### Check tokenization state

While you also receive a result of the tokenization when calling the `complete` endpoint, it may happen that the
tokenization isn't completely finished in that very moment. To check the outcome of the tokenization process you need to
regularly call the `state` endpoint:

`GET /connect/v2/creditcard/tokenization/{tokenizationReference}/state`

If this is `COMPLETE` the tokenization was completed successfully. If it is `FAILURE` it failed, and `errorMessage`
contains a message about the reason.

**Make sure that you don't poll this endpoint too eagerly to avoid rate limits. We advise to check this endpoint about
once every 2 seconds to have a trade-off between load and responsiveness.**

## Next Steps

To create a customer you need to call the endpoint:

`POST /connect/v1/rate-bundle`

In the request body choose as `paymentChoice` value `CREDIT_CARD`. Additionally provide a value for `creditCard`, which
contains an object with a single string `tokenizationReference`, where you need to add the tokenizationReference you
have received in the tokenization process.