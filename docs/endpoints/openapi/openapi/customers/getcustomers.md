# Get customers

Required Scopes: 

Returns all customers from studio in expected slices

Endpoint: GET /v1/customers
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `offset` (string)
    Offset from last request (last ID of the customer)

  - `sliceSize` (integer)
    Desired size of data chunk

  - `customerStatus` (string)
    Defines status of returned customers
    Enum: "MEMBER", "PROSPECT"

  - `lastOffsetId` (integer)
    Last ID of customer from last chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of customers

  - `result.id` (integer, required)
    Unique ID of the customer
    Example: 1001

  - `result.customerNumber` (string)
    Customer number
    Example: "1-12345"

  - `result.firstName` (string)
    First name of the customer
    Example: "Edgar"

  - `result.secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `result.lastName` (string)
    Surname of the customer
    Example: "Bullock"

  - `result.secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `result.dateOfBirth` (string)
    Birthday of the customer
    Example: "1952-05-04"

  - `result.email` (string)
    Email address of the customer
    Example: "example@email.com"

  - `result.gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `result.street` (string)
    Street of the customer
    Example: "Am Bahnhof"

  - `result.houseNumber` (string)
    Number of the customer's house
    Example: 89

  - `result.zipCode` (string)
    Zip code of the customer
    Example: "12133"

  - `result.city` (string)
    City of the customer
    Example: "Munich"

  - `result.country` (string)
    Country of the customer
    Example: "DE"

  - `result.secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `result.cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `result.district` (string)
    District of the customer's address
    Example: "District 12"

  - `result.streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `result.streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `result.portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `result.stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `result.door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `result.province` (string)
    Province of the customer's address
    Example: "Champagne"

  - `result.additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `result.floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `result.buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `result.status` (string, required)
    Status of customer
    Enum: "MEMBER", "PROSPECT", "FORMER_MEMBER"

  - `result.imageUrl` (string)
    Url with an image to download. It will expire after 15 minutes
    Example: "https://example.com"

  - `result.phonePrivate` (string)
    Private phone number of the customer
    Example: "+49 30901820"

  - `result.phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+49 15223433333"

  - `result.phoneBusiness` (string)
    Business phone number of the customer
    Example: "+49 30901820"

  - `result.phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+49 15223433333"

  - `result.idlePeriods` (array)
    List of customer's idle periods

  - `result.idlePeriods.id` (integer, required)
    Unique ID of the idle period
    Example: 1000

  - `result.idlePeriods.startDate` (string, required)
    Start date of the idle period
    Example: "2022-01-01"

  - `result.idlePeriods.endDate` (string, required)
    End date of the idle period
    Example: "2022-10-01"

  - `result.idlePeriods.reason` (string)
    Reason of the idle period
    Example: "Illness"

  - `result.idlePeriods.contract` (object)
    Contract information

  - `result.idlePeriods.contract.id` (integer, required)
    Unique ID of the contract
    Example: 1000

  - `result.idlePeriods.contract.rateName` (string, required)
    Rate name for the contract
    Example: "Premium"

  - `result.idlePeriods.unlimited` (boolean, required)
    Indicates whether the idle period is unlimited

  - `result.bankAccount` (object)
    Customer's bank account information

  - `result.bankAccount.accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `result.bankAccount.bankName` (string)
    Bank name of the customers
    Example: "Deutsche Bank"

  - `result.bankAccount.bic` (string)
    Bic of the customers account
    Example: "DEUTDEFFXXX"

  - `result.bankAccount.iban` (string)
    Iban of the customers account
    Example: "DE91 1000 0000 0123 4567 89"

  - `result.accessRefusal` (boolean, required)
    Indicates whether the customer has an access block currently

  - `result.accessRestrictions` (array)
    List of access restrictions of the customer

  - `result.accessRestrictions.reason` (string, required)
    Reason for the restriction
    Example: "Destroyed equipment"

  - `result.accessRestrictions.startDate` (string)
    Start date of the restriction
    Example: "2024-01-01"

  - `result.accessRestrictions.endDate` (string)
    End date of the restriction
    Example: "2024-06-30"

  - `result.uuid` (string)
    Customer's UUID
    Example: "7be3932c-825b-4401-abff-29e9f9410bc7"

  - `result.referralCode` (string)
    Customer's referral code
    Example: "20J6N"

  - `result.studioId` (integer)
    Studio ID of the customer
    Example: 1238735970

  - `result.preferredLanguage` (object)
    Basic language information

  - `result.preferredLanguage.languageCode` (string, required)
    The language code
    Example: "de"

  - `result.preferredLanguage.countryCode` (string)
    The country code
    Example: "DE"

  - `result.additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `result.additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `result.additionalInformationFieldAssignments.value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

  - `result.thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `result.accessMediums` (array)
    List of access mediums of the customer

  - `result.accessMediums.id` (integer)
    Unique identifier for the access medium
    Example: 1234567890

  - `result.accessMediums.type` (string)
    Represents a type of access medium
    Enum: "CARD_NUMBER", "PIN", "BARCODE", "WALLET_PASS"

  - `result.accessMediums.value` (string)
    Unique identifier for the access medium

  - `result.cardNumbers` (array)
    UID list of the customer card numbers in expected format. (The new property to use is accessMediums)
    Example: ["1290158199"]

  - `hasNext` (boolean, required)
    True if there exists next data slice
    Example: true

  - `offset` (string, required)
    Offset for next query (last ID of the customer)
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

