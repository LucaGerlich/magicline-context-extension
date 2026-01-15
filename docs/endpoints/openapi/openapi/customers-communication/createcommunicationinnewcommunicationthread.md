# Create communication thread

Required Scopes: 

Creates new thread with a new communication for a customer

Endpoint: POST /v1/communications/{customerId}/threads
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer

## Request fields (application/json):

  - `communicationThreadStatus` (string, required)
    The status of a communication thread
    Enum: "CREATED", "ONGOING", "CLOSED"

  - `ticketNumber` (string)
    The ticket number of the third party ticketing system
    Example: "A123456"

  - `subject` (string, required)
    The subject of the communication
    Example: "Complaint"

  - `content` (string, required)
    The content of the communication
    Example: "I received two invoices this month, but I only made one purchase."

  - `communicationDirection` (string, required)
    The direction of the communication
    Enum: "INCOMING", "OUTGOING"

  - `ticketLink` (string)
    The link to the ticket in the third party ticketing system
    Example: "https://ticketing-system.com/ticket/A123456"

  - `communicationChannel` (string, required)
    The channel of the communication
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `agent` (string)
    The employee/agent handling the communication
    Example: "Peter Meyer"

  - `communicationDateTime` (string)
    When this field is not null it will be used as the date time of the communication instead of the current time
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

## Response 200 fields (application/json):

  - `customerId` (integer, required)
    The customer's ID
    Example: 1

  - `communicationId` (integer, required)
    The ID of the communication
    Example: 1

  - `threadId` (integer, required)
    The ID of the communication thread
    Example: 1

  - `communicationThreadStatus` (string, required)
    The status of a communication thread
    Enum: "CREATED", "ONGOING", "CLOSED"

  - `ticketNumber` (string)
    The ticket number of the third party ticketing system
    Example: "A123456"

  - `subject` (string, required)
    The subject of the communication
    Example: "Complaint"

  - `content` (string, required)
    The content of the communication
    Example: "I received two invoices this month, but I only made one purchase."

  - `communicationDirection` (string, required)
    The direction of the communication
    Enum: "INCOMING", "OUTGOING"

  - `ticketLink` (string)
    The link to the ticket in the third party ticketing system
    Example: "https://ticketing-system.com/ticket/A123456"

  - `communicationChannel` (string, required)
    The channel of the communication
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `agent` (string)
    The employee/agent handling the communication
    Example: "Peter Meyer"

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

