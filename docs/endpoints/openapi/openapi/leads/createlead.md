# Create a new Lead based on the config

Required Scopes: 

Creates a new lead based on the configuration

Endpoint: POST /v1/leads/create
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `leadCustomer` (object, required)
    Lead customer information

  - `leadCustomer.thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `leadCustomer.firstname` (string, required)
    First name of the lead customer
    Example: "Max"

  - `leadCustomer.secondFirstname` (string)
    Second first name of the lead customer
    Example: "Peter"

  - `leadCustomer.lastname` (string, required)
    Last name of the lead customer
    Example: "Mustermann"

  - `leadCustomer.secondLastname` (string)
    Second last name of the lead customer
    Example: "Meier"

  - `leadCustomer.email` (string, required)
    Email of the lead customer
    Example: "example@email.com"

  - `leadCustomer.gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `leadCustomer.dateOfBirth` (string)
    Date of birth of the lead customer
    Example: "2000-10-10"

  - `leadCustomer.telephone` (string)
    Telephone number of the lead customer
    Example: "5006001112"

  - `leadCustomer.language` (object)
    Language of the lead customer

  - `leadCustomer.language.languageCode` (string, required)
    The language code
    Example: "de"

  - `leadCustomer.language.countryCode` (string)
    The country code
    Example: "DE"

  - `address` (object)
    Representing lead customer address data with mandatory fields

  - `address.street` (string, required)
    Street of the customer
    Example: "Am Bahnhof"

  - `address.houseNumber` (string, required)
    Number of the customer's house
    Example: "90"

  - `address.zipCode` (string, required)
    Zip code of the customer
    Example: "12133"

  - `address.city` (string, required)
    City of the customer
    Example: "Munich"

  - `address.countryCode` (string, required)
    Country of the customer
    Example: "DE"

  - `address.province` (string)
    Province for southern Europe/US countries
    Example: "Madrid/California"

  - `address.provinceCode` (string)
    Province code for southern Europe/US countries
    Example: "MD/CA"

  - `address.secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `address.cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `address.district` (string)
    District of the customer's address
    Example: "District 12"

  - `address.streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `address.streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `address.portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `address.stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `address.door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `address.additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `address.floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `address.buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `communicationPreferences` (array)
    List of the communication preferences of the lead

  - `communicationPreferences.messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `communicationPreferences.channels` (array)
    The communication channels related to the message category of the communication preference

  - `communicationPreferences.channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `communicationPreferences.channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `communicationPreferences.channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

  - `additionalInformation` (array)
    List of the the additional information about the lead

  - `additionalInformation.additionalFieldId` (integer, required)
    The additional information field unique ID
    Example: 1246357240

  - `additionalInformation.value` (string)
    The additional field value, which can semantically be a boolean, date, text or numeric. For text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.
    Example: "Friends"

  - `additionalInformation.values` (array)
    The additional field values if allowMultiSelection is set to true
    Example: ["Radio","Webinar"]

  - `notes` (string)
    Any notes about the lead
    Example: "Free trials and classes"

  - `externalIdentifier` (string)
    The external ID of the Campaign associated with the lead
    Example: "CMPGN-123"

## Response 200 fields (application/json):

  - `id` (integer, required)
    The unique ID of the lead
    Example: 1246358530

  - `uuid` (string, required)
    The customer unique ID of the created lead
    Example: "2340b1cc-3fe7-4f81-8eca-f92181dd2bb4"

  - `customerNumber` (string, required)
    The customer number of the created lead
    Example: "1-4139"

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

