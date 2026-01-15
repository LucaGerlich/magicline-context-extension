# Create a user payment session

Required Scopes: 

Request to initiate a user session for payments. This is used to collect payment instruments for future recurring payments or one-time transactions.

Endpoint: POST /v1/payments/user-session
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `amount` (number, required)
    Specifies the payment amount for the initiated transaction. Should equal 0 to capture a payment instrument for future recurring payments. The currency is defined by the studio.
    Example: 19.99

  - `scope` (string, required)
    Specifies where the created payment instruments will be used, as the available payment methods differ by scope.
    Enum: "MEMBER_ACCOUNT", "ECOM"

  - `customerId` (integer)
    This field represents the unique identifier for an existing customer within ERP. Providing this ID ensures the payment session is linked to the correct customer record. It is a mutually exclusive field with , meaning you can only provide one or the other.

- : This ID is required for payment sessions involving existing customers.

- : If this field is left empty, a new customer will be treated as a âpotential customerâ and a  will be automatically generated and returned in the response. If omitted, it will not be possible to use it for existing customers.

- :
    Example: 1234567890

  - `finionPayCustomerId` (string)
    This field is the identifier for a customer within the Finion Pay payment service, typically used for customers who are not yet registered in ERP. Use this ID to track repeat payment sessions for a potential customer.

- : This ID should only be provided for subsequent payment sessions for a customer who has been previously identified by Finion Pay but doesnât have an ERP  yet.

- : In the absence of a , a new  will be automatically created and assigned to the user for the current session.

- :
    Example: "753ea8ec-c2ec-4761-824b-bc46eda3f644"

  - `permittedPaymentChoices` (array)
    List of permitted payment choices, i.e. obtained by the contract offer. Acts as a filter for the available payment methods defined by the scope
    Enum: "CASH", "BANK_TRANSFER", "BACS", "SEPA", "CH_DD", "LSV", "CREDIT_CARD", "TWINT", "PAYPAL", "BANCONTACT", "IDEAL"

  - `referenceText` (string, required)
    Allows the definition of the reference text shown on the bank statement of the customer.
    Example: "Gym Joining Fee 01.07.2025"

  - `requireDirectDebitSignature` (boolean)
    When set to true the direct debit form will show a signature field to the user that is required to proceed. This applies to the payment methods SEPA, CH_DD and LSV.

  - `showExistingPaymentInstruments` (boolean)
    When set to true the UPC component will also fetch the user's existing payment instruments. Default is true
    Example: true

## Response 200 fields (application/json):

  - `token` (string, required)
    The token for the user session.
    Example: "CllClFmVlSCs3oe0ND0JloLWlNzdb3QseU4507gf1mSVAHqRTwzKWU"

  - `tokenValidUntil` (string, required)
    The date and time until the token is valid.
    Example: "2025-01-07T16:25:09.416924Z"

  - `finionPayCustomerId` (string, required)
    Identifies a customer in Finion Pay, i.e. to retreive existing payment instruments.
    Example: "753ea8ec-c2ec-4761-824b-bc46eda3f644"

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

