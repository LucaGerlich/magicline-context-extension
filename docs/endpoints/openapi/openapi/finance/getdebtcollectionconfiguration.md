# Get Configuration of Debt Collection

Required Scopes: 

Get Configuration of Debt Collection

Endpoint: GET /v1/debt-collection/configuration
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `client` (object)
    The client matches a studio or location. The complete element should identify the person or company with its details of address, taxId, contact data and bank account information. An address should be complete, but only fields mandatory for all countries are marked as such

  - `client.name1` (string, required)
    Name first line
    Example: "GYMLAB Hamburg"

  - `client.name2` (string)
    Name second line
    Example: "GMBH"

  - `client.legalForm` (string)
    Legal form of the company
    Example: "GmbH"

  - `client.preTaxAttribute` (boolean, required)
    Possible to deduct tax up front

  - `client.vatSerialNo` (string)
    Tax ID of the client
    Example: "DE 142156559"

  - `client.postalCode` (string, required)
    Postal code of the client
    Example: "1180"

  - `client.city` (string, required)
    Cite code of the client
    Example: "Vienna"

  - `client.countryCode` (string)
    Country code of the client, ISO Alpha-2
    Example: "AT"

  - `client.country` (string)
    Country of the client
    Example: "Australia"

  - `client.paymentDetails` (object)
    Describes the payment data.

  - `client.paymentDetails.accountNumber` (string)
    Account number of the debtor
    Example: "91 1000 0000 0123 4567 89"

  - `client.paymentDetails.bankCode` (string)
    Bank code of the clients account
    Example: "DE"

  - `client.paymentDetails.iban` (string)
    Iban of the clients account
    Example: "DE91 1000 0000 0123 4567 89"

  - `client.paymentDetails.bic` (string)
    Bic of the clients account
    Example: "DEUTDEFFXXX"

  - `client.paymentDetails.bank` (string, required)
    Bank name of the client
    Example: "Deutsche Bank"

  - `client.paymentDetails.bankCountryCode` (string)
    Bank country code of the client
    Example: "DE"

  - `client.paymentDetails.accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `client.contactDetails` (array)
    List of contact details

  - `client.contactDetails.type` (string, required)
    Type of contact data
    Enum: "TEL_PRIVATE", "TEL_PRIVATE_MOBILE", "TEL_BUSINESS", "TEL_BUSINESS_MOBILE", "FAX", "EMAIL"

  - `client.contactDetails.value` (string, required)
    Value of contact data
    Example: "s.hannawald@sportaliance.com"

  - `client.contactDetails.status` (object)
    Describes the status of the contact data.

  - `client.contactDetails.status.type` (string, required)
    Type of contact status
    Enum: "NO_EMAIL", "NOT_YET_USED", "VALIDATION_IN_PROGRESS", "VALID", "VALID_READ", "INVALID", "WARNING", "REFUSED", "REFUSED_FULL", "REFUSED_VIRUS"

  - `client.contactDetails.status.statusInformation` (string)
    More details to the overall status
    Example: "The mail server for the recipient domain does not accept messages to this address."

  - `client.addressLine1` (string)
    Address first line
    Example: "Burgring 22"

  - `client.addressLine2` (string)
    Address second line
    Example: "1180 Vienna"

  - `client.addressLine3` (string)
    Address third line
    Example: "Austria"

  - `client.region` (string)
    Region of the client
    Example: "Vienna"

  - `client.addressData` (object)
    Describes the address in detail, so every country has its own fields filled. Use addressLines for preformatted address.

  - `client.addressData.street` (string)
    Street of the client
    Example: "Burgring"

  - `client.addressData.houseNumber` (string)
    House number of the client
    Example: "23A"

  - `client.addressData.addressStatus` (object)
    Describes the status of the address.

  - `client.addressData.addressStatus.type` (string, required)
    Type of address status
    Enum: "VALID", "INVALID"

  - `client.addressData.addressStatus.statusInformation` (string)
    More details on the overall status
    Example: "Letter could not be delivered"

  - `client.addressData.addressStatus.since` (string)
    Current status unchanged since
    Example: "2000-01-01"

  - `debtCollectionType` (string)
    Type of debt collection
    Enum: "TRUST", "PURCHASE"

  - `derecognizeRemainingDebtsOnClosure` (string)
    Debt handling on positive or negative closure of case
    Enum: "BY_PARTNER", "ALWAYS"

  - `derecognizeRemainingDebtsOnRejection` (string)
    Debt handling on rejection or reversal of case
    Enum: "BY_PARTNER", "ALWAYS"

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

