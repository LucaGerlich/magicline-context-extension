# cancelContract

Endpoint: POST /connect/v1/contracts/cancel
Version: 1.0.0

## Query parameters:

  - `recaptchaToken` (string, required)
    client generated Google reCAPTCHA token

## Request fields (application/json):

  - `additionalInformation` (string)

  - `cancelationReasonId` (integer)

  - `cancellationDate` (string, required)

  - `cancellationDateType` (string)
    Enum: "NEXT_POSSIBLE_CANCELLATION_DATE", "ABSOLUTE_CANCELLATION_DATE"

  - `cancellationType` (string, required)
    Enum: "ORDINARY_CANCELLATION", "EXTRAORDINARY_CANCELLATION"

  - `confirmationEmail` (string)

  - `contractId` (integer, required)

  - `customerNumber` (string, required)

  - `dateOfBirth` (string, required)

  - `firstname` (string, required)

  - `lastname` (string, required)

## Response 200 fields (*/*):

  - `additionalInformation` (string)

  - `cancelationReason` (object)

  - `cancelationReason.databaseId` (integer)

  - `cancelationReason.fkOrganizationUnit` (integer, required)

  - `cancelationReason.name` (string)

  - `cancelationReason.optlock` (integer)

  - `cancelationReason.system` (boolean)

  - `cancelationReason.type` (string)
    Enum: "UNDEFINED", "CUSTOM", "CONTRACT_SWITCH", "REST_MATURITY", "DUNNING"

  - `cancelationReason.visibleInNox` (boolean)

  - `cancellationDate` (string)

  - `cancellationReceivedDateTime` (string)

  - `cancellationType` (string)
    Enum: "ORDINARY_CANCELLATION", "EXTRAORDINARY_CANCELLATION"

  - `confirmationEmail` (string)

  - `contractName` (string)

  - `customerNumber` (string)

  - `dateOfBirth` (string)

  - `firstname` (string)

  - `lastname` (string)

  - `studioId` (integer)

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

