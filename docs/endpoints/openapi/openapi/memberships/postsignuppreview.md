# Preview information before signing up for a new membership

Required Scopes: 

Endpoint: POST /v1/memberships/signup/preview
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `contract` (object, required)
    The contract information used for the membership signup

  - `contract.contractOfferTermId` (integer, required)
    Unique ID of the contract offer term
    Example: 1000

  - `contract.startDate` (string, required)
    The start date of the contract
    Example: "2026-02-01"

  - `contract.preuseDate` (string)
    The pre use date of the contract. If not provided, it will be evaluated based on contract offer configuration.
    Example: "2026-01-01"

  - `contract.notes` (string)
    The notes related to the contract
    Example: "Some notes"

  - `contract.thirdPartyId` (string)
    Unique ID of the third party contract in the third party system
    Example: "1000a"

  - `contract.employeeId` (integer)
    Unique ID of the employee who created the membership
    Example: 1239812733

  - `contract.referralCode` (string)
    Referral code to link with recruiter
    Example: "A500D"

  - `contract.selectedSelectableModuleIds` (array)
    The selected modules from the available selectable modules

  - `contract.selectedOptionalModuleIds` (array)
    The selected modules from the available optional modules

  - `contract.initialPaymentRequestToken` (string)
    This token identifies a pre-authorized payment request. It acts as a reference to the payment session initiated by the user. It's not needed for preview endpoints.
    Example: "3JtyH5sakfn2V22vB0napNC2zWMlpFwS9gPQawuk7Jw1F00atOD0BA"

  - `contract.contractSignature` (object)
    The signature SVG for the contract document

  - `contract.contractSignature.base64SvgSignature` (string, required)
    Customer confirmation signature SVG value as base 64 string

  - `contract.textBlockSignatures` (array)
    Signatures for text blocks

  - `contract.textBlockSignatures.base64SvgSignature` (string, required)
    Text block's signature SVG value as base 64 string

  - `contract.textBlockSignatures.textBlockId` (integer, required)
    The ID of the referenced text block of the signature

  - `contract.voucherCode` (string)
    An optional code for a voucher. Only credit and discount vouchers are supported.
    Example: 123

  - `customer` (object, required)
    The customer information used for the membership signup

  - `customer.thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `customer.firstName` (string, required)
    First name of the customer
    Example: "Peter"

  - `customer.secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `customer.lastName` (string, required)
    Last name of the customer
    Example: "Muller"

  - `customer.secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `customer.dateOfBirth` (string, required)
    Date of birth of the customer
    Example: "2019-08-24"

  - `customer.placeOfBirth` (string)
    Place of birth of the customer. Required for Italian studios and nationals.

  - `customer.countryOfBirth` (string)
    Country of birth of the customer. Required for Italian studios and non-Italian nationals

  - `customer.email` (string, required)
    Email address of the customer
    Example: "example@example.com"

  - `customer.gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `customer.phoneNumberPrivate` (string)
    Private phone number of the customer
    Example: "+44123456789"

  - `customer.phoneNumberMobile` (string)
    Mobile phone number of the customer
    Example: "+44987654321"

  - `customer.street` (string, required)
    Street of the customer's address
    Example: "Raboisen Street"

  - `customer.secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `customer.cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `customer.district` (string)
    District of the customer's address
    Example: "District 12"

  - `customer.streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `customer.streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `customer.portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `customer.stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `customer.door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `customer.province` (string)
    Province of the customer's address
    Example: "Champagne"

  - `customer.additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `customer.floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `customer.language` (object, required)
    Language of the customer

  - `customer.language.languageCode` (string, required)
    The language code
    Example: "de"

  - `customer.language.countryCode` (string)
    The country code
    Example: "DE"

  - `customer.houseNumber` (string)
    House number of the customer's address
    Example: "3-4"

  - `customer.buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `customer.city` (string, required)
    City of the customer's address
    Example: "Hamburg"

  - `customer.zipCode` (string, required)
    Zip code of the customer's address
    Example: "220-99"

  - `customer.countryCode` (string, required)
    Country code of the customer's address
    Example: "DE"

  - `customer.taxId` (string)
    Required if the studio is located in Spain or Italy. Alternatively, a valid document identification can be provided.
    Example: "12345678A"

  - `customer.communicationPreferences` (array)
    List of communication preferences for the customer

  - `customer.communicationPreferences.messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `customer.communicationPreferences.channels` (array)
    The communication channels related to the message category of the communication preference

  - `customer.communicationPreferences.channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `customer.communicationPreferences.channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `customer.communicationPreferences.channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

  - `customer.documentIdentification` (object)
    Information from an official document that identifies the customer

  - `customer.documentIdentification.documentNumber` (string, required)
    Document number
    Example: "CX5432112345DS"

  - `customer.documentIdentification.documentType` (string, required)
    Type of the document
    Enum: "ID_CARD", "PASSPORT", "DRIVERS_LICENCE", "RESIDENCE_PERMIT", "NATIONAL_ID_NUMBER", "OTHERS"

  - `customer.paymentRequestToken` (string)
    By assigning the  to the customer, the payment method associated with the token will be used as payment method setting of the customer. Additionally, if the  is associated with a payment instrument, i.e. a SEPA Mandate, BACS Mandate, Credit Card, or other, the payment instrument will be made available in the member account for future collection via payment runs. By leaving this field empty the payment method of the customer will be set to . For reference check 'Create a user payment session'.

  - `customer.additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `customer.additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `customer.additionalInformationFieldAssignments.value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

## Response 200 fields (application/json):

  - `basePrice` (object, required)
    Base price of contract

  - `basePrice.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `basePrice.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `preUseCharge` (object)
    Charge for the time between the start date of use and start date

  - `voucherType` (string)
    Type of a voucher, if a valid voucher code has been provided
    Enum: "CONTRACT", "CREDIT", "DISCOUNT", "COMPANY_FEE_SPLIT", "CHECKIN"

  - `voucherRemarks` (string)
    Voucher remarks, if a valid voucher code has been provided
    Example: "Yoga class not included"

  - `voucherDiscountPeriods` (array)
    List of discount periods for the voucher, if a valid discount voucher code has been provided. Each period has its own discount and effective period.

  - `voucherDiscountPeriods.discountType` (string, required)
    Type of discount (percentage or absolute)
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `voucherDiscountPeriods.discountValue` (object, required)
    Discount value

  - `voucherDiscountPeriods.effectivePeriod` (string, required)
    The type of period for which this discount is applied
    Enum: "UNLIMITED", "INITIAL_TERM", "TIME_BASED"

  - `voucherDiscountPeriods.effectivePeriodTimeBasedTerm` (object)
    The term for which this discount is applied (only present when effectivePeriod is TIME_BASED)

  - `voucherDiscountPeriods.effectivePeriodTimeBasedTerm.value` (integer, required)
    The value of the term
    Example: 2

  - `voucherDiscountPeriods.effectivePeriodTimeBasedTerm.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `voucherDiscountPeriods.discountedBasePrice` (object)
    Discounted base price after applying this discount period

  - `voucherDiscountPeriods.companyAmount` (object)
    Amount the company has to pay during this discount period, if a valid company discount voucher code has been provided

  - `voucherDiscountPeriods.memberAmount` (object)
    Amount the member has to pay during this discount period, if a valid company discount voucher code has been provided

  - `discountedPreUseCharge` (object)
    Discounted pre-use charge, if a valid discount voucher code has been provided

  - `creditValue` (object)
    Voucher credit value, if a valid credit voucher code has been provided

  - `companyFeeSplitType` (string)
    Type of company fee split (percentage or absolute), if a valid company discount voucher code has been provided
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `companyFeeSplitValue` (object)
    Company fee split value, if a valid company discount voucher code has been provided

  - `companyName` (string)
    Name of the company that will pay the company amount, if a valid company discount voucher code has been provided
    Example: "Some company"

  - `companyAmount` (object)
    Amount the company has to pay, if a valid company discount voucher code has been provided. This field is populated when there are 0 or 1 discount periods. For multiple discount periods, use voucherDiscountPeriods[].companyAmount instead to see amounts per discount period.

  - `memberAmount` (object)
    Amount the member has to pay, if a valid company discount voucher code has been provided. This field is populated when there are 0 or 1 discount periods. For multiple discount periods, use voucherDiscountPeriods[].memberAmount instead to see amounts per discount period.

  - `companyAmountWithoutDiscount` (object)
    Amount the company has to pay without discount, if a valid company discount voucher code has been provided

  - `memberAmountWithoutDiscount` (object)
    Amount the member has to pay without discount, if a valid company discount voucher code has been provided

  - `voucherBonusPeriod` (object)
    Bonus period applied with the discount voucher, if valid a discount voucher has been provided

  - `voucherBonusPeriod.term` (object, required)
    The term of the bonus period

  - `voucherBonusPeriod.termStrategy` (string, required)
    Membership offer rate bonus period term strategy.
    Enum: "CONTRACT_START", "FIXED", "END_OF_CURRENT_TERM", "START_OF_NEXT_TERM"

  - `voucherBonusPeriod.displaySeparately` (boolean)
    Indicates whether the bonus period should be displayed separately in the offer details
    Example: true

  - `voucherBonusPeriod.runtimeExtensionType` (string, required)
    Membership offer bonus period type.
    Enum: "WITH_EXTENSION", "WITHOUT_EXTENSION"

  - `voucherBonusPeriod.extendsCancellationPeriod` (boolean)
    Indicates whether the bonus period extends the cancellation period

  - `voucherTextBlocks` (array)
    Voucher related text blocks, if a valid voucher code has been provided

  - `voucherTextBlocks.id` (integer)
    The unique identifier of the text block
    Example: 1234567890

  - `voucherTextBlocks.title` (string)
    The title of the text block
    Example: "Title of 1. text block"

  - `voucherTextBlocks.text` (string)
    The text of the text block
    Example: "Text of 1. text block"

  - `voucherTextBlocks.order` (integer)
    The order of the text block in the contract
    Example: 1

  - `voucherTextBlocks.hasSignature` (boolean)
    Text block configuration has a signature field. You have the option to show a signature input field and it will be added in the contract document. It is not a required field in magicline. It is up to your implementation if you add this field.

  - `voucherTextBlocks.showCommunicationPrivacyOptions` (boolean)
    Text block contains information about the communication privacy options. You are advised to show a matrix with communication settings in combination with this text block.

  - `voucherTextBlocks.attachmentType` (string)
    Indicates the type of attachment for this block
    Enum: "NONE", "FILE", "URL", "CONTRACT_PDF_PREVIEW"

  - `voucherTextBlocks.attachedExternalUrlDto` (object)
    Represents url information.

  - `voucherTextBlocks.attachedExternalUrlDto.title` (string, required)
    Url title
    Example: "Example Resource"

  - `voucherTextBlocks.attachedExternalUrlDto.url` (string, required)
    Url to access the resource
    Example: "https://some-url.com"

  - `voucherTextBlocks.attachedDocument` (object)
    Represents document information.

  - `voucherTextBlocks.attachedDocument.fileName` (string, required)
    Name of the file to download
    Example: "contract.pdf"

  - `voucherTextBlocks.attachedDocument.url` (string, required)
    Temporary valid download link. Expires after 5 hours.
    Example: "https://some-url.com"

  - `voucherTextBlocks.rateBundleModuleId` (integer)
    The ID of the associated rate bundle module. Only set if this is a module consent text block.
    Example: 1234567890

  - `voucherTextBlocks.confirmationRequired` (boolean)

  - `flatFeePreviews` (array)
    Flat fee previews, including discount if a valid discount voucher code has been provided

  - `flatFeePreviews.name` (string, required)
    Name of the sub contract
    Example: "Sauna"

  - `flatFeePreviews.discountPeriods` (array)
    List of discount periods for the sub contract, if a valid discount voucher code has been provided

  - `flatFeePreviews.companyAmount` (object)
    Amount the company has to pay for the sub contract, if a valid company discount voucher code has been provided. This field is populated when there are 0 or 1 discount periods. For multiple discount periods, use discountPeriods[].companyAmount instead to see amounts per discount period.

  - `flatFeePreviews.memberAmount` (object)
    Amount the member has to pay for the sub contract, if a valid company discount voucher code has been provided. This field is populated when there are 0 or 1 discount periods. For multiple discount periods, use discountPeriods[].memberAmount instead to see amounts per discount period.

  - `flatFeePreviews.paidTimePeriodCalculationType` (string)
    The method that is being used to determine the period for the first payment
    Enum: "REFERENCE_DATE", "NORMALIZATION_ON_CALENDAR_UNIT"

  - `flatFeePreviews.paymentFrequency` (object, required)
    Payment frequency information of the sub contract

  - `flatFeePreviews.paymentFrequency.id` (integer)
    The unique identifier of the payment frequency. ( possible for starter package)
    Example: 1234567890

  - `flatFeePreviews.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `flatFeePreviews.paymentFrequency.term` (object)
    Represents a term

  - `flatFeePreviews.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `flatFeePreviews.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `flatFeePreviews.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `flatFeePreviews.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `flatFeePreviews.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `flatFeePreviews.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `flatFeePreviews.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `flatFeePreviews.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active  the respective term has passed

  - `flatFeePreviews.paymentFrequency.recurring` (boolean)
    Whether the cycle of payments repeats indefinitely. Only relevant if type is  or .

  - `flatFeePreviews.paymentFrequency.ageBasedAdjustments` (array)
    List of age-based adjustments for the membership offer module.

  - `flatFeePreviews.paymentFrequency.ageBasedAdjustments.ageRange` (object, required)
    Represents an age range.

  - `flatFeePreviews.paymentFrequency.ageBasedAdjustments.ageRange.startAge` (integer, required)
    Start age of the range, inclusive.
    Example: 18

  - `flatFeePreviews.paymentFrequency.ageBasedAdjustments.ageRange.endAge` (integer, required)
    End age of the range, inclusive.
    Example: 65

  - `flatFeePreviews.paymentFrequency.ageBasedAdjustments.value` (number, required)
    The value of the adjustment, based on .
    Example: 10

  - `flatFeePreviews.paymentFrequency.ageBasedAdjustments.type` (string, required)
    Age based adjustment type
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `flatFeePreviews.paymentFrequency.formattedPaymentFrequency` (string, required)
    The formatted payment frequency
    Example: "Every 6 months"

  - `flatFeePreviews.voucherBonusPeriod` (object)
    Bonus period applied with the discount voucher, if valid a discount voucher code has been provided

  - `flatFeePreviews.identifier` (string, required)
    Unique identifier of the flat fee
    Example: "FLATFEE0-0F7691D0E09A4477A5CC69C8BD3F223B"

  - `flatFeePreviews.discountedPrice` (object)
    Discounted price of the sub contract, if a valid discount voucher code has been provided. Deprecated: Use discountPeriods[].discountedBasePrice instead to see prices per discount period.

  - `voucherSuccessMessage` (string)
    Textual representation of the voucher conditions, if a valid voucher code has been provided
    Example: "Voucher code \"123\" successfully applied: 5% discount on the membership fee"

  - `voucherErrorCode` (string)
    An error code, if the voucher code is invalid
    Enum: "INVALID_CODE"

  - `ageAdjustedPrice` (object)
    The adjusted price, if age-based discounts are configured and the customer is eligible, null otherwise

  - `contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month and per the rate's payment frequency (e.g. 1 week)

  - `contractVolumeInformation.totalContractVolume` (object)
    Total contract volume
    Example: 600

  - `contractVolumeInformation.averagePaymentVolumePerMonth` (object)
    Average payment volume per month
    Example: 50

  - `contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (object)
    Average payment volume per payment frequency term
    Example: 50

  - `moduleConsentTextBlocks` (array)
    Consent texts for modules that are part of the contract

  - `selectedOptionalModulesPreviews` (array)
    Optional module contract preview including discount, company split or credit, if a valid voucher code has been provided

  - `selectedOptionalModulesPreviews.id` (integer, required)
    The ID of the module
    Example: 12345

  - `paymentPreview` (object)
    Detailed payment preview including schedule and due-on-signing amount

  - `paymentPreview.paymentSchedule` (array)
    Payment schedule entries in chronological order

  - `paymentPreview.paymentSchedule.dueDate` (string)
    Due date of the payment in ISO-8601 format
    Example: "2025-12-31"

  - `paymentPreview.paymentSchedule.description` (string)
    Description of the charge
    Example: "Contract Basic"

  - `paymentPreview.paymentSchedule.type` (string)
    Type of membership payment
    Enum: "CONTRACT_FEE", "STARTER_PACKAGE", "FLAT_FEE", "MODULE_FEE", "BONUS_PERIOD"

  - `paymentPreview.paymentSchedule.amount` (object)
    Amount of the charge

  - `paymentPreview.paymentSchedule.mandatoryOnSigning` (boolean)
    Indicates if the payment is mandatory on signing
    Example: true

  - `paymentPreview.dueOnSigningAmount` (object)
    Total amount due at contract signing

  - `voucherEffectivePeriod` (string)
    The type of period for which the voucher is applied, if a valid voucher code has been provided. Deprecated: Use voucherDiscountPeriods[].effectivePeriod instead to see periods per discount period.
    Enum: "UNLIMITED", "INITIAL_TERM", "TIME_BASED"

  - `effectivePeriodTimeBasedTerm` (object)
    Effective period: term for which a discount is applied, if type is time based and a valid voucher code has been provided. Deprecated: Use voucherDiscountPeriods[].effectivePeriodTimeBasedTerm instead to see terms per discount period.

  - `discountedBasePrice` (object)
    Discounted base price, if a valid discount voucher code has been provided. Deprecated: Use voucherDiscountPeriods[].discountedBasePrice instead to see prices per discount period.

  - `discountType` (string)
    Type of discount (percentage or absolute), if a valid discount voucher code has been provided. Deprecated: Use voucherDiscountPeriods[].discountType instead to see discount types per discount period.
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `discountValue` (object)
    Discount value, if a valid discount voucher code has been provided. Deprecated: Use voucherDiscountPeriods[].discountValue instead to see discount values per discount period.

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

