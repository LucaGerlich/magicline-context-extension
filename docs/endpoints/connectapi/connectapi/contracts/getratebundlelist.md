# List rate bundles (german wording: Angebote)

Endpoint: GET /connect/v1/rate-bundle
Version: 1.0.0

## Query parameters:

  - `studioId` (integer, required)
    The Id of the studio to fetch the rate bundles from
    Example: 1

## Response 200 fields (*/*):

  - `allowedPaymentChoices` (array)
    Allowed payment types for this rate bundle. Others than in this list will not be accepted when creating a contract. Please note: The Connect API only supports 'DIRECT_DEBIT' and 'CREDIT_CARD'. Therefore, this list will contain these two values at most.
    Enum: "CASH", "BANK_TRANSFER", "DIRECT_DEBIT", "CREDIT_CARD", "TWINT"

  - `contractSignaturesRequired` (boolean)
    Indicates if a digital signature for the contract (and SEPA agreement) is mandatory.

  - `contractTextBlocks` (array)
    Important contract details such as privacy details or special conditions. Show them to the customer before contract acceptance

  - `contractTextBlocks.attachedDocument` (object)
    Optional contract document attachment You should display a download link if this field is set.

  - `contractTextBlocks.attachedDocument.fileName` (string, required)

  - `contractTextBlocks.attachedDocument.url` (string, required)
    Temporary valid download link. Expires after 5 hours

  - `contractTextBlocks.attachedExternalUrlDto` (object)
    Optional link to external url You should display a link if this field is set with the given title and target url

  - `contractTextBlocks.attachedExternalUrlDto.link` (string)

  - `contractTextBlocks.attachedExternalUrlDto.title` (string)

  - `contractTextBlocks.attachmentType` (string)
    Indicates the type of attachment for this block: None, file (attachedDocument) or Url (attachedExternalUrlDto)
    Enum: "NONE", "FILE", "URL", "CONTRACT_PDF_PREVIEW"

  - `contractTextBlocks.hasSignature` (boolean, required)
    text block configuration has a signature field. You have the option to show a signature input field and it will be added in the contract document. It is not a required field in magicline. It is up to your implementation if you add this field.

  - `contractTextBlocks.id` (integer, required)

  - `contractTextBlocks.isConfirmationRequired` (boolean, required)
    text block configuration contains a confirmation. You are advised to show a check box (or signature if hasSignature=true) in combination with this text block where the user should give his consent.

  - `contractTextBlocks.order` (integer, required)
    order in contract document

  - `contractTextBlocks.rateBundleModuleId` (integer)
    The ID of the associated rate bundle module. Only set if this is a module consent text block.

  - `contractTextBlocks.showCommunicationPrivacyOptions` (boolean, required)
    text block contains information about the communication privacy options You are advised to show a matrix with communication settings in combination with this text block.

  - `contractTextBlocks.text` (string, required)

  - `description` (string, required)

  - `footnote` (string)
    Contractual or legal comments to be displayed below the offer.

  - `id` (integer, required)
    Id of current data block. See name field parameter or name of Dto!

  - `imageUrl` (string)
    Temporary valid download link for rate bundle image. Expires after 24h

  - `initialPaymentRequired` (boolean)
    An initial payment has to be made in order to gain access to the studio. An email will be sent to the user after contract creation with details how to make the payment.

  - `limitedOfferingPeriod` (object)
    The period in which this rate bundle is offered

  - `limitedOfferingPeriod.endDate` (string, required)

  - `limitedOfferingPeriod.startDate` (string, required)

  - `maximumNumberOfSelectableModules` (integer)
    The maximum value of the selectable modules that the customer can choose.

  - `modules` (array, required)
    Included free modules.

  - `modules.consentTextBlock` (object)

  - `modules.imageUrl` (string)

  - `modules.name` (string, required)

  - `modules.paymentFrequencyDto` (object, required)

  - `modules.paymentFrequencyDto.ageBasedAdjustmentDtos` (array)
    Age-based price adjustments. Price adjustments can be either a percentage by which the base price is being discounted or an absolute price.

  - `modules.paymentFrequencyDto.ageBasedAdjustmentDtos.ageBasedAdjustmentType` (string, required)
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `modules.paymentFrequencyDto.ageBasedAdjustmentDtos.ageRangeDto` (object, required)

  - `modules.paymentFrequencyDto.ageBasedAdjustmentDtos.ageRangeDto.endAge` (integer)

  - `modules.paymentFrequencyDto.ageBasedAdjustmentDtos.ageRangeDto.startAge` (integer)

  - `modules.paymentFrequencyDto.ageBasedAdjustmentDtos.value` (number, required)

  - `modules.paymentFrequencyDto.money` (object)
    The price for this payment frequency. Only set if "type" is either "RECURRING" or "NON_RECURRING"

  - `modules.paymentFrequencyDto.money.amount` (number, required)

  - `modules.paymentFrequencyDto.money.currencyCode` (string, required)
    Enum: "UNDEFINED", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"

  - `modules.paymentFrequencyDto.monthDayWithPrices` (array)
    The dates and respective prices on which payments are due. Only set if "type" is "MONTH_DAY"

  - `modules.paymentFrequencyDto.monthDayWithPrices.monthDay` (string, required)

  - `modules.paymentFrequencyDto.monthDayWithPrices.price` (object, required)

  - `modules.paymentFrequencyDto.recurring` (boolean, required)
    Whether the cycle of payments repeats indefinitely. Only relevant if type is "TERM_BASED" or "MONTH_DAY".

  - `modules.paymentFrequencyDto.term` (object)
    The interval in which payments are made. Only set if "type" is "RECURRING"

  - `modules.paymentFrequencyDto.term.term` (integer, required)

  - `modules.paymentFrequencyDto.term.termUnit` (string, required)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `modules.paymentFrequencyDto.termWithPrices` (array)
    The terms and respective prices after which payments are due. Only set if "type" is "TERM_BASED"

  - `modules.paymentFrequencyDto.type` (string, required)
    The kind of intervals in which payments are made
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `modules.paymentFrequencyId` (integer, required)

  - `modules.publicTrialPeriodDto` (object)

  - `modules.publicTrialPeriodDto.trialPeriod` (object)

  - `modules.paymentFrequencyType` (string)
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `modules.paymentFrequencyUnit` (string)
    is set in combination with RECURRING type
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `modules.paymentFrequencyValue` (integer)
    is set in combination with RECURRING type

  - `onlinePaymentType` (string)
    Under development: Indicates if this RateBundle has some kind of special Payment Handling
    Enum: "NONE", "DIRECT_PAYMENT"

  - `preuseType` (string)
    [0=NONE, 1=CHARGEABLE, 2=FREE]
    Enum: "NONE", "CHARGEABLE", "FREE"

  - `rateCodeDto` (array)

  - `rateCodeDto.identifier` (string, required)

  - `selectableModules` (array)
    Selectable free inclusive modules. Customer is only allowed to choose a fixed value of them. The maximum value of the selected modules describes  property.

  - `subDescription` (string)

  - `terms` (array, required)

  - `terms.cancelationStrategy` (string)
    Enum: "TERM", "RECEIPT_DATE"

  - `terms.cancellationPeriod` (integer)

  - `terms.cancellationPeriodUnit` (string)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.contractStartDateOfUse` (string)
    This contract start date of use will be used if none will be send, but can be overridden

  - `terms.contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month and per the rate's payment frequency (e.g. 1 week)

  - `terms.contractVolumeInformation.averagePaymentVolumePerMonth` (number)

  - `terms.contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (number)

  - `terms.contractVolumeInformation.totalContractVolume` (number)

  - `terms.defaultContractStartDate` (string)
    This contract start will be used if none will be send, but can be overridden

  - `terms.extensionCancellationPeriod` (integer)

  - `terms.extensionCancellationPeriodUnit` (string)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.extensionFixedTerm` (integer)

  - `terms.extensionFixedTermUnit` (string)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.extensionType` (string)
    Enum: "NONE", "TERM_EXTENSION", "SUBSEQUENT_RATE_DETAIL"

  - `terms.flatFees` (array)

  - `terms.flatFees.firstBookingDelayUnit` (string)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.flatFees.firstBookingDelayValue` (integer)

  - `terms.flatFees.isStarterPackage` (boolean)

  - `terms.flatFees.paidTimePeriodCalculationType` (string, required)
    Enum: "REFERENCE_DATE", "NORMALIZATION_ON_CALENDAR_UNIT"

  - `terms.flatFees.paymentFrequencyDto` (object, required)
    Payment frequency information

  - `terms.flatFees.paymentFrequency` (string)
    Additional details of payment frequency. Deprecated, formatting should be handled on the client side using information from "paymentFrequencyDto"
    Example: "One time on 01.01, Every 01.01., etc."

  - `terms.flatFees.paymentFrequencyType` (string, required)
    Deprecated, use "paymentFrequencyDto.type" instead
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `terms.flatFees.paymentFrequencyUnit` (string)
    Is set in combination with RECURRING type. Deprecated, use "paymentFrequencyDto.term.termUnit" instead.
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.flatFees.paymentFrequencyValue` (integer)
    Is set in combination with RECURRING type. Deprecated, use "paymentFrequencyDto.term.term" instead.

  - `terms.flatFees.price` (number, required)
    Deprecated, use "paymentFrequencyDto.money.amount" instead

  - `terms.optionalModules` (array)
    Optional modules additionally payable.

  - `terms.paymentFrequencyDto` (object, required)
    The payment frequency of this term

  - `terms.priceAdjustmentRules` (array)
    A list of price adjustment rules which applies to this term. Like a 5% raise every 6 months

  - `terms.priceAdjustmentRules.chargeAdjustmentType` (string)
    Type of the value: Percentage/absolute relative change or new absolute base amount
    Enum: "RELATIVE", "ABSOLUTE", "BASIC_AMOUNT"

  - `terms.priceAdjustmentRules.defaultDescription` (string)
    A complete formatted sentence which contains all details about this price adjustment rule.If the presenation should differ use the separate attributes.

  - `terms.priceAdjustmentRules.recurrenceFrequency` (string)
    Recurrence of price adjustment rule, how often and when applies this rule

  - `terms.priceAdjustmentRules.type` (string)
    States if this rule is overall a RAISE or REDUCTION of the price
    Enum: "RAISE", "REDUCTION", "NEW_BASIC_AMOUNT"

  - `terms.priceAdjustmentRules.value` (string)
    Value of price adjustment rule, might be percentage or amount, depends on chargeAdjustmentType

  - `terms.priceAfterExtension` (number)
    The new price after minimum contract duration. Null if not configured.

  - `terms.rateBonusPeriods` (array)

  - `terms.rateBonusPeriods.displaySeparately` (boolean)

  - `terms.rateBonusPeriods.extendsCancellationPeriod` (boolean)

  - `terms.rateBonusPeriods.runtimeExtensionType` (string)
    Enum: "WITH_EXTENSION", "WITHOUT_EXTENSION"

  - `terms.rateBonusPeriods.termStrategy` (string)
    Enum: "CONTRACT_START", "FIXED", "END_OF_CURRENT_TERM", "START_OF_NEXT_TERM"

  - `terms.rateBonusPeriods.termValue` (integer)

  - `terms.rateStartPrice` (number)
    price for the first period of the contract, if the term has bonus period at the beginning of the contract then it is equal to 0, otherwise is equal to term price.

  - `terms.subsequentRateDto` (object)

  - `terms.termUnitAfterExtension` (string)
    The new term unit after minimum contract duration. Null if not configured.
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.termValueAfterExtension` (integer)
    The new term value after minimum contract duration. Null if not configured.

  - `terms.termValueWithoutBonusPeriod` (integer, required)

  - `terms.ageBasedAdjustmentDtos` (array)
    A list of age-based price adjustments for this term. Deprecated, use "paymentFrequencyDto.ageBasedAdjustmentDtos" instead.

  - `terms.paymentFrequencyType` (string)
    Deprecated, use "paymentFrequencyDto.type" instead.
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `terms.price` (number)
    Deprecated, use "paymentFrequencyDto.money.amount" instead.

  - `terms.termUnit` (string, required)
    Deprecated, use "term.termUnit" instead.
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.termValue` (integer, required)
    Deprecated, use "term.term" instead.

## Response 403 fields (*/*):

  - `errorCodes` (array, required)
    Generic categories of errors. You may map them to default responses
    Enum: "ENTITY_NOT_FOUND", "CONFLICT", "BAD_REQUEST", "REQUIRED_PARAMETER_MISSING", "VALIDATION_FAILED", "FORBIDDEN", "OPERATION_NOT_ALLOWED_FOR_STUDIO", "SERVER_ERROR", "FEATURE_DISABLED", "STUDIO_NOT_IN_GERMANY", "VOUCHER_VALIDATION_FAILED_INVALID_CODE", "VOUCHER_VALIDATION_FAILED_NOT_REDEEMABLE_HERE", "VOUCHER_VALIDATION_FAILED_NOT_IN_VALIDITY_PERIOD", "VOUCHER_VALIDATION_FAILED_NOT_ALLOWED_FOR_RATE", "TRIALSESSION_ALREADY_BOOKED", "ACTIVE_MEMBER_CANNOT_BOOK_TRIAL_SESSION"

  - `message` (string)
    For developer integration and logging purposes. Do not show message in client!

  - `traceId` (string)
    Trace id

## Response 409 fields (*/*):

  - `errorCodes` (array, required)
    Generic categories of errors. You may map them to default responses
    Enum: "ENTITY_NOT_FOUND", "CONFLICT", "BAD_REQUEST", "REQUIRED_PARAMETER_MISSING", "VALIDATION_FAILED", "FORBIDDEN", "OPERATION_NOT_ALLOWED_FOR_STUDIO", "SERVER_ERROR", "FEATURE_DISABLED", "STUDIO_NOT_IN_GERMANY", "VOUCHER_VALIDATION_FAILED_INVALID_CODE", "VOUCHER_VALIDATION_FAILED_NOT_REDEEMABLE_HERE", "VOUCHER_VALIDATION_FAILED_NOT_IN_VALIDITY_PERIOD", "VOUCHER_VALIDATION_FAILED_NOT_ALLOWED_FOR_RATE", "TRIALSESSION_ALREADY_BOOKED", "ACTIVE_MEMBER_CANNOT_BOOK_TRIAL_SESSION"

  - `message` (string)
    For developer integration and logging purposes. Do not show message in client!

  - `traceId` (string)
    Trace id

## Response 500 fields (*/*):

  - `errorCodes` (array, required)
    Generic categories of errors. You may map them to default responses
    Enum: "ENTITY_NOT_FOUND", "CONFLICT", "BAD_REQUEST", "REQUIRED_PARAMETER_MISSING", "VALIDATION_FAILED", "FORBIDDEN", "OPERATION_NOT_ALLOWED_FOR_STUDIO", "SERVER_ERROR", "FEATURE_DISABLED", "STUDIO_NOT_IN_GERMANY", "VOUCHER_VALIDATION_FAILED_INVALID_CODE", "VOUCHER_VALIDATION_FAILED_NOT_REDEEMABLE_HERE", "VOUCHER_VALIDATION_FAILED_NOT_IN_VALIDITY_PERIOD", "VOUCHER_VALIDATION_FAILED_NOT_ALLOWED_FOR_RATE", "TRIALSESSION_ALREADY_BOOKED", "ACTIVE_MEMBER_CANNOT_BOOK_TRIAL_SESSION"

  - `message` (string)
    For developer integration and logging purposes. Do not show message in client!

  - `traceId` (string)
    Trace id

