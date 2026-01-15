# Get Tokenization state

Endpoint: GET /connect/v2/creditcard/tokenization/{tokenizationReference}/state
Version: 1.0.0

## Path parameters:

  - `tokenizationReference` (string, required)

## Response 200 fields (*/*):

  - `errorMessage` (string)

  - `paymentInstrumentDto` (object)
    The created payment instrument, only filled when tokenization completed

  - `paymentInstrumentDto.accountPaymentInstrumentToken` (string)

  - `paymentInstrumentDto.bacsPaymentInstrument` (object)

  - `paymentInstrumentDto.bacsPaymentInstrument.accountHolder` (string)

  - `paymentInstrumentDto.bacsPaymentInstrument.bankAccountNumber` (string)

  - `paymentInstrumentDto.bacsPaymentInstrument.bankLocationId` (string)

  - `paymentInstrumentDto.bacsPaymentInstrument.directDebitPdfFormUrl` (string)

  - `paymentInstrumentDto.bacsPaymentInstrument.mandateId` (string)

  - `paymentInstrumentDto.bacsPaymentInstrument.shopperEmail` (string)

  - `paymentInstrumentDto.banContactCard` (object)

  - `paymentInstrumentDto.banContactCard.cardHolder` (string)

  - `paymentInstrumentDto.banContactCard.cardNumber` (string)

  - `paymentInstrumentDto.banContactCard.expiry` (object)

  - `paymentInstrumentDto.banContactCard.expiry.leapYear` (boolean)

  - `paymentInstrumentDto.banContactCard.expiry.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `paymentInstrumentDto.banContactCard.expiry.monthValue` (integer)

  - `paymentInstrumentDto.banContactCard.expiry.year` (integer)

  - `paymentInstrumentDto.banContactCard.id` (integer)

  - `paymentInstrumentDto.creditCard` (object)

  - `paymentInstrumentDto.creditCard.brand` (string)
    Enum: "amex", "bancontact", "cartebancaire", "cup", "diners", "discover", "elo", "girocard", "hipercard", "jcb", "maestro", "mc", "twint_pos", "visa", "vpay", "unknown"

  - `paymentInstrumentDto.creditCard.issuerCountry` (string)
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `paymentInstrumentDto.creditCard.preferred` (boolean)

  - `paymentInstrumentDto.creditCard.provider` (string)
    Enum: "ADYEN"

  - `paymentInstrumentDto.creditCard.providerToken` (string)

  - `paymentInstrumentDto.idealPaymentInstrument` (object)

  - `paymentInstrumentDto.idealPaymentInstrument.issuer` (string)

  - `paymentInstrumentDto.paymentInstrumentInvalidReason` (string)
    Enum: "CHARGEBACK", "RECURRING_TOKEN_DISABLED"

  - `paymentInstrumentDto.paymentInstrumentStatus` (string)
    Enum: "WAITING_FOR_CONFIRMATION", "CONFIRMED", "INVALID"

  - `paymentInstrumentDto.paymentInstrumentType` (string)
    Enum: "CREDIT_CARD", "PAYPAL", "TERMINAL", "APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY", "BANCONTACT", "IDEAL", "SEPA", "TWINT", "BACS"

  - `paymentInstrumentDto.recurringReference` (string)

  - `paymentInstrumentDto.sepaPaymentInstrumentDto` (object)

  - `paymentInstrumentDto.sepaPaymentInstrumentDto.iban` (string)

  - `paymentInstrumentDto.userAccountToken` (string)

  - `publicUserToken` (string)

  - `state` (string, required)
    State of tokenization, on success this is 'COMPLETE'
    Enum: "INITIATE", "FAILURE", "COMPLETE"

  - `userToken` (string)

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

