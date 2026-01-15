# Get membership offer by id

Required Scopes: 

Returns extended information about the membership offer.

Endpoint: GET /v1/memberships/membership-offers/{membershipOfferId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `membershipOfferId` (integer, required)

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique identifier for the membership offer.

  - `description` (string, required)
    Description of the membership offer.
    Example: "This offer includes access to all gym facilities and group classes."

  - `name` (string, required)
    Name of the membership offer.
    Example: "Standard Membership"

  - `subDescription` (string)
    Sub description for the membership offer.
    Example: "Best value for regular gym-goers."

  - `imageUrl` (string)
    Temporary valid download link for rate bundle image. Expires after 2 hours.
    Example: "https://example.com"

  - `footnote` (string)
    Contractual or legal comments to be displayed below the offer.
    Example: "This offer is valid for new members only. Terms and conditions apply."

  - `preUseType` (string, required)
    Contract pre-use type information.
    Enum: "NOT_AVAILABLE", "CHARGEABLE", "FREE"

  - `limitedOfferingPeriod` (object, required)
    Period in which the membership offer is valid.

  - `limitedOfferingPeriod.startDate` (string, required)
    Start of the interval
    Example: "2025-01-01"

  - `limitedOfferingPeriod.endDate` (string, required)
    End of the interval
    Example: "2026-01-01"

  - `rateCodes` (array, required)
    Rate codes of the membership offer.

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `includedModules` (array, required)
    List of included modules of this membership offer.

  - `includedModules.id` (integer, required)
    Unique identifier for the membership offer module.
    Example: 1234567890

  - `includedModules.name` (string, required)
    Name of the membership offer module.
    Example: "Premium Fitness Package"

  - `includedModules.description` (string, required)
    Description of the membership offer module.
    Example: "Includes access to all gym facilities and group classes."

  - `includedModules.imageUrl` (string)
    Image url of membership offer module. Expires after 5hours.
    Example: "https://some-module.com"

  - `includedModules.term` (object, required)
    Represents the terms of a membership offer.

  - `includedModules.term.extensionType` (string, required)
    Module term extension type
    Enum: "NONE", "TERM_EXTENSION", "SUBSEQUENT_RATE_DETAIL"

  - `includedModules.term.term` (object)
    Represents a term

  - `includedModules.term.term.value` (integer, required)
    The value of the term
    Example: 2

  - `includedModules.term.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `includedModules.term.termExtension` (object)
    Represents a term

  - `includedModules.term.cancelationPeriod` (object)
    Represents a term

  - `includedModules.term.extensionCancelationPeriod` (object)
    Represents a term

  - `includedModules.trialPeriod` (object)
    Represents the trial period of a membership offer.

  - `includedModules.trialPeriod.trialPeriod` (object, required)
    The trial period of the membership offer

  - `includedModules.trialPeriod.description` (string, required)
    Description of the trial period
    Example: "Free trial for 30 days"

  - `includedModules.consentTextBlock` (object)
    Contract text block information.

  - `includedModules.consentTextBlock.id` (integer)
    The unique identifier of the text block
    Example: 1234567890

  - `includedModules.consentTextBlock.title` (string)
    The title of the text block
    Example: "Title of 1. text block"

  - `includedModules.consentTextBlock.text` (string)
    The text of the text block
    Example: "Text of 1. text block"

  - `includedModules.consentTextBlock.order` (integer)
    The order of the text block in the contract
    Example: 1

  - `includedModules.consentTextBlock.hasSignature` (boolean)
    Text block configuration has a signature field. You have the option to show a signature input field and it will be added in the contract document. It is not a required field in magicline. It is up to your implementation if you add this field.

  - `includedModules.consentTextBlock.showCommunicationPrivacyOptions` (boolean)
    Text block contains information about the communication privacy options. You are advised to show a matrix with communication settings in combination with this text block.

  - `includedModules.consentTextBlock.attachmentType` (string)
    Indicates the type of attachment for this block
    Enum: "NONE", "FILE", "URL", "CONTRACT_PDF_PREVIEW"

  - `includedModules.consentTextBlock.attachedExternalUrlDto` (object)
    Represents url information.

  - `includedModules.consentTextBlock.attachedExternalUrlDto.title` (string, required)
    Url title
    Example: "Example Resource"

  - `includedModules.consentTextBlock.attachedExternalUrlDto.url` (string, required)
    Url to access the resource
    Example: "https://some-url.com"

  - `includedModules.consentTextBlock.attachedDocument` (object)
    Represents document information.

  - `includedModules.consentTextBlock.attachedDocument.fileName` (string, required)
    Name of the file to download
    Example: "contract.pdf"

  - `includedModules.consentTextBlock.attachedDocument.url` (string, required)
    Temporary valid download link. Expires after 5 hours.
    Example: "https://some-url.com"

  - `includedModules.consentTextBlock.rateBundleModuleId` (integer)
    The ID of the associated rate bundle module. Only set if this is a module consent text block.
    Example: 1234567890

  - `includedModules.consentTextBlock.confirmationRequired` (boolean)

  - `includedModules.rateCodes` (array)
    Rate codes of the membership offer module.

  - `contractSignaturesRequired` (boolean)
    Indicates if contract signatures are required for this membership offer.

  - `allowedPaymentChoices` (array, required)
    Allowed payment choices for this membership offer.
    Enum: "CASH", "BANK_TRANSFER", "BACS", "SEPA", "CH_DD", "LSV", "CREDIT_CARD", "TWINT", "PAYPAL", "BANCONTACT", "IDEAL"

  - `maximumNumberOfSelectableModules` (integer)
    Maximum number of  for this membership offer. If 0, no modules can be selected.

  - `contractTextBlocks` (array, required)
    List of contract text blocks that are part of this membership offer.

  - `selectableModules` (array)
    List of selectable modules for this membership offer. Limited by .

  - `selectableModules.paymentFrequency` (object, required)
    Represents the payment frequency

  - `selectableModules.paymentFrequency.id` (integer)
    The unique identifier of the payment frequency. ( possible for starter package)
    Example: 1234567890

  - `selectableModules.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `selectableModules.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `selectableModules.paymentFrequency.price.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `selectableModules.paymentFrequency.price.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `selectableModules.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `selectableModules.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `selectableModules.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `selectableModules.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `selectableModules.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `selectableModules.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `selectableModules.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active  the respective term has passed

  - `selectableModules.paymentFrequency.recurring` (boolean)
    Whether the cycle of payments repeats indefinitely. Only relevant if type is  or .

  - `selectableModules.paymentFrequency.ageBasedAdjustments` (array)
    List of age-based adjustments for the membership offer module.

  - `selectableModules.paymentFrequency.ageBasedAdjustments.ageRange` (object, required)
    Represents an age range.

  - `selectableModules.paymentFrequency.ageBasedAdjustments.ageRange.startAge` (integer, required)
    Start age of the range, inclusive.
    Example: 18

  - `selectableModules.paymentFrequency.ageBasedAdjustments.ageRange.endAge` (integer, required)
    End age of the range, inclusive.
    Example: 65

  - `selectableModules.paymentFrequency.ageBasedAdjustments.value` (number, required)
    The value of the adjustment, based on .
    Example: 10

  - `selectableModules.paymentFrequency.ageBasedAdjustments.type` (string, required)
    Age based adjustment type
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `selectableModules.paymentFrequency.formattedPaymentFrequency` (string, required)
    The formatted payment frequency
    Example: "Every 6 months"

  - `terms` (array)
    List of terms that are part of this membership offer.

  - `terms.id` (integer, required)
    Unique identifier of the membership offer term
    Example: 1234567890

  - `terms.contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month
 and per the rate's payment frequency (e.g. 1 week)

  - `terms.contractVolumeInformation.totalContractVolume` (object)
    Total contract volume
    Example: 600

  - `terms.contractVolumeInformation.averagePaymentVolumePerMonth` (object)
    Average payment volume per month
    Example: 50

  - `terms.contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (object)
    Average payment volume per payment frequency term
    Example: 50

  - `terms.extensionTerm` (object)
    Represents a term

  - `terms.defaultContractStartDate` (string)
    The default contract start date
    Example: "2025-08-24"

  - `terms.defaultContractStartDateOfUse` (string)
    The default contract start date of use
    Example: "2025-09-01"

  - `terms.priceAdjustmentRules` (array)
    Price adjustment rules that are part of this membership offer term.

  - `terms.priceAdjustmentRules.defaultDescription` (string, required)
    A complete formatted sentence which contains all details about this price adjustment rule. If the presentation should differ use the separate attributes.
    Example: "Formatted description of price adjustment rule"

  - `terms.priceAdjustmentRules.value` (string, required)
    Value of price adjustment rule, might be percentage or amount, depends on
    Example: "5%"

  - `terms.priceAdjustmentRules.recurrenceFrequency` (string, required)
    Recurrence of price adjustment rule, how often and when applies this rule
    Example: "monthly"

  - `terms.priceAdjustmentRules.type` (string, required)
    States how the rule adjusts the price
    Enum: "RAISE", "REDUCTION", "NEW_BASIC_AMOUNT"

  - `terms.priceAdjustmentRules.chargeAdjustmentType` (string, required)
    How the rule changes the price
    Enum: "RELATIVE", "ABSOLUTE", "BASIC_AMOUNT"

  - `terms.flatFees` (array, required)
    Flat fees that are part of this membership offer.

  - `terms.flatFees.name` (string, required)
    The name of the flat fee
    Example: "Starter Package"

  - `terms.flatFees.identifier` (string)
    The identifier of the flat fee
    Example: "ID12345"

  - `terms.flatFees.formattedPaymentFrequency` (string, required)
    The formatted payment frequency of the flat fee
    Example: "12M"

  - `terms.flatFees.firstBookingDelay` (object)
    The delay before the first booking can be made

  - `terms.flatFees.starterPackage` (boolean)

  - `terms.extensionFixedTerm` (object)
    The fixed term for the extension of the contract.

  - `terms.extensionType` (string, required)
    Membership offer extension type
    Enum: "NONE", "TERM_EXTENSION", "SUBSEQUENT_RATE_DETAIL"

  - `terms.subsequentRate` (object)
    Represents a subsequent rate for a membership offer.

  - `terms.subsequentRate.name` (string, required)
    Name of the subsequent rate
    Example: "Combined fitness and wellness"

  - `terms.cancelationStrategy` (string, required)
    Membership offer cancelation strategy
    Enum: "TERM", "RECEIPT_DATE"

  - `terms.cancelationPeriod` (object)
    The cancelation period for the contract.

  - `terms.extensionCancelationPeriod` (object)
    The cancelation period for the extension of the contract.

  - `terms.rateBonusPeriods` (array)
    Rate bonus periods that are part of this membership offer term.

  - `terms.rateBonusPeriods.term` (object, required)
    The term of the bonus period

  - `terms.rateBonusPeriods.termStrategy` (string, required)
    Membership offer rate bonus period term strategy.
    Enum: "CONTRACT_START", "FIXED", "END_OF_CURRENT_TERM", "START_OF_NEXT_TERM"

  - `terms.rateBonusPeriods.displaySeparately` (boolean)
    Indicates whether the bonus period should be displayed separately in the offer details
    Example: true

  - `terms.rateBonusPeriods.runtimeExtensionType` (string, required)
    Membership offer bonus period type.
    Enum: "WITH_EXTENSION", "WITHOUT_EXTENSION"

  - `terms.rateBonusPeriods.extendsCancellationPeriod` (boolean)
    Indicates whether the bonus period extends the cancellation period

  - `terms.rateStartPrice` (object)
    Price for the first period of the contract, if the term has bonus period at the beginning of the contract then it is equal to 0, otherwise is equal to term price.

  - `terms.optionalModules` (array)
    Optional modules additionally payable.

  - `terms.termAfterExtension` (object)
    The new term after minimum contract duration. Null if not configured.

  - `terms.priceAfterExtension` (object)
    The new price after minimum contract duration. Null if not configured.

  - `timeRestrictions` (object)
    Time restrictions for this membership offer based on opening hours categories. Null if no restrictions apply.

  - `timeRestrictions.openingHoursCategory` (object)
    Opening hours category that defines these restrictions

  - `timeRestrictions.openingHoursCategory.categoryId` (integer, required)
    ID of the opening hours category
    Example: 1234567890

  - `timeRestrictions.openingHoursCategory.name` (string, required)
    Name of the opening hours category
    Example: "Off-Peak"

  - `timeRestrictions.availabilities` (array)
    List of availabilities for this offer

  - `timeRestrictions.availabilities.dayOfWeek` (string, required)
    Day of the week
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `timeRestrictions.availabilities.timeFrom` (string, required)
    Start time in ISO-8601 format
    Example: "06:00:00"

  - `timeRestrictions.availabilities.timeTo` (string, required)
    End time in ISO-8601 format
    Example: "23:00:00"

## Response 400 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 401 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 403 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 404 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 409 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 429 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 500 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

