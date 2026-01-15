# Benefit usage (dry-run possible)

This should be conducted post-identification with  in order to execute a dry-run, ensuring that customers can obtain the benefit, for example has contingent, etc. If this first request was successful, the benefit can be enabled. After the benefit was successfully enabled, this endpoint needs to be called again with , which will subsequently lead to the customer being charged or benefit being used. You can find more information about usage here

Endpoint: POST /open-api/device/time/usage
Security: ApiKeyAuth

## Header parameters:

  - `Accept-Language` (string)
    More information about the header can be found here.
    Example: "de"

## Request fields (application/json):

  - `identification` (any, required)

  - `durationInSeconds` (integer)
    Duration of the benefit usage in seconds.
    Example: 30

  - `shouldExecuteAction` (boolean)
    In a dry run, when the value is set to false, you will receive a validation result without customer being charged. Learn more about it [here](../../general-information/#vending).
    Example: true

## Response 200 fields (application/json):

  - `text` (string)
    If customer is not authorized then it contains message with reason

  - `authorized` (boolean)
    If customer is authorized then is allowed to buy/use product
    Example: true

  - `price` (object)
    Represents a financial data

  - `price.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `price.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

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

