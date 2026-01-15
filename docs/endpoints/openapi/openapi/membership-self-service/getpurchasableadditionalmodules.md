# Get purchasable additional modules

Required Scopes: 

Get purchasable additional modules for a studio and a customer (via main contract)

Endpoint: GET /v1/memberships/{contractId}/self-service/additional-modules/purchasable
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `contractId` (integer, required)
    Unique ID of the main contract

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the additional module
    Example: 203

  - `name` (string, required)
    Name of the additional module rate
    Example: "drink flat"

  - `description` (string)
    Description of the additional module rate
    Example: "drink flat"

  - `imageUrl` (string, required)
    Image url of the additional module
    Example: "https://www.image.com"

  - `paymentFrequencies` (array, required)
    Payment frequencies of the additional module

  - `paymentFrequencies.id` (integer)
    Unique ID of the payment frequency of an additional module
    Example: 203

  - `paymentFrequencies.type` (string, required)
    Payment frequency type of an additional module
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `paymentFrequencies.term` (object)
    Represents a term

  - `paymentFrequencies.term.value` (integer, required)
    The value of the term
    Example: 2

  - `paymentFrequencies.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `paymentFrequencies.price` (object)
    Base price, used only for payment frequencies of type RECURRING

  - `paymentFrequencies.price.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `paymentFrequencies.price.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `paymentFrequencies.monthDaysToPrices` (array)
    Month day to prices list, used for additional module payment frequency type MONTH_DAY

  - `paymentFrequencies.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `paymentFrequencies.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `paymentFrequencies.monthDaysToPrices.monthDay.monthValue` (integer)

  - `paymentFrequencies.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `paymentFrequencies.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `paymentFrequencies.termsToPrices` (array)
    Terms to prices list, used for additional module payment frequency type TERM_BASED. Note that the price will become active AFTER the respective term has passed

  - `termInformation` (object, required)
    Term information of the additional module

  - `termInformation.extension` (object)
    Represents an additional module extension

  - `termInformation.extension.extensionType` (string, required)
    Extension type of an additional module
    Enum: "TERM_EXTENSION", "NEW"

  - `termInformation.extension.termExtension` (object)
    Represents a term

  - `termInformation.extension.extensionCancelationPeriod` (object)
    Represents a term

  - `termInformation.cancelationPeriod` (object)
    Represents a term

  - `trialPeriodConfig` (object)
    Represents the trial period config of an additional module

  - `trialPeriodConfig.description` (string)
    Description of the trial period config
    Example: "Test period for the drink flat"

  - `rateCodes` (array)
    Rate codes of the additional module rate

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

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

