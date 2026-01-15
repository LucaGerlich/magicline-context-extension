# Time zone changes

## Overview

We will change the format for date and time fields in the near future. All clients that use `/connect/v1/trialsession`
to book trial sessions are forced to change their implementation to reflect those upcoming changes. Please find all
details regarding the necessary changes on this page.

**The here described changes are backwards-compatible. We encourage you to change your implementation immediately to be
safe once the format for date and time has been changed.**

Currently we return date and time of slots in the following format: `2021-08-23T09:00:00.000Z`
Date and time of slots are returned in UTC. The browser will then convert to the local time zone of the user. Selected
slots are sent in the same format back to the API.

In the near future we will return date and time with the correct time zone in a new format:
`2021-08-23T11:00:00.000+02:00[Europe/Berlin]`
Date and time can be displayed directly and no longer have to be converted. Use the same format to send the selected
slot back to the API.

A code snippet on how to handle both formats in a backwards-compatible way can be found below, which is also used in
this demo application.
The demo tenant [connectdemo](https://connectdemo.api.magicline.com/connect/) already switched to the new format and can
be used to test your own solution.

## Code snippet

Makes use of [Moment.js](https://momentjs.com/)


```javascript
function formatDate(dateString) {
    if (dateString.endsWith(']')) {
        // upcoming format: date and time string is in correct time zone and needs just to be formatted to present it
        // time zone information will be just removed before
        const dateWithOutTimeZone = dateString.replace(/\[.*\]/, '');
        return moment.parseZone(dateWithOutTimeZone).format('YYYY-MM-DD HH:mm');
    } else {
        // deprecated format: date and time string is in UTC and needs to be converted into the time zone of the browser
        const clientsTimeZone = moment.tz.guess();
        return moment(dateString).tz(clientsTimeZone).format('YYYY-MM-DD HH:mm')
    }
}
```

## Difference from old to new format

### Old format


```
GET https://connectdemo.api.magicline.com/connect/v1/trialsession?startDate=2021-08-23&endDate=2021-08-29&studioId=1210007620`
    {
      "name": "Probetraining",
      "description": "Probetraining in unserem Studio!",
      "bookingWithoutResourcesAllowed": false,
      "slots": [
        {
          "startDateTime": "2021-08-26T08:00:00.000Z",
          "endDateTime": "2021-08-26T09:00:00.000Z"
        },
        {
          "startDateTime": "2021-08-26T09:00:00.000Z",
          "endDateTime": "2021-08-26T10:00:00.000Z"
        },
        ....
      ]
    }


`POST https://connectdemo.api.magicline.com/connect/v1/trialsession/book`
    {
     {
      "leadCustomer": {
        "address": {
          "city": "",
          "houseNumber": "",
          "country": "DE",
          "street": "",
          "zip": ""
        },
        "dateOfBirth": "2000-01-01",
        "email": "",
        "firstname": "John",
        "gender": "MALE",
        "lastname": "Smith",
        "secondLastname": "",
        "phone": ""
      },
      "startDateTime": "2021-08-26T08:00:00.000Z",
      "studioId": 1210007620,
      "note": "",
      "referrerId": null,
      "trainerRequired": true,
      "sourceCampaignId": ""
    }
```

### New format


```
GET https://connectdemo.api.magicline.com/connect/v1/trialsession?startDate=2021-08-23&endDate=2021-08-29&studioId=1210007620`
    {
      "name": "Probetraining",
      "description": "Probetraining in unserem Studio!",
      "bookingWithoutResourcesAllowed": false,
      "slots": [
        {
          "startDateTime": "2021-08-26T10:00:00.000+02:00[Europe/Berlin]",
          "endDateTime": "2021-08-26T11:00:00.000+02:00[Europe/Berlin]"
        },
        {
          "startDateTime": "2021-08-26T11:00:00.000+02:00[Europe/Berlin]",
          "endDateTime": "2021-08-26T12:00:00.000+02:00[Europe/Berlin]"
        },
        ....
      ]
    }

`POST https://connectdemo.api.magicline.com/connect/v1/trialsession/book`
    {
     {
      "leadCustomer": {
        "address": {
          "city": "",
          "houseNumber": "",
          "country": "DE",
          "street": "",
          "zip": ""
        },
        "dateOfBirth": "2000-01-01",
        "email": "",
        "firstname": "John",
        "gender": "MALE",
        "lastname": "Smith",
        "secondLastname": "",
        "phone": ""
      },
      "startDateTime": "2021-08-26T10:00:00.000+02:00[Europe/Berlin]",
      "studioId": 1210007620,
      "note": "",
      "referrerId": null,
      "trainerRequired": true,
      "sourceCampaignId": ""
    }
```