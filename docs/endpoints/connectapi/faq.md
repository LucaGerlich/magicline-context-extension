# Frequently Asked Questions

## How does the integration of the API work?

The Connect API is based on the [REST architectural style](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
and consumes and produces [JSON](https://www.w3schools.com/js/js_json_intro.asp).

As the rate bundle structure is designed in a flexible way, to support every aspect of the fitness industry, it is important
to talk to the studio owner (your client) how the offers are structured (besides other things: Signature needed? Which payment methods?)
to know which attributes of the API need to be considered and which are maybe not relevant for you.
Optional attributes which are not relevant should just be skipped and not sent at all (also not like `textBlockId: 0`).

You can also use the `Try out` feature of this documentation. For every operation you can send and receive data
by using the `try out` block in the upper right corner as well as getting request samples. **As the underlying tenant
is for demo purpose only the data you receive will differ from the one of your client.**

We have set up a very simple demo UI which you can give you a better idea how to interact with the API:

`https://<tenant_name>.api.magicline.com/connect/customer`

## Do I need an access token or credentials to access the API?

No, because this API is meant to be integrated directly into the studio's website. This would require any kind of
credentials to be issued to the client as well, and by that they would be publicly available and thus ineffective.

However, since this API can only be used to access public studio data that can alternatively be viewed on the studio's
website, there is no risk of sensitive data being accessed without permission.

## Why do I not get translated responses on validation errors?

The responses of type `VALIDATION_FAILED` contain a message that should help developers to identify the problem faster.
But the validation of all input fields must be done upfront in the UI before a request is sent.
So providing customer friendly, translated messages must be part of the UI implementation.

Please have a look into the API specification for mandatory fields and required formats.

## Why do I get "Term for this offer not found" as response?

The field `rateBundleTermId` must contain a valid ID from the `terms` array of the rate bundle and **not e.g.
the ID of the bundle itself**.

So verify that the ID is part of that array and the rate bundles have been fetched with
the same studio ID which have been sent in `studioId`.

## Do I need to set the textBlockId in all signatures?

**No** even if this optional value can be sent in all signatures it must only be sent for signatures from the array `textBlockSignatures`.
If text blocks of the rate bundle have the property `hasSignature:true`.

The signatures for the contract itself (`contractSignature`) as well as the sepa signature (`sepaSignature`) must be sent without `textBlockId`.

## How to send the language of the new member?

There are two options to transmit this information. You can either send the language only by setting the `language` of
the customer object. It must be in the ISO 639-1 two-letter code format like `en` or `de`.
Or you can send the more precise information of the locale of the member as ISO 639-1 two-letter language and
country code (e.g. `es_ES` or `de_DE`). That may be the better option for countries with more than one language as e.g.
Switzerland (`de_CH`,`fr_CH`) or Canada.

If for any reasons both values are set, the more precise information of the locale will be used.

If none is set we will try to derive the language from the `countryCode`.

## What do I need to send as a contract start date?

There are two attributes which are related to the start of the contract:

* `startDate` is the effective start of the contract
* `preuseDate` is the date to which the member can start to use the gym


Each term contains information about the pre-usage (If it is allowed and if it will be charged for)

* `preuseType: "NONE" "CHARGEABLE" "FREE"`


and default values for both dates. Depending on the requirements of the gym owner these values can be picked by the
user or the default values from the term need to be sent:

* `defaultContractStartDate >> startDate`
* `contractStartDateOfUse >> preuseDate`


There is no automatism which uses these values, you need to ensure that the correct values will be sent.
The `preuseDate` is optional; The `startDate` is mandatory.