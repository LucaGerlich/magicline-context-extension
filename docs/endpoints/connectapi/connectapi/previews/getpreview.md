# getPreview

Endpoint: POST /connect/v2/preview
Version: 1.0.0

## Query parameters:

  - `landingPageConfigurationId` (integer)

  - `checkoutPageConfigurationId` (integer)

## Request fields (application/json):

  - `contract` (object, required)

  - `contract.contractSignature` (object)

  - `contract.contractSignature.base64Svg` (string, required)
    If signature is set, you have to provide a valid svg value as base 64 string. Required format: data:image/svg+xml,... with or without prefix Check workflow documentation for more details.

  - `contract.contractSignature.textBlockId` (integer)
    If signature is part of a contract text block, set the corresponding id

  - `contract.notes` (string)

  - `contract.optionalRateBundleTermModules` (array)
    Selected optional rate bundle term modules additionally payable.

  - `contract.optionalRateBundleTermModules.id` (integer)

  - `contract.preuseDate` (string)

  - `contract.rateBundleTermId` (integer, required)

  - `contract.selectedRateBundleModules` (array)
    Selected free inclusive rate bundle modules.

  - `contract.sepaSignature` (object)
    if not set, the same value as in contractSignature is used

  - `contract.startDate` (string, required)

  - `contract.textBlockSignatures` (array)

  - `customer` (object, required)

  - `customer.additionalAddressInformation` (string)
    addition for Spain

  - `customer.bankAccount` (object)
    Required in combination with paymentChoice DIRECT_DEBIT

  - `customer.bankAccount.accountHolder` (string, required)

  - `customer.bankAccount.bic` (string)
    BIC will be auto-detected from IBAN if not given

  - `customer.bankAccount.iban` (string, required)

  - `customer.buildingName` (string)
    addition for Turkish addresses

  - `customer.city` (string, required)
    Example: "Hamburg"

  - `customer.cityPart` (string)
    addition for Turkish addresses

  - `customer.communicationPreferences` (array)
    Communication preferences for the customer. If specified, the list must contain an element for each message category.

  - `customer.communicationPreferences.activeCommunicationChannels` (array, required)
    The list of channels on which messages of the given category are allowed to be sent
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "MYSPORTS_MESSAGE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `customer.communicationPreferences.messageCategoryId` (integer, required)
    The ID of the message category

  - `customer.countryCode` (string, required)
    Example: "DE"

  - `customer.countryOfBirth` (string)
    Required for italian studios and none-italian nationals
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `customer.creditCard` (object)
    Required in combination with paymentChoice CREDIT_CARD

  - `customer.creditCard.accountPaymentInstrumentToken` (string)
    This is the 'accountPaymentInstrumentToken' the user has received when he has configured his credit card. Use this if an existing credit card by Mysports is used.

  - `customer.creditCard.tokenizationReference` (string)
    This is the 'reference' you'll receive via /creditcard/tokenization/initiate endpoint. Use this if the customer adds a new credit card while contract signing.

  - `customer.dateOfBirth` (string, required)
    The age must be between 0 and 100 years inclusive.

  - `customer.district` (string)
    addition for Turkish addressses

  - `customer.documentIdentification` (object)
    information from an official document with identifies the customer

  - `customer.documentIdentification.documentNumber` (string, required)

  - `customer.documentIdentification.documentType` (string, required)
    Enum: "ID_CARD", "PASSPORT", "DRIVERS_LICENCE", "RESIDENCE_PERMIT", "NATIONAL_ID_NUMBER", "OTHERS"

  - `customer.door` (string)
    addition for Spain

  - `customer.email` (string, required)

  - `customer.firstname` (string, required)

  - `customer.floor` (string)
    addition for Spain

  - `customer.gender` (string)
    User will be assigned as UNISEX if no gender is set.
    Enum: "MALE", "FEMALE", "UNISEX"

  - `customer.houseNumber` (string, required)
    Example: "3-4"

  - `customer.identityToken` (string)
    [Optional] Should only be set if checkout page has been called with URL param identityToken. If no customer exists with this UUID a new one will be created.
    Example: "2340b1cc-3fe7-4f81-8eca-f92181dd2bb4"

  - `customer.imageObjectKey` (string)
    Object key for pre-uploaded image

  - `customer.language` (string)
    language of customer as ISO 639-1 two-letter code (e.g. es or de)

  - `customer.lastname` (string, required)

  - `customer.locale` (string)
    locale of customer as ISO 639-1 two-letter language and country code (e.g. es_ES or de_DE)

  - `customer.paymentChoice` (string, required)
    Only configured values in the rate bundle allowed. For Contract Voucher redemption use CASH
    Enum: "CASH", "BANK_TRANSFER", "DIRECT_DEBIT", "CREDIT_CARD", "TWINT"

  - `customer.placeOfBirth` (string)
    Required for italian studios and nationals

  - `customer.portal` (string)
    addition for Spain

  - `customer.province` (string)
    addition for southern Europe countries/US (e.g. Madrid, California)

  - `customer.provinceCode` (string)
    addition for US states (e.g. CA)

  - `customer.publicGender` (string)
    Enum: "MALE", "FEMALE", "UNISEX"

  - `customer.referralCode` (string)
    Referral code to link with recruiter

  - `customer.secondFirstname` (string)
    addition for Turkey

  - `customer.secondLastName` (string)
    addition for Spain

  - `customer.secondStreet` (string)
    addition for Turkish addresses

  - `customer.stairway` (string)
    addition for Spain

  - `customer.street` (string, required)
    Example: "Raboisen"

  - `customer.streetBlock` (string)
    addition for Spain

  - `customer.streetType` (string)
    addition for Spain (e.g. calle)

  - `customer.studioCountryCode` (string)
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `customer.taxId` (string)
    Required if the studio is located in Spain or Italy

  - `customer.telephone_mobile` (string)
    If only one number is available use mobile as default.

  - `customer.telephone_private` (string)
    If only one number is available use mobile as default.

  - `customer.zipCode` (string, required)
    Example: 22099

  - `customer.identification` (object)
    Deprecated. Use the identityNumber field.

  - `customer.identification.spain_DNI_NIE` (string)
    Required if the studio is located in Spain

  - `customer.privacyConfiguration` (object)
    Data privacy configuration for marketing purposes. Deprecated. Use communicationPreferences instead.

  - `customer.privacyConfiguration.email` (boolean)
    Marketing contact via email allowed

  - `customer.privacyConfiguration.letter` (boolean)
    Marketing contact via letter allowed

  - `customer.privacyConfiguration.mySportsMessage` (boolean)
    Marketing contact via MySports allowed

  - `customer.privacyConfiguration.phone` (boolean)
    Marketing contact via phone allowed

  - `customer.privacyConfiguration.textMessage` (boolean)
    Marketing contact via text message allowed

  - `landingPageConfigurationId` (integer)

  - `offerUuid` (string)

  - `studioId` (integer, required)

  - `voucherCode` (string)
    Only vouchers of type 'Credit' or 'Discount' are supported here.

