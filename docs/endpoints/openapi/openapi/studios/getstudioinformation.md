# Get studio general information

Required Scopes: 

Returns studio's general information for authenticated subject

Endpoint: GET /v1/studios/information
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `name` (string)
    Studio name
    Example: "Example studio"

  - `description` (string)
    Studio description
    Example: "Example studio description"

  - `country` (string)
    Studio address' country
    Example: "Germany"

  - `countryCode` (string)
    Studio address' country code
    Example: "DE"

  - `studioId` (integer, required)
    Studio Id
    Example: 123

  - `openingDate` (string)
    Studio opening date
    Example: "2025-06-11"

  - `closingDate` (string)
    Studio closing date
    Example: "2029-01-01"

  - `email` (string)
    Studio email address
    Example: "operator@example.com"

  - `logoUrl` (string)
    Url to studio logo
    Example: "https://example.com"

  - `telephone` (string)
    Studio telephone
    Example: "0831/6901234-10"

  - `website` (string)
    Studio website url
    Example: "https://example.com"

  - `openingHours` (array)
    Studio internal opening hours

  - `openingHours.dayOfWeekFrom` (string)
    Start day of given range opening hours
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `openingHours.dayOfWeekTo` (string)
    End day of given range opening hours
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `openingHours.timeFrom` (string)
    Start hour of the range opening hours in ISO-8601 format
    Example: "06:00:00"

  - `openingHours.timeTo` (string)
    End hour of the range opening hours in ISO-8601 format
    Example: "23:00:00"

  - `publicOpeningHours` (array)
    Studio public opening hours

  - `closingHours` (array)
    Studio closing hours

  - `closingHours.reason` (string)
    Reason of closure
    Example: "Public holiday"

  - `closingHours.dateTimeFrom` (string)
    Start of the range closing hours
    Example: "2025-09-21T00:00:00"

  - `closingHours.dateTimeTo` (string)
    End of the range closing hours
    Example: "2025-09-22T00:00:00"

  - `openingHoursCategories` (array)
    Studio opening hours categories with time restrictions

  - `openingHoursCategories.categoryId` (integer, required)
    ID of the opening hours category
    Example: 1234567890

  - `openingHoursCategories.name` (string, required)
    Name of the opening hours category
    Example: "Off-Peak"

  - `openingHoursCategories.openingHours` (array, required)
    List of opening hours for this category

  - `openingHoursCategories.openingHours.dayOfWeek` (string, required)
    Day of the week
    Enum: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"

  - `openingHoursCategories.openingHours.timeFrom` (string, required)
    Start time in ISO-8601 format
    Example: "06:00:00"

  - `openingHoursCategories.openingHours.timeTo` (string, required)
    End time in ISO-8601 format
    Example: "23:00:00"

  - `street` (string)
    Studio address' street
    Example: "Kastanienallee"

  - `houseNumber` (string)
    Studio address' house number
    Example: "83"

  - `zip` (string)
    Studio address' zip code
    Example: "84439"

  - `city` (string)
    Studio address' city
    Example: "Berlin"

  - `accessCodeConfiguration` (object, required)
    Studio access code configurations

  - `accessCodeConfiguration.enabled` (boolean)
    Whether or not the access code is enabled

  - `location` (object)
    Studio location

  - `location.longitude` (number)
    The longitude of the coordination of the location
    Example: 9.993682

  - `location.latitude` (number)
    The latitude of the coordination of the location
    Example: 53.551086

  - `studioTags` (array)
    Tags associated with the studio

  - `studioTags.name` (string, required)
    Unique name of a tag
    Example: "tag123"

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

