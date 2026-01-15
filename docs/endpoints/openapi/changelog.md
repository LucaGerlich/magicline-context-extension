# Changelog

All notable changes to OpenAPI will be documented in this file.

## [1.9.0] - 2026-01-09

### Added

- Added page
- Added documentation section describing the use and behavior of `HEAD` requests for API key validation in the Open API.
- Added documentation for service availability behavior. Endpoints may return `503 Service Unavailable` during periods of high database load.
- Added new endpoints
  - [Get lead config](../openapi/openapi#operation/getLeadConfig)
  - [Validate lead data for creation](../openapi/openapi#operation/validateForLeadCreation)
  - [Create lead](../openapi/openapi#operation/createLead)


### Changed

- Updated use case description for
- Added new fields `language` and `thirdPartyId` to the request of [Validate for lead customer creation](../openapi/openapi#operation/validateForLeadCustomerCreation) and [Create a lead customer](../openapi/openapi#operation/createLeadCustomer) endpoints.
- Added new field `cancelCondition` to class data in the response of the following endpoints:
  - [Get bookable trial offer classes](../openapi/openapi#operation/getBookableTrialOfferClasses)
  - [Get class by id](../openapi/openapi#operation/getClassById)
  - [Get classes](../openapi/openapi#operation/getActiveClasses)


## [1.8.5] - 2025-12-19

### Added

- Added new endpoint [Get idle period by id](../openapi/openapi/membership-self-service/getIdlePeriodById)
- Added new endpoint [Get contract's remaining idle periods](../openapi/openapi/membership-self-service/getRemainingIdlePeriods)


### Changed

- Added new `IDLEPERIOD_TERMVALUE_MISSING` validation status in the response of [Validate idle period validation request](../openapi/openapi/membership-self-service/validateIdlePeriodRequest) endpoint
- Updated request of [Validate idle period validation request](../openapi/openapi/membership-self-service/validateIdlePeriodRequest) and [Create idle period or idle period amendment](../openapi/openapi/membership-self-service/createIdlePeriodAmendment) endpoints:
  - Added new field `unlimited`
  - Fields `temporalUnit` and `termValue` are no longer mandatory
- Added new `unlimited` field to the response of idle period related endpoints:
  - [Get idle periods or idle period amendment](../openapi/openapi/membership-self-service/getIdlePeriods)
  - [Create idle period or idle period amendment](../openapi/openapi/membership-self-service/createIdlePeriodAmendment)
- Added new idle period `unlimited` field to all customer related endpoints (See e.g. response of [Get customer by id](../openapi/openapi/customers/getCustomerById) endpoint)


## [1.8.4] - 2025-12-11

### Changed

- Updated description of the offset parameter in the following endpoints:
  - [Get classes slots](../openapi/openapi#operation/getClassSlotsForMultipleClasses)
  - [Get class slots](../openapi/openapi#operation/getClassSlots)
  - [Get customers account upcoming bookings](../openapi/openapi#operation/getCustomersAccountUpcomingData)
  - [Get customers account transaction history](../openapi/openapi#operation/getCustomersAccountTransactionData)
  - [Get class slots for trial offers](../openapi/openapi#operation/getClassSlotsForTrialOffers)


## [1.8.3] - 2025-12-04

### New

- Added new webhook event types
  - `CONTRACT_IDLE_PERIOD_UPDATED`
  - `STUDIO_OPENING_HOURS_UPDATED`
  - `CUSTOMER_CHECKIN_STUDIOS_UPDATED`
  - `CUSTOMER_HOME_STUDIO_UPDATED`
  - `CONTRACT_ADDITIONAL_MODULE_CREATED`
  - `CONTRACT_ADDITIONAL_MODULE_DELETED`
  - `CONTRACT_ADDITIONAL_MODULE_UPDATED`
  - `CONTRACT_ADDITIONAL_MODULE_CANCELLED`


### Changed

- Delete fields `companyAmountPreUseCharge` and `memberAmountPreUseCharge` from the response of [Preview information before adding a contract to an existing customer](../openapi/openapi#operation/postMembershipPreview) and [Preview information before signing up for a new membership](../openapi/openapi#operation/postSignupPreview) endpoints
- Add field `freeTerms` to the response of [Get idle period config](../openapi/openapi/membership-self-service/getIdlePeriodConfig) endpoint
- Add `class.Id` and `class.title` to
  - [Get class slots](../openapi/openapi#operation/getClassSlots)
  - [Get class slot by id](../openapi/openapi#operation/getClassSlotById)
  - [Get classes slots](../openapi/openapi#operation/getClassSlotsForMultipleClasses)
  - [Get class slots for trial offers](../openapi/openapi#operation/getClassSlotsForTrialOffers)


## [1.8.2] - 2025-11-28

### New

- Add Header to general information


### Changed

- Update the default error language to English


## [1.8.1] - 2025-11-26

### New

- Added new webhook event types `CUSTOMER_ACCESS_MEDIUM_CREATED`, `CUSTOMER_ACCESS_MEDIUM_UPDATED` and `CUSTOMER_ACCESS_MEDIUM_DELETED`
- Added new webhook event types `CONTRACT_IDLE_PERIOD_CANCELLED` and `CONTRACT_IDLE_PERIOD_CREATED`


## [1.8.0] - 2025-11-20

### New

- Added new webhook event types: `CUSTOMER_ACCESS_RESTRICTION_CREATED` and `CUSTOMER_ACCESS_RESTRICTION_DELETED`


### Changed

- Added `voucherDiscountPeriods` to the response of [Preview information before signing up for a new membership](../openapi/openapi#operation/postSignupPreview)
- Added `voucherDiscountPeriods` to the response of [Preview information before adding a contract to an existing customer](../openapi/openapi#operation/postMembershipPreview)
- Update request of endpoint [Preview information before signing up for a new membership](../openapi/openapi#operation/postSignupPreview)
- Update request of endpoint [Sign up a new membership](../openapi/openapi#operation/signupMembership)


## [1.7.0] - 2025-11-05

### Added

- Add new endpoint [Get classes slots](../openapi/openapi#operation/getClassSlotsForMultipleClasses)
- Add new appointment booking validation status `NOT_AVAILABLE` to the response of appointment booking validation and appointment booking for trial offers validation
- Add new address fields to all customer related endpoints (See e.g. response of [Get customer by id](../openapi/openapi/customers/getCustomerById) endpoint)
- Add rateCodes to module and contract endpoints (See e.g. response of [Get contract data by customer id](../openapi/openapi/membership-self-service/getContractData) endpoint)
- Add new fields `secondFirstName` and `secondLastName` to customer data response
- Add new field `timeRestrictions` to [Get membership offer by id](../openapi/openapi#operation/getMembershipOfferById)
- Add new field `openingHoursCategories` to [Get studio general information](../openapi/openapi/studios#operation/getStudioInformation)
- Update response of endpoint [Get idle period config](../openapi/openapi/membership-self-service/getIdlePeriodConfig)
- Add new field `showExistingPaymentInstruments` to the request of [Create a user payment session](../openapi/openapi#operation/userSession)
- Add new parameter for [Get all membership switch configurations for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationsForCustomer)
- Add new parameter for [Get membership switch configuration by id for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationForCustomer)
- Add new parameter for [Preview the membership switch](../openapi/openapi#operation/postMembershipSwitchPreview)
- Update response of endpoint [Preview information before signing up for a new membership](../openapi/openapi#operation/postSignupPreview)


## [1.6.0] - 2025-10-01

### Added

- Added new webhook event type `FINANCE_DEBT_COLLECTION_CASE_UPDATED`


### Changed

- Add new parameter for [Get debt collection cases](../openapi/openapi#operation/getDebtCollectionCases)
- Add new parameter for [Get customer by id from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomerById)
- Add new parameter for [Get customer by](../openapi/openapi/customers/getCustomerBy)
- Add new parameter for [Get customer's measurement](../openapi/openapi/customers/getCustomerMeasurement)
- Adjust response of [Preview the membership switch](../openapi/openapi#operation/postMembershipSwitchPreview)
- Adjust response of [Preview information before signing up for a new membership](../openapi/openapi#operation/postSignupPreview)
- Adjust request body of [Create a user payment session](../openapi/openapi#operation/userSession)


## [1.5.0] - 2025-09-17

### Added

- Added page
- Added page
- Added new endpoint [Preview information before signing up for a new membership](../openapi/openapi#operation/postSignupPreview)
- Update request and response of endpoint [Add a contract to an existing customer](../openapi/openapi#operation/addMembership)
- Update response of endpoint [Get studio general information](../openapi/openapi/studios#operation/getStudioInformation)
- Update response of endpoint [Get devices](../openapi/openapi#operation/getDevices)
- Update request of endpoint [Create customer](../openapi/openapi/customers/createCustomer)


## [1.4.31] - 2025-09-03

### Added

- Added page
- Added new endpoint [Get customer's documents](../openapi/openapi/customers/getDocuments)
- Added new endpoint [Get customer's document](../openapi/openapi/customers/getDocumentById)
- Added new endpoint [Preview the membership switch](../openapi/openapi#operation/postMembershipSwitchPreview)
- Added new endpoint [Perform the membership switch](../openapi/openapi#operation/switchMembership)
- Update request body of endpoint [Add a contract to an existing customer](../openapi/openapi#operation/addMembership)
- Update request body of endpoint [Sign up a new membership](../openapi/openapi#operation/signupMembership)


## [1.4.30] - 2025-08-06

### Added

- Added new endpoint [Create a user payment session](../openapi/openapi#operation/userSession)
- Added new endpoint [Get membership offer by id for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationByIdForCustomer)
- Added new endpoint [Get all membership switch configurations for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationsForCustomer)
- Added new endpoint [Get membership offer by id](../openapi/openapi#operation/getMembershipOfferById)
- Added new endpoint [Get all membership offers](../openapi/openapi#operation/getMembershipOffers)


## [1.4.29] - 2025-07-16

### Added

- Endpoint [Add a new access medium to a customer (Deprecated)](../openapi/openapi/customers/addAccessMedium) is now deprecated and replaced by [Add a new access medium to a customer](../openapi/openapi/customers/addAccessMediums)
- Added new endpoint [Update customer's access medium](../openapi/openapi/customers/updateAccessMediums)
- Added new endpoint [Delete customer's access medium](../openapi/openapi/customers/deleteAccessMediums)
- Added new field `thirdPartyId` to all customer related endpoints (See e.g. response of [Get customer by id](../openapi/openapi/customers/getCustomerById) endpoint)
- Added new field `thirdPartyId` to all customer contract related endpoints (See e.g. response of [Get customer contracts by](../openapi/openapi/customers/getCustomerContractsBy) endpoint)
- Added new endpoint [Redeem checkin voucher](../openapi/openapi#operation/redeemCheckinVoucher)


## [1.4.28] - 2025-07-10

### Added

- Added new endpoint [Switch studio](../openapi/openapi/customers/switchStudio)


## [1.4.27] - 2025-07-09

### Added

- Added new fields `location`,`studioTags`,`openingDate`,`closingDate` to the response of [Get studio general information](../openapi/openapi/studios#operation/getStudioInformation) endpoint
- Added new field `additionalInformationFieldAssignments` to all customer related endpoints (See e.g. response of [Get customer by id](../openapi/openapi/customers/getCustomerById) endpoint)
- Added new endpoint [Get additional information fields](../openapi/openapi/customers/getAdditionalInformationFields)
- Added new endpoint [Sets additional information field assignments](../openapi/openapi/customers/setAdditionalInformationFieldAssignments)
- Added new endpoint [Add a contract to an existing customer](../openapi/openapi#operation/addMembership)
- Added new endpoint [Get studios with active membership offers](../openapi/openapi#operation/getStudiosWithActiveMembershipOffers)
- Added new endpoint [Create customer](../openapi/openapi/customers/createCustomer)
- Update request body of endpoint [Sign up a new membership](../openapi/openapi#operation/signupMembership)
- Added new webhook event type `ADDITIONAL_INFORMATION_FIELDS_UPDATED`
- Added new webhook event type `AUTOMATIC_CUSTOMER_CHECKOUT`


## [1.4.26] - 2025-06-11

### Added

- Updated use case description for
- Added new endpoint [Confirm a trial offer booking](../openapi/openapi#operation/confirmTrialOfferBooking)
- Added new booking status `BOOKED_WITH_CONFIRMATION_REQUIRED` to the response of booking related endpoints
- Added new endpoint [Set customer's access restriction](../openapi/openapi/customers/setAccessRestriction)
- Added new endpoint [Delete customer's access restriction](../openapi/openapi/customers/deleteAccessRestriction)
- `houseNumber` is no longer a required field in all endpoints with address data
- Added new access medium types `BARCODE` and `WALLET_PASS` to the response of customer related endpoints. New types can be added via [Add a new access medium to a customer](../openapi/openapi/customers/addAccessMediums).
- Added new types `PIN` and `WALLET_PASS` to all request bodies of Device API


## [1.4.25] - 2025-05-28

### Added

- Added new endpoint [Upload new document to a customer](../openapi/openapi/customers/uploadDocument)
- Added new endpoint [Sign up a new membership](../openapi/openapi#operation/signupMembership)
- Added new endpoint [Update customer profile image](../openapi/openapi/customers/updateImage)


## [1.4.24] - 2025-05-14

### Added

- Added new endpoints [Get employees](../openapi/openapi#operation/getEmployees) and [Get employee by id](../openapi/openapi#operation/getEmployee)


## [1.4.23] - 2025-03-19

### Added

- Added new webhook event type `CUSTOMER_ACCESS_DISABLED`


## [1.4.22] - 2025-03-05

### Added

- Added new field `cancelationOrigin` to the response DTO of [Get contract data by customer id](../openapi/openapi/membership-self-service/getContractData)
- Added new state `PENDING_WITHDRAWAL_VERIFICATION` to the field cancelationStatus of the response DTO of [Get contract data by customer id](../openapi/openapi/membership-self-service/getContractData)
- Added new webhook event type `CONTRACT_CANCELLED`


## [1.4.21] - 2025-02-25

### Added

- Added new endpoint [Get debt collection configuration](../openapi/openapi#operation/getDebtCollectionConfiguration)
- Added WebHook for updated debt collection configuration `FINANCE_DEBT_COLLECTION_CONFIGURATION_UPDATED`


## [1.4.20] - 2025-01-22

### Added

- Added new endpoint [Add a new access medium to a customer](../openapi/openapi/customers/addAccessMediums)
- Updated the `Customer` model by adding the new field `accessMediums`. This field deprecates `cardNumbers` field and is returned by the following endpoints.
  - [Get customer by id from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomerById)
  - [Get customer by from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomerBy)
  - [Search customers in all relevant studios](../openapi/openapi#operation/searchCrossStudioCustomers)
  - [Get customer by id](../openapi/openapi/customers/getCustomerById)
  - [Get customer by](../openapi/openapi/customers/getCustomerBy)
  - [Search customers](../openapi/openapi/customers/searchCustomers)
  - [Get customers](../openapi/openapi/customers/getCustomers)


## [1.4.19] - 2025-01-08

### Added

- Introducing new `customer communication preferences` features:
  - [Get customer communication preferences](../openapi/openapi#operation/getCommunicationPreferences)
  - [Update customer communication preferences](../openapi/openapi#operation/updateCommunicationPreferences)
- Added new validation statuses to the response of [Validate class slot is bookable](../openapi/openapi#operation/validateClassSlot) endpoint
- Added field `block` to [Update transfer](../openapi/openapi#operation/updateDebtCollection) endpoint to block customers or debts for future debt collection runs
- Added new endpoint to [Get blocked debtors]
- Added new endpoint to [Get blocked debts]
- Added some possible values of `latestRejectionReason`


## [1.4.17] - 2024-11-13

### Added

- Added new field `priceDetails` to all customer contract related endpoints (See e.g. response of [Get customer contracts by](../openapi/openapi/customers/getCustomerContractsBy) endpoint)


## [1.4.16] - 2024-10-09

### Added

- Added new parameter `barcode` and mark the old parameter `qrCodeUuid` as deprecated:
  - [Get customer by from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomerBy)
  - [Get customer by](../openapi/openapi/customers/getCustomerBy)
  - [Get customer's measurement](../openapi/openapi/customers/getCustomerMeasurement)
  - [Get customer contracts by](../openapi/openapi/customers/getCustomerContractsBy)


## [1.4.15] - 2024-10-02

### Added

- Introducing new `cross studio` features:
  - [Get customer's checkin history from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomersCheckinHistory)
- Added new `studioId` and `studioName` field to the response `CustomerCheckin` of endpoint [Get customer's checkin history](../openapi/openapi/customers/getCustomersCheckinHistory)
- Introducing new `Customers Communication` features:
  - [Create communication thread](../openapi/openapi#operation/createCommunicationInNewCommunicationThread)
  - [Update communication thread](../openapi/openapi#operation/createCommunicationInExistingCommunicationThread)


## [1.4.14] - 2024-09-04

### Added

- Introducing new `cross studio` features:
  - [Get customer by id from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomerById)
  - [Get customer by from all relevant studios](../openapi/openapi#operation/getCrossStudioCustomerBy)
  - [Search customers in all relevant studios](../openapi/openapi#operation/searchCrossStudioCustomers)
- Added new `studioId` field to the response `Customers` endpoints (See e.g. response of [Get customer by id](../openapi/openapi/customers/getCustomerById) endpoint)


## [1.4.13] - 2024-08-15

### Changed

- Added `participantStatus` and `classSlotStatus`  properties to all endpoints returning class slot booking result (See e.g. [Get booking by id](../openapi/openapi#operation/getClassBookingById))
- Added `participantStatus` and `appointmentStatus`  properties to all endpoints returning appointment booking result (See e.g. [Get appointment booking by booking id](../openapi/openapi#operation/getAppointmentBooking))
- Added `countryOfBirth` property to the response of [Get customer's master data](../openapi/openapi#operation/getCustomerMasterData) and the request and response of [Create master data amendment](../openapi/openapi#operation/createCustomerMasterDataAmendment) endpoints


## [1.4.12] - 2024-08-07

### Added

- new `Customers` features
  - [Get customer access code](../openapi/openapi/customers/getCustomerAccessCode)
  - Added new `accessCodeConfiguration` field to the response of [Get studio general information](../openapi/openapi/studios#operation/getStudioInformation) endpoint
- Introducing new `trial offer booking` features:
  - [Get bookable trial offer classes](../openapi/openapi#operation/getBookableTrialOfferClasses)
  - [Get bookable trial offer appointments](../openapi/openapi#operation/getBookableTrialOfferAppointments)
  - [Get trial offer config](../openapi/openapi#operation/getTrialOfferConfig)
  - [Validate for lead customer creation](../openapi/openapi#operation/validateForLeadCustomerCreation)
  - [Create a lead customer](../openapi/openapi#operation/createLeadCustomer)
  - [Get class slots for trial offers](../openapi/openapi#operation/getClassSlotsForTrialOffers)
  - [Get bookable appointment slots for trial offers](../openapi/openapi#operation/getBookableAppointmentSlotsForTrialOffers)
  - [Validate class slot is bookable for trial offer](../openapi/openapi/trial-offers#operation/validateClassSlotForTrialOffers)
  - [Validate for appointment booking for trial offers](../openapi/openapi#operation/validateForAppointmentBookingForTrialOffers)
  - [Book a class slot for trial offers](../openapi/openapi#operation/bookClassSlotForTrialOffers)
  - [Book an appointment for trial offers](../openapi/openapi#operation/bookAppointmentForTrialOffer)


## [1.4.11] - 2024-07-24

### Changed

- Extended  use case description with stand-in functionality


## [1.4.10] - 2024-07-03

### Changed

- Added `contractId` and `latestRejectionReason` for each debt in response of [Get debt collection cases](../openapi/openapi#operation/getDebtCollectionCases)
- Added `origin` to the response of [Get Transfer Details](../openapi/openapi#operation/getTransferDetails)


## [1.4.9] - 2024-05-15

### Changed

- Added `required` to all fields of [Create payment data amendment](../openapi/openapi#operation/createCustomerPaymentDataAmendment) to match actual implementation
- Added `classId` in the payload of webhook event type `CLASS_SLOT_UPDATED` and `CLASS_SLOT_CANCELLED`


## [1.4.8] - 2024-05-08

### Added

- Added use case description for
- Added new webhook event type `CLASS_SLOT_UPDATED` (triggered on resource updates)
- Added new endpoint [Get class bookings by customer id](../openapi/openapi#operation/getClassBookingsByCustomerId) to retrieve all class bookings for a `customerId`


### Changed

- `APPOINTMENT_BOOKING_UPDATED` event is now also triggered on resource updates


## [1.4.7] - 2024-04-03

### Added

- Added new `createdDate` property to `contractDetails` in:
  - [Get debtors](../openapi/openapi#operation/getDebtors) response
- Added new `publicName` property to all endpoints returning instructors (See e.g. [Get bookable appointment slots](../openapi/openapi#operation/getBookableAppointmentSlots))
- Added new `cancellationReceiptDate` property to all endpoints returning contracts (See e.g. [Get customer contracts by](../openapi/openapi/customers/getCustomerContractsBy))
- Added new `customerNumber` query param to the endpoint [Get customer by](../openapi/openapi/customers/getCustomerBy) and [Get customer contracts by](../openapi/openapi/customers/getCustomerContractsBy)
- Added the debt claims `id` to the response of [Get customers account transaction history](../openapi/openapi#operation/getCustomersAccountTransactionData) and [Get customers account upcoming bookings](../openapi/openapi#operation/getCustomersAccountUpcomingData) endpoint


## [1.4.6] - 2024-03-20

### Added

- Added new `preferredLanguage` field to the response of `Customers` endpoints (See e.g. response of [Get customer by id](../openapi/openapi/customers/getCustomerById) endpoint).
- Added new `additionalParticipants` field to the response of [Get class slot by id](../openapi/openapi#operation/getClassSlotById) endpoint


## [1.4.5] - 2024-03-13

### Added

- Added use case description for
- Introducing new `tax advisor accounting data` features:
  - [POST create tax advisor Export](../openapi/openapi#operation/createExport)
  - [GET get tax advisor Export](../openapi/openapi#operation/getExport)
- general improvements to parameter documentations across multiple endpoints


## [1.4.4] - 2024-03-06

### Added

- Updated `Data Chunking` section
- Updated `APPOINTMENT_BOOKING_UPDATE` event
- Added use case description for  and
- Introducing new `additional module purchasing` features:
  - [Get additional modules](../openapi/openapi/membership-self-service/getAdditionalModules)
  - [Get purchasable additional modules](../openapi/openapi/membership-self-service/getPurchasableAdditionalModules)
  - [Validate an additional module contract request](../openapi/openapi/membership-self-service/validateAdditionalModuleContractRequest)
  - [Purchase an additional module contract](../openapi/openapi/membership-self-service/purchaseAdditionalModuleContract)
  - [Get an additional module contract](../openapi/openapi/membership-self-service/getAdditionalModuleContract)
  - [Create additional module contract cancelation amendment](../openapi/openapi/membership-self-service/createModuleContractCancelationAmendment)
  - [Withdraw cancelation of the additional module contract](../openapi/openapi/membership-self-service/withdrawAdditionalModuleContractCancelation)


## [1.4.3] - 2024-01-24

### Added

- Introducing `required scopes` in endpoint descriptions
- Introducing new closure reasons in [Update transfer](../openapi/openapi#operation/updateDebtCollection)
  - `HARD_NEGATIVES_IN_DEBTOR_REGISTER`
  - `POSTAL_DELIVERY_NOT_POSSIBLE`
  - `CLAIM_INCREASE_IMPORTED_CASE`
- Introducing an optional free text closure reason in [Update transfer](../openapi/openapi#operation/updateDebtCollection)
- reduce `default slice sizes` in `Customers` endpoints


## [1.4.2] - 2023-11-02

### Added

- Introducing `customer's activity` features:
  - [Get customer's checkin history](../openapi/openapi/customers/getCustomersCheckinHistory)
- Adjustment of [Get customer by](../openapi/openapi/customers/getCustomerBy) endpoint
  - Added new optional query parameter `debtorId`
  - Added new optional query parameter `qrCodeUuid`
- Introducing `Customers` features:
  - [Get customer contracts by](../openapi/openapi/customers/getCustomerContractsBy)


## [1.4.1] - 2023-10-18

- Added new `studioId` field to the response of [Get studio general information](../openapi/openapi/studios#operation/getStudioInformation) endpoint
- Added new query parameter `slotWindowStartDate` to the [Get bookable appointment slots](../openapi/openapi#operation/getBookableAppointmentSlots) endpoint
- Added new webhook event type `CONTRACT_CREATED`


## [1.4.0] - 2023-10-05

- Introducing new `Device` features:
  - [Get devices](../openapi/openapi#operation/getDevices)
  - [Activate device](../openapi/openapi#operation/activateDevice)
- Added `signedDocumentUrl` to the response of [Get customer's contracts](../openapi/openapi/customers/getCustomersContracts) endpoint
- Changed request parameters of [Get customer's measurement](../openapi/openapi/customers/getCustomerMeasurement) endpoint:
  - `cardNumber` is now optional
  - new optional `uuid` parameter


## [1.3.0] - 2023-09-06

- Added new `rejectionReason` property to the request of the [Update transfer](../openapi/openapi#operation/updateDebtCollection) endpoint along with new `closureType` value `REJECTION`
- Added `dunningLevel `and `inDebtCollection` to the response of [Get customers account balance data](../openapi/openapi#operation/getCustomersAccountBalanceData) endpoint
- Added `accessRefusal`,`uuid`and`referralCode`to the response of following endpoints:
  - [Get customers](../openapi/openapi/customers/getCustomers)
  - [Get customer by id](../openapi/openapi/customers/getCustomerById)
  - [Get customer by](../openapi/openapi/customers/getCustomerBy)
  - [Search customers](../openapi/openapi/customers/searchCustomers)


## [1.2.1] - 2023-08-09

### Added

- Introducing `idle period` features:
  - [Get idle period config](../openapi/openapi/membership-self-service/getIdlePeriodConfig)
  - [Validate idle period validation request](../openapi/openapi/membership-self-service/validateIdlePeriodRequest)
  - [Get idle periods or idle period amendment](../openapi/openapi/membership-self-service/getIdlePeriods)
  - [Create idle period or idle period amendment](../openapi/openapi/membership-self-service/createIdlePeriodAmendment)
  - [Withdraw idle period or idle period amendment](../openapi/openapi/membership-self-service/withdrawIdlePeriod)
- Added new `status` to `TransferDetails` in:
  - [Get transfer details](../openapi/openapi#operation/getTransferDetails) response
- Introducing new `Finance` features:
  - [Confirm transfer](../openapi/openapi#operation/confirmTransfer)
- Introducing new `Customer Account` features:
  - [Get customers account balance data](../openapi/openapi#operation/getCustomersAccountBalanceData)
  - [Get customers account transaction history](../openapi/openapi#operation/getCustomersAccountTransactionData)
  - [Get customers account upcoming bookings](../openapi/openapi#operation/getCustomersAccountUpcomingData)


## [1.1.1] - 2023-06-21

- Added multiple fields to the results of the following `Bookable appointment and appointment booking` endpoints:
  - [Book appointment booking](../openapi/openapi#operation/bookAppointmentBooking)
  - [Get appointment booking by booking id](../openapi/openapi#operation/getAppointmentBooking)
  - [Get appointment bookings by customer id](../openapi/openapi#operation/getAppointmentBookings)


## [1.1.0] - 2023-06-07

### Added

- Introducing `Bookable appointment and appointment booking` features:
  - [Get bookable appointments](../openapi/openapi#operation/getBookableAppointments)
  - [Get bookable appointment by bookable appointment id](../openapi/openapi#operation/getBookableAppointment)
  - [Get bookable appointment slots](../openapi/openapi#operation/getBookableAppointmentSlots)
  - [Validate for appointment booking](../openapi/openapi#operation/validateForAppointmentBooking)
  - [Book appointment booking](../openapi/openapi#operation/bookAppointmentBooking)
  - [Get appointment booking by booking id](../openapi/openapi#operation/getAppointmentBooking)
  - [Delete appointment booking by booking id](../openapi/openapi#operation/deleteAppointmentBooking)
  - [Get appointment bookings by customer id](../openapi/openapi#operation/getAppointmentBookings)
- Introducing `Membership self service` features:
  - [Get contract data by customer id](../openapi/openapi/membership-self-service/getContractData)
  - [Create contract cancelation amendment](../openapi/openapi/membership-self-service/createContractCancelationAmendment)
  - [Get contract cancelation reason data](../openapi/openapi/membership-self-service/getContractCancelationReasonData)
  - [Withdraw contract cancelation](../openapi/openapi/membership-self-service/withdrawContractCancelation)
- Added new `status` property to `contactDetails` in:
  - [Get debtors](../openapi/openapi#operation/getDebtors) response
  - [Get transfer details](../openapi/openapi#operation/getTransferDetails) response
- Added new `addressStatus` property to `addressData` in:
  - [Get debtors](../openapi/openapi#operation/getDebtors) response
  - [Get transfer details](../openapi/openapi#operation/getTransferDetails) response


## [1.0.19] - 2023-03-17

### Added

- Introducing Webhook request body `content` property for additional event data


## [1.0.18] - 2023-01-25

### Added

- Introducing `Payment self-service` features:
  - [Get customer's payment data](../openapi/openapi#operation/getCustomerPaymentData)
  - [Create payment data amendment](../openapi/openapi#operation/createCustomerPaymentDataAmendment)


## [1.0.17] - 2023-01-18

### Added

- Introducing new [Get booking by id](../openapi/openapi#operation/getClassBookingById) operation
- Bank account information added to `customer` response body
  - `accountHolder`
  - `bankName`
  - `bic`
  - `iban`


## [1.0.16] - 2023-01-04

### Changed

- Added Managing Activations page.
- Added `amendmentConfigurationStatus` field to endpoints response:
  - [Get customer's contact data](../openapi/openapi#operation/getCustomerContactData)
  - [Get customer's address data](../openapi/openapi#operation/getCustomerAddressData)
  - [Get customer's master data](../openapi/openapi#operation/getCustomerMasterData)
- Added new [section](general-information#rate-limit) `Rate limit` in OpenAPI general information
- Added new http code in OpenApi error handling section
- Added new 429 response code to every OpenAPI endpoint


## [1.0.15] - 2022-12-27

### Changed

- Added `customerStatus` query parameter to [Get customers](../openapi/openapi/customers/getCustomers) endpoint:


## [1.0.14] - 2022-11-28

### Changed

- Added `customerNumber` field to endpoints response:
  - [Get customers](../openapi/openapi/customers/getCustomers)
  - [Get customer by id](../openapi/openapi/customers/getCustomerById)
  - [Get customer by](../openapi/openapi/customers/getCustomerBy)
  - [Search customers](../openapi/openapi/customers/searchCustomers)
- Added contract and subcontract `cancellationDate` field to [Get customer's contracts](../openapi/openapi/customers/getCustomersContracts) response


## [1.0.13] - 2022-10-21

### Added

- Introducing new `Finance` features:
  - [Get transfer details](../openapi/openapi#operation/getTransferDetails)
  - [Get debtors](../openapi/openapi#operation/getDebtors)
  - [Update transfer](../openapi/openapi#operation/updateDebtCollection)