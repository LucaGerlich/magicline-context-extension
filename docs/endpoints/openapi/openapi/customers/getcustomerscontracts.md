# Get customer's contracts

Required Scopes(any of): , 

Returns customer's contracts

Endpoint: GET /v1/customers/{customerId}/contracts
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `status` (string)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the contract
    Example: 1000

  - `createdDate` (string, required)
    Creation date of the contract
    Example: "2022-01-01"

  - `startDate` (string, required)
    Start date of the contract
    Example: "2022-01-01"

  - `endDate` (string, required)
    End date of the contract
    Example: "2022-10-01"

  - `rateName` (string, required)
    Rate name for the contract
    Example: "Premium"

  - `rateCodes` (array)
    Rate codes of this contract

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `contractStatus` (string, required)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

  - `cancellationPeriod` (object)
    Represents a time period

  - `cancellationPeriod.periodValue` (integer, required)
    Defines how many units a given period lasts
    Example: 10

  - `cancellationPeriod.periodUnit` (string, required)
    Unit of the period
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `cancelled` (boolean, required)
    Defines whether or not the current active contract has been cancelled

  - `cancellationDate` (string)
    Contract cancellation date
    Example: "2022-10-10"

  - `cancellationReceiptDate` (string)
    Contract cancellation receipt date
    Example: "2022-10-10"

  - `cancellationReason` (string)
    Reason of the contract cancellation
    Example: "Officially ordered studio closure"

  - `priceDetails` (object, required)
    Price details of the contract

  - `priceDetails.basePrice` (object, required)
    Base price of the contract

  - `priceDetails.basePrice.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `priceDetails.basePrice.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `priceDetails.currentPrice` (object, required)
    Current price of the contract. This price takes into account any adjustments that have been made to the base price

  - `priceDetails.paymentFrequency` (object, required)
    Payment frequency of the contract

  - `priceDetails.paymentFrequency.id` (integer)
    Unique ID of the payment frequency of a contract
    Example: 203

  - `priceDetails.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `priceDetails.paymentFrequency.term` (object)
    Represents a term

  - `priceDetails.paymentFrequency.term.value` (integer, required)
    The value of the term
    Example: 2

  - `priceDetails.paymentFrequency.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `priceDetails.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `priceDetails.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `priceDetails.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `priceDetails.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active AFTER the respective term has passed

  - `lastPossibleCancellationDate` (string, required)
    Latest date when the contract can be cancelled

  - `term` (object, required)
    Represents a time period

  - `extensionTerm` (object, required)
    Represents a time period

  - `flatFeeContracts` (array)
    List of flat fee contracts

  - `flatFeeContracts.endDate` (string)
    End date of contract

  - `flatFeeContracts.paymentFrequency` (string, required)
    Type of payment frequency
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `flatFeeContracts.price` (number, required)
    Base price of the contract
    Example: 19.9

  - `moduleContracts` (array)
    List of module contracts

  - `signedDocumentUrl` (string)
    Url to download the contract related document. It will expire after 15 minutes

  - `thirdPartyId` (string)
    Unique ID of the third party contract in the third party system
    Example: "1000a"

## Response 400 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 401 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 403 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 404 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 409 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 429 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

## Response 500 fields (application/json):

  - `errorMessage` (string, required)
    Resolved message in the context-specific default locale

  - `errorCode` (string)
    Key for translation files

  - `traceId` (string)
    Datadog trace id

  - `reference` (string)
    Reference to validation error
    Example: "parent.child"

  - `args` (array)
    Arguments referenced by format specifiers while resolving the message from translation files

  - `typedArgs` (array)
    Same as  but with type information

  - `typedArgs.value` (object)

  - `typedArgs.type` (string)
    Enum: "TIMESTAMP", "BOOLEAN", "DATE", "MONTH_DAY", "TIME", "TERM", "TERM_LIST", "INTEGER", "DECIMAL", "STRING", "MONEY", "LIMITABLE_CONFIG_PROPERTY", "I18N_KEY", "I18N_KEY_LIST", "PERMISSION_LIST", "ENUM", "AVAILABILITY_LIST"

