# Post customer's benefit usage

Required Scopes(any of): , 

Endpoint: POST /v1/customers/{customerId}/benefits/{benefitKey}/use
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

  - `benefitKey` (string, required)
    Key of the benefit to use

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

