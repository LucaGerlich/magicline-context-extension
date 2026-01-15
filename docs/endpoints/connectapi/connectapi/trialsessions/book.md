# Book a trial session

Book a free slot. Might return errorCode CONFLICT if configured resources are overbooked for this slot. In this case its advised to reload free slots and let the user select a different slot. If you get a validation error make sure all required fields are filled. Required fields are returned by the  endpoint.

Endpoint: POST /connect/v1/trialsession/book
Version: 1.0.0

## Request fields (application/json):

  - `leadCustomer` (object, required)

  - `leadCustomer.address` (object)

  - `leadCustomer.address.city` (string)
    Example: "Hamburg"

  - `leadCustomer.address.country` (string)
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `leadCustomer.address.details` (object)

  - `leadCustomer.address.details.additionalInformation` (string)

  - `leadCustomer.address.details.block` (string)

  - `leadCustomer.address.details.buildingName` (string)

  - `leadCustomer.address.details.cityPart` (string)

  - `leadCustomer.address.details.district` (string)

  - `leadCustomer.address.details.door` (string)

  - `leadCustomer.address.details.floor` (string)

  - `leadCustomer.address.details.portal` (string)

  - `leadCustomer.address.details.province` (string)

  - `leadCustomer.address.details.provinceCode` (string)

  - `leadCustomer.address.details.secondStreet` (string)

  - `leadCustomer.address.details.stairway` (string)

  - `leadCustomer.address.details.streetType` (string)

  - `leadCustomer.address.houseNumber` (string)
    Example: "1b"

  - `leadCustomer.address.street` (string)
    Example: "HeinrichstraÃe"

  - `leadCustomer.address.zip` (string)
    Example: 20095

  - `leadCustomer.communicationPreferences` (array)
    Communication preferences for the customer. If specified, the list must contain an element for each message category.

  - `leadCustomer.communicationPreferences.activeCommunicationChannels` (array)
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "MYSPORTS_MESSAGE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `leadCustomer.communicationPreferences.messageCategoryId` (integer)

  - `leadCustomer.countryOfBirth` (string)
    Enum: "UNDEFINED", "AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AN", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DG", "DJ", "DK", "DM", "DO", "DZ", "EA", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "EZ", "FI", "FJ", "FK", "FM", "FO", "FR", "FX", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "IC", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SU", "SV", "SX", "SY", "SZ", "TA", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UK", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XI", "XU", "XK", "YE", "YT", "YU", "ZA", "ZM", "ZR", "ZW"

  - `leadCustomer.customerUUID` (string)
    Should only be set if booking page has been called with URL param identityToken. If no lead exists with this UUID a new one will be created.
    Example: "2340b1cc-3fe7-4f81-8eca-f92181dd2bb4"

  - `leadCustomer.dateOfBirth` (string)
    Example: "1985-05-29"

  - `leadCustomer.email` (string)
    Example: "mm@test.de"

  - `leadCustomer.firstname` (string, required)
    Example: "Max"

  - `leadCustomer.gender` (string)
    Enum: "MALE", "FEMALE", "UNISEX"

  - `leadCustomer.lastname` (string, required)
    Example: "Mustermann"

  - `leadCustomer.phone` (string)
    Example: "+49 40 123 555"

  - `leadCustomer.placeOfBirth` (string)
    Example: "Rom"

  - `leadCustomer.privacyConfiguration` (object)
    Data privacy configuration for marketing purposes

  - `leadCustomer.privacyConfiguration.email` (boolean)
    Marketing contact via email allowed

  - `leadCustomer.privacyConfiguration.letter` (boolean)
    Marketing contact via letter allowed

  - `leadCustomer.privacyConfiguration.mySportsMessage` (boolean)
    Marketing contact via MySports allowed

  - `leadCustomer.privacyConfiguration.phone` (boolean)
    Marketing contact via phone allowed

  - `leadCustomer.privacyConfiguration.textMessage` (boolean)
    Marketing contact via text message allowed

  - `leadCustomer.secondFirstname` (string)
    Example: "Martin"

  - `leadCustomer.secondLastname` (string)
    Example: "Muster"

  - `leadCustomer.studioId` (integer)
    Only set if lead is fetched

  - `leadCustomer.taxId` (string)
    Example: "56982134w"

  - `note` (string)
    Example: "become fit"

  - `participants` (integer)
    Example: 2

  - `referralCode` (string)
    Example: "ABCXYZ"

  - `referrerId` (integer)
    Example: 10

  - `sourceCampaignId` (integer)
    Example: 2

  - `startDateTime` (string, required)
    Example: "2019-04-15T07:00:00.000Z"

  - `studioId` (integer, required)
    Example: 1

  - `trainerRequired` (boolean, required)
    Depends on bookingWithoutResourcesAllowed
    Example: true

## Response 200 fields (*/*):

  - `customerNumber` (string)
    Customer number of prospect

  - `id` (integer, required)
    Id of current data block. See name field parameter or name of Dto!

  - `uuid` (string)
    Can be used to execute follow up actions (Booking of appointment, singing a contract with this exact customer.
    Example: "2340b1cc-3fe7-4f81-8eca-f92181dd2bb4"

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

