# Get devices

Required Scopes: 

Returns devices for a studio

Endpoint: GET /v1/devices
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `id` (integer)
    Device id
    Example: 26

  - `name` (string)
    Device name
    Example: "Turnstile (left)"

  - `active` (boolean, required)
    Device state. If the value is false then the device is inactive and must be activated before use

  - `model` (string)
    Device model
    Enum: "GENERIC_VENDING_READER", "GENERIC_CARD_READER", "GENERIC_TIME_READER"

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

