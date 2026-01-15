# Create customer

Required Scopes: 

Creates a new customer (prospect) with comprehensive data to allow for future conversion to a full member

Endpoint: POST /v1/customers/create
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `firstName` (string, required)
    First name of the customer
    Example: "Peter"

  - `secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `lastName` (string, required)
    Last name of the customer
    Example: "Muller"

  - `secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `dateOfBirth` (string, required)
    Date of birth of the customer
    Example: "2019-08-24"

  - `placeOfBirth` (string)
    Place of birth of the customer. Required for Italian studios and nationals.

  - `countryOfBirth` (string)
    Country of birth of the customer. Required for Italian studios and non-Italian nationals

  - `email` (string, required)
    Email address of the customer
    Example: "example@example.com"

  - `gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `phoneNumberPrivate` (string)
    Private phone number of the customer
    Example: "+44123456789"

  - `phoneNumberMobile` (string)
    Mobile phone number of the customer
    Example: "+44987654321"

  - `street` (string, required)
    Street of the customer's address
    Example: "Raboisen Street"

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

  - `province` (string)
    Province of the customer's address
    Example: "Champagne"

  - `additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `language` (object, required)
    Language of the customer

  - `language.languageCode` (string, required)
    The language code
    Example: "de"

  - `language.countryCode` (string)
    The country code
    Example: "DE"

  - `houseNumber` (string)
    House number of the customer's address
    Example: "3-4"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `city` (string, required)
    City of the customer's address
    Example: "Hamburg"

  - `zipCode` (string, required)
    Zip code of the customer's address
    Example: "220-99"

  - `countryCode` (string, required)
    Country code of the customer's address
    Example: "DE"

  - `taxId` (string)
    Required if the studio is located in Spain or Italy. Alternatively, a valid document identification can be provided.
    Example: "12345678A"

  - `communicationPreferences` (array)
    List of communication preferences for the customer

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

  - `documentIdentification` (object)
    Information from an official document that identifies the customer

  - `documentIdentification.documentNumber` (string, required)
    Document number
    Example: "CX5432112345DS"

  - `documentIdentification.documentType` (string, required)
    Type of the document
    Enum: "ID_CARD", "PASSPORT", "DRIVERS_LICENCE", "RESIDENCE_PERMIT", "NATIONAL_ID_NUMBER", "OTHERS"

  - `paymentRequestToken` (string)
    By assigning the  to the customer, the payment method associated with the token will be used as payment method setting of the customer. Additionally, if the  is associated with a payment instrument, i.e. a SEPA Mandate, BACS Mandate, Credit Card, or other, the payment instrument will be made available in the member account for future collection via payment runs. By leaving this field empty the payment method of the customer will be set to . For reference check 'Create a user payment session'.

  - `additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `additionalInformationFieldAssignments.value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

## Response 200 fields (application/json):

  - `customerId` (integer, required)
    Unique ID of the customer
    Example: 1000

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

