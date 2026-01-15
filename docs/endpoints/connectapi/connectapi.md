# Magicline Connect API

[//]: # (The content of this file is used as the descrption of the API)

# Scope of this API

This API can be used to integrate Magicline operations into third party clients like websites or apps.

Following operations are supported

* Online contract conclusion
* Trial session slot booking
* Lead creation


Version: 1.0.0

## Servers

Generated server url
```
https://connectdemo.api.magicline.com
```

## Download OpenAPI description

[Magicline Connect API](https://redocly.sportalliance.com/_spec/apis/magicline/connectapi/connectapi.yaml)

## Campaigns

List your marketing campaigns

### List all campaigns

 - [GET /connect/v1/campaign](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/campaigns/listallactivecampaigns.md)

## Terminal

/terminal

### getCustomerDataByCodiceFiscale

 - [GET /connect/v1/terminal/customer-data-by-codicefiscale](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/terminal/getcustomerdatabycodicefiscale.md)

## TrialSessions

Allow prospects to book a trial session

### Get free slots for a trial session

 - [GET /connect/v1/trialsession](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/trialsessions/getbookableitem.md): Returns free slots for a studio where a trial session appointment can be booked.

### Book a trial session

 - [POST /connect/v1/trialsession/book](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/trialsessions/book.md): Book a free slot. Might return errorCode CONFLICT if configured resources are overbooked for this slot. In this case its advised to reload free slots and let the user select a different slot. If you get a validation error make sure all required fields are filled. Required fields are returned by the  endpoint.

### Get mandatory field configuration

 - [GET /connect/v1/trialsession/config/validation](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/trialsessions/getleadconfig.md): Returns the configuration which needs to be considered e.g. for form fields and their validation.

## Tenant

Tenant information

### getTenantInfo

 - [GET /connect/v1/tenant](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/tenant/gettenantinfo.md)

## Referral

Additional referral information for member creation

### List all referrals by studioId

 - [GET /connect/v1/referral](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/referral/getreferralsbystudioid.md)

## Image

Allow prospect to upload image

### generatePreSignedUrlForPreUpload

 - [GET /connect/v1/prospectimage/uploadurl](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/image/generatepresignedurlforpreupload.md)

## Promotions

Getting information about external promotion participation

### confirmCustomerParticipation

 - [POST /connect/v1/promotion/confirm-participation](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/promotions/confirmcustomerparticipation.md)

## AddressData

/addressdata

### getProvinceInformation

 - [GET /connect/v1/addressdata/italy/province](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/addressdata/getprovinceinformation.md)

## ContractVoucher

/contractvoucher

### Redeem a ContractVoucher. Only Vouchers of type 'Rate' are supported here.

 - [POST /connect/v1/contractvoucher/{contractVoucherCode}/redeem](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contractvoucher/redeemcontractvoucher.md)

### Validates a ContractVoucher and returns basic voucher information to display. Only Vouchers of type 'Rate' are supported here.

 - [GET /connect/v1/contractvoucher/{contractVoucherCode}/validate](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contractvoucher/validatecontractvoucher.md)

## Validation

/validation

### Validates the taxId against country based validation rules.

 - [POST /connect/v1/validation/taxId](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/validation/validatetaxid.md): For some countries additional customer related attributes might be needed for that. Country will be derived from given studioId.

## Contracts

List rates and create new members

### getActiveContracts

 - [POST /connect/v1/contracts](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/getactivecontracts.md)

### cancelContract

 - [POST /connect/v1/contracts/cancel](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/cancelcontract.md)

### cancelContractManual

 - [POST /connect/v1/contracts/cancel-request](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/cancelcontractmanual.md)

### getStudioInfo

 - [GET /connect/v1/contracts/studios/{studioId}](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/getstudioinfo.md)

### List rate bundles (german wording: Angebote)

 - [GET /connect/v1/rate-bundle](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/getratebundlelist.md)

### Create a new customer and a new contract

 - [POST /connect/v1/rate-bundle](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/createcustomerandcontract.md)

### getActiveStudiosInGermanyV2

 - [GET /connect/v2/contracts/studios](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/contracts/getactivestudiosingermanyv2.md)

## CreditCard Tokenization

Store credit cards for new members

### Initiate Tokenization

 - [POST /connect/v2/creditcard/tokenization/initiate](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/creditcard-tokenization/initiatetokenizationv2.md)

### Load payment methods

 - [GET /connect/v2/creditcard/tokenization/payment-methods](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/creditcard-tokenization/paymentmethodsv2.md)

### Complete Tokenization

 - [POST /connect/v2/creditcard/tokenization/{tokenizationReference}/complete](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/creditcard-tokenization/completetokenizationv2.md)

### Get Tokenization state

 - [GET /connect/v2/creditcard/tokenization/{tokenizationReference}/state](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/creditcard-tokenization/tokenizationstatev2.md)

### Complete Tokenization (deprecated)

 - [POST /connect/v1/creditcard/tokenization/{tokenizationReference}/complete](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/creditcard-tokenization/completetokenization.md)

### Get Tokenization state (deprecated)

 - [GET /connect/v1/creditcard/tokenization/{tokenizationReference}/state](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/creditcard-tokenization/tokenizationstate.md)

## BankAccount

### validateIbanAndLookupBic

 - [GET /connect/v1/bankaccount](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/bankaccount/validateibanandlookupbic.md)

### validateAccountHolderName

 - [GET /connect/v1/bankaccount/validate/accountholder](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/bankaccount/validateaccountholdername.md)

## FeatureCheck

### Lists all active features of the organization unit

 - [GET /connect/v1/featurecheck/activefeatures](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/featurecheck/getactivefeatures.md)

## I18n

### Returns a list of tuples with every available country code and the localized country name

 - [GET /connect/v1/i18n/countries](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/i18n/getcountries.md)

## Leads

### Create leads for prospective customers

 - [POST /connect/v1/lead](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/leads/createlead.md)

### Returns information about an existing lead record

 - [GET /connect/v1/lead/{uuid}](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/leads/getleadcustomerbyuuid.md)

## Studios

### Get the studio's default communication settings.

 - [GET /connect/v1/studio/{studioId}/communication-settings](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getdefaultcommunicationconfiguration.md): Get the studio's default communication settings. The returned list contains an entry for each existing message category.

### getSepaAgreementTextForRateBundle

 - [GET /connect/v1/studio/{studioId}/rate/{rateBundleId}/sepa/agreement](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getsepaagreementtextforratebundle.md)

### getSepaAgreementText

 - [GET /connect/v1/studio/{studioId}/sepa/agreement](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getsepaagreementtext.md)

### Get utilization for the studio.

 - [GET /connect/v1/studio/{studioId}/utilization](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getutilizationpublic.md): Return information about the utilization of this studio. Needs to be enabled for public view in the configuration.

### List all studios

 - [GET /connect/v2/studio](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getstudiolist.md): You can add optional filters. Parameters addressSearchQuery and studioTags are combined by AND

### Fetch detail information for one studio

 - [GET /connect/v2/studio/details/{studioId}](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getstudiodetails.md)

### Fetch information for one studio

 - [GET /connect/v2/studio/{studioId}](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getstudio.md)

### Fetch enabled communication feature modules for one studio

 - [GET /connect/v2/studio/{studioId}/communicationFeatures](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getenabledcommunicationfeaturemodules.md)

### Fetch legal information for one studio

 - [GET /connect/v2/studio/{studioId}/legalinfo](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/studios/getstudiolegallinks.md)

## Previews

### getPreview

 - [POST /connect/v2/preview](https://redocly.sportalliance.com/apis/magicline/connectapi/connectapi/previews/getpreview.md)

