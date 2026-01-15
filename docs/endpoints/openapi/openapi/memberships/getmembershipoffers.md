# Get all membership offers

Required Scopes: 

Returns all available membership offers.

Endpoint: GET /v1/memberships/membership-offers
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique identifier for the membership offer.

  - `description` (string, required)
    Description of the membership offer.
    Example: "This offer includes access to all gym facilities and group classes."

  - `name` (string, required)
    Name of the membership offer.
    Example: "Standard Membership"

  - `subDescription` (string)
    Sub description for the membership offer.
    Example: "Best value for regular gym-goers."

  - `imageUrl` (string)
    Temporary valid download link for rate bundle image. Expires after 2 hours.
    Example: "https://example.com"

  - `footnote` (string)
    Contractual or legal comments to be displayed below the offer.
    Example: "This offer is valid for new members only. Terms and conditions apply."

  - `preUseType` (string, required)
    Contract pre-use type information.
    Enum: "NOT_AVAILABLE", "CHARGEABLE", "FREE"

  - `limitedOfferingPeriod` (object, required)
    Period in which the membership offer is valid.

  - `limitedOfferingPeriod.startDate` (string, required)
    Start of the interval
    Example: "2025-01-01"

  - `limitedOfferingPeriod.endDate` (string, required)
    End of the interval
    Example: "2026-01-01"

  - `rateCodes` (array, required)
    Rate codes of the membership offer.

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `terms` (array, required)
    List of terms that are part of this membership offer.

  - `terms.id` (integer, required)
    Unique identifier of the membership offer term
    Example: 1234567890

  - `terms.term` (object)
    Represents a term

  - `terms.term.value` (integer, required)
    The value of the term
    Example: 2

  - `terms.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `terms.contractVolumeInformation` (object)
    Contains the total amount to be paid during the initial runtime of the contract and the average amounts per month
 and per the rate's payment frequency (e.g. 1 week)

  - `terms.contractVolumeInformation.totalContractVolume` (object)
    Total contract volume
    Example: 600

  - `terms.contractVolumeInformation.totalContractVolume.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `terms.contractVolumeInformation.totalContractVolume.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `terms.contractVolumeInformation.averagePaymentVolumePerMonth` (object)
    Average payment volume per month
    Example: 50

  - `terms.contractVolumeInformation.averagePaymentVolumePerPaymentFrequencyTerm` (object)
    Average payment volume per payment frequency term
    Example: 50

  - `terms.paymentFrequency` (object, required)
    Represents the payment frequency

  - `terms.paymentFrequency.id` (integer)
    The unique identifier of the payment frequency. ( possible for starter package)
    Example: 1234567890

  - `terms.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `terms.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `terms.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `terms.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `terms.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `terms.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `terms.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `terms.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `terms.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active  the respective term has passed

  - `terms.paymentFrequency.recurring` (boolean)
    Whether the cycle of payments repeats indefinitely. Only relevant if type is  or .

  - `terms.paymentFrequency.ageBasedAdjustments` (array)
    List of age-based adjustments for the membership offer module.

  - `terms.paymentFrequency.ageBasedAdjustments.ageRange` (object, required)
    Represents an age range.

  - `terms.paymentFrequency.ageBasedAdjustments.ageRange.startAge` (integer, required)
    Start age of the range, inclusive.
    Example: 18

  - `terms.paymentFrequency.ageBasedAdjustments.ageRange.endAge` (integer, required)
    End age of the range, inclusive.
    Example: 65

  - `terms.paymentFrequency.ageBasedAdjustments.value` (number, required)
    The value of the adjustment, based on .
    Example: 10

  - `terms.paymentFrequency.ageBasedAdjustments.type` (string, required)
    Age based adjustment type
    Enum: "ABSOLUTE", "PERCENTAGE"

  - `terms.paymentFrequency.formattedPaymentFrequency` (string, required)
    The formatted payment frequency
    Example: "Every 6 months"

  - `terms.extensionTerm` (object)
    Represents a term

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