## Response 200 fields (*/*):

  - `ageAdjustedPrice` (number)
    The adjusted price, if age-based discounts are configured and the customer is eligible, null otherwise

  - `basePrice` (number)
    base price of contract

  - `companyAmount` (number)
    Amount the company has to pay

  - `companyAmountPreUseCharge` (number)
    Amount the company has to pay for pre use charge

  - `companyAmountWithoutDiscount` (number)
    Amount the company has to pay without discount

  - `companyFeeSplitType` (string)
    Type of company fee split (percentage or absolute), if valid a company discount voucher is provided
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `companyFeeSplitValue` (number)
    Company fee split value, if a valid company discount voucher is provided

  - `companyName` (string)
    Name of the company that will pay the company amount

  - `contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month and per the rate's payment frequency (e.g. 1 week)

  - `contractVolumeInformation.averagePaymentVolumePerMonth` (number)

  - `contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (number)

  - `contractVolumeInformation.totalContractVolume` (number)

  - `creditValue` (number)
    Voucher credit value, if a valid credit voucher is provided

  - `discountType` (string)
    Type of discount (percentage or absolute), if valid a (company) discount voucher is provided
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `discountValue` (number)
    Discount value, if a valid (company) discount voucher is provided

  - `discountedBasePrice` (number)
    Discounted base price, if a valid (company) discount voucher is provided

  - `discountedPreUseCharge` (number)
    Discounted pre use charge, if a valid (company) discount voucher is provided

  - `effectivePeriodTimeBasedTerm` (integer)
    Effective period: term in which a discount is applied if type is time base

  - `effectivePeriodTimeBasedTermUnit` (string)
    Effective period: term unit in which a discount is applied if type is time base
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `flatFeePreviews` (array)
    Flat fee previews, including discount if a valid discount voucher is provided

  - `flatFeePreviews.companyAmount` (number)

  - `flatFeePreviews.creditValue` (number)

  - `flatFeePreviews.discountedPrice` (number)

  - `flatFeePreviews.identifier` (string)

  - `flatFeePreviews.memberAmount` (number)

  - `flatFeePreviews.name` (string)

  - `flatFeePreviews.paidTimePeriodCalculationType` (string)
    Enum: "REFERENCE_DATE", "NORMALIZATION_ON_CALENDAR_UNIT"

  - `flatFeePreviews.paymentFrequency` (string)

  - `flatFeePreviews.paymentFrequencyDto` (object)

  - `flatFeePreviews.paymentFrequencyDto.ageBasedAdjustmentDtos` (array)
    Age-based price adjustments. Price adjustments can be either a percentage by which the base price is being discounted or an absolute price.

  - `flatFeePreviews.paymentFrequencyDto.ageBasedAdjustmentDtos.ageBasedAdjustmentType` (string, required)
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `flatFeePreviews.paymentFrequencyDto.ageBasedAdjustmentDtos.ageRangeDto` (object, required)

  - `flatFeePreviews.paymentFrequencyDto.ageBasedAdjustmentDtos.ageRangeDto.endAge` (integer)

  - `flatFeePreviews.paymentFrequencyDto.ageBasedAdjustmentDtos.ageRangeDto.startAge` (integer)

  - `flatFeePreviews.paymentFrequencyDto.ageBasedAdjustmentDtos.value` (number, required)

  - `flatFeePreviews.paymentFrequencyDto.money` (object)
    The price for this payment frequency. Only set if "type" is either "RECURRING" or "NON_RECURRING"

  - `flatFeePreviews.paymentFrequencyDto.money.amount` (number, required)

  - `flatFeePreviews.paymentFrequencyDto.money.currencyCode` (string, required)
    Enum: "UNDEFINED", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"

  - `flatFeePreviews.paymentFrequencyDto.monthDayWithPrices` (array)
    The dates and respective prices on which payments are due. Only set if "type" is "MONTH_DAY"

  - `flatFeePreviews.paymentFrequencyDto.monthDayWithPrices.monthDay` (string, required)

  - `flatFeePreviews.paymentFrequencyDto.monthDayWithPrices.price` (object, required)

  - `flatFeePreviews.paymentFrequencyDto.recurring` (boolean, required)
    Whether the cycle of payments repeats indefinitely. Only relevant if type is "TERM_BASED" or "MONTH_DAY".

  - `flatFeePreviews.paymentFrequencyDto.term` (object)
    The interval in which payments are made. Only set if "type" is "RECURRING"

  - `flatFeePreviews.paymentFrequencyDto.term.term` (integer, required)

  - `flatFeePreviews.paymentFrequencyDto.term.termUnit` (string, required)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `flatFeePreviews.paymentFrequencyDto.termWithPrices` (array)
    The terms and respective prices after which payments are due. Only set if "type" is "TERM_BASED"

  - `flatFeePreviews.paymentFrequencyDto.type` (string, required)
    The kind of intervals in which payments are made
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `flatFeePreviews.paymentFrequencyType` (string)
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `flatFeePreviews.paymentFrequencyUnit` (string)
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `flatFeePreviews.paymentFrequencyValue` (integer)

  - `flatFeePreviews.voucherBonusPeriod` (object)

  - `flatFeePreviews.voucherBonusPeriod.displaySeparately` (boolean)

  - `flatFeePreviews.voucherBonusPeriod.extendsCancellationPeriod` (boolean)

  - `flatFeePreviews.voucherBonusPeriod.runtimeExtensionType` (string)
    Enum: "WITH_EXTENSION", "WITHOUT_EXTENSION"

  - `flatFeePreviews.voucherBonusPeriod.termStrategy` (string)
    Enum: "CONTRACT_START", "FIXED", "END_OF_CURRENT_TERM", "START_OF_NEXT_TERM"

  - `flatFeePreviews.voucherBonusPeriod.termValue` (integer)

  - `memberAmount` (number)
    Amount the member has to pay

  - `memberAmountPreUseCharge` (number)
    Amount the member has to pay for pre use charge

  - `memberAmountWithoutDiscount` (number)
    Amount the member has to pay without discount

  - `moduleConsentTextBlocks` (array)
    Consent texts for modules that are part of the contract

  - `moduleConsentTextBlocks.attachedDocument` (object)
    Optional contract document attachment You should display a download link if this field is set.

  - `moduleConsentTextBlocks.attachedDocument.fileName` (string, required)

  - `moduleConsentTextBlocks.attachedDocument.url` (string, required)
    Temporary valid download link. Expires after 5 hours

  - `moduleConsentTextBlocks.attachedExternalUrlDto` (object)
    Optional link to external url You should display a link if this field is set with the given title and target url

  - `moduleConsentTextBlocks.attachedExternalUrlDto.link` (string)

  - `moduleConsentTextBlocks.attachedExternalUrlDto.title` (string)

  - `moduleConsentTextBlocks.attachmentType` (string)
    Indicates the type of attachment for this block: None, file (attachedDocument) or Url (attachedExternalUrlDto)
    Enum: "NONE", "FILE", "URL", "CONTRACT_PDF_PREVIEW"

  - `moduleConsentTextBlocks.hasSignature` (boolean, required)
    text block configuration has a signature field. You have the option to show a signature input field and it will be added in the contract document. It is not a required field in magicline. It is up to your implementation if you add this field.

  - `moduleConsentTextBlocks.id` (integer, required)

  - `moduleConsentTextBlocks.isConfirmationRequired` (boolean, required)
    text block configuration contains a confirmation. You are advised to show a check box (or signature if hasSignature=true) in combination with this text block where the user should give his consent.

  - `moduleConsentTextBlocks.order` (integer, required)
    order in contract document

  - `moduleConsentTextBlocks.rateBundleModuleId` (integer)
    The ID of the associated rate bundle module. Only set if this is a module consent text block.

  - `moduleConsentTextBlocks.showCommunicationPrivacyOptions` (boolean, required)
    text block contains information about the communication privacy options You are advised to show a matrix with communication settings in combination with this text block.

  - `moduleConsentTextBlocks.text` (string, required)

  - `preUseCharge` (number)
    Charge for the time between startdateofuse and startdate

  - `selectedOptionalModulesPreviews` (array)
    Optional module contract preview including discount, company split or credit, if a valid voucher is provided

  - `voucherBonusPeriod` (object)
    Bonus period applied with the (company) discount voucher, if valid a (company) discount voucher is provided

  - `voucherEffectivePeriod` (string)
    Effective period type in which a discount is applied
    Enum: "UNLIMITED", "INITIAL_TERM", "TIME_BASED"

  - `voucherErrorCode` (string)
    An error code, if the voucher code is invalid
    Enum: "ENTITY_NOT_FOUND", "CONFLICT", "BAD_REQUEST", "REQUIRED_PARAMETER_MISSING", "VALIDATION_FAILED", "FORBIDDEN", "OPERATION_NOT_ALLOWED_FOR_STUDIO", "SERVER_ERROR", "FEATURE_DISABLED", "STUDIO_NOT_IN_GERMANY", "VOUCHER_VALIDATION_FAILED_INVALID_CODE", "VOUCHER_VALIDATION_FAILED_NOT_REDEEMABLE_HERE", "VOUCHER_VALIDATION_FAILED_NOT_IN_VALIDITY_PERIOD", "VOUCHER_VALIDATION_FAILED_NOT_ALLOWED_FOR_RATE", "TRIALSESSION_ALREADY_BOOKED", "ACTIVE_MEMBER_CANNOT_BOOK_TRIAL_SESSION"

  - `voucherErrorMessage` (string)
    A readable, non-localized error message, if the voucher code is invalid

  - `voucherRemarks` (string)
    Voucher remarks, if a valid voucher code is provided

  - `voucherSuccessMessage` (string)
    Textual representation of the voucher conditions, if a valid voucher is provided

  - `voucherTextBlocks` (array)
    Voucher related text blocks, if a valid voucher is provided

  - `voucherType` (string)
    Type of a voucher, if a valid voucher code is provided
    Enum: "CONTRACT", "CREDIT", "DISCOUNT", "COMPANY_FEE_SPLIT", "CHECKIN"

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

