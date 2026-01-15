# Get membership switch configuration by id for a customer

Required Scopes: 

Returns extended information about the membership offer.

Endpoint: GET /v1/memberships/{customerId}/membership-switch/configs/{configId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer to load a membership switch configuration for

  - `configId` (integer, required)
    The ID of the membership switch configuration

## Query parameters:

  - `studioId` (integer)
    An optional studio ID to validate whether the specified membership switch configuration is available for that studio

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the configuration
    Example: 1000

  - `name` (string, required)
    Name of the configuration
    Example: "Premium Membership Upgrade"

  - `presentation` (object, required)
    Presentation details for the membership switch configuration

  - `presentation.bannerText` (string)
    Text associated to the configured presentation banner

  - `presentation.imageUrl` (string)
    Image URL of the presentation banner. It will expire after 15 minutes.

  - `sourceContracts` (array, required)
    List of source contracts for the membership switch

  - `sourceContracts.id` (integer, required)
    Unique ID of the source contract rate
    Example: 1000

  - `sourceContracts.rateName` (string, required)
    Name of the source contract rate
    Example: "Basic Membership"

  - `destinationMembershipOffers` (array, required)
    List of destination membership offers

  - `destinationMembershipOffers.id` (integer, required)
    Unique identifier for the membership offer.

  - `destinationMembershipOffers.description` (string, required)
    Description of the membership offer.
    Example: "This offer includes access to all gym facilities and group classes."

  - `destinationMembershipOffers.name` (string, required)
    Name of the membership offer.
    Example: "Standard Membership"

  - `destinationMembershipOffers.subDescription` (string)
    Sub description for the membership offer.
    Example: "Best value for regular gym-goers."

  - `destinationMembershipOffers.imageUrl` (string)
    Temporary valid download link for rate bundle image. Expires after 2 hours.
    Example: "https://example.com"

  - `destinationMembershipOffers.footnote` (string)
    Contractual or legal comments to be displayed below the offer.
    Example: "This offer is valid for new members only. Terms and conditions apply."

  - `destinationMembershipOffers.preUseType` (string, required)
    Contract pre-use type information.
    Enum: "NOT_AVAILABLE", "CHARGEABLE", "FREE"

  - `destinationMembershipOffers.limitedOfferingPeriod` (object, required)
    Period in which the membership offer is valid.

  - `destinationMembershipOffers.limitedOfferingPeriod.startDate` (string, required)
    Start of the interval
    Example: "2025-01-01"

  - `destinationMembershipOffers.limitedOfferingPeriod.endDate` (string, required)
    End of the interval
    Example: "2026-01-01"

  - `destinationMembershipOffers.rateCodes` (array, required)
    Rate codes of the membership offer.

  - `destinationMembershipOffers.rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `destinationMembershipOffers.rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `destinationMembershipOffers.includedModules` (array, required)
    List of included modules of this membership offer.

  - `destinationMembershipOffers.includedModules.id` (integer, required)
    Unique identifier for the membership offer module.
    Example: 1234567890

  - `destinationMembershipOffers.includedModules.name` (string, required)
    Name of the membership offer module.
    Example: "Premium Fitness Package"

  - `destinationMembershipOffers.includedModules.description` (string, required)
    Description of the membership offer module.
    Example: "Includes access to all gym facilities and group classes."

  - `destinationMembershipOffers.includedModules.imageUrl` (string)
    Image url of membership offer module. Expires after 5hours.
    Example: "https://some-module.com"

  - `destinationMembershipOffers.includedModules.term` (object, required)
    Represents the terms of a membership offer.

  - `destinationMembershipOffers.includedModules.term.extensionType` (string, required)
    Module term extension type
    Enum: "NONE", "TERM_EXTENSION", "SUBSEQUENT_RATE_DETAIL"

  - `destinationMembershipOffers.includedModules.term.term` (object)
    Represents a term

  - `destinationMembershipOffers.includedModules.term.term.value` (integer, required)
    The value of the term
    Example: 2

  - `destinationMembershipOffers.includedModules.term.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `destinationMembershipOffers.includedModules.term.termExtension` (object)
    Represents a term

  - `destinationMembershipOffers.includedModules.term.cancelationPeriod` (object)
    Represents a term

  - `destinationMembershipOffers.includedModules.term.extensionCancelationPeriod` (object)
    Represents a term

  - `destinationMembershipOffers.includedModules.trialPeriod` (object)
    Represents the trial period of a membership offer.

  - `destinationMembershipOffers.includedModules.trialPeriod.trialPeriod` (object, required)
    The trial period of the membership offer

  - `destinationMembershipOffers.includedModules.trialPeriod.description` (string, required)
    Description of the trial period
    Example: "Free trial for 30 days"

  - `destinationMembershipOffers.includedModules.consentTextBlock` (object)
    Contract text block information.

  - `destinationMembershipOffers.includedModules.consentTextBlock.id` (integer)
    The unique identifier of the text block
    Example: 1234567890

  - `destinationMembershipOffers.includedModules.consentTextBlock.title` (string)
    The title of the text block
    Example: "Title of 1. text block"

  - `destinationMembershipOffers.includedModules.consentTextBlock.text` (string)
    The text of the text block
    Example: "Text of 1. text block"

  - `destinationMembershipOffers.includedModules.consentTextBlock.order` (integer)
    The order of the text block in the contract
    Example: 1

  - `destinationMembershipOffers.includedModules.consentTextBlock.hasSignature` (boolean)
    Text block configuration has a signature field. You have the option to show a signature input field and it will be added in the contract document. It is not a required field in magicline. It is up to your implementation if you add this field.

  - `destinationMembershipOffers.includedModules.consentTextBlock.showCommunicationPrivacyOptions` (boolean)
    Text block contains information about the communication privacy options. You are advised to show a matrix with communication settings in combination with this text block.

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachmentType` (string)
    Indicates the type of attachment for this block
    Enum: "NONE", "FILE", "URL", "CONTRACT_PDF_PREVIEW"

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachedExternalUrlDto` (object)
    Represents url information.

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachedExternalUrlDto.title` (string, required)
    Url title
    Example: "Example Resource"

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachedExternalUrlDto.url` (string, required)
    Url to access the resource
    Example: "https://some-url.com"

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachedDocument` (object)
    Represents document information.

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachedDocument.fileName` (string, required)
    Name of the file to download
    Example: "contract.pdf"

  - `destinationMembershipOffers.includedModules.consentTextBlock.attachedDocument.url` (string, required)
    Temporary valid download link. Expires after 5 hours.
    Example: "https://some-url.com"

  - `destinationMembershipOffers.includedModules.consentTextBlock.rateBundleModuleId` (integer)
    The ID of the associated rate bundle module. Only set if this is a module consent text block.
    Example: 1234567890

  - `destinationMembershipOffers.includedModules.consentTextBlock.confirmationRequired` (boolean)

  - `destinationMembershipOffers.includedModules.rateCodes` (array)
    Rate codes of the membership offer module.

  - `destinationMembershipOffers.contractSignaturesRequired` (boolean)
    Indicates if contract signatures are required for this membership offer.

  - `destinationMembershipOffers.allowedPaymentChoices` (array, required)
    Allowed payment choices for this membership offer.
    Enum: "CASH", "BANK_TRANSFER", "BACS", "SEPA", "CH_DD", "LSV", "CREDIT_CARD", "TWINT", "PAYPAL", "BANCONTACT", "IDEAL"

  - `destinationMembershipOffers.maximumNumberOfSelectableModules` (integer)
    Maximum number of  for this membership offer. If 0, no modules can be selected.

  - `destinationMembershipOffers.contractTextBlocks` (array, required)
    List of contract text blocks that are part of this membership offer.

  - `destinationMembershipOffers.selectableModules` (array)
    List of selectable modules for this membership offer. Limited by .

  - `destinationMembershipOffers.selectableModules.paymentFrequency` (object, required)
    Represents the payment frequency

  - `destinationMembershipOffers.selectableModules.paymentFrequency.id` (integer)
    The unique identifier of the payment frequency. ( possible for starter package)
    Example: 1234567890

  - `destinationMembershipOffers.selectableModules.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `destinationMembershipOffers.selectableModules.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `destinationMembershipOffers.selectableModules.paymentFrequency.price.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `destinationMembershipOffers.selectableModules.paymentFrequency.price.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `destinationMembershipOffers.selectableModules.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `destinationMembershipOffers.selectableModules.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `destinationMembershipOffers.selectableModules.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `destinationMembershipOffers.selectableModules.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `destinationMembershipOffers.selectableModules.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `destinationMembershipOffers.selectableModules.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `destinationMembershipOffers.selectableModules.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active  the respective term has passed

  - `destinationMembershipOffers.selectableModules.paymentFrequency.recurring` (boolean)
    Whether the cycle of payments repeats indefinitely. Only relevant if type is  or .

  - `destinationMembershipOffers.selectableModules.paymentFrequency.ageBasedAdjustments` (array)
    List of age-based adjustments for the membership offer module.

  - `destinationMembershipOffers.selectableModules.paymentFrequency.ageBasedAdjustments.ageRange` (object, required)
    Represents an age range.

  - `destinationMembershipOffers.selectableModules.paymentFrequency.ageBasedAdjustments.ageRange.startAge` (integer, required)
    Start age of the range, inclusive.
    Example: 18

  - `destinationMembershipOffers.selectableModules.paymentFrequency.ageBasedAdjustments.ageRange.endAge` (integer, required)
    End age of the range, inclusive.
    Example: 65

  - `destinationMembershipOffers.selectableModules.paymentFrequency.ageBasedAdjustments.value` (number, required)
    The value of the adjustment, based on .
    Example: 10

  - `destinationMembershipOffers.selectableModules.paymentFrequency.ageBasedAdjustments.type` (string, required)
    Age based adjustment type
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `destinationMembershipOffers.selectableModules.paymentFrequency.formattedPaymentFrequency` (string, required)
    The formatted payment frequency
    Example: "Every 6 months"

  - `destinationMembershipOffers.terms` (array)
    List of terms that are part of this membership offer.

  - `destinationMembershipOffers.terms.id` (integer, required)
    Unique identifier of the membership offer term
    Example: 1234567890

  - `destinationMembershipOffers.terms.contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month
 and per the rate's payment frequency (e.g. 1 week)

  - `destinationMembershipOffers.terms.contractVolumeInformation.totalContractVolume` (object)
    Total contract volume
    Example: 600

  - `destinationMembershipOffers.terms.contractVolumeInformation.averagePaymentVolumePerMonth` (object)
    Average payment volume per month
    Example: 50

  - `destinationMembershipOffers.terms.contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (object)
    Average payment volume per payment frequency term
    Example: 50

  - `destinationMembershipOffers.terms.extensionTerm` (object)
    Represents a term

  - `destinationMembershipOffers.terms.defaultContractStartDate` (string)
    The default contract start date
    Example: "2025-08-24"

  - `destinationMembershipOffers.terms.defaultContractStartDateOfUse` (string)
    The default contract start date of use
    Example: "2025-09-01"

  - `destinationMembershipOffers.terms.priceAdjustmentRules` (array)
    Price adjustment rules that are part of this membership offer term.

  - `destinationMembershipOffers.terms.priceAdjustmentRules.defaultDescription` (string, required)
    A complete formatted sentence which contains all details about this price adjustment rule. If the presentation should differ use the separate attributes.
    Example: "Formatted description of price adjustment rule"

  - `destinationMembershipOffers.terms.priceAdjustmentRules.value` (string, required)
    Value of price adjustment rule, might be percentage or amount, depends on
    Example: "5%"

  - `destinationMembershipOffers.terms.priceAdjustmentRules.recurrenceFrequency` (string, required)
    Recurrence of price adjustment rule, how often and when applies this rule
    Example: "monthly"

  - `destinationMembershipOffers.terms.priceAdjustmentRules.type` (string, required)
    States how the rule adjusts the price
    Enum: "RAISE", "REDUCTION", "NEW_BASIC_AMOUNT"

  - `destinationMembershipOffers.terms.priceAdjustmentRules.chargeAdjustmentType` (string, required)
    How the rule changes the price
    Enum: "RELATIVE", "ABSOLUTE", "BASIC_AMOUNT"

  - `destinationMembershipOffers.terms.flatFees` (array, required)
    Flat fees that are part of this membership offer.

  - `destinationMembershipOffers.terms.flatFees.name` (string, required)
    The name of the flat fee
    Example: "Starter Package"

  - `destinationMembershipOffers.terms.flatFees.identifier` (string)
    The identifier of the flat fee
    Example: "ID12345"

  - `destinationMembershipOffers.terms.flatFees.formattedPaymentFrequency` (string, required)
    The formatted payment frequency of the flat fee
    Example: "12M"

  - `destinationMembershipOffers.terms.flatFees.firstBookingDelay` (object)
    The delay before the first booking can be made

  - `destinationMembershipOffers.terms.flatFees.starterPackage` (boolean)

  - `destinationMembershipOffers.terms.extensionFixedTerm` (object)
    The fixed term for the extension of the contract.

  - `destinationMembershipOffers.terms.extensionType` (string, required)
    Membership offer extension type
    Enum: "NONE", "TERM_EXTENSION", "SUBSEQUENT_RATE_DETAIL"

  - `destinationMembershipOffers.terms.subsequentRate` (object)
    Represents a subsequent rate for a membership offer.

  - `destinationMembershipOffers.terms.subsequentRate.name` (string, required)
    Name of the subsequent rate
    Example: "Combined fitness and wellness"

  - `destinationMembershipOffers.terms.cancelationStrategy` (string, required)
    Membership offer cancelation strategy
    Enum: "TERM", "RECEIPT_DATE"

  - `destinationMembershipOffers.terms.cancelationPeriod` (object)
    The cancelation period for the contract.

  - `destinationMembershipOffers.terms.extensionCancelationPeriod` (object)
    The cancelation period for the extension of the contract.

  - `destinationMembershipOffers.terms.rateBonusPeriods` (array)
    Rate bonus periods that are part of this membership offer term.

  - `destinationMembershipOffers.terms.rateBonusPeriods.term` (object, required)
    The term of the bonus period

  - `destinationMembershipOffers.terms.rateBonusPeriods.termStrategy` (string, required)
    Membership offer rate bonus period term strategy.
    Enum: "CONTRACT_START", "FIXED", "END_OF_CURRENT_TERM", "START_OF_NEXT_TERM"

  - `destinationMembershipOffers.terms.rateBonusPeriods.displaySeparately` (boolean)
    Indicates whether the bonus period should be displayed separately in the offer details
    Example: true

  - `destinationMembershipOffers.terms.rateBonusPeriods.runtimeExtensionType` (string, required)
    Membership offer bonus period type.
    Enum: "WITH_EXTENSION", "WITHOUT_EXTENSION"

  - `destinationMembershipOffers.terms.rateBonusPeriods.extendsCancellationPeriod` (boolean)
    Indicates whether the bonus period extends the cancellation period

  - `destinationMembershipOffers.terms.rateStartPrice` (object)
    Price for the first period of the contract, if the term has bonus period at the beginning of the contract then it is equal to 0, otherwise is equal to term price.

  - `destinationMembershipOffers.terms.optionalModules` (array)
    Optional modules additionally payable.

  - `destinationMembershipOffers.terms.termAfterExtension` (object)
    The new term after minimum contract duration. Null if not configured.

  - `destinationMembershipOffers.terms.priceAfterExtension` (object)
    The new price after minimum contract duration. Null if not configured.

  - `destinationMembershipOffers.timeRestrictions` (object)
    Time restrictions for this membership offer based on opening hours categories. Null if no restrictions apply.

  - `destinationMembershipOffers.timeRestrictions.openingHoursCategory` (object)
    Opening hours category that defines these restrictions

  - `destinationMembershipOffers.timeRestrictions.openingHoursCategory.categoryId` (integer, required)
    ID of the opening hours category
    Example: 1234567890

  - `destinationMembershipOffers.timeRestrictions.openingHoursCategory.name` (string, required)
    Name of the opening hours category
    Example: "Off-Peak"

  - `destinationMembershipOffers.timeRestrictions.availabilities` (array)
    List of availabilities for this offer

  - `destinationMembershipOffers.timeRestrictions.availabilities.dayOfWeek` (string, required)
    Day of the week
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `destinationMembershipOffers.timeRestrictions.availabilities.timeFrom` (string, required)
    Start time in ISO-8601 format
    Example: "06:00:00"

  - `destinationMembershipOffers.timeRestrictions.availabilities.timeTo` (string, required)
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

