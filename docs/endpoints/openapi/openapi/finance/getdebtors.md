# Get Debtors

Required Scopes: 

Returns debtors for specified debtCollectionRunId in slices

Endpoint: GET /v1/debt-collection/{debtCollectionRunId}/debtors
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `debtCollectionRunId` (integer, required)
    Unique ID of the debt collection run

## Query parameters:

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

  - `result.membershipNr` (string, required)
    Membership number of the debtor
    Example: "1568462597"

  - `result.countryCode` (string)
    Country code of the debtor
    Example: "AT"

  - `result.country` (string)
    Country of the debtor
    Example: "Austria"

  - `result.identificationNumber` (string)
    Identification number of the debtor
    Example: "ATU143543"

  - `result.paymentDetails` (object)
    Describes the payment data.

  - `result.paymentDetails.accountNumber` (string)
    Account number of the debtor
    Example: "91 1000 0000 0123 4567 89"

  - `result.paymentDetails.bankCode` (string)
    Bank code of the clients account
    Example: "DE"

  - `result.paymentDetails.iban` (string)
    Iban of the clients account
    Example: "DE91 1000 0000 0123 4567 89"

  - `result.paymentDetails.bic` (string)
    Bic of the clients account
    Example: "DEUTDEFFXXX"

  - `result.paymentDetails.bank` (string, required)
    Bank name of the client
    Example: "Deutsche Bank"

  - `result.paymentDetails.bankCountryCode` (string)
    Bank country code of the client
    Example: "DE"

  - `result.paymentDetails.accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `result.contractDetails` (array)
    Contract data of the debtor

  - `result.contractDetails.id` (integer, required)
    Id of the contract
    Example: 123123213

  - `result.contractDetails.rateName` (string)
    Rate name of the contract
    Example: "Gold"

  - `result.contractDetails.startDate` (string, required)
    Start date of the contract
    Example: "1952-05-04"

  - `result.contractDetails.endDate` (string, required)
    End date of the contract
    Example: "1953-05-04"

  - `result.contractDetails.createdDate` (string, required)
    Creation date of the contract
    Example: "2022-01-01"

  - `result.contractDetails.cancelled` (boolean, required)
    If the contract is cancelled

  - `result.contractDetails.contractPeriod` (object)
    Describes a recurrence with period and frequency

  - `result.contractDetails.contractPeriod.period` (string, required)
    Represents a period
    Enum: "DAY", "MONTH", "WEEK", "YEAR", "ONCE"

  - `result.contractDetails.contractPeriod.frequency` (integer)
    Frequency of the recurrence, eq. for period Month and frequency 2 this claim will appear every second month
    Example: 2

  - `result.contractDetails.extensionPeriod` (object)
    Describes a recurrence with period and frequency

  - `result.contractDetails.cancellationPeriod` (object)
    Describes a recurrence with period and frequency

  - `result.birthdate` (string)
    Birth date of the debtor
    Example: "1952-05-04"

  - `result.firstName` (string, required)
    First name of the debtor
    Example: "Sven"

  - `result.lastName` (string, required)
    Last name of the debtor name
    Example: "Hannawald"

  - `result.secondLastName` (string)
    Second last name of the debtor name
    Example: "Shmidt"

  - `result.sex` (string, required)
    Sex of the debtor
    Example: "MALE"

  - `result.postalCode` (string)
    Postal code of the debtor
    Example: "1180"

  - `result.city` (string, required)
    City of the debtor
    Example: "Vienna"

  - `result.liablePerson` (object)
    The LiablePerson is used for members not being responsible themself for payments. The complete element should identify the liable person with its details of address, contact data and bank account information. It includes also country specific elements.

  - `result.liablePerson.firstName` (string, required)
    First name of liable person
    Example: "Sven"

  - `result.liablePerson.lastName` (string, required)
    Last name of liable person
    Example: "Hannawald"

  - `result.liablePerson.secondLastName` (string)
    Second last name liable person
    Example: "Shmidt"

  - `result.liablePerson.birthdate` (string)
    Birthdate of liable person
    Example: "1952-05-04"

  - `result.liablePerson.sex` (string)
    Sex of liable person
    Example: "MALE"

  - `result.liablePerson.postalCode` (string)
    Postal code of liable person
    Example: "1180"

  - `result.liablePerson.city` (string)
    City of liable person
    Example: "Vienna"

  - `result.liablePerson.countryCode` (string)
    Country code of liable person
    Example: "AT"

  - `result.liablePerson.contactDetails` (array)
    Contact data of liable person

  - `result.liablePerson.contactDetails.type` (string, required)
    Type of contact data
    Enum: "TEL_PRIVATE", "TEL_PRIVATE_MOBILE", "TEL_BUSINESS", "TEL_BUSINESS_MOBILE", "FAX", "EMAIL"

  - `result.liablePerson.contactDetails.value` (string, required)
    Value of contact data
    Example: "s.hannawald@sportaliance.com"

  - `result.liablePerson.contactDetails.status` (object)
    Describes the status of the contact data.

  - `result.liablePerson.contactDetails.status.type` (string, required)
    Type of contact status
    Enum: "NO_EMAIL", "NOT_YET_USED", "VALIDATION_IN_PROGRESS", "VALID", "VALID_READ", "INVALID", "WARNING", "REFUSED", "REFUSED_FULL", "REFUSED_VIRUS"

  - `result.liablePerson.contactDetails.status.statusInformation` (string)
    More details to the overall status
    Example: "The mail server for the recipient domain does not accept messages to this address."

  - `result.liablePerson.identificationNumber` (string)
    Identification number of liable person
    Example: "ATU143543"

  - `result.liablePerson.addressLine1` (string)
    Address first line
    Example: "Burgring 22"

  - `result.liablePerson.addressLine2` (string)
    Address second line
    Example: "1180 Vienna"

  - `result.liablePerson.addressLine3` (string)
    Address third line
    Example: "Austria"

  - `result.liablePerson.region` (string)
    Region of liable person
    Example: "Vienna"

  - `result.liablePerson.addressData` (object)
    Address details of the liable person

  - `result.liablePerson.addressData.street` (string)
    Street of the client
    Example: "Burgring"

  - `result.liablePerson.addressData.houseNumber` (string)
    House number of the client
    Example: "23A"

  - `result.liablePerson.addressData.addressStatus` (object)
    Describes the status of the address.

  - `result.liablePerson.addressData.addressStatus.type` (string, required)
    Type of address status
    Enum: "VALID", "INVALID"

  - `result.liablePerson.addressData.addressStatus.statusInformation` (string)
    More details on the overall status
    Example: "Letter could not be delivered"

  - `result.liablePerson.addressData.addressStatus.since` (string)
    Current status unchanged since
    Example: "2000-01-01"

  - `result.contactDetails` (array)
    Contact numbers of the debtor

  - `result.collectionCases` (array)
    Collection case of the debtor

  - `result.collectionCases.collectionCaseId` (string, required)
    ID identifying this Collection case in UUID format
    Example: "123e4567-e89b-42d3-a456-556642440000"

  - `result.collectionCases.openAmount` (number, required)
    Total amount open of all debts
    Example: 1231

  - `result.collectionCases.debt` (array, required)
    List of debts the member needs to pay

  - `result.collectionCases.debt.debtId` (string, required)
    Unique Id for this debt in UUID format
    Example: "123e4567-e89b-42d3-a456-556642440000"

  - `result.collectionCases.debt.debtDate` (string, required)
    Due date of the debt
    Example: "1952-05-04"

  - `result.collectionCases.debt.contractStartDate` (string)
    If contract debt, it is set to the start date of the contract, otherwise due date
    Example: "1952-05-04"

  - `result.collectionCases.debt.amount` (number, required)
    Amount to collect for this debt
    Example: 333

  - `result.collectionCases.debt.currency` (string, required)
    ISO 4217 currency code
    Example: "USD"

  - `result.collectionCases.debt.type` (string, required)
    Type of debt collection
    Enum: "PRINCIPAL_CLAIM", "SALE", "DEBT_CLAIM", "FLAT_FEE", "DUNNING_FEE", "BANK_FEE"

  - `result.collectionCases.debt.designation` (string, required)
    Description of debt

  - `result.collectionCases.debt.recurrence` (object, required)
    Describes a recurrence with period and frequency

  - `result.collectionCases.debt.servicePeriodStartDate` (string)
    Start date of the rendered service, YYYY-MM-DD format
    Example: "1952-05-04"

  - `result.collectionCases.debt.servicePeriodEndDate` (string)
    End date of the rendered service, YYYY-MM-DD format
    Example: "1952-05-04"

  - `result.collectionCases.debt.maturityType` (string)
    Defines if a claim was changed due to rest maturity
    Enum: "NORMAL", "RESIDUAL"

  - `result.collectionCases.debt.latestRejectionReason` (string)
    Latest reason on why the payment was not successful
    Enum: "PURCHASE_LIMIT", "INVALID_IBAN", "CLOSED_BANKACCOUNT", "FRAUD", "INSOLVENCY", "DECEASED", "INCOMPLETE_ADDRESS", "INVALID_ADDRESS", "INVALID_OR_MISSING_INFORMATION", "CHARGED_BACK", "ALREADY_PURCHASED", "ALREADY_CHARGED_BACK", "CONTESTED_CONTRACT", "WITHDRAWN_MANDATE", "INVALID_SEPA_MANDATE", "IBAN_BLACKLISTED", "TERMINATED_CONTRACT", "IBAN_NOT_SEPA_DIRECT_DEBIT_CAPABLE", "AMOUNT_EXCEEDS_LIMIT", "NON_CONTRACTUAL", "PURCHASING_SUSPENDED", "INSTRUCTED_BY_STUDIO", "MISSING_LIABLE_PERSON", "IBAN_INVALID_SINCE_LAST_PAYMENT_RUN", "ACCOUNT_CLOSED_BEFORE_COLLECTION", "DEBT_OVERAGED", "DUNNING_UNSUCCESSFUL", "AUTOMATIC_CHARGEBACK", "STUDIO_CLOSED_DOWN", "REPEATED_INVALID_SEPA_MANDATE", "SETTLEMENT_AGREEMENT", "INVALID_SEPA_CREDITOR_ID", "INSUFFICIENT_COVERING", "OPPOSITION", "INVALID_BANK_INFORMATION", "INVALID_MANDATE", "AUTHORIZATION_DECLINED", "INVALID_CARD", "CARD_EXPIRED", "REVOKED_BY_CUSTOMER", "UNSUPPORTED_DEBT_CLAIM_TYPE", "PURCHASESTOP_FRAUD", "ALREADY_REJECTED", "CONSUMPTION_CREDIT_CHARGEBACK_DEBT_CLAIM_TYPE", "MANUALLY_REJECTED", "MANUALLY_SET_PURCHASESTOP", "OTHER", "OTHER_NO_FORWARDING_TO_EXTERNAL_COLLECTION_AGENCY", "UNKNOWN"

  - `result.collectionCases.debt.contractId` (integer)
    The field returns the contract_id from which the debt claim was created. It can be used to fetch the contract details using __GET /v1/customers/contracts/by__. In the case of non-contractual debt claims, this field is empty.

  - `result.collectionCases.debt.block` (object)
    Debt is blocked for collection cases

  - `result.collectionCases.debt.block.limitType` (string, required)
    Option to set customer or debt to blocklist
    Enum: "DISABLED", "LIMITED", "UNLIMITED"

  - `result.collectionCases.debt.block.endDate` (string)
    Block customer or debt until
    Example: "2022-09-20"

  - `result.collectionCases.extHumanId` (string)
    Human identifier given by the debt collection agency

  - `result.collectionCases.extReferenceId` (string)
    Identifier given by the debt collection agency

  - `result.region` (string)
    Region of the debtor
    Example: "Vienna"

  - `result.addressData` (object)
    Describes the address in detail, so every country has its own fields filled. Use addressLines for preformatted address.

  - `result.block` (object)
    Debtor is blocked for collection cases

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

