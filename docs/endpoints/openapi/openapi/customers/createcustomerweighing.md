# Save weighing results

Required Scopes(any of): , 

Saves weighing details for given customer

Endpoint: POST /v1/customers/{customerId}/weighing
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `benefitKey` (string)
    Key of the benefit to use

## Request fields (application/json):

  - `databaseId` (integer)
    Database id of the weighing

  - `basalMetabolicRate` (number)
    Basal metabolic rate

  - `bodyFatMass` (number)
    Body fat mass in kg

  - `bodyMassIndex` (number)
    Body mass index in kg/m^2

  - `fatFreeMass` (number)
    Total fat free mass (aka Lean Body Mass) in kg

  - `percentBodyFat` (number)
    Body fat in percent

  - `percentSkeletalMuscleMass` (number)
    Skeletal muscle mass in percent

  - `skeletalMuscleMass` (number)
    Skeletal muscle mass in kg

  - `totalBodyWater` (number)
    Total body water in liters

  - `visceralFatLevel` (integer)
    Visceral fat level (1-9)

  - `weight` (number)
    Body weight in kg

  - `height` (number)
    Body height in cm

  - `bfmLeftArm` (number)
    Body Fat Mass of the left arm in kg

  - `bfmLeftLeg` (number)
    Body Fat Mass of the left leg in kg

  - `bfmPercentLeftArm` (number)
    Body Fat Mass of the left arm in percent

  - `bfmPercentLeftLeg` (number)
    Body Fat Mass of the left leg in percent

  - `bfmPercentRightArm` (number)
    Body Fat Mass of the right arm in percent

  - `bfmPercentRightLeg` (number)
    Body Fat Mass of the right leg in percent

  - `bfmPercentTrunk` (number)
    Body Fat Mass of the trunk in percent

  - `bfmRightArm` (number)
    Body Fat Mass of the right arm in kg

  - `bfmRightLeg` (number)
    Body Fat Mass of the right leg in kg

  - `bfmTrunk` (number)
    Body Fat Mass of the trunk in kg

  - `ffmLeftArm` (number)
    Fat Free Mass of the left arm in kg

  - `ffmLeftLeg` (number)
    Fat Free Mass of the left leg in kg

  - `ffmPercentLeftArm` (number)
    Fat Free Mass of the left arm in percent

  - `ffmPercentLeftLeg` (number)
    Fat Free Mass of the left leg in percent

  - `ffmPercentRightArm` (number)
    Fat Free Mass of the right arm in percent

  - `ffmPercentRightLeg` (number)
    Fat Free Mass of the right leg in percent

  - `ffmPercentTrunk` (number)
    Fat Free Mass of the trunk in percent

  - `ffmRightArm` (number)
    Fat Free Mass of the right arm in kg

  - `ffmRightLeg` (number)
    Fat Free Mass of the right leg in kg

  - `ffmTrunk` (number)
    Fat Free Mass of the trunk in kg

  - `rawResults` (string, required)
    The raw results. Might be passed back to partner-provided widgets

## Response 200 fields (application/json):

  - `databaseId` (integer)
    Database id of the weighing

  - `basalMetabolicRate` (number)
    Basal metabolic rate

  - `bodyFatMass` (number)
    Body fat mass in kg

  - `bodyMassIndex` (number)
    Body mass index in kg/m^2

  - `fatFreeMass` (number)
    Total fat free mass (aka Lean Body Mass) in kg

  - `percentBodyFat` (number)
    Body fat in percent

  - `percentSkeletalMuscleMass` (number)
    Skeletal muscle mass in percent

  - `skeletalMuscleMass` (number)
    Skeletal muscle mass in kg

  - `totalBodyWater` (number)
    Total body water in liters

  - `visceralFatLevel` (integer)
    Visceral fat level (1-9)

  - `weight` (number)
    Body weight in kg

  - `height` (number)
    Body height in cm

  - `bfmLeftArm` (number)
    Body Fat Mass of the left arm in kg

  - `bfmLeftLeg` (number)
    Body Fat Mass of the left leg in kg

  - `bfmPercentLeftArm` (number)
    Body Fat Mass of the left arm in percent

  - `bfmPercentLeftLeg` (number)
    Body Fat Mass of the left leg in percent

  - `bfmPercentRightArm` (number)
    Body Fat Mass of the right arm in percent

  - `bfmPercentRightLeg` (number)
    Body Fat Mass of the right leg in percent

  - `bfmPercentTrunk` (number)
    Body Fat Mass of the trunk in percent

  - `bfmRightArm` (number)
    Body Fat Mass of the right arm in kg

  - `bfmRightLeg` (number)
    Body Fat Mass of the right leg in kg

  - `bfmTrunk` (number)
    Body Fat Mass of the trunk in kg

  - `ffmLeftArm` (number)
    Fat Free Mass of the left arm in kg

  - `ffmLeftLeg` (number)
    Fat Free Mass of the left leg in kg

  - `ffmPercentLeftArm` (number)
    Fat Free Mass of the left arm in percent

  - `ffmPercentLeftLeg` (number)
    Fat Free Mass of the left leg in percent

  - `ffmPercentRightArm` (number)
    Fat Free Mass of the right arm in percent

  - `ffmPercentRightLeg` (number)
    Fat Free Mass of the right leg in percent

  - `ffmPercentTrunk` (number)
    Fat Free Mass of the trunk in percent

  - `ffmRightArm` (number)
    Fat Free Mass of the right arm in kg

  - `ffmRightLeg` (number)
    Fat Free Mass of the right leg in kg

  - `ffmTrunk` (number)
    Fat Free Mass of the trunk in kg

  - `rawResults` (string, required)
    The raw results. Might be passed back to partner-provided widgets

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

