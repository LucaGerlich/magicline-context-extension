# Working with appointments

## Intro

Use case description of how to use the appointments collection to enable appointment booking and cancellations with the Open API.

## Relevant Endpoints

- [GET bookable appointments](../openapi/openapi#operation/getBookableAppointments)
- [GET bookable appointment](../openapi/openapi#operation/getBookableAppointment)
- [GET bookable appointment slots](../openapi/openapi#operation/getBookableAppointmentSlots)
- [POST validate appointment booking slot](../openapi/openapi#operation/validateForAppointmentBooking)
- [POST book an appointment slot](../openapi/openapi#operation/bookAppointmentBooking)
- [GET appointment booking](../openapi/openapi#operation/getAppointmentBooking)
- [GET appointment bookings for a customer](../openapi/openapi#operation/getAppointmentBookings)
- [DELETE appointment booking](../openapi/openapi#operation/deleteAppointmentBooking)


## Appointment configuration in the 

The   offers comprehensive appointment scheduling and management functionality which is exposed via the Open API. In comparison to the classes collection - where class slots are a fixed entity which can be booked - bookable appointment slots are calculated on the fly and require checks on availability of resources (studio personnel, locations, equipment) and necessary contingents of customers.

An important aspect to note is that the following configuration requirements in the   must be met for appointments to be visible and retrievable via the Open API:

- Appointment must be set to Bookable under the booking options configuration
- Appointment must be available for online booking


Further information on how appointments are handled in the   can be found here: [How to create appointment based service](https://support.magicline.com/hc/en-001/articles/4576396418065-How-to-create-appointment-based-service)

## Display, validation and booking of appointment slots

Booking of appointment slots follows the following UX setup:

- [GET bookable appointments](../openapi/openapi#operation/getBookableAppointments) retrieves the complete list of possible bookable appointments that a studio has configured to be available via the Open API
- [GET bookable appointment slots](../openapi/openapi#operation/getBookableAppointmentSlots) returns the bookable slots for a specific bookableAppointmentId. For certain time constellations partners may receive a 200 response with an empty array - this indicates that there are no bookable slots available for this time period.
- [POST validate appointment booking slot](../openapi/openapi#operation/validateForAppointmentBooking): As with most post endpoints on the   Open API we provide a validate endpoint for partners to integrate into their UI/UX flows to make sure an appointment is actually bookable for a specific customer. Keep in mind that, similar to the classes collection, studio operators may configure certain appointments to only be bookable for certain rates, additional modules and/or member codes. Partners should use this endpoint whenever a customer is about to book an appointment slot, to make sure this appointment slot is still available.
- [POST book an appointment slot](../openapi/openapi#operation/bookAppointmentBooking) handles the actual booking of an appointment slot and returns the details of the appointment slot booking
- [DELETE appointment booking](../openapi/openapi#operation/deleteAppointmentBooking) allows partners to delete an appointment slot booking for a specific customer


In addition to the above implementation flow we also offer the [GET appointment booking](../openapi/openapi#operation/getAppointmentBooking), which lets partners sync any updates to an appointment booking based on the specific bookingId. Furthermore, the [GET appointment bookings for a customer](../openapi/openapi#operation/getAppointmentBookings) allows partners to retrieve all appointment bookings within a timeframe of +/- 2 weeks for a specific customer to display in their application and services.

## Using the slotWindowStartDate parameter

In order to give partners flexibility with appointment slot scheduling, the appointments collection offers an additional parameter `slotWindowStartDate` which allows partners to specify from which start date they want to fetch available appointment slots. The maximum time window for checking for available slots from the `slotWindowStartDate` is 6 days and handled by the `daysAhead` parameter.

## Cross facility appointment bookings

The   Open API supports cross facility bookings for appointments given the following requirements are met:

- studios have the respective partner integration enabled and activated
- customers who want to book appointments across facilities have an inclusive contingent that makes them eligible to book
- partners adhere to the API-key per studio concept (i.e. all bookings in a specific studio must happen in the context of that studios API-key)


## Appointment collection webhook events

In order to inform partners about necessary changes to bookable appointments and appointment slots, the appointment collection offers a variety of webhook events. For appointment bookings happening in the   itself, we offer the `APPOINTMENT_BOOKING_CREATED` event that partners can use to display this booking in their products and services.

Full list of events can be found here: [Event types](../webhooks/event-types/)