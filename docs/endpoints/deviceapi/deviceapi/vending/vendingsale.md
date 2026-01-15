# Product sale (dry-run possible)

This should be conducted post-identification with  in order to execute a dry-run, ensuring that customers can obtain the product, for example has enough credit, etc. If this first request was successful, the product can be dispensed. After the product was sucessfully dispensed, this endpoint needs to be called again with , which will subsequently lead to the customer being charged. You can find more information about sale here

Endpoint: POST /open-api/device/vending/sale
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

  - `productId` (string, required)
    Shelf where the product is located
    Example: "1"

  - `price` (number, required)
    Price of the product according to vending machine. If the price is different than in Magicline then the request will be rejected
    Example: 1.29

  - `shouldExecuteAction` (boolean)
    In a dry run, when the value is set to false, you will receive a validation result without customer being charged. Learn more about it [here](../../general-information/#vending).
    Example: true

## Response 200 fields (application/json):

  - `text` (string)
    If customer is not authorized then it contains message with reason

  - `authorized` (boolean)
    If customer is authorized then is allowed to buy/use product
    Example: true

  - `consumptionCredit` (number)
    Customers consumption credit
    Example: 6.4

  - `transactionId` (string)
    Unique ID of the transaction (you have to generate it)
    Example: "4671fde7-bb07-4fe5-aa0e-947d9ccb842f"

  - `price` (number)
    Price of the product
    Example: 1.29

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

