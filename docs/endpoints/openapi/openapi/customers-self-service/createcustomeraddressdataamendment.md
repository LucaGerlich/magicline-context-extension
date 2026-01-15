# Create address data amendment

Required Scopes: 

Creates request for address data amendment for specified customerId

Endpoint: POST /v1/customers/{customerId}/self-service/address-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `street` (string, required)
    Street of the customer
    Example: "Am Bahnhof"

  - `houseNumber` (string)
    Number of the customer's house
    Example: "90"

  - `zipCode` (string, required)
    Zip code of the customer
    Example: "12133"

  - `city` (string, required)
    City of the customer
    Example: "Munich"

  - `countryCode` (string, required)
    Country of the customer
    Example: "DE"

  - `province` (string)
    Province for southern Europe/US countries
    Example: "Madrid/California"

  - `provinceCode` (string)
    Province code for southern Europe/US countries
    Example: "MD/CA"

  - `secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `district` (string)
    District of the customer's address
    Example: "District 12"

  - `streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

## Response 200 fields (application/json):

  - `id` (integer)
    Amendment proposal id

  - `street` (string, required)
    Street of the customer
    Example: "Am Bahnhof"

  - `houseNumber` (string)
    Number of the customer's house
    Example: "90"

  - `zipCode` (string, required)
    Zip code of the customer
    Example: "12133"

  - `city` (string, required)
    City of the customer
    Example: "Munich"

  - `countryCode` (string, required)
    Country of the customer
    Example: "DE"

  - `province` (string)
    Province for southern Europe/US countries
    Example: "Madrid/California"

  - `provinceCode` (string)
    Province code for southern Europe/US countries
    Example: "MD/CA"

  - `secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `district` (string)
    District of the customer's address
    Example: "District 12"

  - `streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

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

