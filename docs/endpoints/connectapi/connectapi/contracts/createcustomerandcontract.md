# Create a new customer and a new contract

Endpoint: POST /connect/v1/rate-bundle
Version: 1.0.0

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

  - ` customer id` (integer, required)

  - ` customer member name` (string)

  - ` customer member number` (string, required)

  - ` token for additional requests after member creation` (object)

  - ` token for additional requests after member creation.token` (string, required)

  - ` token for additional requests after member creation.tokenValidUntil` (string, required)

  - `Optional payment url where the user needs to be redirected to` (string)

  - `Quick registration url for MySports` (string)

  - `id` (integer, required)
    Id of current data block. See name field parameter or name of Dto!

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

