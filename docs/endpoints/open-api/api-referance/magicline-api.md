# Magicline API

* Appointment, bookable appointment and slots operations
* Redeem checkin vouchers
* Class and slots operations
* Cross studio operations
* Get customers and contracts
* Retrieve customer accounting details
* Retrieve customer communication details
* Get device information
* Employee operations
* Debt collection operations
* Leads operations
* Manage membership contracts
* Membership operations
* Payment operations
* Get studio information
* Get trial offers information

Version: 1.9.0

## Servers

Demo tenant
```
https://open-api-demo.open-api.magicline.com
```

## Security

### ApiKeyAuth

API key received from our team

Type: apiKey
In: header
Name: X-API-KEY

## Download OpenAPI description

[Magicline API](https://redocly.sportalliance.com/_spec/apis/magicline/openapi/openapi.yaml)

## Appointments

Appointment, bookable appointment and slots operations

### Get bookable appointments

 - [GET /v1/appointments/bookable](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getbookableappointments.md): Required Scopes: 

Returns bookable appointments

# Get bookable appointments

Required Scopes: 

Returns bookable appointments

Endpoint: GET /v1/appointments/bookable
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `offset` (string)
    Offset from last request (last ID of the bookable appointment)

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of bookable appointments

  - `result.id` (integer, required)
    Unique ID of the bookable appointment
    Example: 1001

  - `result.title` (string)
    Title of the bookable appointment
    Example: "Mission Beach body"

  - `result.duration` (integer)
    Duration of the bookable appointment in minutes
    Example: 45

  - `result.category` (string)
    Category of the bookable appointment
    Example: "Fitness"

  - `result.description` (string)
    Description of the bookable appointment
    Example: "Get your body ready for beaches"

  - `result.imgUrl` (string)
    Image URL assigned to display this bookable appointment

  - `hasNext` (boolean, required)
    True if there exists next data slice
    Example: true

  - `offset` (string, required)
    Offset for next query (last ID of the bookable appointment)
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


### Get bookable appointment

 - [GET /v1/appointments/bookable/{bookableAppointmentId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getbookableappointment.md): Required Scopes: 

Returns bookable appointment

# Get bookable appointment

Required Scopes: 

Returns bookable appointment

Endpoint: GET /v1/appointments/bookable/{bookableAppointmentId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `bookableAppointmentId` (integer, required)
    Id of the bookable appointment

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the bookable appointment
    Example: 1001

  - `title` (string)
    Title of the bookable appointment
    Example: "Mission Beach body"

  - `duration` (integer)
    Duration of the bookable appointment in minutes
    Example: 45

  - `category` (string)
    Category of the bookable appointment
    Example: "Fitness"

  - `description` (string)
    Description of the bookable appointment
    Example: "Get your body ready for beaches"

  - `imgUrl` (string)
    Image URL assigned to display this bookable appointment

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


### Get bookable appointment slots

 - [GET /v1/appointments/bookable/{bookableAppointmentId}/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getbookableappointmentslots.md): Required Scopes: 

Returns bookable appointment slots

# Get bookable appointment slots

Required Scopes: 

Returns bookable appointment slots

Endpoint: GET /v1/appointments/bookable/{bookableAppointmentId}/slots
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `bookableAppointmentId` (integer, required)
    Id of the bookable appointment

## Query parameters:

  - `customerId` (integer)
    Id of the customer

  - `daysAhead` (integer)
    Days from now on to look ahead

  - `slotWindowStartDate` (string)
    Bookable appointment slots are calculated in the window from slotWindowStartDate to (slotWindowStartDate + daysAhead)

## Response 200 fields (application/json):

  - `startDateTime` (string)
    Start date time of the bookable appointment slot
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `endDateTime` (string)
    End date time of the bookable appointment slot
    Example: "2022-06-22T10:00:00.000+02:00[Europe/Berlin]"

  - `instructors` (array)
    List of instructors

  - `instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

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


### Validate for appointment booking

 - [POST /v1/appointments/bookable/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/validateforappointmentbooking.md): Required Scopes: 

Returns validation result

# Validate for appointment booking

Required Scopes: 

Returns validation result

Endpoint: POST /v1/appointments/bookable/validate
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `customerId` (integer, required)
    Unique ID of the customer
    Example: 203

  - `bookableAppointmentId` (integer, required)
    Unique ID of the bookable appointment
    Example: 20334

  - `startDateTime` (string, required)
    Start date time of the bookable appointment slot
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `endDateTime` (string, required)
    End date time of the bookable appointment slot
    Example: "2022-06-22T10:00:00.000+02:00[Europe/Berlin]"

  - `instructorIds` (array)
    Instructor ID list of the bookable appointment slot

## Response 200 fields (application/json):

  - `validationStatus` (string, required)
    Status of the booking validation
    Enum: "PAST_START_DATE_TIME", "END_DATE_TIME_NOT_AFTER_START_DATE_TIME", "PERIOD_DOES_NOT_MATCH", "CUSTOMER_IN_OTHER_BOOKING", "CUSTOMER_IDLE", "NO_CONTINGENT", "BOOKABLE_APPOINTMENT_RESTRICTIONS_NOT_FULFILLED", "BOOKING_LIMIT_REACHED", "DATE_TIME_BEFORE_EARLIEST_BOOKING_DATE_TIME", "DATE_TIME_AFTER_LATEST_BOOKING_DATE_TIME", "STUDIO_CLOSED", "RESOURCE_NOT_AVAILABLE", "NOT_AVAILABLE", "AVAILABLE"

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


### Book an appointment booking

 - [POST /v1/appointments/booking/book](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/bookappointmentbooking.md): Required Scopes: 

Book an appointment booking for given customer

# Book an appointment booking

Required Scopes: 

Book an appointment booking for given customer

Endpoint: POST /v1/appointments/booking/book
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `customerId` (integer, required)
    Unique ID of the customer
    Example: 203

  - `bookableAppointmentId` (integer, required)
    Unique ID of the bookable appointment
    Example: 20334

  - `startDateTime` (string, required)
    Start date time of the bookable appointment slot
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `endDateTime` (string, required)
    End date time of the bookable appointment slot
    Example: "2022-06-22T10:00:00.000+02:00[Europe/Berlin]"

  - `instructorIds` (array)
    Instructor ID list of the bookable appointment slot

## Response 200 fields (application/json):

  - `bookingId` (integer, required)
    Unique ID of the appointment booking
    Example: 2033

  - `bookingStatus` (string, required)
    Status of the appointment booking
    Enum: "BOOKED", "BOOKED_WITH_CONFIRMATION_REQUIRED", "CANCELED"

  - `startDateTime` (string, required)
    Start date and time of the appointment booking

  - `endDateTime` (string, required)
    End date and time of the appointment booking

  - `title` (string)
    Title of the appointment booking
    Example: "Mission Beach body"

  - `duration` (integer)
    Duration of the appointment booking in minutes
    Example: 45

  - `category` (string)
    Category of the appointment booking
    Example: "Fitness"

  - `description` (string)
    Description of the appointment booking
    Example: "Get your body ready for beaches"

  - `imgUrl` (string)
    Image URL assigned to display this appointment booking

  - `instructors` (array)
    Instructors list of the appointment booking

  - `instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `appointmentStatus` (string, required)
    The status of an appointment
    Enum: "PLANNED", "CANCELED", "COMPLETED"

  - `participantStatus` (string, required)
    The status of a participant
    Enum: "PARTICIPATING", "NOT_PARTICIPATING", "UNSET"

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


### Get an appointment booking

 - [GET /v1/appointments/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getappointmentbooking.md): Required Scopes: 

Get an appointment booking by id

# Get an appointment booking

Required Scopes: 

Get an appointment booking by id

Endpoint: GET /v1/appointments/booking/{bookingId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `bookingId` (integer, required)
    Id of the appointment booking

## Response 200 fields (application/json):

  - `bookingId` (integer, required)
    Unique ID of the appointment booking
    Example: 2033

  - `bookingStatus` (string, required)
    Status of the appointment booking
    Enum: "BOOKED", "BOOKED_WITH_CONFIRMATION_REQUIRED", "CANCELED"

  - `startDateTime` (string, required)
    Start date and time of the appointment booking

  - `endDateTime` (string, required)
    End date and time of the appointment booking

  - `title` (string)
    Title of the appointment booking
    Example: "Mission Beach body"

  - `duration` (integer)
    Duration of the appointment booking in minutes
    Example: 45

  - `category` (string)
    Category of the appointment booking
    Example: "Fitness"

  - `description` (string)
    Description of the appointment booking
    Example: "Get your body ready for beaches"

  - `imgUrl` (string)
    Image URL assigned to display this appointment booking

  - `instructors` (array)
    Instructors list of the appointment booking

  - `instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `appointmentStatus` (string, required)
    The status of an appointment
    Enum: "PLANNED", "CANCELED", "COMPLETED"

  - `participantStatus` (string, required)
    The status of a participant
    Enum: "PARTICIPATING", "NOT_PARTICIPATING", "UNSET"

  - `customerId` (integer, required)
    Unique ID of the customer
    Example: 1234

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


### Delete an appointment booking

 - [DELETE /v1/appointments/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/deleteappointmentbooking.md): Required Scopes: 

Delete an appointment booking by id

# Delete an appointment booking

Required Scopes: 

Delete an appointment booking by id

Endpoint: DELETE /v1/appointments/booking/{bookingId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `bookingId` (integer, required)
    Id of the appointment booking

## Response 200 fields (application/json):

  - `success` (string)

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


### Get appointment bookings for a customer

 - [GET /v1/appointments/booking](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getappointmentbookings.md): Required Scopes: 

Get appointment bookings with a period starting and ending within a timeframe of +/- 2 weeks for a specific customer

# Get appointment bookings for a customer

Required Scopes: 

Get appointment bookings with a period starting and ending within a timeframe of +/- 2 weeks for a specific customer

Endpoint: GET /v1/appointments/booking
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `customerId` (integer, required)
    Id of the customer

## Response 200 fields (application/json):

  - `bookingId` (integer, required)
    Unique ID of the appointment booking
    Example: 2033

  - `bookingStatus` (string, required)
    Status of the appointment booking
    Enum: "BOOKED", "BOOKED_WITH_CONFIRMATION_REQUIRED", "CANCELED"

  - `startDateTime` (string, required)
    Start date and time of the appointment booking

  - `endDateTime` (string, required)
    End date and time of the appointment booking

  - `title` (string)
    Title of the appointment booking
    Example: "Mission Beach body"

  - `duration` (integer)
    Duration of the appointment booking in minutes
    Example: 45

  - `category` (string)
    Category of the appointment booking
    Example: "Fitness"

  - `description` (string)
    Description of the appointment booking
    Example: "Get your body ready for beaches"

  - `imgUrl` (string)
    Image URL assigned to display this appointment booking

  - `instructors` (array)
    Instructors list of the appointment booking

  - `instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `appointmentStatus` (string, required)
    The status of an appointment
    Enum: "PLANNED", "CANCELED", "COMPLETED"

  - `participantStatus` (string, required)
    The status of a participant
    Enum: "PARTICIPATING", "NOT_PARTICIPATING", "UNSET"

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


## Checkin vouchers

Redeem checkin vouchers

### Redeem checkin voucher

 - [POST /v1/checkin-vouchers/redeem](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/checkin-vouchers/redeemcheckinvoucher.md): Required Scopes: 

Redeem checkin voucher

# Redeem checkin voucher

Required Scopes: 

Redeem checkin voucher

Endpoint: POST /v1/checkin-vouchers/redeem
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `voucherCode` (string, required)
    Voucher code to redeem
    Example: "CHVB1-YL29-MYVA"

  - `firstname` (string, required)
    First name of the lead customer
    Example: "Max"

  - `lastname` (string, required)
    Last name of the lead customer
    Example: "Mustermann"

  - `email` (string, required)
    Email of the lead customer
    Example: "example@email.com"

## Response 200 fields (application/json):

  - `studioAccessCode` (string, required)
    Code to checkin to a studio
    Example: "PTKXPMUO"

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


## Classes

Class and slots operations

### Get classes

 - [GET /v1/classes](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getactiveclasses.md): Required Scopes: 

Returns classes with at least one scheduled appointment for the period of one day before to fourteen days ahead

# Get classes

Required Scopes: 

Returns classes with at least one scheduled appointment for the period of one day before to fourteen days ahead

Endpoint: GET /v1/classes
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `offset` (string)
    Offset from last request (last ID of the class)

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of classes

  - `result.id` (integer, required)
    Unique ID of the class
    Example: 1001

  - `result.title` (string)
    Title of the class
    Example: "Mission Beach body"

  - `result.type` (string)
    Defines whether a class is held in the studio or virtually
    Enum: "STUDIO", "STREAM"

  - `result.duration` (integer)
    Duration of the class in minutes
    Example: 45

  - `result.category` (string)
    Category of the class
    Example: "Fitness"

  - `result.description` (string)
    Description of the class
    Example: "Get your body ready for beaches"

  - `result.imgUrl` (string)
    Image URL assigned to display this class

  - `result.bookable` (boolean, required)
    Whether this class can be booked

  - `result.cancelCondition` (object)
    Cancelation condition of a class

  - `result.cancelCondition.cancelationAfterLatestPossible` (boolean)
    Whether cancelation after latest term is possible
    Example: true

  - `result.cancelCondition.latestCancelTerm` (object)
    The latest term before which the class can be canceled

  - `result.cancelCondition.latestCancelTerm.value` (integer, required)
    The value of the term with minutes
    Example: 2

  - `result.cancelCondition.latestCancelTerm.unit` (string, required)
    Represents a temporal unit with minutes
    Enum: "MINUTES", "HOURS", "DAY", "WEEK", "MONTH", "YEAR"

  - `hasNext` (boolean, required)
    True if there exists next data slice
    Example: true

  - `offset` (string, required)
    Offset for next query (last ID of the class)
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


### Get class by id

 - [GET /v1/classes/{classId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassbyid.md): Required Scopes: 

Returns a class for specified id

# Get class by id

Required Scopes: 

Returns a class for specified id

Endpoint: GET /v1/classes/{classId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `classId` (integer, required)
    Id of the class.

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the class
    Example: 1001

  - `title` (string)
    Title of the class
    Example: "Mission Beach body"

  - `type` (string)
    Defines whether a class is held in the studio or virtually
    Enum: "STUDIO", "STREAM"

  - `duration` (integer)
    Duration of the class in minutes
    Example: 45

  - `category` (string)
    Category of the class
    Example: "Fitness"

  - `description` (string)
    Description of the class
    Example: "Get your body ready for beaches"

  - `imgUrl` (string)
    Image URL assigned to display this class

  - `bookable` (boolean, required)
    Whether this class can be booked

  - `cancelCondition` (object)
    Cancelation condition of a class

  - `cancelCondition.cancelationAfterLatestPossible` (boolean)
    Whether cancelation after latest term is possible
    Example: true

  - `cancelCondition.latestCancelTerm` (object)
    The latest term before which the class can be canceled

  - `cancelCondition.latestCancelTerm.value` (integer, required)
    The value of the term with minutes
    Example: 2

  - `cancelCondition.latestCancelTerm.unit` (string, required)
    Represents a temporal unit with minutes
    Enum: "MINUTES", "HOURS", "DAY", "WEEK", "MONTH", "YEAR"

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


### Get classes slots

 - [GET /v1/classes/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassslotsformultipleclasses.md): Required Scopes: 

Returns class slots within the timeframe of daysAhead starting from slotWindowStartDate, for multiple classes

# Get classes slots

Required Scopes: 

Returns class slots within the timeframe of daysAhead starting from slotWindowStartDate, for multiple classes

Endpoint: GET /v1/classes/slots
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `daysAhead` (integer)
    Days from now on to look ahead

  - `slotWindowStartDate` (string)
    Class slots are retrieved within the time window from slotWindowStartDate to (slotWindowStartDate + daysAhead)

  - `offset` (string)
    Offset from last request

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of class slots

  - `result.id` (integer, required)
    Unique ID of a class slot
    Example: 1001

  - `result.startDateTime` (string)
    Class slot start date and time with zone
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `result.endDateTime` (string)
    Class slot end date and time with zone
    Example: "2022-06-22T09:00:00.000+02:00[Europe/Berlin]"

  - `result.classInformation` (object)
    Basic information of a class

  - `result.classInformation.id` (integer, required)
    Unique ID of the class
    Example: 1001

  - `result.classInformation.title` (string)
    Title of the class
    Example: "Mission Beach body"

  - `result.instructors` (array)
    List of instructors

  - `result.instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `result.instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `result.instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `result.instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `result.location` (object)
    Represents location data

  - `result.location.id` (integer, required)
    Unique ID of the location
    Example: 203

  - `result.location.name` (string, required)
    Name of the location
    Example: "Room 1"

  - `result.location.description` (string)
    Description of the location
    Example: "Room located behind reception"

  - `result.earliestBookingDateTime` (string)
    Class slot earliest booking date and time with zone
    Example: "2022-06-15T00:00:00.000+02:00[Europe/Berlin]"

  - `result.latestBookingDateTime` (string)
    Class slot latest booking date and time with zone
    Example: "2022-06-15T23:59:59.999+02:00[Europe/Berlin]"

  - `result.maxParticipants` (integer)
    Maximum participants allowed for a class slot
    Example: 25

  - `result.maxWaitingListParticipants` (integer)
    Maximum number of waiting list participants allowed for a class slot
    Example: 5

  - `result.bookedParticipants` (integer)
    Current number of booked participants of a class slot
    Example: 25

  - `result.additionalParticipants` (integer, required)
    Additional participants added by the operator
    Example: 5

  - `result.waitingListParticipants` (integer)
    Current number of waiting list participants of a class slot
    Example: 2

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


### Get class slots

 - [GET /v1/classes/{classId}/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassslots.md): Required Scopes: 

Returns class slots for specified class id and the period of one day before to fourteen days ahead

# Get class slots

Required Scopes: 

Returns class slots for specified class id and the period of one day before to fourteen days ahead

Endpoint: GET /v1/classes/{classId}/slots
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `classId` (integer, required)
    Id of the class.

## Query parameters:

  - `offset` (string)
    Offset from last request

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of class slots

  - `result.id` (integer, required)
    Unique ID of a class slot
    Example: 1001

  - `result.startDateTime` (string)
    Class slot start date and time with zone
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `result.endDateTime` (string)
    Class slot end date and time with zone
    Example: "2022-06-22T09:00:00.000+02:00[Europe/Berlin]"

  - `result.classInformation` (object)
    Basic information of a class

  - `result.classInformation.id` (integer, required)
    Unique ID of the class
    Example: 1001

  - `result.classInformation.title` (string)
    Title of the class
    Example: "Mission Beach body"

  - `result.instructors` (array)
    List of instructors

  - `result.instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `result.instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `result.instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `result.instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `result.location` (object)
    Represents location data

  - `result.location.id` (integer, required)
    Unique ID of the location
    Example: 203

  - `result.location.name` (string, required)
    Name of the location
    Example: "Room 1"

  - `result.location.description` (string)
    Description of the location
    Example: "Room located behind reception"

  - `result.earliestBookingDateTime` (string)
    Class slot earliest booking date and time with zone
    Example: "2022-06-15T00:00:00.000+02:00[Europe/Berlin]"

  - `result.latestBookingDateTime` (string)
    Class slot latest booking date and time with zone
    Example: "2022-06-15T23:59:59.999+02:00[Europe/Berlin]"

  - `result.maxParticipants` (integer)
    Maximum participants allowed for a class slot
    Example: 25

  - `result.maxWaitingListParticipants` (integer)
    Maximum number of waiting list participants allowed for a class slot
    Example: 5

  - `result.bookedParticipants` (integer)
    Current number of booked participants of a class slot
    Example: 25

  - `result.additionalParticipants` (integer, required)
    Additional participants added by the operator
    Example: 5

  - `result.waitingListParticipants` (integer)
    Current number of waiting list participants of a class slot
    Example: 2

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


### Get class slot by id

 - [GET /v1/classes/{classId}/slots/{classSlotId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassslotbyid.md): Required Scopes: 

Returns class slots for specified class slot id

# Get class slot by id

Required Scopes: 

Returns class slots for specified class slot id

Endpoint: GET /v1/classes/{classId}/slots/{classSlotId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `classId` (integer, required)
    Id of the class.

  - `classSlotId` (integer, required)
    Unique ID of the class slot

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of a class slot
    Example: 1001

  - `startDateTime` (string)
    Class slot start date and time with zone
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

  - `endDateTime` (string)
    Class slot end date and time with zone
    Example: "2022-06-22T09:00:00.000+02:00[Europe/Berlin]"

  - `classInformation` (object)
    Basic information of a class

  - `classInformation.id` (integer, required)
    Unique ID of the class
    Example: 1001

  - `classInformation.title` (string)
    Title of the class
    Example: "Mission Beach body"

  - `instructors` (array)
    List of instructors

  - `instructors.id` (integer, required)
    Unique ID of the instructor
    Example: 101

  - `instructors.firstName` (string, required)
    Instructor's first name
    Example: "Anna"

  - `instructors.lastName` (string, required)
    Instructor's last name
    Example: "Chodakowska"

  - `instructors.publicName` (string)
    Public name that should be shown to customers
    Example: "Peter2000"

  - `location` (object)
    Represents location data

  - `location.id` (integer, required)
    Unique ID of the location
    Example: 203

  - `location.name` (string, required)
    Name of the location
    Example: "Room 1"

  - `location.description` (string)
    Description of the location
    Example: "Room located behind reception"

  - `earliestBookingDateTime` (string)
    Class slot earliest booking date and time with zone
    Example: "2022-06-15T00:00:00.000+02:00[Europe/Berlin]"

  - `latestBookingDateTime` (string)
    Class slot latest booking date and time with zone
    Example: "2022-06-15T23:59:59.999+02:00[Europe/Berlin]"

  - `maxParticipants` (integer)
    Maximum participants allowed for a class slot
    Example: 25

  - `maxWaitingListParticipants` (integer)
    Maximum number of waiting list participants allowed for a class slot
    Example: 5

  - `bookedParticipants` (integer)
    Current number of booked participants of a class slot
    Example: 25

  - `additionalParticipants` (integer, required)
    Additional participants added by the operator
    Example: 5

  - `waitingListParticipants` (integer)
    Current number of waiting list participants of a class slot
    Example: 2

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


### Book a class slot

 - [POST /v1/classes/booking/book](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/bookclassslot.md): Required Scopes: 

Book a class slot for given customer

# Book a class slot

Required Scopes: 

Book a class slot for given customer

Endpoint: POST /v1/classes/booking/book
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `customerId` (integer, required)
    Unique ID of the customer
    Example: 203

  - `classSlotId` (integer, required)
    Unique ID of the class slot
    Example: 20334

## Response 200 fields (application/json):

  - `bookingId` (integer, required)
    Unique ID of a class booking
    Example: 2033

  - `bookingStatus` (string, required)
    Status of the class slot booking
    Enum: "BOOKED", "BOOKED_WITH_CONFIRMATION_REQUIRED", "WAITING_LIST", "CANCELED"

  - `classSlotId` (integer, required)
    Unique ID of a class slot
    Example: 14928

  - `classId` (integer, required)
    Unique ID of a class
    Example: 14928

  - `customerId` (integer, required)
    Unique ID of a customer
    Example: 14925548

  - `classSlotStatus` (string, required)
    The status of a class slot
    Enum: "PLANNED", "CANCELED", "COMPLETED"

  - `participantStatus` (string, required)
    The status of a participant
    Enum: "PARTICIPATING", "NOT_PARTICIPATING", "UNSET"

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


### Validate class slot is bookable

 - [POST /v1/classes/booking/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/validateclassslot.md): Required Scopes: 

Validate class slot is available to book for given customer

# Validate class slot is bookable

Required Scopes: 

Validate class slot is available to book for given customer

Endpoint: POST /v1/classes/booking/validate
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `customerId` (integer, required)
    Unique ID of the customer
    Example: 203

  - `classSlotId` (integer, required)
    Unique ID of the class slot
    Example: 20334

## Response 200 fields (application/json):

  - `validationStatus` (string, required)
    Status of the booking validation
    Enum: "AVAILABLE", "NO_CONTINGENT", "BOOKING_LIMIT_REACHED", "CUSTOMER_ALREADY_BOOKED", "CUSTOMER_IDLE", "CUSTOMER_IN_OTHER_BOOKING", "DISPLAY_ONLY", "DATE_TIME_BEFORE_EARLIEST_BOOKING_DATE_TIME", "DATE_TIME_AFTER_LATEST_BOOKING_DATE_TIME", "STUDIO_CLOSED", "NOT_AVAILABLE"

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


### Get class booking by id

 - [GET /v1/classes/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassbookingbyid.md): Required Scopes: 

Returns class booking for specified booking id

# Get class booking by id

Required Scopes: 

Returns class booking for specified booking id

Endpoint: GET /v1/classes/booking/{bookingId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `bookingId` (integer, required)
    Id of the booking

## Response 200 fields (application/json):

  - `bookingId` (integer, required)
    Unique ID of a class booking
    Example: 2033

  - `bookingStatus` (string, required)
    Status of the class slot booking
    Enum: "BOOKED", "BOOKED_WITH_CONFIRMATION_REQUIRED", "WAITING_LIST", "CANCELED"

  - `classSlotId` (integer, required)
    Unique ID of a class slot
    Example: 14928

  - `classId` (integer, required)
    Unique ID of a class
    Example: 14928

  - `customerId` (integer, required)
    Unique ID of a customer
    Example: 14925548

  - `classSlotStatus` (string, required)
    The status of a class slot
    Enum: "PLANNED", "CANCELED", "COMPLETED"

  - `participantStatus` (string, required)
    The status of a participant
    Enum: "PARTICIPATING", "NOT_PARTICIPATING", "UNSET"

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


### Cancel a class booking

 - [DELETE /v1/classes/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/cancelclassslotbyid.md): Required Scopes: 

Cancel booking of a class slot for given bookingId

# Cancel a class booking

Required Scopes: 

Cancel booking of a class slot for given bookingId

Endpoint: DELETE /v1/classes/booking/{bookingId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `bookingId` (integer, required)
    Unique id of the booking to be cancelled

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


### Get class bookings by customer id

 - [GET /v1/classes/booking](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassbookingsbycustomerid.md): Required Scopes: 

Returns class booking with a period starting and ending within a timeframe of +/- 2 weeks for a specific customer

# Get class bookings by customer id

Required Scopes: 

Returns class booking with a period starting and ending within a timeframe of +/- 2 weeks for a specific customer

Endpoint: GET /v1/classes/booking
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `customerId` (integer, required)
    Id of the customer

## Response 200 fields (application/json):

  - `bookingId` (integer, required)
    Unique ID of a class booking
    Example: 2033

  - `bookingStatus` (string, required)
    Status of the class slot booking
    Enum: "BOOKED", "BOOKED_WITH_CONFIRMATION_REQUIRED", "WAITING_LIST", "CANCELED"

  - `classSlotId` (integer, required)
    Unique ID of a class slot
    Example: 14928

  - `classId` (integer, required)
    Unique ID of a class
    Example: 14928

  - `customerId` (integer, required)
    Unique ID of a customer
    Example: 14925548

  - `classSlotStatus` (string, required)
    The status of a class slot
    Enum: "PLANNED", "CANCELED", "COMPLETED"

  - `participantStatus` (string, required)
    The status of a participant
    Enum: "PARTICIPATING", "NOT_PARTICIPATING", "UNSET"

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


## Cross Studio

Cross studio operations

### Get customer by

 - [GET /v1/cross-studio/customers/by](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getcrossstudiocustomerby.md): Required Scopes: 

Returns customer by one of the given parameters from all studios with activated partner integration

# Get customer by

Required Scopes: 

Returns customer by one of the given parameters from all studios with activated partner integration

Endpoint: GET /v1/cross-studio/customers/by
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumber` (string)
    Card number to identify the customer

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `debtorId` (string)
    Unique ID of the debtor

  - `barcode` (string)
    Barcode to identify the customer

  - `pin` (string)
    PIN to identify the customer

  - `customerNumber` (string)
    Customer number to identify the customer

  - `qrCodeUuid` (string)
    QR code UUID to identify the customer

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


### Get customer by id

 - [GET /v1/cross-studio/customers/{customerId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getcrossstudiocustomerbyid.md): Required Scopes: 

Returns customer by given id from all studios with activated partner integration

# Get customer by id

Required Scopes: 

Returns customer by given id from all studios with activated partner integration

Endpoint: GET /v1/cross-studio/customers/{customerId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

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


### Search customers

 - [POST /v1/cross-studio/customers/search](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/searchcrossstudiocustomers.md): Required Scopes: 

Returns all customers from all studios with activated partner integration by given criteria

# Search customers

Required Scopes: 

Returns all customers from all studios with activated partner integration by given criteria

Endpoint: POST /v1/cross-studio/customers/search
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


### Get customer's checkin history

 - [GET /v1/cross-studio/customers/{customerId}/activities/checkins](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getcrossstudiocustomerscheckinhistory.md): Required Scopes: 

Returns a list of studio checkins of the customer from all studios with activated partner integration for a specific time span (default is one month from today) in expected slices

# Get customer's checkin history

Required Scopes: 

Returns a list of studio checkins of the customer from all studios with activated partner integration for a specific time span (default is one month from today) in expected slices

Endpoint: GET /v1/cross-studio/customers/{customerId}/activities/checkins
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `fromDate` (string)
    The from date of the time span

  - `toDate` (string)
    The to date of the time span, should not be greater than 365 days from the start date.

  - `sliceSize` (integer)
    Desired size of data chunk

  - `offset` (string)
    Offset from last request

## Response 200 fields (application/json):

  - `result` (array, required)
    List of checkins

  - `result.checkinId` (integer, required)
    Unique ID of the studio visit
    Example: 1001

  - `result.checkInDateTime` (string)
    Check in time of the studio visit in ISO-8601 format
    Example: "2023-12-03T10:15:30+01:00"

  - `result.checkOutDateTime` (string)
    Check out time of the studio visit in ISO-8601 format
    Example: "2023-12-03T10:16:30+01:00"

  - `result.studioId` (integer)
    Studio ID of the checkin studio
    Example: 123

  - `result.studioName` (string)
    Studio name of the checkin studio
    Example: "Example studio"

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


### Get studios with active membership offers

 - [GET /v1/cross-studio/membership-offers/studios](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getstudioswithactivemembershipoffers.md): Required Scopes: 

Returns all studios with at least one active membership offer.

# Get studios with active membership offers

Required Scopes: 

Returns all studios with at least one active membership offer.

Endpoint: GET /v1/cross-studio/membership-offers/studios
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `name` (string)
    Studio name
    Example: "Example studio"

  - `description` (string)
    Studio description
    Example: "Example studio description"

  - `country` (string)
    Studio address' country
    Example: "Germany"

  - `countryCode` (string)
    Studio address' country code
    Example: "DE"

  - `studioId` (integer, required)
    Studio Id
    Example: 123

  - `openingDate` (string)
    Studio opening date
    Example: "2025-06-11"

  - `closingDate` (string)
    Studio closing date
    Example: "2029-01-01"

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


## Customers

Get customers and contracts

### Get customers

 - [GET /v1/customers](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomers.md): Required Scopes: 

Returns all customers from studio in expected slices

# Get customers

Required Scopes: 

Returns all customers from studio in expected slices

Endpoint: GET /v1/customers
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `offset` (string)
    Offset from last request (last ID of the customer)

  - `sliceSize` (integer)
    Desired size of data chunk

  - `customerStatus` (string)
    Defines status of returned customers
    Enum: "MEMBER", "PROSPECT"

  - `lastOffsetId` (integer)
    Last ID of customer from last chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of customers

  - `result.id` (integer, required)
    Unique ID of the customer
    Example: 1001

  - `result.customerNumber` (string)
    Customer number
    Example: "1-12345"

  - `result.firstName` (string)
    First name of the customer
    Example: "Edgar"

  - `result.secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `result.lastName` (string)
    Surname of the customer
    Example: "Bullock"

  - `result.secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `result.dateOfBirth` (string)
    Birthday of the customer
    Example: "1952-05-04"

  - `result.email` (string)
    Email address of the customer
    Example: "example@email.com"

  - `result.gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `result.street` (string)
    Street of the customer
    Example: "Am Bahnhof"

  - `result.houseNumber` (string)
    Number of the customer's house
    Example: 89

  - `result.zipCode` (string)
    Zip code of the customer
    Example: "12133"

  - `result.city` (string)
    City of the customer
    Example: "Munich"

  - `result.country` (string)
    Country of the customer
    Example: "DE"

  - `result.secondStreet` (string)
    Second street line of the customer's address
    Example: "Second Street"

  - `result.cityPart` (string)
    City part of the customer's address
    Example: "Tegel"

  - `result.district` (string)
    District of the customer's address
    Example: "District 12"

  - `result.streetType` (string)
    Street type of the customer's address
    Example: "Avenue"

  - `result.streetBlock` (string)
    Street block of the customer's address
    Example: "5th block"

  - `result.portal` (string)
    Portal of the customer's address
    Example: "Portal 1"

  - `result.stairway` (string)
    Stairway of the customer's address
    Example: "Right stairway"

  - `result.door` (string)
    Door of the customer's address
    Example: "Door 1"

  - `result.province` (string)
    Province of the customer's address
    Example: "Champagne"

  - `result.additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `result.floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `result.buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `result.status` (string, required)
    Status of customer
    Enum: "MEMBER", "PROSPECT", "FORMER_MEMBER"

  - `result.imageUrl` (string)
    Url with an image to download. It will expire after 15 minutes
    Example: "https://example.com"

  - `result.phonePrivate` (string)
    Private phone number of the customer
    Example: "+49 30901820"

  - `result.phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+49 15223433333"

  - `result.phoneBusiness` (string)
    Business phone number of the customer
    Example: "+49 30901820"

  - `result.phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+49 15223433333"

  - `result.idlePeriods` (array)
    List of customer's idle periods

  - `result.idlePeriods.id` (integer, required)
    Unique ID of the idle period
    Example: 1000

  - `result.idlePeriods.startDate` (string, required)
    Start date of the idle period
    Example: "2022-01-01"

  - `result.idlePeriods.endDate` (string, required)
    End date of the idle period
    Example: "2022-10-01"

  - `result.idlePeriods.reason` (string)
    Reason of the idle period
    Example: "Illness"

  - `result.idlePeriods.contract` (object)
    Contract information

  - `result.idlePeriods.contract.id` (integer, required)
    Unique ID of the contract
    Example: 1000

  - `result.idlePeriods.contract.rateName` (string, required)
    Rate name for the contract
    Example: "Premium"

  - `result.idlePeriods.unlimited` (boolean, required)
    Indicates whether the idle period is unlimited

  - `result.bankAccount` (object)
    Customer's bank account information

  - `result.bankAccount.accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `result.bankAccount.bankName` (string)
    Bank name of the customers
    Example: "Deutsche Bank"

  - `result.bankAccount.bic` (string)
    Bic of the customers account
    Example: "DEUTDEFFXXX"

  - `result.bankAccount.iban` (string)
    Iban of the customers account
    Example: "DE91 1000 0000 0123 4567 89"

  - `result.accessRefusal` (boolean, required)
    Indicates whether the customer has an access block currently

  - `result.accessRestrictions` (array)
    List of access restrictions of the customer

  - `result.accessRestrictions.reason` (string, required)
    Reason for the restriction
    Example: "Destroyed equipment"

  - `result.accessRestrictions.startDate` (string)
    Start date of the restriction
    Example: "2024-01-01"

  - `result.accessRestrictions.endDate` (string)
    End date of the restriction
    Example: "2024-06-30"

  - `result.uuid` (string)
    Customer's UUID
    Example: "7be3932c-825b-4401-abff-29e9f9410bc7"

  - `result.referralCode` (string)
    Customer's referral code
    Example: "20J6N"

  - `result.studioId` (integer)
    Studio ID of the customer
    Example: 1238735970

  - `result.preferredLanguage` (object)
    Basic language information

  - `result.preferredLanguage.languageCode` (string, required)
    The language code
    Example: "de"

  - `result.preferredLanguage.countryCode` (string)
    The country code
    Example: "DE"

  - `result.additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `result.additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `result.additionalInformationFieldAssignments.value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

  - `result.thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `result.accessMediums` (array)
    List of access mediums of the customer

  - `result.accessMediums.id` (integer)
    Unique identifier for the access medium
    Example: 1234567890

  - `result.accessMediums.type` (string)
    Represents a type of access medium
    Enum: "CARD_NUMBER", "PIN", "BARCODE", "WALLET_PASS"

  - `result.accessMediums.value` (string)
    Unique identifier for the access medium

  - `result.cardNumbers` (array)
    UID list of the customer card numbers in expected format. (The new property to use is accessMediums)
    Example: ["1290158199"]

  - `hasNext` (boolean, required)
    True if there exists next data slice
    Example: true

  - `offset` (string, required)
    Offset for next query (last ID of the customer)
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


### Get customer's checkin history

 - [GET /v1/customers/{customerId}/activities/checkins](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerscheckinhistory.md): Required Scopes: 

Returns a list of studio checkins of the customer for a specific time span (default is one month from today) in expected slices

# Get customer's checkin history

Required Scopes: 

Returns a list of studio checkins of the customer for a specific time span (default is one month from today) in expected slices

Endpoint: GET /v1/customers/{customerId}/activities/checkins
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `fromDate` (string)
    The from date of the time span

  - `toDate` (string)
    The to date of the time span, should not be greater than 365 days from the start date.

  - `sliceSize` (integer)
    Desired size of data chunk

  - `offset` (string)
    Offset from last request

## Response 200 fields (application/json):

  - `result` (array, required)
    List of checkins

  - `result.checkinId` (integer, required)
    Unique ID of the studio visit
    Example: 1001

  - `result.checkInDateTime` (string)
    Check in time of the studio visit in ISO-8601 format
    Example: "2023-12-03T10:15:30+01:00"

  - `result.checkOutDateTime` (string)
    Check out time of the studio visit in ISO-8601 format
    Example: "2023-12-03T10:16:30+01:00"

  - `result.studioId` (integer)
    Studio ID of the checkin studio
    Example: 123

  - `result.studioName` (string)
    Studio name of the checkin studio
    Example: "Example studio"

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


### Get customer by id

 - [GET /v1/customers/{customerId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerbyid.md): Required Scopes: 

Returns customer by given id

# Get customer by id

Required Scopes: 

Returns customer by given id

Endpoint: GET /v1/customers/{customerId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

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


### Get customer by

 - [GET /v1/customers/by](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerby.md): Required Scopes: 

Returns customer by one of the given parameters

# Get customer by

Required Scopes: 

Returns customer by one of the given parameters

Endpoint: GET /v1/customers/by
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumber` (string)
    Card number to identify the customer

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `debtorId` (string)
    Unique ID of the debtor

  - `barcode` (string)
    Barcode to identify the customer

  - `pin` (string)
    PIN to identify the customer

  - `customerNumber` (string)
    Customer number to identify the customer

  - `qrCodeUuid` (string)
    QR code UUID to identify the customer

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


### Search customers

 - [POST /v1/customers/search](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/searchcustomers.md): Required Scopes: 

Returns all customers from studio by given criteria

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


### Get customer's contracts

 - [GET /v1/customers/{customerId}/contracts](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerscontracts.md): Required Scopes(any of): , 

Returns customer's contracts

# Get customer's contracts

Required Scopes(any of): , 

Returns customer's contracts

Endpoint: GET /v1/customers/{customerId}/contracts
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `status` (string)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the contract
    Example: 1000

  - `createdDate` (string, required)
    Creation date of the contract
    Example: "2022-01-01"

  - `startDate` (string, required)
    Start date of the contract
    Example: "2022-01-01"

  - `endDate` (string, required)
    End date of the contract
    Example: "2022-10-01"

  - `rateName` (string, required)
    Rate name for the contract
    Example: "Premium"

  - `rateCodes` (array)
    Rate codes of this contract

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `contractStatus` (string, required)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

  - `cancellationPeriod` (object)
    Represents a time period

  - `cancellationPeriod.periodValue` (integer, required)
    Defines how many units a given period lasts
    Example: 10

  - `cancellationPeriod.periodUnit` (string, required)
    Unit of the period
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `cancelled` (boolean, required)
    Defines whether or not the current active contract has been cancelled

  - `cancellationDate` (string)
    Contract cancellation date
    Example: "2022-10-10"

  - `cancellationReceiptDate` (string)
    Contract cancellation receipt date
    Example: "2022-10-10"

  - `cancellationReason` (string)
    Reason of the contract cancellation
    Example: "Officially ordered studio closure"

  - `priceDetails` (object, required)
    Price details of the contract

  - `priceDetails.basePrice` (object, required)
    Base price of the contract

  - `priceDetails.basePrice.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `priceDetails.basePrice.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `priceDetails.currentPrice` (object, required)
    Current price of the contract. This price takes into account any adjustments that have been made to the base price

  - `priceDetails.paymentFrequency` (object, required)
    Payment frequency of the contract

  - `priceDetails.paymentFrequency.id` (integer)
    Unique ID of the payment frequency of a contract
    Example: 203

  - `priceDetails.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `priceDetails.paymentFrequency.term` (object)
    Represents a term

  - `priceDetails.paymentFrequency.term.value` (integer, required)
    The value of the term
    Example: 2

  - `priceDetails.paymentFrequency.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `priceDetails.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `priceDetails.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `priceDetails.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `priceDetails.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active AFTER the respective term has passed

  - `lastPossibleCancellationDate` (string, required)
    Latest date when the contract can be cancelled

  - `term` (object, required)
    Represents a time period

  - `extensionTerm` (object, required)
    Represents a time period

  - `flatFeeContracts` (array)
    List of flat fee contracts

  - `flatFeeContracts.endDate` (string)
    End date of contract

  - `flatFeeContracts.paymentFrequency` (string, required)
    Type of payment frequency
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `flatFeeContracts.price` (number, required)
    Base price of the contract
    Example: 19.9

  - `moduleContracts` (array)
    List of module contracts

  - `signedDocumentUrl` (string)
    Url to download the contract related document. It will expire after 15 minutes

  - `thirdPartyId` (string)
    Unique ID of the third party contract in the third party system
    Example: "1000a"

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


### Get customer's measurement

 - [GET /v1/customers/measurement/latest](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomermeasurement.md): Required Scopes(any of): , 

Returns customer's latest measurement for specified customer.

# Get customer's measurement

Required Scopes(any of): , 

Returns customer's latest measurement for specified customer.

Endpoint: GET /v1/customers/measurement/latest
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumber` (string)
    Card number to identify the customer

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `barcode` (string)
    Barcode to identify the customer

  - `pin` (string)
    PIN to identify the customer

  - `qrCodeUuid` (string)
    QR code UUID to identify the customer

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the customer
    Example: 1001

  - `firstName` (string)
    First name of the customer
    Example: "Edgar"

  - `lastName` (string)
    Surname of the customer
    Example: "Bullock"

  - `age` (integer)
    Age of the customer
    Example: 16

  - `dateOfBirth` (string)
    Birthday of the customer
    Example: "2000-01-01"

  - `gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `height` (number)
    Height of the customer
    Example: 180.2

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


### Get customer's contracts by

 - [GET /v1/customers/contracts/by](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomercontractsby.md): Required Scopes(any of): , 

Returns customer's contracts by one of the given parameters

# Get customer's contracts by

Required Scopes(any of): , 

Returns customer's contracts by one of the given parameters

Endpoint: GET /v1/customers/contracts/by
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumber` (string)
    Card number to identify the customer

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `debtorId` (string)
    Unique ID of the debtor

  - `barcode` (string)
    Barcode to identify the customer

  - `pin` (string)
    PIN to identify the customer

  - `customerNumber` (string)
    Customer number to identify the customer

  - `status` (string)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

  - `qrCodeUuid` (string)
    QR code UUID to identify the customer

## Response 200 fields (application/json):

  - `id` (integer, required)
    Unique ID of the contract
    Example: 1000

  - `createdDate` (string, required)
    Creation date of the contract
    Example: "2022-01-01"

  - `startDate` (string, required)
    Start date of the contract
    Example: "2022-01-01"

  - `endDate` (string, required)
    End date of the contract
    Example: "2022-10-01"

  - `rateName` (string, required)
    Rate name for the contract
    Example: "Premium"

  - `rateCodes` (array)
    Rate codes of this contract

  - `rateCodes.name` (string)
    The name of the rate code
    Example: "Standard Rate"

  - `rateCodes.identifier` (string)
    Unique identifier for the rate code.
    Example: "RC12345"

  - `contractStatus` (string, required)
    The contracts desired or current status
    Enum: "ACTIVE", "INACTIVE"

  - `cancellationPeriod` (object)
    Represents a time period

  - `cancellationPeriod.periodValue` (integer, required)
    Defines how many units a given period lasts
    Example: 10

  - `cancellationPeriod.periodUnit` (string, required)
    Unit of the period
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `cancelled` (boolean, required)
    Defines whether or not the current active contract has been cancelled

  - `cancellationDate` (string)
    Contract cancellation date
    Example: "2022-10-10"

  - `cancellationReceiptDate` (string)
    Contract cancellation receipt date
    Example: "2022-10-10"

  - `cancellationReason` (string)
    Reason of the contract cancellation
    Example: "Officially ordered studio closure"

  - `priceDetails` (object, required)
    Price details of the contract

  - `priceDetails.basePrice` (object, required)
    Base price of the contract

  - `priceDetails.basePrice.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `priceDetails.basePrice.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `priceDetails.currentPrice` (object, required)
    Current price of the contract. This price takes into account any adjustments that have been made to the base price

  - `priceDetails.paymentFrequency` (object, required)
    Payment frequency of the contract

  - `priceDetails.paymentFrequency.id` (integer)
    Unique ID of the payment frequency of a contract
    Example: 203

  - `priceDetails.paymentFrequency.type` (string, required)
    Payment frequency type of a contract
    Enum: "FREE", "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED"

  - `priceDetails.paymentFrequency.term` (object)
    Represents a term

  - `priceDetails.paymentFrequency.term.value` (integer, required)
    The value of the term
    Example: 2

  - `priceDetails.paymentFrequency.term.unit` (string, required)
    Represents a temporal unit
    Enum: "DAY", "WEEK", "MONTH", "YEAR"

  - `priceDetails.paymentFrequency.price` (object)
    Base price, used only for payment frequencies of type

  - `priceDetails.paymentFrequency.monthDaysToPrices` (array)
    Month day to prices list, used for contract payment frequency type

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay` (object, required)
    The month day of the month day to price mapping

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.month` (string)
    Enum: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.monthValue` (integer)

  - `priceDetails.paymentFrequency.monthDaysToPrices.monthDay.dayOfMonth` (integer)

  - `priceDetails.paymentFrequency.monthDaysToPrices.price` (object, required)
    Represents a financial data

  - `priceDetails.paymentFrequency.termsToPrices` (array)
    Terms to prices list, used for contract payment frequency type . Note that the price will become active AFTER the respective term has passed

  - `lastPossibleCancellationDate` (string, required)
    Latest date when the contract can be cancelled

  - `term` (object, required)
    Represents a time period

  - `extensionTerm` (object, required)
    Represents a time period

  - `flatFeeContracts` (array)
    List of flat fee contracts

  - `flatFeeContracts.endDate` (string)
    End date of contract

  - `flatFeeContracts.paymentFrequency` (string, required)
    Type of payment frequency
    Enum: "NON_RECURRING", "RECURRING", "MONTH_DAY", "TERM_BASED", "FREE"

  - `flatFeeContracts.price` (number, required)
    Base price of the contract
    Example: 19.9

  - `moduleContracts` (array)
    List of module contracts

  - `signedDocumentUrl` (string)
    Url to download the contract related document. It will expire after 15 minutes

  - `thirdPartyId` (string)
    Unique ID of the third party contract in the third party system
    Example: "1000a"

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


### Save weighing results

 - [POST /v1/customers/{customerId}/weighing](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/createcustomerweighing.md): Required Scopes(any of): , 

Saves weighing details for given customer

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


### Get customer's benefits

 - [GET /v1/customers/{customerId}/benefits](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getbenefits.md): Required Scopes(any of): , 

Returns all customer's benefits

# Get customer's benefits

Required Scopes(any of): , 

Returns all customer's benefits

Endpoint: GET /v1/customers/{customerId}/benefits
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `key` (array)
    Benefit keys to validate, when provided, service will check only them
    Example: "FIRST_KEY&key=SECOND_KEY"

## Response 200 fields (application/json):

  - `key` (string, required)
    Benefit key
    Example: "BENEFIT_KEY"

  - `valid` (boolean, required)
    Validation result

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


### Get customer's benefits by card number

 - [GET /v1/customers/benefits](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getbenefitsbycardnumber.md): Required Scopes(any of): , 

Returns customer's benefits by card number

# Get customer's benefits by card number

Required Scopes(any of): , 

Returns customer's benefits by card number

Endpoint: GET /v1/customers/benefits
Version: 1.9.0
Security: ApiKeyAuth

## Query parameters:

  - `cardNumber` (string, required)
    Card number to identify the customer

  - `cardNumberFormat` (string)
    Defines how card numbers are interpreted
    Enum: "DECIMAL", "HEX_MSB", "HEX_LSB"

  - `key` (array)
    Benefit keys to validate, when provided, service will check only them
    Example: "FIRST_KEY&key=SECOND_KEY"

## Response 200 fields (application/json):

  - `key` (string, required)
    Benefit key
    Example: "BENEFIT_KEY"

  - `valid` (boolean, required)
    Validation result

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


### Post customer's benefit usage

 - [POST /v1/customers/{customerId}/benefits/{benefitKey}/use](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/usebenefit.md): Required Scopes(any of): , 

Returns the used benefit

# Post customer's benefit usage

Required Scopes(any of): , 

Endpoint: POST /v1/customers/{customerId}/benefits/{benefitKey}/use
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

  - `benefitKey` (string, required)
    Key of the benefit to use

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


### Get customer's access code

 - [GET /v1/customers/{customerId}/access-code](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomeraccesscode.md): Required Scopes: 

Returns customer's access code

# Get customer's access code

Required Scopes: 

Returns customer's access code

Endpoint: GET /v1/customers/{customerId}/access-code
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `format` (string, required)
    Represents an access code format the content should be encoded into or decoded from
    Enum: "QR_CODE"

  - `expiresAt` (string)
    Access code expiry date and time with zone
    Example: "2024-06-13T10:33:00Z"

  - `content` (string, required)
    Access code content that should be rendered in a format defined by the format property
    Example: "0049267681211943991"

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


### Add a new access medium to a customer

 - [POST /v1/customers/{customerId}/access-mediums](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/addaccessmediums.md): Required Scopes: 

Returns the newly added access medium

# Add a new access medium to a customer

Required Scopes: 

Returns the newly added access medium

Endpoint: POST /v1/customers/{customerId}/access-mediums
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `id` (integer)
    Unique identifier for the access medium
    Example: 1234567890

  - `type` (string)
    Represents a type of access medium
    Enum: "CARD_NUMBER", "PIN", "BARCODE", "WALLET_PASS"

  - `value` (string)
    Unique identifier for the access medium

## Response 200 fields (application/json):

  - `id` (integer)
    Unique identifier for the access medium
    Example: 1234567890

  - `type` (string)
    Represents a type of access medium
    Enum: "CARD_NUMBER", "PIN", "BARCODE", "WALLET_PASS"

  - `value` (string)
    Unique identifier for the access medium

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


### Update customer's access medium

 - [PUT /v1/customers/{customerId}/access-mediums/{accessMediumId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/updateaccessmediums.md): Required Scopes: 

Updates the customer's access medium. Only previously created mediums may be updated.

# Update customer's access medium

Required Scopes: 

Updates the customer's access medium. Only previously created mediums may be updated.

Endpoint: PUT /v1/customers/{customerId}/access-mediums/{accessMediumId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

  - `accessMediumId` (integer, required)
    Unique ID of the access medium

## Request fields (application/json):

  - `value` (string)
    Unique identifier for the access medium

## Response 200 fields (application/json):

  - `id` (integer)
    Unique identifier for the access medium
    Example: 1234567890

  - `type` (string)
    Represents a type of access medium
    Enum: "CARD_NUMBER", "PIN", "BARCODE", "WALLET_PASS"

  - `value` (string)
    Unique identifier for the access medium

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


### Delete customer's access medium

 - [DELETE /v1/customers/{customerId}/access-mediums/{accessMediumId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/deleteaccessmediums.md): Required Scopes: 

Deletes the customer's access medium. Only previously created mediums may be deleted.

# Delete customer's access medium

Required Scopes: 

Deletes the customer's access medium. Only previously created mediums may be deleted.

Endpoint: DELETE /v1/customers/{customerId}/access-mediums/{accessMediumId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

  - `accessMediumId` (integer, required)
    Unique ID of the access medium

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


### Returns all documents for a customer

 - [GET /v1/customers/{customerId}/documents](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getdocuments.md): Required Scopes: 

Returns all documents for a customer

# Returns all documents for a customer

Required Scopes: 

Returns all documents for a customer

Endpoint: GET /v1/customers/{customerId}/documents
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `offset` (string)
    Offset from last request

  - `sliceSize` (integer)
    Desired size of data chunk

## Response 200 fields (application/json):

  - `result` (array, required)
    List of items

  - `result.url` (string)
    URL to download document valid for 15 minutes

  - `result.id` (integer)
    Unique ID of the document
    Example: 1241246660

  - `result.fileName` (string)
    Name of the document

  - `result.description` (string)
    Description of the document

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


### Upload new document to a customer

 - [POST /v1/customers/{customerId}/documents](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/uploaddocument.md): Required Scopes: 

Returns the newly uploaded document information

# Upload new document to a customer

Required Scopes: 

Returns the newly uploaded document information

Endpoint: POST /v1/customers/{customerId}/documents
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `description` (string)
    Document description
    Example: "Member contract"

## Request fields (multipart/form-data):

  - `file` (string, required)
    Upload file with correct extension.

## Response 200 fields (application/json):

  - `id` (integer)
    Unique ID of the document
    Example: 1241246660

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


### Returns document for a customer

 - [GET /v1/customers/{customerId}/documents/{id}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getdocumentbyid.md): Required Scopes: 

Returns document for a customer

# Returns document for a customer

Required Scopes: 

Returns document for a customer

Endpoint: GET /v1/customers/{customerId}/documents/{id}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

  - `id` (integer, required)
    Unique ID of the document

## Response 200 fields (application/json):

  - `url` (string)
    URL to download document valid for 15 minutes

  - `id` (integer)
    Unique ID of the document
    Example: 1241246660

  - `fileName` (string)
    Name of the document

  - `description` (string)
    Description of the document

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


### Update customer profile image

 - [PUT /v1/customers/{customerId}/images](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/updateimage.md): Required Scopes: 

Updates customer profile image. The image will be rescaled(1200x1200) and converted to mime type .

# Update customer profile image

Required Scopes: 

Updates customer profile image. The image will be rescaled(1200x1200) and converted to mime type .

Endpoint: PUT /v1/customers/{customerId}/images
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (multipart/form-data):

  - `image` (string, required)
    Upload image with correct extension. Supported mime types:

## Response 200 fields (application/json):

  - `imageUrl` (string)
    Url with an image to download. It will expire after 15 minutes
    Example: "https://example.com"

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


### Set customer's access restriction

 - [PUT /v1/customers/{customerId}/access-restrictions](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/setaccessrestriction.md): Required Scopes: 

Creates or updates access restriction for the customer.
If the customer already has an access restriction, it will be updated with the provided data. Only previously created restrictions may be updated.
If no such restriction exists, it will be created. It is necessary to provide either both  and  or neither of them.

# Set customer's access restriction

Required Scopes: 

Creates or updates access restriction for the customer.
If the customer already has an access restriction, it will be updated with the provided data. Only previously created restrictions may be updated.
If no such restriction exists, it will be created. It is necessary to provide either both  and  or neither of them.


Endpoint: PUT /v1/customers/{customerId}/access-restrictions
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)

## Request fields (application/json):

  - `reason` (string, required)
    Reason for the restriction
    Example: "Destroyed equipment"

  - `startDate` (string)
    Start date of the restriction
    Example: "2024-01-01"

  - `endDate` (string)
    End date of the restriction
    Example: "2024-06-30"

## Response 200 fields (application/json):

  - `reason` (string, required)
    Reason for the restriction
    Example: "Destroyed equipment"

  - `startDate` (string)
    Start date of the restriction
    Example: "2024-01-01"

  - `endDate` (string)
    End date of the restriction
    Example: "2024-06-30"

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


### Delete customer's access restriction

 - [DELETE /v1/customers/{customerId}/access-restrictions](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/deleteaccessrestriction.md): Required Scopes: 

Deletes the customer's access restriction. Only previously created restrictions may be deleted.

# Delete customer's access restriction

Required Scopes: 

Deletes the customer's access restriction. Only previously created restrictions may be deleted.

Endpoint: DELETE /v1/customers/{customerId}/access-restrictions
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)

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


### Create customer

 - [POST /v1/customers/create](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/createcustomer.md): Required Scopes: 

Creates a new customer (prospect) with comprehensive data to allow for future conversion to a full member

# Create customer

Required Scopes: 

Creates a new customer (prospect) with comprehensive data to allow for future conversion to a full member

Endpoint: POST /v1/customers/create
Version: 1.9.0
Security: ApiKeyAuth

## Request fields (application/json):

  - `thirdPartyId` (string)
    Unique ID of the third party customer in the third party system
    Example: "A1000"

  - `firstName` (string, required)
    First name of the customer
    Example: "Peter"

  - `secondFirstName` (string)
    Second first name of the customer
    Example: "Thomas"

  - `lastName` (string, required)
    Last name of the customer
    Example: "Muller"

  - `secondLastName` (string)
    Second last name of the customer
    Example: "Meyer"

  - `dateOfBirth` (string, required)
    Date of birth of the customer
    Example: "2019-08-24"

  - `placeOfBirth` (string)
    Place of birth of the customer. Required for Italian studios and nationals.

  - `countryOfBirth` (string)
    Country of birth of the customer. Required for Italian studios and non-Italian nationals

  - `email` (string, required)
    Email address of the customer
    Example: "example@example.com"

  - `gender` (string)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `phoneNumberPrivate` (string)
    Private phone number of the customer
    Example: "+44123456789"

  - `phoneNumberMobile` (string)
    Mobile phone number of the customer
    Example: "+44987654321"

  - `street` (string, required)
    Street of the customer's address
    Example: "Raboisen Street"

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

  - `language` (object, required)
    Language of the customer

  - `language.languageCode` (string, required)
    The language code
    Example: "de"

  - `language.countryCode` (string)
    The country code
    Example: "DE"

  - `houseNumber` (string)
    House number of the customer's address
    Example: "3-4"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `city` (string, required)
    City of the customer's address
    Example: "Hamburg"

  - `zipCode` (string, required)
    Zip code of the customer's address
    Example: "220-99"

  - `countryCode` (string, required)
    Country code of the customer's address
    Example: "DE"

  - `taxId` (string)
    Required if the studio is located in Spain or Italy. Alternatively, a valid document identification can be provided.
    Example: "12345678A"

  - `communicationPreferences` (array)
    List of communication preferences for the customer

  - `communicationPreferences.messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `communicationPreferences.channels` (array)
    The communication channels related to the message category of the communication preference

  - `communicationPreferences.channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `communicationPreferences.channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `communicationPreferences.channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

  - `documentIdentification` (object)
    Information from an official document that identifies the customer

  - `documentIdentification.documentNumber` (string, required)
    Document number
    Example: "CX5432112345DS"

  - `documentIdentification.documentType` (string, required)
    Type of the document
    Enum: "ID_CARD", "PASSPORT", "DRIVERS_LICENCE", "RESIDENCE_PERMIT", "NATIONAL_ID_NUMBER", "OTHERS"

  - `paymentRequestToken` (string)
    By assigning the  to the customer, the payment method associated with the token will be used as payment method setting of the customer. Additionally, if the  is associated with a payment instrument, i.e. a SEPA Mandate, BACS Mandate, Credit Card, or other, the payment instrument will be made available in the member account for future collection via payment runs. By leaving this field empty the payment method of the customer will be set to . For reference check 'Create a user payment session'.

  - `additionalInformationFieldAssignments` (array)
    List of additional information field assignments of the customer

  - `additionalInformationFieldAssignments.additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `additionalInformationFieldAssignments.value` (string, required)
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


### Get additional information fields

 - [GET /v1/customers/additional-information-fields](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getadditionalinformationfields.md): Required Scopes: 

Returns additional information fields available for assignment to customers. 

# Get additional information fields

Required Scopes: 

Returns additional information fields available for assignment to customers. 

Endpoint: GET /v1/customers/additional-information-fields
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `id` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `name` (string, required)
    The name of the additional information field
    Example: "Membership Type"

  - `type` (string, required)
    The type of an additional information field. This defines how the field is used and what kind of data it can hold.
    Enum: "BOOLEAN", "DATE", "LIST", "NUMERIC", "TEXT"

  - `abbreviation` (string)
    The abbreviation of the additional information field
    Example: "MT"

  - `listItems` (array)
    A list of list items. This is only used if the field type is a list.

  - `listItems.id` (integer, required)
    The unique ID of the additional information list item
    Example: 12345

  - `listItems.name` (string, required)
    The name of the additional information list item
    Example: "First Option"

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


### Sets additional information field assignments

 - [PUT /v1/customers/{customerId}/additional-information-field-assignments](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/setadditionalinformationfieldassignments.md): Required Scopes: 

Sets additional information field assignments for a customer. We overwrite existing values, so you need to provide all field assignments that you want to set. If you want to remove a field assignment, don't add it.

# Sets additional information field assignments

Required Scopes: 

Sets additional information field assignments for a customer. We overwrite existing values, so you need to provide all field assignments that you want to set. If you want to remove a field assignment, don't add it.

Endpoint: PUT /v1/customers/{customerId}/additional-information-field-assignments
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

## Response 200 fields (application/json):

  - `additionalInformationFieldId` (integer, required)
    The unique ID of the additional information field
    Example: 1234567890

  - `value` (string, required)
    The value of the additional information field assignment. For list fields this is the id of the selected item, for text fields this is the text value, for numeric fields must be positive or negative integers, for date fields this is the date in ISO-8601 format, and for boolean fields this is 'true' or 'false'.

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


### Switch studio

 - [POST /v1/customers/{customerId}/switch-studio](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/switchstudio.md): Required Scopes: 

Switches the studio of the given customer to the specified target studio. The API key of the customer's source studio must be used for this request.

# Switch studio

Required Scopes: 

Switches the studio of the given customer to the specified target studio. The API key of the customer's source studio must be used for this request.

Endpoint: POST /v1/customers/{customerId}/switch-studio
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)

## Request fields (application/json):

  - `targetStudioId` (integer, required)
    The ID of the studio to be switched to
    Example: 123456789

  - `switchDate` (string, required)
    Date of the switch. The date must be the current date or in the past
    Example: "2024-01-01"

  - `description` (string)
    A description of the studio switch that will be stored in the customer history

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


### Add a new access medium to a customer (deprecated)

 - [PUT /v1/customers/{customerId}/access-medium](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/addaccessmedium.md): Required Scopes: 

Returns the newly added access medium

## Customers Account

Retrieve customer accounting details

### Get customer's account balance data

 - [GET /v1/customers/{customerId}/account/balances](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-account/getcustomersaccountbalancedata.md): Required Scopes: 

Returns customer's current account balance data

# Get customer's account balance data

Required Scopes: 

Returns customer's current account balance data

Endpoint: GET /v1/customers/{customerId}/account/balances
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `accountBalance` (object)
    Represents a financial data

  - `accountBalance.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `accountBalance.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `consumptionCredit` (object)
    Represents a financial data

  - `dunningLevel` (string)
    The dunning level of the customer
    Example: "Dunning Level 1"

  - `inDebtCollection` (boolean, required)
    Whether the customers open debt claims where transferred to a debt collection agency

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


### Get customer's account past transactions in slices

 - [GET /v1/customers/{customerId}/account/transactions](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-account/getcustomersaccounttransactiondata.md): Required Scopes: 

Returns customer's account transaction data for the past excluding today

# Get customer's account past transactions in slices

Required Scopes: 

Returns customer's account transaction data for the past excluding today

Endpoint: GET /v1/customers/{customerId}/account/transactions
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `sliceSize` (integer)
    Desired size of data chunk

  - `offset` (string)
    Offset from last request

## Response 200 fields (application/json):

  - `result` (array, required)
    List of booking entries

  - `result.id` (integer, required)
    The internal id of the entry

  - `result.dueDate` (string, required)
    Date to booking is/was to be paid

  - `result.description` (string)
    Description of the booking

  - `result.amount` (object)
    Represents a financial data

  - `result.amount.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `result.amount.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `result.openAmount` (object)
    Represents a financial data

  - `result.installmentPlan` (boolean, required)
    Whether or not the booking was transferred into an installment plan

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


### Get customer's account upcoming transactions in slices within the next year

 - [GET /v1/customers/{customerId}/account/transactions/upcoming](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-account/getcustomersaccountupcomingdata.md): Required Scopes: 

Returns customer's account upcoming transaction data including today

# Get customer's account upcoming transactions in slices within the next year

Required Scopes: 

Returns customer's account upcoming transaction data including today

Endpoint: GET /v1/customers/{customerId}/account/transactions/upcoming
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Query parameters:

  - `sliceSize` (integer)
    Desired size of data chunk

  - `offset` (string)
    Offset from last request

## Response 200 fields (application/json):

  - `result` (array, required)
    List of booking entries

  - `result.id` (integer, required)
    The internal id of the entry

  - `result.dueDate` (string, required)
    Date to booking is/was to be paid

  - `result.description` (string)
    Description of the booking

  - `result.amount` (object)
    Represents a financial data

  - `result.amount.amount` (number, required)
    Amount of the finance data tuple
    Example: 20

  - `result.amount.currency` (string, required)
    Currency of the finance data tuple
    Example: "EUR"

  - `result.openAmount` (object)
    Represents a financial data

  - `result.installmentPlan` (boolean, required)
    Whether or not the booking was transferred into an installment plan

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


## Customers Communication

Retrieve customer communication details

### Create communication thread

 - [POST /v1/communications/{customerId}/threads](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/createcommunicationinnewcommunicationthread.md): Required Scopes: 

Creates new thread with a new communication for a customer

# Create communication thread

Required Scopes: 

Creates new thread with a new communication for a customer

Endpoint: POST /v1/communications/{customerId}/threads
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer

## Request fields (application/json):

  - `communicationThreadStatus` (string, required)
    The status of a communication thread
    Enum: "CREATED", "ONGOING", "CLOSED"

  - `ticketNumber` (string)
    The ticket number of the third party ticketing system
    Example: "A123456"

  - `subject` (string, required)
    The subject of the communication
    Example: "Complaint"

  - `content` (string, required)
    The content of the communication
    Example: "I received two invoices this month, but I only made one purchase."

  - `communicationDirection` (string, required)
    The direction of the communication
    Enum: "INCOMING", "OUTGOING"

  - `ticketLink` (string)
    The link to the ticket in the third party ticketing system
    Example: "https://ticketing-system.com/ticket/A123456"

  - `communicationChannel` (string, required)
    The channel of the communication
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `agent` (string)
    The employee/agent handling the communication
    Example: "Peter Meyer"

  - `communicationDateTime` (string)
    When this field is not null it will be used as the date time of the communication instead of the current time
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

## Response 200 fields (application/json):

  - `customerId` (integer, required)
    The customer's ID
    Example: 1

  - `communicationId` (integer, required)
    The ID of the communication
    Example: 1

  - `threadId` (integer, required)
    The ID of the communication thread
    Example: 1

  - `communicationThreadStatus` (string, required)
    The status of a communication thread
    Enum: "CREATED", "ONGOING", "CLOSED"

  - `ticketNumber` (string)
    The ticket number of the third party ticketing system
    Example: "A123456"

  - `subject` (string, required)
    The subject of the communication
    Example: "Complaint"

  - `content` (string, required)
    The content of the communication
    Example: "I received two invoices this month, but I only made one purchase."

  - `communicationDirection` (string, required)
    The direction of the communication
    Enum: "INCOMING", "OUTGOING"

  - `ticketLink` (string)
    The link to the ticket in the third party ticketing system
    Example: "https://ticketing-system.com/ticket/A123456"

  - `communicationChannel` (string, required)
    The channel of the communication
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `agent` (string)
    The employee/agent handling the communication
    Example: "Peter Meyer"

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


### Update communication thread

 - [PUT /v1/communications/{customerId}/threads/{threadId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/createcommunicationinexistingcommunicationthread.md): Required Scopes: 

Adds new communication for a customer to an existing communication thread and updates the thread

# Update communication thread

Required Scopes: 

Adds new communication for a customer to an existing communication thread and updates the thread

Endpoint: PUT /v1/communications/{customerId}/threads/{threadId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer

  - `threadId` (integer, required)
    The ID of the communication thread

## Request fields (application/json):

  - `communicationThreadStatus` (string, required)
    The status of a communication thread
    Enum: "CREATED", "ONGOING", "CLOSED"

  - `ticketNumber` (string)
    The ticket number of the third party ticketing system
    Example: "A123456"

  - `subject` (string, required)
    The subject of the communication
    Example: "Complaint"

  - `content` (string, required)
    The content of the communication
    Example: "I received two invoices this month, but I only made one purchase."

  - `communicationDirection` (string, required)
    The direction of the communication
    Enum: "INCOMING", "OUTGOING"

  - `ticketLink` (string)
    The link to the ticket in the third party ticketing system
    Example: "https://ticketing-system.com/ticket/A123456"

  - `communicationChannel` (string, required)
    The channel of the communication
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `agent` (string)
    The employee/agent handling the communication
    Example: "Peter Meyer"

  - `communicationDateTime` (string)
    When this field is not null it will be used as the date time of the communication instead of the current time
    Example: "2022-06-22T08:00:00.000+02:00[Europe/Berlin]"

## Response 200 fields (application/json):

  - `customerId` (integer, required)
    The customer's ID
    Example: 1

  - `communicationId` (integer, required)
    The ID of the communication
    Example: 1

  - `threadId` (integer, required)
    The ID of the communication thread
    Example: 1

  - `communicationThreadStatus` (string, required)
    The status of a communication thread
    Enum: "CREATED", "ONGOING", "CLOSED"

  - `ticketNumber` (string)
    The ticket number of the third party ticketing system
    Example: "A123456"

  - `subject` (string, required)
    The subject of the communication
    Example: "Complaint"

  - `content` (string, required)
    The content of the communication
    Example: "I received two invoices this month, but I only made one purchase."

  - `communicationDirection` (string, required)
    The direction of the communication
    Enum: "INCOMING", "OUTGOING"

  - `ticketLink` (string)
    The link to the ticket in the third party ticketing system
    Example: "https://ticketing-system.com/ticket/A123456"

  - `communicationChannel` (string, required)
    The channel of the communication
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `agent` (string)
    The employee/agent handling the communication
    Example: "Peter Meyer"

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


### Get communication preferences

 - [GET /v1/communications/{customerId}/communication-preferences](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/getcommunicationpreferences.md): Required Scopes: 

Get communication preferences for a customer

# Get communication preferences

Required Scopes: 

Get communication preferences for a customer

Endpoint: GET /v1/communications/{customerId}/communication-preferences
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer

## Response 200 fields (application/json):

  - `messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `channels` (array)
    The communication channels related to the message category of the communication preference

  - `channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

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


### Update communication preferences

 - [PUT /v1/communications/{customerId}/communication-preferences](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/updatecommunicationpreferences.md): Required Scopes: 

Update communication preferences for a customer

# Update communication preferences

Required Scopes: 

Update communication preferences for a customer

Endpoint: PUT /v1/communications/{customerId}/communication-preferences
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    The ID of the customer

## Request fields (application/json):

  - `messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `channels` (array)
    The communication channels related to the message category of the communication preference

  - `channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

## Response 200 fields (application/json):

  - `messageCategory` (string)
    The message category of the communication preference
    Enum: "CONTRACT", "GENERAL", "APPOINTMENT", "NEWSLETTER", "LOYALTY_PROGRAM"

  - `channels` (array)
    The communication channels related to the message category of the communication preference

  - `channels.communicationChannel` (string, required)
    The communication channel
    Enum: "LETTER", "EMAIL", "TEXT_MESSAGE", "PHONE", "FAX", "CONVERSATION", "CHAT", "OTHER"

  - `channels.customerOverridable` (boolean)
    Indicates if the customer can override the communication channel
    Example: true

  - `channels.active` (boolean)
    Indicates if the communication channel is active
    Example: true

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


## Customers Self-service

### Get customer's contact data

 - [GET /v1/customers/{customerId}/self-service/contact-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomercontactdata.md): Required Scopes: 

Returns customer current contact data along with requested change of this data

# Get customer's contact data

Required Scopes: 

Returns customer current contact data along with requested change of this data

Endpoint: GET /v1/customers/{customerId}/self-service/contact-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `email` (string)
    Email address of the customer
    Example: "email@example.com"

  - `phonePrivate` (string)
    Private phone number of the customer
    Example: "+49 00000000"

  - `phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+49 00000000000"

  - `phoneBusiness` (string)
    Business phone number of the customer
    Example: "+49 00000000"

  - `phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+49 00000000000"

  - `amendmentConfigurationStatus` (string, required)
    Status of the amendment configuration.
    Enum: "READ", "CHANGES_REQUIRE_VERIFICATION", "CHANGES_WITHOUT_VERIFICATION"

  - `pendingAmendment` (object)
    Pending amendment

  - `pendingAmendment.id` (integer)
    Amendment proposal id

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


### Create contact data amendment

 - [POST /v1/customers/{customerId}/self-service/contact-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomercontactdataamendment.md): Required Scopes: 

Creates request for contact data amendment for specified customerId

# Create contact data amendment

Required Scopes: 

Creates request for contact data amendment for specified customerId

Endpoint: POST /v1/customers/{customerId}/self-service/contact-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `email` (string)
    Email address of the customer
    Example: "email@example.com"

  - `phonePrivate` (string)
    Private phone number of the customer
    Example: "+49 00000000"

  - `phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+49 00000000000"

  - `phoneBusiness` (string)
    Business phone number of the customer
    Example: "+49 00000000"

  - `phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+49 00000000000"

## Response 200 fields (application/json):

  - `id` (integer)
    Amendment proposal id

  - `email` (string)
    Email address of the customer
    Example: "email@example.com"

  - `phonePrivate` (string)
    Private phone number of the customer
    Example: "+49 00000000"

  - `phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+49 00000000000"

  - `phoneBusiness` (string)
    Business phone number of the customer
    Example: "+49 00000000"

  - `phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+49 00000000000"

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


### Get customer's address data

 - [GET /v1/customers/{customerId}/self-service/address-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomeraddressdata.md): Required Scopes: 

Returns customer current address data along with requested change of this data

# Get customer's address data

Required Scopes: 

Returns customer current address data along with requested change of this data

Endpoint: GET /v1/customers/{customerId}/self-service/address-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `street` (string, required)
    Street of the customer
    Example: "Am Bahnhof"

  - `houseNumber` (string)
    Number of the customer's house
    Example: "90"

  - `zipCode` (string, required)
    Zip code of the customer
    Example: "12133"

  - `city` (string, required)
    City of the customer
    Example: "Munich"

  - `countryCode` (string, required)
    Country of the customer
    Example: "DE"

  - `province` (string)
    Province for southern Europe/US countries
    Example: "Madrid/California"

  - `provinceCode` (string)
    Province code for southern Europe/US countries
    Example: "MD/CA"

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

  - `additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

  - `amendmentConfigurationStatus` (string, required)
    Status of the amendment configuration.
    Enum: "READ", "CHANGES_REQUIRE_VERIFICATION", "CHANGES_WITHOUT_VERIFICATION"

  - `pendingAmendment` (object)
    Pending amendment

  - `pendingAmendment.id` (integer)
    Amendment proposal id

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


### Create address data amendment

 - [POST /v1/customers/{customerId}/self-service/address-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomeraddressdataamendment.md): Required Scopes: 

Creates request for address data amendment for specified customerId

# Create address data amendment

Required Scopes: 

Creates request for address data amendment for specified customerId

Endpoint: POST /v1/customers/{customerId}/self-service/address-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `street` (string, required)
    Street of the customer
    Example: "Am Bahnhof"

  - `houseNumber` (string)
    Number of the customer's house
    Example: "90"

  - `zipCode` (string, required)
    Zip code of the customer
    Example: "12133"

  - `city` (string, required)
    City of the customer
    Example: "Munich"

  - `countryCode` (string, required)
    Country of the customer
    Example: "DE"

  - `province` (string)
    Province for southern Europe/US countries
    Example: "Madrid/California"

  - `provinceCode` (string)
    Province code for southern Europe/US countries
    Example: "MD/CA"

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

  - `additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

## Response 200 fields (application/json):

  - `id` (integer)
    Amendment proposal id

  - `street` (string, required)
    Street of the customer
    Example: "Am Bahnhof"

  - `houseNumber` (string)
    Number of the customer's house
    Example: "90"

  - `zipCode` (string, required)
    Zip code of the customer
    Example: "12133"

  - `city` (string, required)
    City of the customer
    Example: "Munich"

  - `countryCode` (string, required)
    Country of the customer
    Example: "DE"

  - `province` (string)
    Province for southern Europe/US countries
    Example: "Madrid/California"

  - `provinceCode` (string)
    Province code for southern Europe/US countries
    Example: "MD/CA"

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

  - `additionalAddressInformation` (string)
    Additional address information of the customer's address
    Example: "Additional information"

  - `floor` (string)
    Floor of the customer's address
    Example: "2nd floor"

  - `buildingName` (string)
    Building name
    Example: "Empire State Building"

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


### Get customer's master data

 - [GET /v1/customers/{customerId}/self-service/master-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomermasterdata.md): Required Scopes: 

Returns customer current master data along with requested change of this data

# Get customer's master data

Required Scopes: 

Returns customer current master data along with requested change of this data

Endpoint: GET /v1/customers/{customerId}/self-service/master-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `firstName` (string, required)
    First name of the customer
    Example: "Edgar"

  - `lastName` (string, required)
    Surname of the customer
    Example: "Bullock"

  - `gender` (string, required)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `dateOfBirth` (string, required)
    Birthday of the customer
    Example: "1952-05-04"

  - `countryOfBirth` (string)
    Birth country of the customer
    Example: "DE"

  - `customerTitle` (string, required)
    Title of the customer
    Enum: "NONE", "DR", "PROF"

  - `amendmentConfigurationStatus` (string, required)
    Status of the amendment configuration.
    Enum: "READ", "CHANGES_REQUIRE_VERIFICATION", "CHANGES_WITHOUT_VERIFICATION"

  - `pendingAmendment` (object)
    Pending amendment

  - `pendingAmendment.id` (integer)
    Amendment proposal id

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


### Create master data amendment

 - [POST /v1/customers/{customerId}/self-service/master-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomermasterdataamendment.md): Required Scopes: 

Creates request for master data amendment for specified customerId

# Create master data amendment

Required Scopes: 

Creates request for master data amendment for specified customerId

Endpoint: POST /v1/customers/{customerId}/self-service/master-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `firstName` (string, required)
    First name of the customer
    Example: "Edgar"

  - `lastName` (string, required)
    Surname of the customer
    Example: "Bullock"

  - `gender` (string, required)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `dateOfBirth` (string, required)
    Birthday of the customer
    Example: "1952-05-04"

  - `countryOfBirth` (string)
    Birth country of the customer
    Example: "DE"

  - `customerTitle` (string, required)
    Title of the customer
    Enum: "NONE", "DR", "PROF"

## Response 200 fields (application/json):

  - `id` (integer)
    Amendment proposal id

  - `firstName` (string, required)
    First name of the customer
    Example: "Edgar"

  - `lastName` (string, required)
    Surname of the customer
    Example: "Bullock"

  - `gender` (string, required)
    Gender of the customer
    Enum: "MALE", "FEMALE", "UNISEX"

  - `dateOfBirth` (string, required)
    Birthday of the customer
    Example: "1952-05-04"

  - `countryOfBirth` (string)
    Birth country of the customer
    Example: "DE"

  - `customerTitle` (string, required)
    Title of the customer
    Enum: "NONE", "DR", "PROF"

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


### Get customer's payment data

 - [GET /v1/customers/{customerId}/self-service/payment-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomerpaymentdata.md): Required Scopes: 

Returns customer current payment data along with requested change of this data

# Get customer's payment data

Required Scopes: 

Returns customer current payment data along with requested change of this data

Endpoint: GET /v1/customers/{customerId}/self-service/payment-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Response 200 fields (application/json):

  - `accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `bankName` (string)
    Name of the bank
    Example: "Deutsche Bank"

  - `iban` (string)
    Iban of the clients account
    Example: "DE91 1000 0000 0123 4567 89"

  - `bic` (string)
    Bic of the clients account
    Example: "DEUTDEFFXXX"

  - `requireSignature` (boolean)
    Is customer signature required to make amendment
    Example: true

  - `amendmentConfigurationStatus` (string, required)
    Status of the amendment configuration.
    Enum: "READ", "CHANGES_REQUIRE_VERIFICATION", "CHANGES_WITHOUT_VERIFICATION"

  - `pendingAmendment` (object)
    Pending amendment

  - `pendingAmendment.id` (integer)
    Amendment proposal id

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


### Create payment data amendment

 - [POST /v1/customers/{customerId}/self-service/payment-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomerpaymentdataamendment.md): Required Scopes: 

Creates request for payment data amendment for specified customerId

# Create payment data amendment

Required Scopes: 

Creates request for payment data amendment for specified customerId

Endpoint: POST /v1/customers/{customerId}/self-service/payment-data
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

## Request fields (application/json):

  - `accountHolder` (string, required)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `bankName` (string, required)
    Name of the bank
    Example: "Deutsche Bank"

  - `iban` (string, required)
    Iban of the clients account
    Example: "DE91 1000 0000 0123 4567 89"

  - `bic` (string, required)
    Bic of the clients account
    Example: "DEUTDEFFXXX"

  - `signature` (object)
    Representing customer signature

  - `signature.base64SvgSignature` (string, required)
    Customer confirmation signature SVG value as base 64 string

## Response 200 fields (application/json):

  - `id` (integer)
    Amendment proposal id

  - `accountHolder` (string)
    The account holder of the bank account
    Example: "Sven Hannawald"

  - `bankName` (string)
    Name of the bank
    Example: "Deutsche Bank"

  - `iban` (string)
    Iban of the clients account
    Example: "DE91 1000 0000 0123 4567 89"

  - `bic` (string)
    Bic of the clients account
    Example: "DEUTDEFFXXX"

  - `requireSignature` (boolean)
    Is customer signature required to make amendment
    Example: true

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


### Withdraw customer's amendment

 - [DELETE /v1/customers/{customerId}/self-service/amendment/{amendmentId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/withdrawamendment.md): Required Scopes: 

Withdraw customer's amendment

# Withdraw customer's amendment

Required Scopes: 

Withdraw customer's amendment

Endpoint: DELETE /v1/customers/{customerId}/self-service/amendment/{amendmentId}
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `customerId` (integer, required)
    Unique ID of the customer

  - `amendmentId` (integer, required)
    Unique ID of the amendment

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


## Devices

Get device information

### Get devices

 - [GET /v1/devices](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/devices/getdevices.md): Required Scopes: 

Returns devices for a studio

# Get devices

Required Scopes: 

Returns devices for a studio

Endpoint: GET /v1/devices
Version: 1.9.0
Security: ApiKeyAuth

## Response 200 fields (application/json):

  - `id` (integer)
    Device id
    Example: 26

  - `name` (string)
    Device name
    Example: "Turnstile (left)"

  - `active` (boolean, required)
    Device state. If the value is false then the device is inactive and must be activated before use

  - `model` (string)
    Device model
    Enum: "GENERIC_VENDING_READER", "GENERIC_CARD_READER", "GENERIC_TIME_READER"

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


### Activate device

 - [PUT /v1/devices/{deviceId}/activate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/devices/activatedevice.md): Required Scopes: 

Activates device and returns token

# Activate device

Required Scopes: 

Activates device and returns token

Endpoint: PUT /v1/devices/{deviceId}/activate
Version: 1.9.0
Security: ApiKeyAuth

## Path parameters:

  - `deviceId` (integer, required)

## Response 200 fields (application/json):

  - `id` (integer)
    Device id
    Example: 26

  - `accessToken` (string)
    Device token for further communication
    Example: "53cda15a-5652-4f62-9b97-508f870ff40b"

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




## Employees

Employee operations

### Get employees

 - [GET /v1/employees](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/employees/getemployees.md): Required Scopes: 

Returns employees for studio defined by used x-api-key.

### Get employee

 - [GET /v1/employees/{id}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/employees/getemployee.md): Required Scopes: 

Returns employee by id

## Finance

Debt collection operations

### Get Configuration of Debt Collection

 - [GET /v1/debt-collection/configuration](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/getdebtcollectionconfiguration.md): Required Scopes: 

Get Configuration of Debt Collection

### Get Debtors

 - [GET /v1/debt-collection/{debtCollectionRunId}/debtors](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/getdebtors.md): Required Scopes: 

Returns debtors for specified debtCollectionRunId in slices

### Get Transfer Details

 - [GET /v1/debt-collection/{debtCollectionRunId}/details](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/gettransferdetails.md): Required Scopes: 

Get transfer details by specified debtCollectionRunId

### Update debt collection

 - [POST /v1/debt-collection/update](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/updatedebtcollection.md): Required Scopes: 

### Confirm transfer retrieval

 - [POST /v1/debt-collection/{debtCollectionRunId}/confirmTransfer](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/confirmtransfer.md): Required Scopes: 

After fetching all data (details and debtors) related to a transfer use this endpoint to confirm the retrieval. This will flag the related data in Magicline as retrieved by the Agency. This endpoint should only be called if the status of the transfer is WAITING_FOR_CONFIRMATION (see getTransferDetails)

### Get debt collection cases

 - [GET /v1/debt-collection/cases](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/getdebtcollectioncases.md): Required Scopes: 

Returns the current state of debt collection cases specified by debtorId, collectionCaseId and agencyCollectionCaseId. Each parameter has maximum allowable 50 ids.

### Get blocked debt collection debtors

 - [GET /v1/debt-collection/blocked/debtors](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/getdebtcollectionblockeddebtors.md): Required Scopes: 

### Get blocked debt collection debts

 - [GET /v1/debt-collection/blocked/debts](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/getdebtcollectionblockeddebts.md): Required Scopes: 

### Create tax advisor export

 - [POST /v1/taxadvisor/exports/create](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/createexport.md): Required Scopes: 

Returns the export id

### Get tax advisor export by id

 - [GET /v1/taxadvisor/exports/{exportId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/finance/getexport.md): Required Scopes: 

Returns export download data like the download URL

## Leads

Leads operations

### Getting the config of the lead

 - [GET /v1/leads/config](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/leads/getleadconfig.md): Required Scopes: 

Returns generic lead data configuration

### Validate for lead creation

 - [POST /v1/leads/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/leads/validateforleadcreation.md): Required Scopes: 

Validates the lead data for creation

### Create a new Lead based on the config

 - [POST /v1/leads/create](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/leads/createlead.md): Required Scopes: 

Creates a new lead based on the configuration

## Membership Self-service

Manage membership contracts

### Get customer's contract data

 - [GET /v1/memberships/{customerId}/self-service/contract-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getcontractdata.md): Required Scopes: 

Returns customer's current contract data for memberships

### Create contract cancelation amendment

 - [POST /v1/memberships/{customerId}/self-service/ordinary-contract-cancelation](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/createcontractcancelationamendment.md): Required Scopes: 

Creates contract cancelation amendment for specified contract id

### Get studio's contract cancelation reason data

 - [GET /v1/memberships/self-service/contract-cancelation-reasons](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getcontractcancelationreasondata.md): Required Scopes: 

Get available contract cancelation reasons for the studio

### withdraw cancelation of contract

 - [POST /v1/memberships/{customerId}/self-service/withdraw-ordinary-contract-cancelation/{contractId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/withdrawcontractcancelation.md): Required Scopes: 

Withdraws contract cancelation amendment or reverts cancelation for specific contract id

### Get the idle period configuration of the contract

 - [GET /v1/memberships/{contractId}/self-service/idle-periods/config](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getidleperiodconfig.md): Required Scopes: 

Get the idle period configuration of the contract

### Validate an idle period request

 - [POST /v1/memberships/{contractId}/self-service/idle-periods/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/validateidleperiodrequest.md): Required Scopes: 

Validate if an idle period or idle period amendment can be created with the data from the idle period request

### Get the idle periods of the contract

 - [GET /v1/memberships/{contractId}/self-service/idle-periods](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getidleperiods.md): Required Scopes: 

Get contract idle periods. Amendments are returned, when a idle period is in status pending verification

### Create a contract idle period amendment

 - [POST /v1/memberships/{contractId}/self-service/idle-periods](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/createidleperiodamendment.md): Required Scopes: 

Create a contract idle period amendment. When the amendment is accepted, it will become an idle period. ATTENTION: Please see https://developer.magicline.com/apis/openapi/general-information#multipartform-data-requests

### Get contract idle period by id

 - [GET /v1/memberships/{contractId}/self-service/idle-periods/{idlePeriodId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getidleperiodbyid.md): Required Scopes: 

Get contract idle period or amendment by id.

### Withdraw a contract idle period

 - [DELETE /v1/memberships/{contractId}/self-service/idle-periods/{idlePeriodId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/withdrawidleperiod.md): Required Scopes: 

Withdraw a contract idle period or amendment.

### Get additional modules

 - [GET /v1/memberships/self-service/additional-modules](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getadditionalmodules.md): Required Scopes: 

Get additional modules for a studio

### Get purchasable additional modules

 - [GET /v1/memberships/{contractId}/self-service/additional-modules/purchasable](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getpurchasableadditionalmodules.md): Required Scopes: 

Get purchasable additional modules for a studio and a customer (via main contract)

### Validate an additional module contract request

 - [POST /v1/memberships/{contractId}/self-service/additional-modules/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/validateadditionalmodulecontractrequest.md): Required Scopes: 

Validate an additional module contract request

### Purchase an additional module contract

 - [POST /v1/memberships/{contractId}/self-service/additional-modules/purchase](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/purchaseadditionalmodulecontract.md): Required Scopes: 

Purchase an additional module contract

### Get an additional module contract

 - [GET /v1/memberships/{contractId}/self-service/additional-module-contracts/{additionalModuleContractId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getadditionalmodulecontract.md): Required Scopes: 

Get an additional module contract via additional module contract id

### Create additional module contract cancelation amendment 

 - [POST /v1/memberships/{contractId}/self-service/additional-module-contracts/{additionalModuleContractId}/ordinary-cancelation](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/createmodulecontractcancelationamendment.md): Required Scopes: 

Creates additional module contract cancelation amendment for specified contract id and additional module contract id

### withdraw cancelation of the additional module contract

 - [POST /v1/memberships/{contractId}/self-service/additional-module-contracts/{additionalModuleContractId}/withdraw-cancelation](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/withdrawadditionalmodulecontractcancelation.md): Required Scopes: 

Withdraws additional module contract cancelation amendment or reverts cancelation for specific additional module contract id

### Get contract's remaining idle periods

 - [GET /v1/memberships/{contractId}/self-service/idle-periods/remaining](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/membership-self-service/getremainingidleperiods.md): Required Scopes: 

Returns contract's remaining idle periods

## Memberships

Membership operations

### Get all membership offers

 - [GET /v1/memberships/membership-offers](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/getmembershipoffers.md): Required Scopes: 

Returns all available membership offers.

### Get membership offer by id

 - [GET /v1/memberships/membership-offers/{membershipOfferId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/getmembershipofferbyid.md): Required Scopes: 

Returns extended information about the membership offer.

### Preview information before signing up for a new membership

 - [POST /v1/memberships/signup/preview](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/postsignuppreview.md): Required Scopes: 

### Sign up a new membership

 - [POST /v1/memberships/signup](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/signupmembership.md): Required Scopes: 

Returns customer id within the result dto.

### Preview information before adding a contract to an existing customer

 - [POST /v1/memberships/customers/{customerId}/add-membership/preview](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/postmembershippreview.md): Required Scopes: 

### Add a contract to an existing customer

 - [POST /v1/memberships/customers/{customerId}/add-membership](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/addmembership.md): Required Scopes: 

### Get all membership switch configurations for a customer

 - [GET /v1/memberships/{customerId}/membership-switch/configs](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/getmembershipswitchconfigurationsforcustomer.md): Required Scopes: 

Returns all available membership switch configurations for a customer.

### Get membership switch configuration by id for a customer

 - [GET /v1/memberships/{customerId}/membership-switch/configs/{configId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/getmembershipswitchconfigurationforcustomer.md): Required Scopes: 

Returns extended information about the membership offer.

### Preview the membership switch

 - [POST /v1/memberships/{customerId}/membership-switch/preview](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/postmembershipswitchpreview.md): Required Scopes: 

Returns information about an impact of a membership switch of a given contract.

### Perform the membership switch

 - [POST /v1/memberships/{customerId}/membership-switch](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/memberships/switchmembership.md): Required Scopes: 

Performs the membership switch for a given contract.

## Payments

Payment operations

### Create a user payment session

 - [POST /v1/payments/user-session](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/payments/usersession.md): Required Scopes: 

Request to initiate a user session for payments. This is used to collect payment instruments for future recurring payments or one-time transactions.

## Studios

Get studio information

### Get studio utilization

 - [GET /v1/studios/utilization](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/studios/getutilization.md): Required Scopes: 

Returns information about current checkin count and maximum studio capacity

### Get studio general information

 - [GET /v1/studios/information](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/studios/getstudioinformation.md): Required Scopes: 

Returns studio's general information for authenticated subject

### Confirm contract activation

 - [POST /v1/studios/confirmActivation](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/studios/confirmactivation.md): If your integration has webhook access, then you need to activate webhook events via this endpoint

## Trial Offers

Get trial offers information

### Get bookable trial offer classes

 - [GET /v1/trial-offers/bookable-trial-offers/classes](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/getbookabletrialofferclasses.md): Required Scopes: 

Get pageable bookable trial offer classes within the next year

### Get bookable trial offer appointments

 - [GET /v1/trial-offers/bookable-trial-offers/appointments/bookable](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/getbookabletrialofferappointments.md): Required Scopes: 

Get pageable bookable trial offer appointments within the next year

### Get trial offer config

 - [GET /v1/trial-offers/config/{configId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/gettrialofferconfig.md): Required Scopes: 

Get trial offer config by config id

### Validate for lead customer creation

 - [POST /v1/trial-offers/lead/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/validateforleadcustomercreation.md): Required Scopes: 

Validate for the creation of a new lead customer

### Create a lead customer

 - [POST /v1/trial-offers/lead/create](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/createleadcustomer.md): Required Scopes: 

Create a lead customer

### Get class slots for trial offers

 - [GET /v1/trial-offers/bookable-trial-offers/classes/{classId}/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/getclassslotsfortrialoffers.md): Required Scopes: 

Returns class slots for trial offers for specified class id and the period of one day before to fourteen days ahead

### Get bookable appointment slots for trial offers

 - [GET /v1/trial-offers/bookable-trial-offers/appointments/bookable/{bookableAppointmentId}/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/getbookableappointmentslotsfortrialoffers.md): Required Scopes: 

Returns bookable appointment slots for trial offers

### Validate class slot is bookable for trial offers

 - [POST /v1/trial-offers/classes/booking/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/validateclassslotfortrialoffers.md): Required Scopes: 

Validate class slot for trial offers is available to book for given customer

### Validate for appointment booking for trial offers

 - [POST /v1/trial-offers/appointments/booking/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/validateforappointmentbookingfortrialoffers.md): Required Scopes: 

Returns validation result for trial offers appointment booking

### Book a class slot for trial offers

 - [POST /v1/trial-offers/classes/booking/book](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/bookclassslotfortrialoffers.md): Required Scopes: 

Book a class slot for trial offers for given customer

### Book an appointment for trial offers

 - [POST /v1/trial-offers/appointments/booking/book](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/bookappointmentfortrialoffer.md): Required Scopes: 

Book an appointment for trial offers for given customer

### Confirm the booking of trial offers

 - [POST /v1/trial-offers/bookings/{bookingId}/confirm](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/trial-offers/confirmtrialofferbooking.md): Required Scopes: 

Confirm the booking of trial offers for classes or appointments if required
