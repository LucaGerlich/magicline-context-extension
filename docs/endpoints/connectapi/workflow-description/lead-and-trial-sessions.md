# Lead and trial sessions

## Gather leads

1. Select the studio
`GET /connect/v2/studio`
2. (Optional) Pick campaign
`GET /connect/v1/campaign`
3. Send lead data
`POST /connect/v1/lead`


## Proof of identity

The field `documentIdentification` is a combination of a `documentType` and a `documentNumber`.
It is a flexible way to store a specific number, e.g. an identification card number.

**Following types are available:**

* ID_CARD
* PASSPORT
* DRIVERS_LICENSE
* RESIDENCE_PERMIT
* NATIONAL_ID_NUMBER (e.g. for the turkish TC Kimlik number)


There is an automatic validation:

* Both, the `documentType` and the `documentNumber` must be filled
* For NATIONAL_ID_NUMBER in Turkey there is a validation for the T.C. Kimlik number


## Online trial sessions

Normally, a new prospect is created when a trial session appointment is booked.
The gym can continue to work with this record later when a contract is signed.

### Processing optional identityToken

Sometimes, however, the prospect is already known to the studio.
In this case, the studio can send him a special URL to book a trial session.
This link contains a UUID that **must** be used to load the data of the known prospect, and also it **must be sent when booking the trial training**.

The URL parameter name you need to react to is `identityToken` (Type UUID), e.g. `https://connectdemo.api.magicline.com/connect/trial-session?identityToken=2340b1cc-3fe7-4f81-8eca-f92181dd2bb4`

The existing data should be displayed but also the user could edit or enhance that data and the client should send this data like for a request without a UUID.
The data of the existing prospect will then be updated accordingly and **the `identityToken` must be sent as `customerUUID` as part of the customer data.**

### Flow of trial training booking

Be aware that the minimal data for the lead depends on the mandatory field configuration. So this must be loaded up front and the form field validation must be adapted to this configuration.
The data will be again validated when sending the trial session slot booking and gets rejected if invalid.

1. Select the studio
`GET /connect/v1/studio`
2. (Optional) Pick referral
`GET /connect/v1/referral`
3. Collect available slots
`GET /connect/v1/trialsession`
4. (Optional) Load existing lead data by `identityToken`
`GET /connect/v1/lead/customer/{uuid}`
5. Fetch mandatory field configuration
`GET /connect/v1/trialsession/config/validation`
6. Send trial session booking data
`POST /connect/v1/trialsession/book`


## Detailed communication preferences for new leads

When creating a new customer with

`POST /connect/v1/trialsession/book`
or

`POST /connect/v1/lead`

you can specify the customer's detailed communication preferences using the `communicationPreferences` array inside
the `customer` DTO. This array is expected to contain an entry for each message category. Therefore, **you need to fetch
all message categories first**. You can achieve this by fetching a studio's default communication settings:

`GET /connect/v1/studio/{studioId}/communication-settings`

The list contains an entry for each existing message category. You need to decide for which categories you want to ask
the customer for consent. For example, you can match each category by its name.