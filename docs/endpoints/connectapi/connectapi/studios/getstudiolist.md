# List all studios

You can add optional filters. Parameters addressSearchQuery and studioTags are combined by AND

Endpoint: GET /connect/v2/studio
Version: 1.0.0

## Query parameters:

  - `studioTags` (array)
    Filter by identifier of StudioTag (german wording: Standort Code). Dynamic attribute configured at studio (e.g for Brands or Locations). Multiple Tags are combined by OR.

  - `addressSearchQuery` (string)
    Search prefix for zipCode or city of studio address.

## Response 200 fields (*/*):

  - `address` (object)

  - `address.additionalAddressInformation` (string)
    addition for Spain

  - `address.buildingName` (string)
    addition for Turkey

  - `address.city` (string)

  - `address.cityPart` (string)
    addition for Turkey

  - `address.countryCode` (string)

  - `address.countryCodeAlpha2` (string)

  - `address.district` (string)
    addition for Turkey

  - `address.door` (string)
    addition for Spain

  - `address.floor` (string)
    addition for Spain

  - `address.houseNumber` (string)

  - `address.latitude` (number)

  - `address.longitude` (number)

  - `address.portal` (string)
    addition for Spain

  - `address.province` (string)
    addition for southern Europe/US countries (e.g. Madrid, California)

  - `address.provinceCode` (string)
    addition for US (e.g. CA for California)

  - `address.secondStreet` (string)
    addition for Turkey

  - `address.stairway` (string)
    addition for Spain

  - `address.street` (string)

  - `address.streetAddition` (string)

  - `address.streetBlock` (string)
    addition for Spain

  - `address.streetType` (string)
    addition for Spain (e.g. calle)

  - `address.zipCode` (string)

  - `closingDate` (string)
    Studio is either fully closed, or temporarily closed from this date on. It is up to the studio owner to decide how to interpret this value on his website.

  - `currencyCode` (string)
    Studio currency code
    Enum: "UNDEFINED", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"

  - `hasRateBundles` (boolean)
    Does this studio has contract offers for online sign up

  - `id` (integer, required)
    Id of current data block. See name field parameter or name of Dto!

  - `masterStudioId` (integer)

  - `openingDate` (string)
    If this value is set, inform the customer about a delayed contract start. Send start date with min value of openingDate!

  - `openingHours` (array)
    List of day ranges with openingHours, dayOfWeek 1 = MONDAY, dayOfWeek 7 = SUNDAY. Might be one range 1 - 7 if  openingHours does not differ from day to day or multiple ranges like 1-5 and 6-7 if the studio has different opening hours on week days and weekends.

  - `openingHours.dayOfWeekFrom` (string)
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `openingHours.dayOfWeekTo` (string)
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `openingHours.timeFrom` (object)

  - `openingHours.timeFrom.hour` (integer)

  - `openingHours.timeFrom.minute` (integer)

  - `openingHours.timeFrom.nano` (integer)

  - `openingHours.timeFrom.second` (integer)

  - `openingHours.timeTo` (object)

  - `studioEmail` (string)

  - `studioName` (string, required)

  - `studioPhone` (string)

  - `studioTags` (array)

  - `studioTags.identifier` (string, required)

  - `studioTags.name` (string, required)

  - `trialSessionBookable` (boolean)
    Has this studio trial session configured for online booking of slots

  - `trialSessionName` (string)
    Name of the trial session benefit which you can book appointments for

  - `zoneId` (object)
    Timezone of the studios location

  - `zoneId.id` (string)

  - `zoneId.rules` (object)

  - `zoneId.rules.fixedOffset` (boolean)

  - `zoneId.rules.transitionRules` (array)

  - `zoneId.rules.transitionRules.dayOfMonthIndicator` (integer)

  - `zoneId.rules.transitionRules.dayOfWeek` (string)
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `zoneId.rules.transitionRules.localTime` (object)

  - `zoneId.rules.transitionRules.midnightEndOfDay` (boolean)

  - `zoneId.rules.transitionRules.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `zoneId.rules.transitionRules.offsetAfter` (object)

  - `zoneId.rules.transitionRules.offsetAfter.totalSeconds` (integer)

  - `zoneId.rules.transitionRules.offsetBefore` (object)

  - `zoneId.rules.transitionRules.standardOffset` (object)

  - `zoneId.rules.transitionRules.timeDefinition` (string)
    Enum: "UTC", "WALL", "STANDARD"

  - `zoneId.rules.transitions` (array)

  - `zoneId.rules.transitions.dateTimeAfter` (string)

  - `zoneId.rules.transitions.dateTimeBefore` (string)

  - `zoneId.rules.transitions.duration` (object)

  - `zoneId.rules.transitions.duration.negative` (boolean)

  - `zoneId.rules.transitions.duration.positive` (boolean)

  - `zoneId.rules.transitions.duration.seconds` (integer)

  - `zoneId.rules.transitions.duration.units` (array)

  - `zoneId.rules.transitions.duration.units.dateBased` (boolean)

  - `zoneId.rules.transitions.duration.units.durationEstimated` (boolean)

  - `zoneId.rules.transitions.duration.units.timeBased` (boolean)

  - `zoneId.rules.transitions.duration.zero` (boolean)

  - `zoneId.rules.transitions.gap` (boolean)

  - `zoneId.rules.transitions.instant` (string)

  - `zoneId.rules.transitions.overlap` (boolean)

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

