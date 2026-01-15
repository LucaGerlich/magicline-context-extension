# Device API


## Servers

Demo tenant
```
https://open-api-demo.devices.magicline.com
```

## Security

### ApiKeyAuth

Bearer token which you received by calling [activate](../../openapi/openapi/devices#activateDevice)

Type: http
Scheme: bearer
Bearer Format: oauth2

## Download OpenAPI description

[Device API](https://redocly.sportalliance.com/_spec/apis/magicline/deviceapi/deviceapi.yaml)

## Access

Here are all the endpoints that are necessary for `GenericCardReader` to be successfully used. This endpoints should be used for device with model `GENERIC_CARD_READER`. The model can be found in response from `getDevices` which was already described in authentication process.

### Checks if customer is authorized (dry-run possible)

 - [POST /open-api/device/cardreader/identification](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/access/cardreaderidentification.md): You can find more information about identification here.

## Vending

Here are all the endpoints that are necessary for `GenericVending` to be successfully used. This endpoints should be used for device with model `GENERIC_VENDING_READER`. The model can be found in response from `getDevices` which was already described in authentication process.

### Checks if customer is authorized to use vending device

 - [POST /open-api/device/vending/identification](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/vending/vendingidentification.md): You can find more information about identification here.

### Product sale (dry-run possible)

 - [POST /open-api/device/vending/sale](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/vending/vendingsale.md): This should be conducted post-identification with  in order to execute a dry-run, ensuring that customers can obtain the product, for example has enough credit, etc. If this first request was successful, the product can be dispensed. After the product was sucessfully dispensed, this endpoint needs to be called again with , which will subsequently lead to the customer being charged. You can find more information about sale here

### Top up customer's consumption credit

 - [POST /open-api/device/vending/revalue](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/vending/vendingrevalue.md): This should be used to top up customer's consumption credit.

## Time

### Get available intervals with prices

 - [GET /open-api/device/time/price](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/time/timeprice.md): Returns a list of available time intervals with their corresponding prices. This allows the device to display the options to the customer.

### Checks if customer is authorized to use time device

 - [POST /open-api/device/time/identification](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/time/timeidentification.md): You can find more information about identification here.

### Benefit usage (dry-run possible)

 - [POST /open-api/device/time/usage](https://redocly.sportalliance.com/apis/magicline/deviceapi/deviceapi/time/timeusage.md): This should be conducted post-identification with  in order to execute a dry-run, ensuring that customers can obtain the benefit, for example has contingent, etc. If this first request was successful, the benefit can be enabled. After the benefit was successfully enabled, this endpoint needs to be called again with , which will subsequently lead to the customer being charged or benefit being used. You can find more information about usage here

