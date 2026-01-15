# Get mandatory field configuration

Returns the configuration which needs to be considered e.g. for form fields and their validation.

Endpoint: GET /connect/v1/trialsession/config/validation
Version: 1.0.0

## Query parameters:

  - `studioId` (integer, required)
    Example: 1

## Response 200 fields (*/*):

  - `addressMode` (string)
    Defines validation mode for full address. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `dateOfBirthMode` (string)
    Defines validation mode for birthdate. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `emailMode` (string)
    Defines validation mode for email address. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `genderMode` (string)
    Defines validation mode for gender. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `minimumAge` (integer)
    minimum age to book a trial session (dateOfBirthMode is mandatory if value is set)

  - `nameMode` (string)
    Defines validation mode for full name. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `placeOfBirthMode` (string)
    Defines validation mode fro place of birth. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `taxIdMode` (string)
    Defines validation mode for tax id. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `telephoneMode` (string)
    Defines validation mode for telephone number. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

  - `zipMode` (string)
    Defines validation mode for zip code. INACTIVE: hide it, OPTIONAL: Show it as optional form field, MANDATORY: Show it as mandatory form field.
    Enum: "INACTIVE", "OPTIONAL", "MANDATORY"

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

