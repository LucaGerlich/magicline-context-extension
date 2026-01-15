# Search customers

Required Scopes: 

Returns all customers from studio by given criteria

Endpoint: POST /v1/customers/search
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `firstName` (string)
    Substring of customer first name starts from beginning
    Example: "Edga"

  - `lastName` (string)
    Substring of customer last name starts from beginning
    Example: "Bull"

  - `email` (string)
    Customer email
    Example: "example@email.com"

  - `dateOfBirth` (string)
    Customer date of birth
    Example: "1952-05-04"

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the customer
    Example: 1001

  - `customerNumber` (string)
    Customer number
    Example: "1-12345"

  - `firstName` (string)
    First name of the customer
    Example: "Edgar"

  - `secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `lastName` (string)
    Surname of the customer
    Example: "Bullock"

  - `secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `dateOfBirth` (string)
    Birthday of the customer
    Example: "1952-05-04"

  - `email` (string)
    Email address of the customer
    Example: "example@email.com"

  - `gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `street` (string)
    Street of the customer
    Example: "Am Bahnhof"

  - `houseNumber` (string)
    Number of the customer's house
    Example: 89

  - `zipCode` (string)
    Zip code of the customer
    Example: "12133"

  - `city` (string)
    City of the customer
    Example: "Munich"

  - `country` (string)
    Country of the customer
    Example: "DE"

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

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `status` (string, required)
    Status of customer
    Enum: "MEMBER", "PROSPECT", "FORMER_MEMBER"

  - `imageUrl` (string)
    Url with an image to download. It will expire after 15 minutes
    Example: "https://example.com"

  - `phonePrivate` (string)
    Private phone number of the customer
    Example: "+49 30901820"

  - `phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+49 15223433333"

  - `phoneBusiness` (string)
    Business phone number of the customer
    Example: "+49 30901820"

  - `phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+49 15223433333"

  - `idlePeriods` (array)
    List of customer's idle periods

  - `idlePeriods.id` (integer, required)
    Unique ID of the idle period
    Example: 1000

  - `idlePeriods.startDate` (string, required)
    Start date of the idle period
    Example: "2022-01-01"

  - `idlePeriods.endDate` (string, required)
    End date of the idle period
    Example: "2022-10-01"

  - `idlePeriods.reason` (string)
    Reason of the idle period
    Example: "Illness"

  - `idlePeriods.contract` (object)
    Contract information

  - `idlePeriods.contract.id` (integer, required)
    Unique ID of the contract
    Example: 1000

  - `idlePeriods.contract.rateName` (string, required)
    Rate name for the contract
    Example: "Premium"

  - `idlePeriods.unlimited` (boolean, required)
    Indicates whether the idle period is unlimited

  - `bankAccount` (object)
    Customer's bank account information

  - `bankAccount.accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `bankAccount.bankName` (string)
    Bank name of the customers
    Example: "Deutsche Bank"

  - `bankAccount.bic` (string)
    Bic of the customers account
    Example: "DEUTDEFFXXX"

  - `bankAccount.iban` (string)
    Iban of the customers account
    Example: "DE91 1000 0000 0123 4567 89"

  - `accessRefusal` (boolean, required)
    Indicates whether the customer has an access block currently

  - `accessRestrictions` (array)
    List of access restrictions of the customer

  - `accessRestrictions.reason` (string, required)
    Reason for the restriction
    Example: "Destroyed equipment"

  - `accessRestrictions.startDate` (string)
    Start date of the restriction
    Example: "2024-01-01"

  - `accessRestrictions.endDate` (string)
    End date of the restriction
    Example: "2024-06-30"

  - `uuid` (string)
    Customer's UUID
    Example: "7be3932c-825b-4401-abff-29e9f9410bc7"

  - `referralCode` (string)
    Customer's referral code
    Example: "20J6N"

  - `studioId` (integer)
    Studio ID of the customer
    Example: 1238735970

  - `preferredLanguage` (object)
    Basic language information

  - `preferredLanguage.languageCode` (string, required)
    The language code
    Example: "de"

  - `preferredLanguage.countryCode` (string)
    The country code
    Example: "DE"

  - `additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `additionalInformationFieldAssignments.value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

  - `thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `accessMediums` (array)
    List of access mediums of the customer

  - `accessMediums.id` (integer)
    Unique identifier for the access medium
    Example: 1234567890

  - `accessMediums.type` (string)
    Represents a type of access medium
    Enum: "CARD_NUMBER", "PIN", "BARCODE", "WALLET_PASS"

  - `accessMediums.value` (string)
    Unique identifier for the access medium

  - `cardNumbers` (array)
    UID list of the customer card numbers in expected format. (The new property to use is accessMediums)
    Example: ["1290158199"]

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

