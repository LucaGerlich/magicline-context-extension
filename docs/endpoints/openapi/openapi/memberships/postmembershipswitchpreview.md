# Preview the membership switch

Required Scopes: 

Returns information about an impact of a membership switch of a given contract.

Endpoint: POST /v1/memberships/{customerId}/membership-switch/preview
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer to preview the membership switch for

## Query parameters:

  - `studioId` (integer)
    An optional studio ID to retrieve studio-specific offer information for, such as pricing

## Request fields (application/json):

  - `configId` (integer, required)
    Unique ID of the membership switch configuration
    Example: 1234567890

  - `membershipOfferTermId` (integer, required)
    Unique ID of the membership switch offer term
    Example: 1234567890

  - `sourceContractId` (integer, required)
    Unique ID of the contract which is being switched from
    Example: 1234567890

  - `startDate` (string, required)
    The start date of the contract
    Example: "2025-08-24"

  - `notes` (string)
    The notes related to the membership switch
    Example: "Some notes"

  - `thirdPartyId` (string)
    Unique ID of the third party contract in the third party system
    Example: "1000a"

  - `selectedSelectableModuleIds` (array)
    The selected modules from the available selectable modules

  - `selectedOptionalModuleIds` (array)
    The selected modules from the available optional modules

  - `initialPaymentRequestToken` (string)
    This token identifies a pre-authorized payment request. It acts as a reference to the payment session initiated by the user. It's not needed for preview endpoints.
    Example: "3JtyH5sakfn2V22vB0napNC2zWMlpFwS9gPQawuk7Jw1F00atOD0BA"

## Response 200 fields (application/json):

  - `contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month
 and per the rate's payment frequency (e.g. 1 week)

  - `contractVolumeInformation.totalContractVolume` (object)
    Total contract volume
    Example: 600

  - `contractVolumeInformation.totalContractVolume.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `contractVolumeInformation.totalContractVolume.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `contractVolumeInformation.averagePaymentVolumePerMonth` (object)
    Average payment volume per month
    Example: 50

  - `contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (object)
    Average payment volume per payment frequency term
    Example: 50

  - `ageAdjustedPrice` (object)
    The price adjusted for the age of the member, if applicable

  - `moduleConsentTextBlocks` (array)
    List of contract text blocks that are part of this membership switch.

  - `moduleConsentTextBlocks.id` (integer)
    The unique identifier of the text block
    Example: 1234567890

  - `moduleConsentTextBlocks.title` (string)
    The title of the text block
    Example: "Title of 1. text block"

  - `moduleConsentTextBlocks.text` (string)
    The text of the text block
    Example: "Text of 1. text block"

  - `moduleConsentTextBlocks.order` (integer)
    The order of the text block in the contract
    Example: 1

  - `moduleConsentTextBlocks.hasSignature` (boolean)
    Text block configuration has a signature field. You have the option to show a signature input field and it will be added in the contract document. It is not a required field in magicline. It is up to your implementation if you add this field.

  - `moduleConsentTextBlocks.showCommunicationPrivacyOptions` (boolean)
    Text block contains information about the communication privacy options. You are advised to show a matrix with communication settings in combination with this text block.

  - `moduleConsentTextBlocks.attachmentType` (string)
    Indicates the type of attachment for this block
    Enum: "NONE", "FILE", "URL", "CONTRACT_PDF_PREVIEW"

  - `moduleConsentTextBlocks.attachedExternalUrlDto` (object)
    Represents url information.

  - `moduleConsentTextBlocks.attachedExternalUrlDto.title` (string, required)
    Url title
    Example: "Example Resource"

  - `moduleConsentTextBlocks.attachedExternalUrlDto.url` (string, required)
    Url to access the resource
    Example: "https://some-url.com"

  - `moduleConsentTextBlocks.attachedDocument` (object)
    Represents document information.

  - `moduleConsentTextBlocks.attachedDocument.fileName` (string, required)
    Name of the file to download
    Example: "contract.pdf"

  - `moduleConsentTextBlocks.attachedDocument.url` (string, required)
    Temporary valid download link. Expires after 5 hours.
    Example: "https://some-url.com"

  - `moduleConsentTextBlocks.rateBundleModuleId` (integer)
    The ID of the associated rate bundle module. Only set if this is a module consent text block.
    Example: 1234567890

  - `moduleConsentTextBlocks.confirmationRequired` (boolean)

  - `paymentPreview` (object)
    Detailed payment preview including schedule and due-on-signing amount

  - `paymentPreview.paymentSchedule` (array)
    Payment schedule entries in chronological order

  - `paymentPreview.paymentSchedule.dueDate` (string)
    Due date of the payment in ISO-8601 format
    Example: "2025-12-31"

  - `paymentPreview.paymentSchedule.description` (string)
    Description of the charge
    Example: "Contract Basic"

  - `paymentPreview.paymentSchedule.type` (string)
    Type of membership payment
    Enum: "CONTRACT_FEE", "STARTER_PACKAGE", "FLAT_FEE", "MODULE_FEE", "BONUS_PERIOD"

  - `paymentPreview.paymentSchedule.amount` (object)
    Amount of the charge

  - `paymentPreview.paymentSchedule.mandatoryOnSigning` (boolean)
    Indicates if the payment is mandatory on signing
    Example: true

  - `paymentPreview.dueOnSigningAmount` (object)
    Total amount due at contract signing

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

