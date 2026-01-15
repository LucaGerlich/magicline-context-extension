# Sign up a new membership

Required Scopes: 

Returns customer id within the result dto.

Endpoint: POST /v1/memberships/signup
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `contract` (object, required)
    The contract information used for the membership signup

  - `contract.contractOfferTermId` (integer, required)
    Unique ID of the contract offer term
    Example: 1000

  - `contract.startDate` (string, required)
    The start date of the contract
    Example: "2026-02-01"

  - `contract.preuseDate` (string)
    The pre use date of the contract. If not provided, it will be evaluated based on contract offer configuration.
    Example: "2026-01-01"

  - `contract.notes` (string)
    The notes related to the contract
    Example: "Some notes"

  - `contract.thirdPartyId` (string)
    Unique ID of the third party contract in the third party system
    Example: "1000a"

  - `contract.employeeId` (integer)
    Unique ID of the employee who created the membership
    Example: 1239812733

  - `contract.referralCode` (string)
    Referral code to link with recruiter
    Example: "A500D"

  - `contract.selectedSelectableModuleIds` (array)
    The selected modules from the available selectable modules

  - `contract.selectedOptionalModuleIds` (array)
    The selected modules from the available optional modules

  - `contract.initialPaymentRequestToken` (string)
    This token identifies a pre-authorized payment request. It acts as a reference to the payment session initiated by the user. It's not needed for preview endpoints.
    Example: "3JtyH5sakfn2V22vB0napNC2zWMlpFwS9gPQawuk7Jw1F00atOD0BA"

  - `contract.contractSignature` (object)
    The signature SVG for the contract document

  - `contract.contractSignature.base64SvgSignature` (string, required)
    Customer confirmation signature SVG value as base 64 string

  - `contract.textBlockSignatures` (array)
    Signatures for text blocks

  - `contract.textBlockSignatures.base64SvgSignature` (string, required)
    Text block's signature SVG value as base 64 string

  - `contract.textBlockSignatures.textBlockId` (integer, required)
    The ID of the referenced text block of the signature

  - `contract.voucherCode` (string)
    An optional code for a voucher. Only credit and discount vouchers are supported.
    Example: 123

  - `customer` (object, required)
    The customer information used for the membership signup

  - `customer.thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `customer.firstName` (string, required)
    First name of the customer
    Example: "Peter"

  - `customer.secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `customer.lastName` (string, required)
    Last name of the customer
    Example: "Muller"

  - `customer.secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `customer.dateOfBirth` (string, required)
    Date of birth of the customer
    Example: "2019-08-24"

  - `customer.placeOfBirth` (string)
    Place of birth of the customer. Required for Italian studios and nationals.

  - `customer.countryOfBirth` (string)
    Country of birth of the customer. Required for Italian studios and non-Italian nationals

  - `customer.email` (string, required)
    Email address of the customer
    Example: "example@example.com"

  - `customer.gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `customer.phoneNumberPrivate` (string)
    Private phone number of the customer
    Example: "+44123456789"

  - `customer.phoneNumberMobile` (string)
    Mobile phone number of the customer
    Example: "+44987654321"

  - `customer.street` (string, required)
    Street of the customer's address
    Example: "Raboisen Street"

  - `customer.secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `customer.cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `customer.district` (string)
    District of the customer's address
    Example: "District 12"

  - `customer.streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `customer.streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `customer.portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `customer.stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `customer.door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `customer.province` (string)
    Province of the customer's address
    Example: "Champagne"

  - `customer.additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `customer.floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `customer.language` (object, required)
    Language of the customer

  - `customer.language.languageCode` (string, required)
    The language code
    Example: "de"

  - `customer.language.countryCode` (string)
    The country code
    Example: "DE"

  - `customer.houseNumber` (string)
    House number of the customer's address
    Example: "3-4"

  - `customer.buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `customer.city` (string, required)
    City of the customer's address
    Example: "Hamburg"

  - `customer.zipCode` (string, required)
    Zip code of the customer's address
    Example: "220-99"

  - `customer.countryCode` (string, required)
    Country code of the customer's address
    Example: "DE"

  - `customer.taxId` (string)
    Required if the studio is located in Spain or Italy. Alternatively, a valid document identification can be provided.
    Example: "12345678A"

  - `customer.communicationPreferences` (array)
    List of communication preferences for the customer

  - `customer.communicationPreferences.messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `customer.communicationPreferences.channels` (array)
    The communication channels related to the message category of the communication preference

  - `customer.communicationPreferences.channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `customer.communicationPreferences.channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `customer.communicationPreferences.channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

  - `customer.documentIdentification` (object)
    Information from an official document that identifies the customer

  - `customer.documentIdentification.documentNumber` (string, required)
    Document number
    Example: "CX5432112345DS"

  - `customer.documentIdentification.documentType` (string, required)
    Type of the document
    Enum: "ID_CARD", "PASSPORT", "DRIVERS_LICENCE", "RESIDENCE_PERMIT", "NATIONAL_ID_NUMBER", "OTHERS"

  - `customer.paymentRequestToken` (string)
    By assigning the  to the customer, the payment method associated with the token will be used as payment method setting of the customer. Additionally, if the  is associated with a payment instrument, i.e. a SEPA Mandate, BACS Mandate, Credit Card, or other, the payment instrument will be made available in the member account for future collection via payment runs. By leaving this field empty the payment method of the customer will be set to . For reference check 'Create a user payment session'.

  - `customer.additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `customer.additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `customer.additionalInformationFieldAssignments.value` (string, required)
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

