# Get available intervals with prices

Returns a list of available time intervals with their corresponding prices. This allows the device to display the options to the customer.

Endpoint: GET /open-api/device/time/price
Security: ApiKeyAuth

## Header parameters:

  - `Accept-Language` (string)
    More information about the header can be found here.
    Example: "de"

## Response 200 fields (application/json):

  - `selection` (array)
    List of available time intervals with their corresponding prices.

  - `selection.durationInSeconds` (integer)
    Duration of the interval in seconds.
    Example: 300

  - `selection.price` (object)
    Represents a financial data

  - `selection.price.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `selection.price.currency` (string, required)
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

