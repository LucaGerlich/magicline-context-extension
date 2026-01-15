# Get classes slots

Required Scopes: 

Returns class slots within the timeframe of daysAhead starting from slotWindowStartDate, for multiple classes

Endpoint: GET /v1/classes/slots
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `daysAhead` (integer)
    Days from now on to look ahead

  - `slotWindowStartDate` (string)
    Class slots are retrieved within the time window from slotWindowStartDate to (slotWindowStartDate + daysAhead)

  - `offset` (string)
    Offset from last request

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of class slots

  - `result.id` (integer, required)
    Unique ID of a class slot
    Example: 1001

  - `result.startDateTime` (string)
    Class slot start date and time with zone
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `result.endDateTime` (string)
    Class slot end date and time with zone
    Example: "2022-06-22T09:00:00.000+02:00[Europe/Berlin]"

  - `result.classInformation` (object)
    Basic information of a class

  - `result.classInformation.id` (integer, required)
    Unique ID of the class
    Example: 1001

  - `result.classInformation.title` (string)
    Title of the class
    Example: "Mission Beach body"

  - `result.instructors` (array)
    List of instructors

  - `result.instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `result.instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `result.instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `result.instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `result.location` (object)
    Represents location data

  - `result.location.id` (integer, required)
    Unique ID of the location
    Example: 203

  - `result.location.name` (string, required)
    Name of the location
    Example: "Room 1"

  - `result.location.description` (string)
    Description of the location
    Example: "Room located behind reception"

  - `result.earliestBookingDateTime` (string)
    Class slot earliest booking date and time with zone
    Example: "2022-06-15T00:00:00.000+02:00[Europe/Berlin]"

  - `result.latestBookingDateTime` (string)
    Class slot latest booking date and time with zone
    Example: "2022-06-15T23:59:59.999+02:00[Europe/Berlin]"

  - `result.maxParticipants` (integer)
    Maximum participants allowed for a class slot
    Example: 25

  - `result.maxWaitingListParticipants` (integer)
    Maximum number of waiting list participants allowed for a class slot
    Example: 5

  - `result.bookedParticipants` (integer)
    Current number of booked participants of a class slot
    Example: 25

  - `result.additionalParticipants` (integer, required)
    Additional participants added by the operator
    Example: 5

  - `result.waitingListParticipants` (integer)
    Current number of waiting list participants of a class slot
    Example: 2

  - `hasNext` (boolean, required)
    True if there exists next data slice
    Example: true

  - `offset` (string, required)
    Offset for next query
    Example: "1234567890"

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

