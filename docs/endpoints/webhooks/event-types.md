# Event Types

This page details all events currently available via the  Open API (this list will keep on growing).

style

  td {
    max-width: 120px;
    word-wrap: break-word;
  }

| Event type | Description | Details |
|  --- | --- | --- |
| ADDITIONAL_INFORMATION_FIELDS_UPDATED | Occurs whenever an additional information field was updated | `entityId` is the `studioId` |
| AGGREGATOR_MEMBER_CREATED | Occurs whenever an aggregator member was created | `entityId` is the `customerId`, `content.aggregatorId` is the aggregator member id |
| APPOINTMENT_BOOKING_CANCELLED | Occurs whenever an appointment booking was cancelled | `entityId` is the `bookingId` |
| APPOINTMENT_BOOKING_CREATED | Occurs whenever an appointment booking was created | `entityId` is the `bookingId` |
| APPOINTMENT_BOOKING_UPDATED | Occurs whenever an appointment booking time or resource was updated | `entityId` is the `bookingId` |
| AUTOMATIC_CUSTOMER_CHECKOUT | Occurs whenever one or multiple customers were automatically checked out from a facility | `entityId` is the `studioId`, content is the `checkouts` object with a list of `customerId` and `checkoutTime` pairs, e.g. `checkouts:{[{"customerId": 123, "checkoutTime": "2023-10-01T12:00:00Z"}]}` |
| CONTRACT_ADDITIONAL_MODULE_CREATED | Occurs whenever an additional module is created on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the main contract, `content.moduleContractId` is the id of the created additional module contract |
| CONTRACT_ADDITIONAL_MODULE_DELETED | Occurs whenever an additional module is deleted on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the main contract, `content.moduleContractId` is the id of the deleted additional module contract |
| CONTRACT_ADDITIONAL_MODULE_UPDATED | Occurs whenever an additional module is updated on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the main contract, `content.moduleContractId` is the id of the updated additional module contract |
| CONTRACT_ADDITIONAL_MODULE_CANCELLED | Occurs whenever an additional module is cancelled on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the main contract, `content.moduleContractId` is the id of the cancelled additional module contract |
| CONTRACT_UPDATED | Occurs whenever a contract was changed | `entityId` is the `customerId`, `content.contractId` is the id of updated contract |
| CONTRACT_CREATED | Occurs whenever a main contract was created | `entityId` is the `customerId`, `content.contractId` is the id of created contract |
| CONTRACT_CANCELLED | Occurs whenever a contract was cancelled | `entityId` is the `customerId`, `content.contractId` is the id of cancelled contract |
| CONTRACT_IDLE_PERIOD_CREATED | Occurs whenever an idle period is created on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the contract, `content.idlePeriodId` is the id of the created idle period |
| CONTRACT_IDLE_PERIOD_CANCELLED | Occurs whenever an idle period is removed on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the contract, `content.idlePeriodId` is the id of the cancelled idle period |
| CONTRACT_IDLE_PERIOD_UPDATED | Occurs whenever an idle period is updated on a customer's contract | `entityId` is the `customerId`, `content.contractId` is the id of the contract, `content.idlePeriodId` is the id of the updated idle period |
| CUSTOMER_ACCESS_MEDIUM_CREATED | Occurs whenever an access medium is created for a customer | `entityId` is the `customerId` |
| CUSTOMER_ACCESS_MEDIUM_UPDATED | Occurs whenever an access medium is updated for a customer | `entityId` is the `customerId` |
| CUSTOMER_ACCESS_MEDIUM_DELETED | Occurs whenever an access medium is removed for a customer | `entityId` is the `customerId` |
| CUSTOMER_ACCESS_RESTRICTION_CREATED | Occurs whenever an access restriction is created for a customer | `entityId` is the `customerId` |
| CUSTOMER_ACCESS_RESTRICTION_DELETED | Occurs whenever an access restriction is removed for a customer | `entityId` is the `customerId` |
| CUSTOMER_CHECKIN | Occurs whenever a customer has physically checked in at a facility | `entityId` is the `customerId` |
| CUSTOMER_CHECKOUT | Occurs whenever a customer has physically checked out from a facility | `entityId` is the `customerId` |
| CUSTOMER_CHECKIN_STUDIOS_UPDATED | Occurs whenever the checkin studios are updated for a customer | `entityId` is the `customerId` |
| CUSTOMER_CREATED | Occurs whenever a customer has been created at a facility | `entityId` is the `customerId` |
| CUSTOMER_DELETED | Occurs whenever a customer has been deleted | `entityId` is the `customerId` |
| CUSTOMER_UPDATED | Occurs whenever a customer's data has been changed | `entityId` is the `customerId` |
| CUSTOMER_COMMUNICATION_PREFERENCES_UPDATED | Occurs whenever a customer's communication preferences are updated | `entityId` is the `customerId` |
| CUSTOMER_ACCESS_DISABLED | Occurs whenever a customer's access was disabled. It is not possible to request customer data after this event. | `entityId` is the `customerId` |
| CUSTOMER_HOME_STUDIO_UPDATED | Occurs whenever a customer's home studio was changed. | `entityId` is the `customerId`, `content.sourceStudioId` is the id of the previous home studio, `content.targetStudioId` is the id of the new home studio |
| CLASS_BOOKING_CANCELLED | Occurs whenever a class booking was cancelled | `entityId` is the `bookingId` |
| CLASS_BOOKING_CREATED | Occurs whenever a class booking was created | `entityId` is the `bookingId` |
| CLASS_BOOKING_UPDATED | Occurs whenever a class booking was updated | `entityId` is the `bookingId` |
| CLASS_SLOT_CANCELLED | Occurs whenever a class slot was cancelled | `entityId` is the `classSlotId`, `content.classId` is the id of belonging class |
| CLASS_SLOT_UPDATED | Occurs whenever a class slot time or resource was updated | `entityId` is the `classSlotId`, `content.classId` is the id of belonging class |
| DEVICE_CREATED | Occurs whenever a device was created | `entityId` is the `deviceId` |
| EMPLOYEE_CREATED | Occurs whenever a employee has been created at a facility | `entityId` is the `employeeId` |
| EMPLOYEE_DELETED | Occurs whenever a employee has been deleted | `entityId` is the `employeeId` |
| EMPLOYEE_UPDATED | Occurs whenever a employee's data has been changed | `entityId` is the `employeeId` |
| FINANCE_DEBT_COLLECTION_RUN_CREATED | Occurs whenever a debt collection run was created | `entityId` is the `debtCollectionRunId` |
| FINANCE_DEBT_COLLECTION_CONFIGURATION_UPDATED | Occurs whenever the debt collection configuration was updated |  |
| FINANCE_DEBT_COLLECTION_CASE_UPDATED | Occurs whenever a debt collection case was updated | `entityId` is the `caseAdjustmentRequestId`. Content additionally contains the `agencyDebtCollectionCaseId` if set, or else the `collectionCaseId` |
| STUDIO_OPENING_HOURS_UPDATED | Occurs whenever the opening hours are updated for a studio | `entityId` is the `studioId` |
| TAX_ADVISOR_EXPORT_CREATED | Occurs whenever a tax advisor export was created | `entityId` is the `exportId` |