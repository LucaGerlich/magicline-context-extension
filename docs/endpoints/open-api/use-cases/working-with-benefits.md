# Working with benefits

## Intro

Use case description of how to use benefits via the   Open API.

## Relevant Endpoints

- [GET customer's benefits](../openapi/openapi#operation/getBenefits)
- [GET customer's benefits by card number](../openapi/openapi#operation/getBenefitsByCardNumber)
- [POST customer's benefit usage](../openapi/openapi#operation/useBenefit)
- [POST save weighing results](../openapi/openapi#operation/createCustomerWeighing)


## Benefits in the   World

Benefits are a common element in the   software that enable studio operators to grant their customers access
to certain services within their clubs (i.e. Sauna or Peronal Training). In the context of the   integration,
we offer partners the option to integrate their partner specific benefits in the   upon activation.
This allows operators to work with partner benefits to configure which customers are eligible and offers a
diverse set of configuration to drive upsells based on partner benefits.

Partner benefits are configurable in the partner integration detail view

## Validating customer benefits

To allow easy handling of your benefits via the Open API we offer a set of generic endpoints
that inform you about a customers eligibility regarding your benefits.

You can choose between:

- [GET customer's benefits](../openapi/openapi#operation/getBenefits) - here you can pass the customerId to gather which of your benefits (identified by their `BENEFIT_KEY`) a customer can use
- [GET customer's benefits by card number](../openapi/openapi#operation/getBenefitsByCardNumber) - here you can pass a customers cardNumber to gather which of your benefits (identified by their `BENEFIT_KEY`) a customer can use


## Posting benefit usage

Once you have validated a customers eligibility to use your benefit,
it is crucially important to post the usage of your benefit back to the   using the 'Post customer's benefit usage endpoint'.

[POST customer's benefit usage](../openapi/openapi#operation/useBenefit)

This ensures that the   remains the single source of truth regarding contingents of your benefits
that can be configured in the   and that upsell mechanisms work as intended.

br
**Exception:** if you are a body measurement partner and post weighing results back to the  .
You can opt to choose between the 'Post customer's benefit usage endpoint' or you can simply pass along your benefit key
when posting the measurement results via the 'Save weighing results endpoint'.

[POST save weighing results](../openapi/openapi#operation/createCustomerWeighing)

## Cross-facility benefit usage for partner benefits

To handle situations where your partner integration may be activated in multiple studios of the same tenant,
the Open API has a built-in cross facility usage function. This functionality enables customers to use partner benefits in related studios
of the same tenant where the same partner integration is activated.

br
In this use case, we assume two studios of the same tenant (Studio A and Studio B ) and a customer with their data set in Studio A.
Both Studios have the same partner integration activated which has the cross facility partner benefit.
Customer A has an additional module attached to her contract which allows her to use the benefit 5 times per month.

br
If the customer A tries to use this benefit in Studio B,
  will check the inclusive contingent in Studio A and if the customer uses the benefit in Studio B,
will reduce the inclusive contingent in Studio A.