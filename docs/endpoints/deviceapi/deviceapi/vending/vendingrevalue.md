# Top up customer's consumption credit

This should be used to top up customer's consumption credit.

Endpoint: POST /open-api/device/vending/revalue
Security: ApiKeyAuth

## Header parameters:

  - `Accept-Language` (string)
    More information about the header can be found here.
    Example: "de"

## Request fields (application/json):

  - `identification` (any, required)

  - `transactionId` (string, required)
    Unique ID of the transaction (you have to generate it)
    Example: "4671fde7-bb07-4fe5-aa0e-947d9ccb842f"

  - `amount` (number, required)
    Amount customer wats to top up his consumption credit
    Example: 5

## Response 400 fields (application/json):

  - `errorMessage` (string)
    This message is intended for display to the customer and its language depends on the  header.

  - `errorCode` (string)

  - `traceId` (string)
    This ID will help us provide you with better support. If you encounter any issues and require our assistance, please include this ID or the complete error object in your request.

## Response 403 fields (application/json):

  - `errorMessage` (string)
    This message is intended for display to the customer and its language depends on the  header.

  - `errorCode` (string)

  - `traceId` (string)
    This ID will help us provide you with better support. If you encounter any issues and require our assistance, please include this ID or the complete error object in your request.

## Response 404 fields (application/json):

  - `errorMessage` (string)
    This message is intended for display to the customer and its language depends on the  header.

  - `errorCode` (string)

  - `traceId` (string)
    This ID will help us provide you with better support. If you encounter any issues and require our assistance, please include this ID or the complete error object in your request.

## Response 500 fields (application/json):

  - `errorMessage` (string)
    This message is intended for display to the customer and its language depends on the  header.

  - `errorCode` (string)

  - `traceId` (string)
    This ID will help us provide you with better support. If you encounter any issues and require our assistance, please include this ID or the complete error object in your request.

## Response 503 fields (application/json):

  - `errorMessage` (string)
    This message is intended for display to the customer and its language depends on the  header.

  - `errorCode` (string)

  - `traceId` (string)
    This ID will help us provide you with better support. If you encounter any issues and require our assistance, please include this ID or the complete error object in your request.

