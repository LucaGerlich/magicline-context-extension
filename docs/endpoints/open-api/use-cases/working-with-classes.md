# Working with classes

## Intro

Use case description of how to use classes endpoints to enable class schedules, class booking and cancellations with the Open API

## Relevant Endpoints

- [GET classes](../openapi/openapi#operation/getActiveClasses)
- [GET class by id](../openapi/openapi#operation/getClassById)
- [GET class slots](../openapi/openapi#operation/getClassSlots)
- [GET class slot by id](../openapi/openapi#operation/getClassSlotById)
- [GET class booking by id](../openapi/openapi#operation/getClassBookingById)
- [POST book a class slot](../openapi/openapi#operation/bookClassSlot)
- [POST validate if class slot is bookable](../openapi/openapi#operation/validateClassSlot)
- [DELETE a class booking](../openapi/openapi#operation/cancelClassSlotById)


## Class configuration in the 

The  offers comprehensive class scheduling and management functionality which is exposed via the Open API. The general setup of the classes collection of the Open API is constructed to help with third party UI requirements.

An important aspect to note is that the following configuration requirements in the  must be met for classes to be visible and retrievable via the Open API:

- Class must be set to Bookable under the Booking options configuration
- Class must be available for online booking
- Class must have `classSlots` scheduled


Further information on configurations for classes in the   can be found here: [Course management](https://support.magicline.com/hc/en-001/sections/4407938591761-Course-management)

## Display, validation and booking of class slots

The UX flow envisioned here follows the following logic:

- [GET classes](../openapi/openapi#operation/getActiveClasses/) allows partners to display all possible classes that are scheduled for an individual studio
- [GET class by id](../openapi/openapi#operation/getClassById/) returns details for a specific class
- [GET class slots](../openapi/openapi#operation/getClassSlots/) returns the actual bookable slots with further information around earliest and latest booking times
- [GET class slot by id](../openapi/openapi#operation/getClassSlotById/) narrows this list down to one specific `classSlot`


From here we offer the option to [POST validate if class slot is bookable](../openapi/openapi#operation/validateClassSlot) a potential class booking. This should be used to avoid showing a book button in the UI which may not lead to a successful class booking for the customers. Classes can be configured in the   to be only available for certain memberships (i.e. PremiumClass is only available for customers with a Premium membership).

Once partners have validated wether or not a specific customer can book a slot, they can proceed with the actual booking using the [POST book a class slot](../openapi/openapi#operation/bookClassSlot) endpoint.

The [DELETE a class booking](../openapi/openapi#operation/cancelClassSlotById/) endpoint is used for cancelling an existing classSlot booking.

The classes collection also offers the [GET class booking by id](../openapi/openapi#operation/getClassBookingById) endpoint which allows partners to sync class booking details including the customerId.

## Cross facility booking of class slots

The   Open API supports cross facility bookings of class slots out of the box. All necessary checks happen on the   side, so partners can simply use the classes collection as is. The main requirements for cross facility class bookings are:

- Partners can only book classes for studios where their developer application is integrated and active
- Classes must be configured to allow booking from customers outside of the respective studio


The envisioned implementation flow is that a partner will use the [GET classes](../openapi/openapi#operation/getActiveClasses) endpoint from studio A to show the available class schedule to a customer from studio B. Partners then validate if the customer can book this class via the validate endpoint and if successful book the class via the book endpoint. Hereby partners need to keep in mind to stay in the correct api-key context, so for validation and booking in studio A, partners need to use the api-key from studio A.

## Stand-In functionality for class slots

Within the   operators can opt to set up a stand-in instructor resource to any class slot. This often happens due to sickness or other reasons which result in an absence of the initially planned instructor resource. The classes collection of the Open API always returns the final set of instructors saved to a class slot, i.e. if instructor A was initially assigned to class slot A but falls out sick and is replaced by instructor B, the class slot dto will only show instructor B as resource.

## Classes collection webhook events

In order to inform partners about necessary changes to classes and class slots, the classes collection offers a variety of webhook events. For class bookings happening in the   itself, we offer the `CLASS_BOOKING_CREATED` event that partners can use to display this booking in their products and services.

Full list of events can be found here: [Event types](../webhooks/event-types)