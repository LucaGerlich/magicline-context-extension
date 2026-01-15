# Working with tax advisor accounting data

## Intro

How to use the tax advisor accounting data export via the  Open API.

## Relevant Endpoints

- [POST create export](../openapi/openapi#operation/createExport)
- [GET get export](../openapi/openapi#operation/getExport)


## Tax advisor accounting data export

The  offers an integrated bookkeeping system which automatically creates accounting data for every transactions processed within the system.
With this export have the opportunity to automate your bookkeeping processes by consuming the accounting data export via the Open API.
You can request the data for a facility for any given time period with a maximum range of 90 days per API call.
The  will return an accounting data export in three different formats that contains all information necessary for importing it into your bookkeeping system.

## Retrieving tax advisor accounting data

The accounting data export can only be used for individual facility.

The following requests can be submitted:

- [POST create Export](../openapi/openapi#operation/createExport) - will create the accounting data export for a facility.
- [GET get Export](../openapi/openapi#operation/getExport) - will allow you to download the created accounting data export.


You can export a maximum of 90 days of accounting data per request. As the accounting data is provided on a daily basis,
the maximum date of any export is the export request date minus 1 day.

The POST triggers the export creation via an asynchronous process.
You will receive the webhook event `TAX_ADVISOR_EXPORT_CREATED` via the provided webhook URL.
The webhook event notifies you that a requested export is ready to download.
By calling the GET endpoint with the provided export id, you can retrieve the export file.