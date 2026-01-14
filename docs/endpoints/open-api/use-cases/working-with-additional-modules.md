# Working with additional modules

## Intro

Use case description of how additional modules work in the   and how partners can use the additional modules endpoints to drive upsell in their products.

## Relevant Endpoints

- [GET additional modules](../openapi/openapi#operation/getAdditionalModules)
- [GET purchasable additional modules](../openapi/openapi#operation/getPurchasableAdditionalModules)
- [POST validate an additional module contract request](../openapi/openapi#operation/validateAdditionalModuleContractRequest)
- [POST purchase an additional module contract](../openapi/openapi#operation/purchaseAdditionalModuleContract)
- [GET an additional module contract](../openapi/openapi#operation/getAdditionalModuleContract)
- [POST create additional module contract cancelation amendment](../openapi/openapi#operation/createModuleContractCancelationAmendment)
- [POST Withdraw cancelation of the additional module contract](../openapi/openapi#operation/withdrawAdditionalModuleContractCancelation)


## Additional modules and additional module contracts in the 

Customers main contracts can be extended with additional module contracts that contains specific services and can be configured independently from the main contract. The additional module contracts are based on additional modules. A common example is an additional service like a towel flat-rate or a sauna service. These are configured in the   as additional modules which can be booked to the existing main contract of a customer (by creating a new additional module contract) and usually incur a recurring monthly fee to a customers account.

In the context of the Open API this can also be specific to a partner integration benefit (if applicable) which is offered as an upsell additional module and linked via an additional module contract to a customers contract. There is no limitation on the amount of additional module contracts that can be attached to a customers contract.

The following configuration requirements in the   must be met for additional modules to be visible and retrievable via the Open API:

- Additional module must be set to active as a status
- Additional module must be available for online booking
- Additional module must set a term configuration
- Additional module must set a payment method


Example of an additional module configuration in the  :

Further information and an example implementation in our MySports ecosystem can be found here: [How to make additional modules bookable via MySports Web & App ](https://support.magicline.com/hc/en-001/articles/22822269261713-How-to-make-additional-modules-bookable-via-MySports-Web-App#h_01HQB1RR5XSBEFMN397BZF2YB9)

## Display, validation and booking of additional modules

Booking of additional module via the Open API follows the following envisioned user flow:

- the [GET additional modules](../openapi/openapi#operation/getAdditionalModules/) endpoint delivers all additional modules that a studio operator has configured for online booking for a respective studio
- passing the parameter `contractId` to the [GET purchasable additional modules](../openapi/openapi#operation/getPurchasableAdditionalModules/) endpoint retrieves the available additional modules that can be purchased for this contract and thus the respective customer. From this overview the customer can select a desired additional module
- to enable partners to optimize their UI and avoid showing additional modules as bookable which in fact are not, the [POST Validate an additional module contract request](../openapi/openapi#operation/validateAdditionalModuleContractRequest/) contract request allows partners to make sure an additional module can in fact be purchased for a specific `contractId` and `additionalModuleId`
- the actual purchase of an additional module to a customers contract is done via the [POST purchase an additional module contract](../openapi/openapi#operation/purchaseAdditionalModuleContract). During the process of adding an additional module to a customers contract, the additional module is transformed into an additional module contract.
- the additional module contracts can be selected individually via the [GET an additional module contract](../openapi/openapi#operation/getAdditionalModuleContract) endpoint which utilizes the `additionalModuleContractId` as its identifier
- customers can opt to cancel an additional module via the [POST create additional module contract cancelation amendment](../openapi/openapi#operation/createModuleContractCancelationAmendment) endpoint which, after adhering to the cancelation configurations for that particular additional module contract, creates a cancelation amendment for the additional module contract. This can be revoked via the [POST Withdraw cancelation of the additional module contract](../openapi/openapi#operation/withdrawAdditionalModuleContractCancelation) endpoint, which will create an contact withdrawal amendment. It is possible to setup a direct cancelation or withdrawal, where no amendment is created, by setting the belonging config within the partner benefit config:


Additional module contract configuration on the partner integration detail view:

## Additional module contract webhook events

The additional module collection uses the existing contract events, as the additional module contacts are always attached to an existing main contract of a customer. Once additional module contracts are added, edited or removed a `CONTRACT_UPDATE` event will be thrown containing the `contractId` of the respective customers main contract.

Full list of events can be found here: [Event types](../webhooks/event-types/)