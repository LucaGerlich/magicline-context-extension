# Initiate Tokenization

Endpoint: POST /connect/v2/creditcard/tokenization/initiate
Version: 1.0.0

## Request fields (application/json):

  - `browserInfo` (string, required)
    Browser Info object, is obtained from Adyen card component and must be serialized to string

  - `origin` (string, required)
    Origin, obtained via window.location.origin

  - `paymentMethod` (string, required)
    Payment Method, is obtained from Adyen card component and must be serialized to string

  - `returnUrl` (string, required)
    Return url for redirects. If user is redirected to banking page, he will be redirected to this url after authentication.

  - `studioId` (integer, required)
    Studio Id

## Response 200 fields (*/*):

  - `action` (string)
    Action object by Adyen (serialized to Json string). If this is not 'null' pass it to the Adyen web component

  - `errorMessage` (string)

  - `reference` (string, required)
    Reference for tokenization process, use it in further requests

  - `resultCode` (string, required)
    Result code by payment provider, usually 'IdentifyShopper' or 'RedirectShopper', then 'action' needs to be passed to Adyen component. Display generic error message when this is 'Error'. For a complete list see: https://docs.adyen.com/online-payments/payment-result-codes

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

