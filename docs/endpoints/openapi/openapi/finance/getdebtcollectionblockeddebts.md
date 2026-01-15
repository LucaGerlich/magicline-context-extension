# Get blocked debt collection debts

Required Scopes: 

Endpoint: GET /v1/debt-collection/blocked/debts
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `debtId` (array)
    Unique ID of the debt

  - `offset` (string)
    Offset from last request

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of debtors

  - `result.debtorId` (string, required)
    Debtor unique id
    Example: "2334545"

  - `result.block` (object)
    Debtor is blocked for collection cases

  - `result.block.limitType` (string, required)
    Option to set customer or debt to blocklist
    Enum: "DISABLED", "LIMITED", "UNLIMITED"

  - `result.block.endDate` (string)
    Block customer or debt until
    Example: "2022-09-20"

  - `result.debts` (array)
    Debts of the debtor

  - `result.debts.debtId` (string, required)
    Unique Id for this debt in UUID format
    Example: "123e4567-e89b-42d3-a456-556642440000"

  - `result.debts.debtDate` (string, required)
    Due date of the debt
    Example: "1952-05-04"

  - `result.debts.contractStartDate` (string)
    If contract debt, it is set to the start date of the contract, otherwise due date
    Example: "1952-05-04"

  - `result.debts.amount` (number, required)
    Amount to collect for this debt
    Example: 333

  - `result.debts.currency` (string, required)
    ISO 4217 currency code
    Example: "USD"

  - `result.debts.type` (string, required)
    Type of debt collection
    Enum: "PRINCIPAL_CLAIM", "SALE", "DEBT_CLAIM", "FLAT_FEE", "DUNNING_FEE", "BANK_FEE"

  - `result.debts.designation` (string, required)
    Description of debt

  - `result.debts.recurrence` (object, required)
    Describes a recurrence with period and frequency

  - `result.debts.recurrence.period` (string, required)
    Represents a period
    Enum: "DAY", "MONTH", "WEEK", "YEAR", "ONCE"

  - `result.debts.recurrence.frequency` (integer)
    Frequency of the recurrence, eq. for period Month and frequency 2 this claim will appear every second month
    Example: 2

  - `result.debts.servicePeriodStartDate` (string)
    Start date of the rendered service, YYYY-MM-DD format
    Example: "1952-05-04"

  - `result.debts.servicePeriodEndDate` (string)
    End date of the rendered service, YYYY-MM-DD format
    Example: "1952-05-04"

  - `result.debts.maturityType` (string)
    Defines if a claim was changed due to rest maturity
    Enum: "NORMAL", "RESIDUAL"

  - `result.debts.latestRejectionReason` (string)
    Latest reason on why the payment was not successful
    Enum: "PURCHASE_LIMIT", "INVALID_IBAN", "CLOSED_BANKACCOUNT", "FRAUD", "INSOLVENCY", "DECEASED", "INCOMPLETE_ADDRESS", "INVALID_ADDRESS", "INVALID_OR_MISSING_INFORMATION", "CHARGED_BACK", "ALREADY_PURCHASED", "ALREADY_CHARGED_BACK", "CONTESTED_CONTRACT", "WITHDRAWN_MANDATE", "INVALID_SEPA_MANDATE", "IBAN_BLACKLISTED", "TERMINATED_CONTRACT", "IBAN_NOT_SEPA_DIRECT_DEBIT_CAPABLE", "AMOUNT_EXCEEDS_LIMIT", "NON_CONTRACTUAL", "PURCHASING_SUSPENDED", "INSTRUCTED_BY_STUDIO", "MISSING_LIABLE_PERSON", "IBAN_INVALID_SINCE_LAST_PAYMENT_RUN", "ACCOUNT_CLOSED_BEFORE_COLLECTION", "DEBT_OVERAGED", "DUNNING_UNSUCCESSFUL", "AUTOMATIC_CHARGEBACK", "STUDIO_CLOSED_DOWN", "REPEATED_INVALID_SEPA_MANDATE", "SETTLEMENT_AGREEMENT", "INVALID_SEPA_CREDITOR_ID", "INSUFFICIENT_COVERING", "OPPOSITION", "INVALID_BANK_INFORMATION", "INVALID_MANDATE", "AUTHORIZATION_DECLINED", "INVALID_CARD", "CARD_EXPIRED", "REVOKED_BY_CUSTOMER", "UNSUPPORTED_DEBT_CLAIM_TYPE", "PURCHASESTOP_FRAUD", "ALREADY_REJECTED", "CONSUMPTION_CREDIT_CHARGEBACK_DEBT_CLAIM_TYPE", "MANUALLY_REJECTED", "MANUALLY_SET_PURCHASESTOP", "OTHER", "OTHER_NO_FORWARDING_TO_EXTERNAL_COLLECTION_AGENCY", "UNKNOWN"

  - `result.debts.contractId` (integer)
    The field returns the contract_id from which the debt claim was created. It can be used to fetch the contract details using __GET /v1/customers/contracts/by__. In the case of non-contractual debt claims, this field is empty.

  - `result.debts.block` (object)
    Debt is blocked for collection cases

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

