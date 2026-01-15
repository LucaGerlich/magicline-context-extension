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

### Get bookable appointment

 - [GET /v1/appointments/bookable/{bookableAppointmentId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getbookableappointment.md): Required Scopes: 

Returns bookable appointment

### Get bookable appointment slots

 - [GET /v1/appointments/bookable/{bookableAppointmentId}/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getbookableappointmentslots.md): Required Scopes: 

Returns bookable appointment slots

### Validate for appointment booking

 - [POST /v1/appointments/bookable/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/validateforappointmentbooking.md): Required Scopes: 

Returns validation result

### Book an appointment booking

 - [POST /v1/appointments/booking/book](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/bookappointmentbooking.md): Required Scopes: 

Book an appointment booking for given customer

### Get an appointment booking

 - [GET /v1/appointments/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getappointmentbooking.md): Required Scopes: 

Get an appointment booking by id

### Delete an appointment booking

 - [DELETE /v1/appointments/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/deleteappointmentbooking.md): Required Scopes: 

Delete an appointment booking by id

### Get appointment bookings for a customer

 - [GET /v1/appointments/booking](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/appointments/getappointmentbookings.md): Required Scopes: 

Get appointment bookings with a period starting and ending within a timeframe of +/- 2 weeks for a specific customer

## Checkin vouchers

Redeem checkin vouchers

### Redeem checkin voucher

 - [POST /v1/checkin-vouchers/redeem](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/checkin-vouchers/redeemcheckinvoucher.md): Required Scopes: 

Redeem checkin voucher

## Classes

Class and slots operations

### Get classes

 - [GET /v1/classes](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getactiveclasses.md): Required Scopes: 

Returns classes with at least one scheduled appointment for the period of one day before to fourteen days ahead

### Get class by id

 - [GET /v1/classes/{classId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassbyid.md): Required Scopes: 

Returns a class for specified id

### Get classes slots

 - [GET /v1/classes/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassslotsformultipleclasses.md): Required Scopes: 

Returns class slots within the timeframe of daysAhead starting from slotWindowStartDate, for multiple classes

### Get class slots

 - [GET /v1/classes/{classId}/slots](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassslots.md): Required Scopes: 

Returns class slots for specified class id and the period of one day before to fourteen days ahead

### Get class slot by id

 - [GET /v1/classes/{classId}/slots/{classSlotId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassslotbyid.md): Required Scopes: 

Returns class slots for specified class slot id

### Book a class slot

 - [POST /v1/classes/booking/book](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/bookclassslot.md): Required Scopes: 

Book a class slot for given customer

### Validate class slot is bookable

 - [POST /v1/classes/booking/validate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/validateclassslot.md): Required Scopes: 

Validate class slot is available to book for given customer

### Get class booking by id

 - [GET /v1/classes/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassbookingbyid.md): Required Scopes: 

Returns class booking for specified booking id

### Cancel a class booking

 - [DELETE /v1/classes/booking/{bookingId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/cancelclassslotbyid.md): Required Scopes: 

Cancel booking of a class slot for given bookingId

### Get class bookings by customer id

 - [GET /v1/classes/booking](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/classes/getclassbookingsbycustomerid.md): Required Scopes: 

Returns class booking with a period starting and ending within a timeframe of +/- 2 weeks for a specific customer

## Cross Studio

Cross studio operations

### Get customer by

 - [GET /v1/cross-studio/customers/by](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getcrossstudiocustomerby.md): Required Scopes: 

Returns customer by one of the given parameters from all studios with activated partner integration

### Get customer by id

 - [GET /v1/cross-studio/customers/{customerId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getcrossstudiocustomerbyid.md): Required Scopes: 

Returns customer by given id from all studios with activated partner integration

### Search customers

 - [POST /v1/cross-studio/customers/search](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/searchcrossstudiocustomers.md): Required Scopes: 

Returns all customers from all studios with activated partner integration by given criteria

### Get customer's checkin history

 - [GET /v1/cross-studio/customers/{customerId}/activities/checkins](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getcrossstudiocustomerscheckinhistory.md): Required Scopes: 

Returns a list of studio checkins of the customer from all studios with activated partner integration for a specific time span (default is one month from today) in expected slices

### Get studios with active membership offers

 - [GET /v1/cross-studio/membership-offers/studios](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/cross-studio/getstudioswithactivemembershipoffers.md): Required Scopes: 

Returns all studios with at least one active membership offer.

## Customers

Get customers and contracts

### Get customers

 - [GET /v1/customers](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomers.md): Required Scopes: 

Returns all customers from studio in expected slices

### Get customer's checkin history

 - [GET /v1/customers/{customerId}/activities/checkins](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerscheckinhistory.md): Required Scopes: 

Returns a list of studio checkins of the customer for a specific time span (default is one month from today) in expected slices

### Get customer by id

 - [GET /v1/customers/{customerId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerbyid.md): Required Scopes: 

Returns customer by given id

### Get customer by

 - [GET /v1/customers/by](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerby.md): Required Scopes: 

Returns customer by one of the given parameters

### Search customers

 - [POST /v1/customers/search](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/searchcustomers.md): Required Scopes: 

Returns all customers from studio by given criteria

### Get customer's contracts

 - [GET /v1/customers/{customerId}/contracts](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomerscontracts.md): Required Scopes(any of): , 

Returns customer's contracts

### Get customer's measurement

 - [GET /v1/customers/measurement/latest](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomermeasurement.md): Required Scopes(any of): , 

Returns customer's latest measurement for specified customer.

### Get customer's contracts by

 - [GET /v1/customers/contracts/by](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomercontractsby.md): Required Scopes(any of): , 

Returns customer's contracts by one of the given parameters

### Save weighing results

 - [POST /v1/customers/{customerId}/weighing](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/createcustomerweighing.md): Required Scopes(any of): , 

Saves weighing details for given customer

### Get customer's benefits

 - [GET /v1/customers/{customerId}/benefits](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getbenefits.md): Required Scopes(any of): , 

Returns all customer's benefits

### Get customer's benefits by card number

 - [GET /v1/customers/benefits](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getbenefitsbycardnumber.md): Required Scopes(any of): , 

Returns customer's benefits by card number

### Post customer's benefit usage

 - [POST /v1/customers/{customerId}/benefits/{benefitKey}/use](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/usebenefit.md): Required Scopes(any of): , 

### Get customer's access code

 - [GET /v1/customers/{customerId}/access-code](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getcustomeraccesscode.md): Required Scopes: 

Returns customer's access code

### Add a new access medium to a customer

 - [POST /v1/customers/{customerId}/access-mediums](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/addaccessmediums.md): Required Scopes: 

Returns the newly added access medium

### Update customer's access medium

 - [PUT /v1/customers/{customerId}/access-mediums/{accessMediumId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/updateaccessmediums.md): Required Scopes: 

Updates the customer's access medium. Only previously created mediums may be updated.

### Delete customer's access medium

 - [DELETE /v1/customers/{customerId}/access-mediums/{accessMediumId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/deleteaccessmediums.md): Required Scopes: 

Deletes the customer's access medium. Only previously created mediums may be deleted.

### Returns all documents for a customer

 - [GET /v1/customers/{customerId}/documents](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getdocuments.md): Required Scopes: 

Returns all documents for a customer

### Upload new document to a customer

 - [POST /v1/customers/{customerId}/documents](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/uploaddocument.md): Required Scopes: 

Returns the newly uploaded document information

### Returns document for a customer

 - [GET /v1/customers/{customerId}/documents/{id}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getdocumentbyid.md): Required Scopes: 

Returns document for a customer

### Update customer profile image

 - [PUT /v1/customers/{customerId}/images](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/updateimage.md): Required Scopes: 

Updates customer profile image. The image will be rescaled(1200x1200) and converted to mime type .

### Set customer's access restriction

 - [PUT /v1/customers/{customerId}/access-restrictions](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/setaccessrestriction.md): Required Scopes: 

Creates or updates access restriction for the customer.
If the customer already has an access restriction, it will be updated with the provided data. Only previously created restrictions may be updated.
If no such restriction exists, it will be created. It is necessary to provide either both  and  or neither of them.


### Delete customer's access restriction

 - [DELETE /v1/customers/{customerId}/access-restrictions](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/deleteaccessrestriction.md): Required Scopes: 

Deletes the customer's access restriction. Only previously created restrictions may be deleted.

### Create customer

 - [POST /v1/customers/create](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/createcustomer.md): Required Scopes: 

Creates a new customer (prospect) with comprehensive data to allow for future conversion to a full member

### Get additional information fields

 - [GET /v1/customers/additional-information-fields](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/getadditionalinformationfields.md): Required Scopes: 

Returns additional information fields available for assignment to customers. 

### Sets additional information field assignments

 - [PUT /v1/customers/{customerId}/additional-information-field-assignments](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/setadditionalinformationfieldassignments.md): Required Scopes: 

Sets additional information field assignments for a customer. We overwrite existing values, so you need to provide all field assignments that you want to set. If you want to remove a field assignment, don't add it.

### Switch studio

 - [POST /v1/customers/{customerId}/switch-studio](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/switchstudio.md): Required Scopes: 

Switches the studio of the given customer to the specified target studio. The API key of the customer's source studio must be used for this request.

### Add a new access medium to a customer (deprecated)

 - [PUT /v1/customers/{customerId}/access-medium](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers/addaccessmedium.md): Required Scopes: 

Returns the newly added access medium

## Customers Account

Retrieve customer accounting details

### Get customer's account balance data

 - [GET /v1/customers/{customerId}/account/balances](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-account/getcustomersaccountbalancedata.md): Required Scopes: 

Returns customer's current account balance data

### Get customer's account past transactions in slices

 - [GET /v1/customers/{customerId}/account/transactions](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-account/getcustomersaccounttransactiondata.md): Required Scopes: 

Returns customer's account transaction data for the past excluding today

### Get customer's account upcoming transactions in slices within the next year

 - [GET /v1/customers/{customerId}/account/transactions/upcoming](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-account/getcustomersaccountupcomingdata.md): Required Scopes: 

Returns customer's account upcoming transaction data including today

## Customers Communication

Retrieve customer communication details

### Create communication thread

 - [POST /v1/communications/{customerId}/threads](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/createcommunicationinnewcommunicationthread.md): Required Scopes: 

Creates new thread with a new communication for a customer

### Update communication thread

 - [PUT /v1/communications/{customerId}/threads/{threadId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/createcommunicationinexistingcommunicationthread.md): Required Scopes: 

Adds new communication for a customer to an existing communication thread and updates the thread

### Get communication preferences

 - [GET /v1/communications/{customerId}/communication-preferences](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/getcommunicationpreferences.md): Required Scopes: 

Get communication preferences for a customer

### Update communication preferences

 - [PUT /v1/communications/{customerId}/communication-preferences](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-communication/updatecommunicationpreferences.md): Required Scopes: 

Update communication preferences for a customer

## Customers Self-service

### Get customer's contact data

 - [GET /v1/customers/{customerId}/self-service/contact-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomercontactdata.md): Required Scopes: 

Returns customer current contact data along with requested change of this data

### Create contact data amendment

 - [POST /v1/customers/{customerId}/self-service/contact-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomercontactdataamendment.md): Required Scopes: 

Creates request for contact data amendment for specified customerId

### Get customer's address data

 - [GET /v1/customers/{customerId}/self-service/address-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomeraddressdata.md): Required Scopes: 

Returns customer current address data along with requested change of this data

### Create address data amendment

 - [POST /v1/customers/{customerId}/self-service/address-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomeraddressdataamendment.md): Required Scopes: 

Creates request for address data amendment for specified customerId

### Get customer's master data

 - [GET /v1/customers/{customerId}/self-service/master-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomermasterdata.md): Required Scopes: 

Returns customer current master data along with requested change of this data

### Create master data amendment

 - [POST /v1/customers/{customerId}/self-service/master-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomermasterdataamendment.md): Required Scopes: 

Creates request for master data amendment for specified customerId

### Get customer's payment data

 - [GET /v1/customers/{customerId}/self-service/payment-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/getcustomerpaymentdata.md): Required Scopes: 

Returns customer current payment data along with requested change of this data

### Create payment data amendment

 - [POST /v1/customers/{customerId}/self-service/payment-data](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/createcustomerpaymentdataamendment.md): Required Scopes: 

Creates request for payment data amendment for specified customerId

### Withdraw customer's amendment

 - [DELETE /v1/customers/{customerId}/self-service/amendment/{amendmentId}](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/customers-self-service/withdrawamendment.md): Required Scopes: 

Withdraw customer's amendment

## Devices

Get device information

### Get devices

 - [GET /v1/devices](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/devices/getdevices.md): Required Scopes: 

Returns devices for a studio

### Activate device

 - [PUT /v1/devices/{deviceId}/activate](https://redocly.sportalliance.com/apis/magicline/openapi/openapi/devices/activatedevice.md): Required Scopes: 

Activates device and returns token

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

