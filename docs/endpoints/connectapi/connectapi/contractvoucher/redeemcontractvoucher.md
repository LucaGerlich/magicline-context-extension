# Redeem a ContractVoucher. Only Vouchers of type 'Rate' are supported here.

Endpoint: POST /connect/v1/contractvoucher/{contractVoucherCode}/redeem
Version: 1.0.0

## Path parameters:

  - `contractVoucherCode` (string, required)

## Request fields (application/json):

  - `contractStartDate` (string)

  - `contractStartPreuseDate` (string)

  - `customerDto` (object)

  - `customerDto.additionalAddressInformation` (string)
    addition for Spain

  - `customerDto.bankAccount` (object)
    Required in combination with paymentChoice DIRECT_DEBIT

  - `customerDto.bankAccount.accountHolder` (string, required)

  - `customerDto.bankAccount.bic` (string)
    BIC will be auto-detected from IBAN if not given

  - `customerDto.bankAccount.iban` (string, required)

  - `customerDto.buildingName` (string)
    addition for Turkish addresses

  - `customerDto.city` (string, required)
    Example: "Hamburg"

  - `customerDto.cityPart` (string)
    addition for Turkish addresses

  - `customerDto.communicationPreferences` (array)
    Communication preferences for the customer. If specified, the list must contain an element for each message category.

  - `customerDto.communicationPreferences.activeCommunicationChannels` (array, required)
    The list of channels on which messages of the given category are allowed to be sent
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "MYSPORTS_MESSAGE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `customerDto.communicationPreferences.messageCategoryId` (integer, required)
    The ID of the message category

  - `customerDto.countryCode` (string, required)
    Example: "DE"

  - `customerDto.countryOfBirth` (string)
    Required for italian studios and none-italian nationals
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `customerDto.creditCard` (object)
    Required in combination with paymentChoice CREDIT_CARD

  - `customerDto.creditCard.accountPaymentInstrumentToken` (string)
    This is the 'accountPaymentInstrumentToken' the user has received when he has configured his credit card. Use this if an existing credit card by Mysports is used.

  - `customerDto.creditCard.tokenizationReference` (string)
    This is the 'reference' you'll receive via /creditcard/tokenization/initiate endpoint. Use this if the customer adds a new credit card while contract signing.

  - `customerDto.dateOfBirth` (string, required)
    The age must be between 0 and 100 years inclusive.

  - `customerDto.district` (string)
    addition for Turkish addressses

  - `customerDto.documentIdentification` (object)
    information from an official document with identifies the customer

  - `customerDto.documentIdentification.documentNumber` (string, required)

  - `customerDto.documentIdentification.documentType` (string, required)
    Enum: "ID_CARD", "PASSPORT", "DRIVERS_LICENCE", "RESIDENCE_PERMIT", "NATIONAL_ID_NUMBER", "OTHERS"

  - `customerDto.door` (string)
    addition for Spain

  - `customerDto.email` (string, required)

  - `customerDto.firstname` (string, required)

  - `customerDto.floor` (string)
    addition for Spain

  - `customerDto.gender` (string)
    User will be assigned as UNISEX if no gender is set.
    Enum: "MALE", "FEMALE", "UNISEX"

  - `customerDto.houseNumber` (string, required)
    Example: "3-4"

  - `customerDto.identityToken` (string)
    [Optional] Should only be set if checkout page has been called with URL param identityToken. If no customer exists with this UUID a new one will be created.
    Example: "2340b1cc-3fe7-4f81-8eca-f92181dd2bb4"

  - `customerDto.imageObjectKey` (string)
    Object key for pre-uploaded image

  - `customerDto.language` (string)
    language of customer as ISO 639-1 two-letter code (e.g. es or de)

  - `customerDto.lastname` (string, required)

  - `customerDto.locale` (string)
    locale of customer as ISO 639-1 two-letter language and country code (e.g. es_ES or de_DE)

  - `customerDto.paymentChoice` (string, required)
    Only configured values in the rate bundle allowed. For Contract Voucher redemption use CASH
    Enum: "CASH", "BANK_TRANSFER", "DIRECT_DEBIT", "CREDIT_CARD", "TWINT"

  - `customerDto.placeOfBirth` (string)
    Required for italian studios and nationals

  - `customerDto.portal` (string)
    addition for Spain

  - `customerDto.province` (string)
    addition for southern Europe countries/US (e.g. Madrid, California)

  - `customerDto.provinceCode` (string)
    addition for US states (e.g. CA)

  - `customerDto.publicGender` (string)
    Enum: "MALE", "FEMALE", "UNISEX"

  - `customerDto.referralCode` (string)
    Referral code to link with recruiter

  - `customerDto.secondFirstname` (string)
    addition for Turkey

  - `customerDto.secondLastName` (string)
    addition for Spain

  - `customerDto.secondStreet` (string)
    addition for Turkish addresses

  - `customerDto.stairway` (string)
    addition for Spain

  - `customerDto.street` (string, required)
    Example: "Raboisen"

  - `customerDto.streetBlock` (string)
    addition for Spain

  - `customerDto.streetType` (string)
    addition for Spain (e.g. calle)

  - `customerDto.studioCountryCode` (string)
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `customerDto.taxId` (string)
    Required if the studio is located in Spain or Italy

  - `customerDto.telephone_mobile` (string)
    If only one number is available use mobile as default.

  - `customerDto.telephone_private` (string)
    If only one number is available use mobile as default.

  - `customerDto.zipCode` (string, required)
    Example: 22099

  - `customerDto.identification` (object)
    Deprecated. Use the identityNumber field.

  - `customerDto.identification.spain_DNI_NIE` (string)
    Required if the studio is located in Spain

  - `customerDto.privacyConfiguration` (object)
    Data privacy configuration for marketing purposes. Deprecated. Use communicationPreferences instead.

  - `customerDto.privacyConfiguration.email` (boolean)
    Marketing contact via email allowed

  - `customerDto.privacyConfiguration.letter` (boolean)
    Marketing contact via letter allowed

  - `customerDto.privacyConfiguration.mySportsMessage` (boolean)
    Marketing contact via MySports allowed

  - `customerDto.privacyConfiguration.phone` (boolean)
    Marketing contact via phone allowed

  - `customerDto.privacyConfiguration.textMessage` (boolean)
    Marketing contact via text message allowed

  - `organizationUnitId` (integer)

## Response 200 fields (*/*):

  - `customerNumber` (string)

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

