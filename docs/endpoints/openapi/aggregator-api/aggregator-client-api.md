# Aggregator Client API

[//]: # (The content of this file is used as the descrption of the API)



## Security

### ApiKeyAuth

Validate apiKey header value with one you received from our team during integration setup.


Type: apiKey
In: header
Name: X-API-KEY

## Download OpenAPI description

[Aggregator Client API](https://redocly.sportalliance.com/_spec/apis/magicline/aggregator/aggregator-client.yaml)

## Other

### Member validation

 - [POST /member-validation](https://redocly.sportalliance.com/apis/magicline/aggregator/aggregator-client/other/membervalidation.md)

### Checkin validation

 - [POST /checkin-validation](https://redocly.sportalliance.com/apis/magicline/aggregator/aggregator-client/other/checkinvalidation.md)


# Member validation

Endpoint: POST /member-validation
Security: ApiKeyAuth

## Request fields (application/json):

  - `aggregatorId` (string, required)
    Aggregator id
    Example: "8213712939218"

## Response 200 fields (application/json):

  - `aggregatorId` (string, required)
    Aggregator id
    Example: "8213712939218"

  - `firstName` (string, required)
    First name of the customer
    Example: "Edgar"

  - `lastName` (string, required)
    Surname of the customer
    Example: "Bullock"

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
    Example: "89"

  - `zipCode` (string)
    Zip code of the customer
    Example: "12133"

  - `city` (string)
    City of the customer
    Example: "Angermünde"

  - `country` (string)
    Country of the customer
    Example: "DE"

  - `phonePrivate` (string)
    Private phone number of the customer
    Example: "+4930901820"

  - `phonePrivateMobile` (string)
    Private mobile phone number of the customer
    Example: "+4915223433333"

  - `phoneBusiness` (string)
    Business phone number of the customer
    Example: "+4930901820"

  - `phoneBusinessMobile` (string)
    Business mobile phone number of the customer
    Example: "+4915223433333"

# Checkin validation

Endpoint: POST /checkin-validation
Security: ApiKeyAuth

## Request fields (application/json):

  - `aggregatorId` (string, required)
    Aggregator id
    Example: "8213712939218"

  - `customerId` (integer, required)
    Unique ID of the Magicline customer
    Example: 20322323
