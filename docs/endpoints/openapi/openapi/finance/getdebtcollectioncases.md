# Get debt collection cases

Required Scopes: 

Returns the current state of debt collection cases specified by debtorId, collectionCaseId and agencyCollectionCaseId. Each parameter has maximum allowable 50 ids.

Endpoint: GET /v1/debt-collection/cases
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `debtorId` (array)
    Unique ID of the debtor

  - `collectionCaseId` (array)
    The case id provided by Magicline. This is returned from the 'Get Debtors' endpoint as 'collectionCaseId'

  - `agencyCollectionCaseId` (array)
    The case ID used by the agency. This relates to the 'agencyCollectionCaseId' parameter used in the 'Update debt collection' endpoint.

  - `caseAdjustmentRequestId` (integer)
    The request ID delivered by webhook entityId. It contains the latest changes to a case in the Magicline.

## Response 200 fields (application/json):

  - `debtorId` (string, required)
    Debtor unique id
    Example: "2334545"

  - `agencyCollectionCases` (array, required)
    List of debt collection cases

  - `agencyCollectionCases.agencyCollectionCaseId` (string, required)
    ID the agency has assigned to this case
    Example: "agency-id-123"

  - `agencyCollectionCases.publicCollectionCaseId` (string)
    Optional customer facing identifier for this case, if there is one that differs from agencyCollectionCaseId and is used in human correspondence.
    Example: "case-john-wayne-1"

  - `agencyCollectionCases.collectionCaseIds` (array, required)
    List of collection case ids which we have created, aggregated for that collection case
    Example: ["123e4567-e89b-42d3-a456-556642440000"]

  - `agencyCollectionCases.closure` (object)
    Must be set in case the case has been closed, omit this entirely if the case isn't closed.

  - `agencyCollectionCases.closure.type` (string, required)
    Closure type
    Enum: "POSITIVE", "NEGATIVE", "REVERSAL", "REJECTION"

  - `agencyCollectionCases.closure.options` (array)
    Additional settings for case closures

  - `agencyCollectionCases.closure.options.key` (string, required)
    Additional option key
    Enum: "WRITE_OFF_REMAINING_DEBTS"

  - `agencyCollectionCases.closure.options.value` (string, required)
    The option value, see the option key description for allowed values.
    Example: "value"

  - `agencyCollectionCases.closure.date` (string, required)
    Closure date
    Example: "2022-09-20"

  - `agencyCollectionCases.closure.rejectionReason` (string)
    Mandatory if type is REJECTION. This defines why the case was rejected by the agency.
    Enum: "CLAIMS_ALREADY_IN_COURT", "MISSING_COMPENSATION_BLOCKING_DUNNING_PROCESS", "NO_INFORMATION_ABOUT_LEGAL_REPRESENTATIVE", "NO_COLLECTION_ABROAD_POSSIBLE", "COLLECTING_FROM_INHERIT_NOT_POSSIBLE", "CLAIMS_TIME_BARRED_OR_RESIDUAL_DEBT_DISCHARGE_GRANTED", "REMAINING_CLAIM_BELOW_LIMIT", "NOTIFICATION_OBLIGATIONS_NOT_POSSIBLE", "FRAUD", "CONFLICT_OF_INTEREST", "WITHDRAWN_BY_STUDIO", "NO_PROCESSING_AT_ALL", "HARD_NEGATIVES_IN_DEBTOR_REGISTER", "POSTAL_DELIVERY_NOT_POSSIBLE", "CLAIM_INCREASE_IMPORTED_SYSTEM"

  - `agencyCollectionCases.closure.closureReason` (string)
    Optional closure reason.
    Example: "Not successful due to mail not successfully delivered"

  - `agencyCollectionCases.debts` (array, required)
    Debts which were transferred to the agency. At least all changed debts must be included, also unchanged debts can be included.

  - `agencyCollectionCases.debts.debtId` (string, required)
    Debt id from the Transfer, identifying a debt, in UUID format
    Example: "123e4567-e89b-42d3-a456-556642440000"

  - `agencyCollectionCases.debts.originalAmount` (number, required)
    Transferred amount to debt collection agency. Cancelled amount + paid amount should not be higher than original amount.
    Example: 100

  - `agencyCollectionCases.debts.canceledAmount` (number, required)
    Not accepted amount. If the case is closed and writeOffRemainingDebts is set, they will be written off and not opened again.

  - `agencyCollectionCases.debts.paidAmount` (number, required)
    Paid amount, the status should always contain the amount which was paid to the debt collection agency. If paidAmount is higher than original amount, the loose rest will still be booked to the debtor.
    Example: 100

  - `agencyCollectionCases.debts.currency` (string, required)
    ISO 4217 currency of the debt code
    Example: "EUR"

  - `agencyCollectionCases.debts.block` (object)
    Option to block the debt for future collection cases. If no block is sent an existing block will be removed.

  - `agencyCollectionCases.debts.block.limitType` (string, required)
    Option to set customer or debt to blocklist
    Enum: "DISABLED", "LIMITED", "UNLIMITED"

  - `agencyCollectionCases.debts.block.endDate` (string, required)
    Block customer or debt until
    Example: "2022-09-20"

  - `block` (object)
    Option to block the debtor for future collection cases. If no block is sent an existing block will be removed.

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

