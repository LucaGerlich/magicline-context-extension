# Checks if customer is authorized to use vending device

You can find more information about identification here.

Endpoint: POST /open-api/device/vending/identification
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

## Response 200 fields (application/json):

  - `text` (string)
    If customer is not authorized then it contains message with reason

  - `authorized` (boolean)
    If customer is authorized then is allowed to use the device
    Example: true

  - `consumptionCredit` (number)
    Customers consumption credit
    Example: 6.4

  - `transactionId` (string)
    Unique ID of the transaction
    Example: "4671fde7-bb07-4fe5-aa0e-947d9ccb842f"

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

