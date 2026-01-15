# Create leads for prospective customers

Endpoint: POST /connect/v1/lead
Version: 1.0.0

## Request fields (application/json):

  - `additionalAddressInformation` (string)
    addition for Spain

  - `city` (string)
    Example: "Hamburg"

  - `communicationPreferences` (array)
    Communication preferences for the customer. If specified, the list must contain an element for each message category.

  - `communicationPreferences.activeCommunicationChannels` (array)
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "MYSPORTS_MESSAGE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `communicationPreferences.messageCategoryId` (integer)

  - `countryCode` (string)
    Example: "DE"

  - `dateOfBirth` (string)

  - `door` (string)
    addition for Spain

  - `email` (string)

  - `firstname` (string, required)

  - `firstname2` (string)
    addition for Turkey

  - `floor` (string)
    addition for Spain

  - `gender` (string)
    User will be assigned as UNISEX if no gender is set.
    Enum: "MALE", "FEMALE", "UNISEX"

  - `houseNumber` (string)
    Example: "3-4"

  - `lastname` (string, required)

  - `lastname2` (string)
    addition for Spain

  - `locale` (string)
    locale of customer as ISO 639-1 two-letter language and country code (e.g. es_ES or de_DE)

  - `notes` (string)
    Example: "any notes about this lead"

  - `phone` (string)

  - `portal` (string)
    addition for Spain

  - `privacyConfiguration` (object)
    Data privacy configuration for marketing purposes

  - `privacyConfiguration.email` (boolean)
    Marketing contact via email allowed

  - `privacyConfiguration.letter` (boolean)
    Marketing contact via letter allowed

  - `privacyConfiguration.mySportsMessage` (boolean)
    Marketing contact via MySports allowed

  - `privacyConfiguration.phone` (boolean)
    Marketing contact via phone allowed

  - `privacyConfiguration.textMessage` (boolean)
    Marketing contact via text message allowed

  - `province` (string)
    addition for southern Europe/US countries (e.g. Madrid, California)

  - `provinceCode` (string)
    addition for US state abbreviation (e.g. CA)

  - `sourceCampaignId` (integer)

  - `stairway` (string)
    addition for Spain

  - `street` (string)
    Example: "Raboisen"

  - `streetBlock` (string)
    addition for Spain

  - `streetType` (string)
    addition for Spain (e.g. calle)

  - `studioId` (integer, required)

  - `taxId` (string)
    addition for Spain and Italy

  - `zipCode` (string)
    Example: 22099

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

