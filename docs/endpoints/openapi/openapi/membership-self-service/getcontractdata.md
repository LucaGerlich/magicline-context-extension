# Get customer's contract data

Required Scopes: 

Returns customer's current contract data for memberships

Endpoint: GET /v1/memberships/{customerId}/self-service/contract-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `id` (integer, required)
    Id of the contract
    Example: 1000

  - `startDate` (string, required)
    Start date of the contract
    Example: "2022-01-15"

  - `endDate` (string, required)
    End date of the contract
    Example: "2025-10-15"

  - `rateName` (string, required)
    Name of the contract rate
    Example: "Premium"

  - `contractStatus` (string, required)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

  - `cancelationPeriod` (object)
    Represents a time period

  - `cancelationPeriod.periodValue` (integer, required)
    Defines how many units a given period lasts
    Example: 10

  - `cancelationPeriod.periodUnit` (string, required)
    Unit of the period
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `cancelationStatus` (string, required)
    Cancelation status of the contract cancelation
    Enum: "CANCELED", "PENDING_VERIFICATION", "PENDING_WITHDRAWAL_VERIFICATION"

  - `cancelationDate` (string)
    Date the cancelation of the contract was or will be canceled
    Example: "2023-01-25"

  - `cancelationReason` (string)
    Name of the reason why the contract was canceled
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

  - `lastPossibleCancelationDate` (string)
    Latest date the contract can be canceled
    Example: "2023-01-25"

  - `availableCancelationDates` (array)
    dates the contract can be canceled to
    Example: ["2023-01-25","2023-02-25"]

  - `cancelationOrigin` (string)
    Cancelation origin of the contract cancelation
    Enum: "STUDIO", "CUSTOMER"

  - `rateCodes` (array)
    Rate codes of this contract

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `price` (number, required)
    Base price of the contract
    Example: 19.9

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

