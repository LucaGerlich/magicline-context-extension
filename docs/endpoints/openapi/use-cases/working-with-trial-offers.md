# Working with trial offers

## Intro

Use case description of how trial offers are serviced via the Open API and what user flow is envisioned for partners

## Relevant Endpoints

- [GET Get trial offer config](../openapi/openapi#operation/getTrialOfferConfig)
- [GET Get bookable trial offer appointments](../openapi/openapi#operation/getBookableTrialOfferAppointments)
- [GET Get bookable trial offer classes](../openapi/openapi#operation/getBookableTrialOfferClasses)
- [POST Validate for lead customer creation](../openapi/openapi#operation/validateForLeadCustomerCreation)
- [POST Create a lead customer](../openapi/openapi#operation/createLeadCustomer)
- [GET Get class slots for trial offers](../openapi/openapi#operation/getClassSlotsForTrialOffers)
- [GET Get bookable appointment slots for trial offers](../openapi/openapi#operation/getBookableAppointmentSlotsForTrialOffers)
- [POST Validate class slot is bookable for trial offer](../openapi/openapi#operation/validateClassSlotForTrialOffers)
- [POST Validate for appointment booking for trial offers](../openapi/openapi#operation/validateForAppointmentBookingForTrialOffers)
- [POST Book a class slot for trial offers](../openapi/openapi#operation/bookClassSlotForTrialOffers)
- [POST Book an appointment for trial offers](../openapi/openapi#operation/bookAppointmentForTrialOffer)
- [POST Confirm a trial offer booking](../openapi/openapi#operation/confirmTrialOfferBooking)


## Trial offers in the 

Trial offers are a central piece for enticing new leads to join up by testing a day in the gym or a specific class.
Within the , operators can setup a distinct Trial Offer Configuration which details booking configurations as well as determining what information is required on enrolment.

Besides the administrational setup, operator then configure what services and/or classes are bookable under a specific trial offer configuration.

## Display, validation and booking of trial offers

The Trial Offer collection in the Open API follows the following envisioned user flow:

- the [GET Get bookable trial offer appointments](../openapi/openapi#operation/getBookableTrialOfferAppointments) & [GET Get bookable trial offer classes](../openapi/openapi#operation/getBookableTrialOfferClasses), return the available bookable trial sessions of a respective studio. Using the `classId` or `bookableAppointmentId`, partners can furthermore retrieve bookable classes or bookable appointment slots with the [GET Get class slots for trial offers](../openapi/openapi#operation/getClassSlotsForTrialOffers) and the [GET Get bookable appointment slots for trial offers](../openapi/openapi#operation/getBookableAppointmentSlotsForTrialOffers) endpoints
- each of the bookable trial offer classes or appointments has a `trialOfferConfigId` which needs to be passed to the [GET Get trial offer config](../openapi/openapi#operation/getTrialOfferConfig) endpoint to retrieve the configuration data. This data will inform partners about which data is required to create a lead customer, necessary for the further booking of a trial session
- the [POST Create a lead customer](../openapi/openapi#operation/createLeadCustomer) endpoint is a mandatory step to retrieve the `customerId` needed for further booking. We offer a [POST Validate for lead customer creation](../openapi/openapi#operation/validateForLeadCustomerCreation) endpoint to make sure partners UI does not show booking options when none are available
- the same logic is applied when conducting the actual booking. The [POST Validate class slot is bookable for trial offer](../openapi/openapi#operation/validateClassSlotForTrialOffers) and the [POST Validate for appointment booking for trial offers](../openapi/openapi#operation/validateForAppointmentBookingForTrialOffers) endpoints should be used to check if any issues arise when trying to book. The actual booking is then done via the [POST Book a class slot for trial offers](../openapi/openapi#operation/bookClassSlotForTrialOffers) and [POST Book an appointment for trial offers](../openapi/openapi#operation/bookAppointmentForTrialOffer) endpoints


## Trial offer booking confirmation

Within the trial offer configuration the `confirmationOfBookingTerm` object defines until when a booking needs to be confirmed in order to take place, for example: Personal Training Trial Session is booked by a lead with a `confirmationOfBookingTerm` set to 2 days. This means that the lead needs to confirm this booking no latest than 2 days before the appointment. If no confirmation occurs, the appointment is automatically cancelled.

The actual confirmation is handled by the integration partner, who needs to send a confirmation email (or similar) to the lead. This email (or similar) needs to contain a simple confirmation link that the lead needs to follow in order to confirm their trial offer booking. When the lead clicks on the confirmation link, the partner should call the [POST Confirm a trial offer booking](../openapi/openapi#operation/confirmTrialOfferBooking) endpoint to confirm the booking.
This endpoint will return a ResultDTO containing a `CONFIRMED` status, which indicates that the booking has been successfully confirmed, or a ResultDTO containing a `EXPIRED` status, which indicates that the confirmation has taken place too late.

To inform partners about the successful booking confirmation, a webhook of type `CLASS_BOOKING_CREATED` or `APPOINTMENT_BOOKING_CREATED` is sent.

## Trial offer webhook events

For the trial offer collection, all events related to the classes and bookable appointments are relevant.

Full list of events can be found here: [Event types](../webhooks/event-types/)