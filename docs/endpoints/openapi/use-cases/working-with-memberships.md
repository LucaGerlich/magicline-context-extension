# Working with memberships collection

## Introduction

The Membership Collection allows partners to manage three distinct use cases in relation to online contract signing:

1. [Sign a new membership for a new member](#sign-a-new-membership-for-a-new-member)
2. [Add a new membership to an existing member](#add-a-new-membership-to-an-existing-member)
3. [Switch a membership for an existing member](#switch-a-membership-for-an-existing-member)


## Sign a new membership for a new member

### Relevant Endpoints

- [GET Membership offers](../openapi/openapi#operation/getMembershipOffers)
- [GET Membership offer details](../openapi/openapi#operation/getMembershipOfferById)
- [POST Create contract preview](../openapi/openapi#operation/postSignupPreview)
- [POST Create membership contract](../openapi/openapi#operation/signupMembership)
- ([POST Create user payment session](../openapi/openapi#operation/userSession))


### Membership Signup in 

The membership signup flow is a multi-stage process that allows partners to retrieve available offers, calculate precise
pricing including discounts and vouchers, and securely handle payments. Unlike simple bookings, this implementation
requires careful orchestration of the Universal Payment Component (UPC) to handle both recurring billing setup and
immediate upfront payments.

Besides the retrieval of offers, the core complexity lies in the **Contract Preview** for accurate pricing and the
**Dual Payment Session** strategy to link recurring and one-time payment methods to a single customer profile.

### Membership offers in 

Membership offers are a central piece to configure offers to attract (new) members. Within the ,
operators can setup a multiple offers with different terms to provide a variety of offers. Also here operators can
configure elements for presentation (Marketing texts and images) as well as accepted payment types and module add-ons.

Besides the presentation and the administrational setup, operator then configure what offers should be available by a
adding it to the active Open API offer configuration as well as the order of them.

### Display, validation and preview

The Membership Signup collection in the Open API follows the following envisioned user flow:

- **Fetching Offers**: The [GET Membership offers](../openapi/openapi#operation/getMembershipOffers) endpoint returns all available membership options configured by the
studio.
- **Offer Details & Modules**: Once an offer is selected, partners use [GET Membership offer details](../openapi/openapi#operation/getMembershipOfferById) to fetch
comprehensive data. This response includes "Modules" (e.g., Drink-Flatrate, Solarium) which are subdivided into three
specific groups:
  - **Included Modules** (`includedModules`): Free services that are automatically part of the offer, regardless of
the contract term selected.
  - **Selectable Modules** (`selectableModules`): Free add-ons from which the customer may choose. This selection is
constrained by the `maximumNumberOfSelectableModules` field (e.g., "Choose 1 of 3").
  - **Optional Modules** (`terms.optionalModules`): Paid add-ons that the customer can choose to add freely. **Note**:
These are nested within specific terms, meaning available optional modules and their prices may vary depending on
the contract duration (term) selected.
- **Member Information Collection**: Partners must gather personal details (name, address, DOB) and contract specifics (
start date).
- **Pricing Authority & Selection**: Before proceeding to payment, the [POST Create contract preview](../openapi/openapi#operation/postSignupPreview) endpoint is
mandatory. You must pass the selected module IDs in this request using `contract.selectedSelectableModuleIds` and
`contract.selectedOptionalModuleIds`. This endpoint acts as the **authoritative source** for the
`dueOnSigningAmount` (exact upfront cost), calculating the total including any paid optional modules, age-based
adjustments, or vouchers.


### Payment Session Orchestration (UPC)

To handle payments, partners must integrate the Universal Payment Component. A critical requirement is the creation of
two distinct payment sessions that are linked to the same customer identity.

1. **Session 1: Recurring Payment `MEMBER_ACCOUNT`)** The first session establishes the payment instrument for future
monthly fees.
  - **Scope**: `MEMBER_ACCOUNT`
  - **Amount**: `0` (Zero)
  - **Result**: Returns a `finionPayCustomerId`. This ID is crucial as it identifies the potential customer within the
payment system before they exist in the ERP.
2. **Session 2: Upfront Payment (ECOM)** If the `dueOnSigningAmount` from the preview is greater than zero, a second
session is required for the immediate charge.
  - **Scope**: `ECOM`
  - **Amount**: Must match the `dueOnSigningAmount` from the preview.
  - **Linking**: You **must** pass the `finionPayCustomerId` returned from Session 1 into this request. This ensures
the upfront payment and recurring token belong to the same entity.
3. **Widget Mounting & Persistence** The UPC widget is mounted using the tokens returned from these sessions. To handle
page reloads or browser navigation without losing payment state, session tokens and the `finionPayCustomerId` should
be stored in `sessionStorage` and restored if the page refreshes.


### Finalizing the Contract

Once the payment widgets successfully process the transactions, they return distinct success tokens. The final step is
to call the [POST Create membership contract](../openapi/openapi#operation/signupMembership) endpoint.

It is vital to map the tokens and selected modules to the correct fields in the payload:

- **Module Selection**: Ensure `contract.selectedSelectableModuleIds` and `contract.selectedOptionalModuleIds` match the
values sent to the Preview endpoint.
- **Recurring Token**: The token from Session 1 (MEMBER_ACCOUNT) must be mapped to `customer.paymentRequestToken`.
- **Upfront Token**: The token from Session 2 (ECOM) must be mapped to `contract.initialPaymentRequestToken`.


### Common Integration Challenges

- **Price Calculation**: Never calculate the upfront amount manually by summing flat fees. Always use the
`preview.paymentPreview.dueOnSigningAmount.amount` from the Preview API.
- **Module Dependencies**: Remember that Optional Modules are linked to specific terms. If a user changes their contract
duration (Term), you must re-check which Optional Modules are available.
- **Amount Formatting**: Payment amounts must always be sent in decimal format (e.g., 19.99), not in cents.
- **Token Distinctness**: Never use the same token for both recurring and upfront fields. Each widget session produces a
unique token that must be routed to its specific field in the final signup request.
- **Reference Text**: The `referenceText` field is mandatory for payment sessions and will appear on the customer's bank
statement.


For payment-related endpoints and concepts, see [Working with Payment API](../usecases/payment-api).

## Add a new membership to an existing member

### Introduction

Use case description of how to add a new contract to an existing customer via the Open API. This flow differs from the
signup process as it leverages existing customer master data, simplifying the payload but maintaining the need for
precise payment orchestration.

### Relevant Endpoints

- [GET Membership offers](../openapi/openapi#operation/getMembershipOffers)
- [GET Membership offer details](../openapi/openapi#operation/getMembershipOfferById)
- [POST Preview information before adding a contract to an existing customer](../openapi/openapi#operation/postMembershipPreview)
- [POST Add a contract to an existing customer](../openapi/openapi#operation/addMembership)
- ([POST Create user payment session](../openapi/openapi#operation/userSession))


### Adding Contracts in 

The flow for adding a contract to an existing customer allows partners to assign new memberships or services to users
who are already registered in the system. Since the customer's personal data (name, address, DOB, etc.) is already
stored, the process focuses purely on the **Contract Configuration** and **Payment Setup**.

The central element of this flow is the `customerId` path variable. You must ensure you have a valid customer ID,
which can be retrieved via the .

### Display, validation and preview

The "Add Contract" flow follows this envisioned user sequence:

- **Fetching Offers**: The [GET Membership offers](../openapi/openapi#operation/getMembershipOffers) endpoint returns all available options.
- **Offer Details & Modules**: Use [GET Membership offer details](../openapi/openapi#operation/getMembershipOfferById) to fetch comprehensive data. This includes the module
configuration, which behaves identically to the signup flow:
  - **Included Modules** (`includedModules`): Always part of the offer.
  - **Selectable Modules** (`selectableModules`): Free add-ons limited by a maximum count.
  - **Optional Modules** (`terms.optionalModules`): Paid add-ons specific to the selected term.
- **Pricing Authority & Preview**: Before finalising,
the [POST Preview information before adding a contract to an existing customer](../openapi/openapi#operation/postMembershipPreview) endpoint is mandatory.
  - **Path Variable**: Requires `{customerId}`.
  - **Payload**: Contains only the contract specifics (start date, offer term ID) and module selections (
`selectedSelectableModuleIds`, `selectedOptionalModuleIds`).
  - **Purpose**: Acts as the authoritative source for the dueOnSigningAmount, calculating costs specific to this
customer (e.g., applying existing loyalty discounts or age-based rules using the stored DOB).


### Payment Session Orchestration (UPC)

Even for existing customers, you must integrate the Universal Payment Component (UPC) if the new contract requires
payment method collection or an upfront fee.

**Critical Difference**: unlike the signup flow, you do **not** use `finionPayCustomerId`. Instead, you link sessions
directly to the existing ERP `customerId`.

1. **Session 1: Recurring Payment (`MEMBER_ACCOUNT`)** Required if the new contract has recurring fees and you need to
capture a new payment method (or verify an existing one).
  - **Scope**: `MEMBER_ACCOUNT`
  - **Amount**: `0` (Zero)
  - **Customer ID**: Pass the existing ERP `{customerId}` in the request body.
2. **Session 2: Upfront Payment (ECOM)** Required if the `dueOnSigningAmount` from the preview is greater than zero.
  - **Scope**: `ECOM`
  - **Amount**: Must match the `dueOnSigningAmount` from the preview.
  - **Customer ID**: Pass the existing ERP `{customerId}` in the request body.
  - **Linkage**: By sending the same `customerId` in both requests, the system automatically links the payment
sessions.
3. **Widget Mounting** Mount the UPC widget using the tokens returned. Since the customer is known, the widget may
pre-fill known data or show existing payment instruments if configured (`showExistingPaymentInstruments: true`).


### Finalising the Contract

Once payment is handled (if applicable), call the [POST Add a contract to an existing customer](../openapi/openapi#operation/addMembership) endpoint.

- **Path Variable**: Ensure the `{customerId}` matches the one used in the preview and payment sessions.
- **Module Selection**: Ensure `contract.selectedSelectableModuleIds` and `contract.selectedOptionalModuleIds` match the
values sent to the Preview.
- **Payment Tokens**:
  - Map the **Recurring Token** (Session 1) to `contract.paymentRequestToken` (if a new method was collected).
  - Map the **Upfront Token** (Session 2) to `contract.initialPaymentRequestToken`.


### Common Integration Challenges

- **Customer ID Validity**: Ensure the `customerId` is valid and the user is active. Calls to the preview or contract
endpoints with an invalid ID will fail.
- **Payload Reduction**: Do not send customer master data (email, address, etc.) in the preview or final contract call.
The system pulls this from the existing record.
- **Module Dependencies**: Just like in signup, ensure that any selected **Optional Modules** are valid for the specific
**Term** chosen in the contract configuration.
- **Price Calculation**: Always rely on the preview endpoint's `dueOnSigningAmount` rather than manual calculation, as
existing customers might have specific attributes (e.g., grandfathered rates or loyalty statuses) that affect pricing.


## Switch a membership for an existing member

### Introduction

Use case description of how to upgrade, downgrade, or change an existing customer's contract via the Open API. Unlike
adding a new contract, this workflow requires validating "Switch Configurations" defined by the operator to determine
which current contracts (`sourceContractId`) are eligible for a switch and to which target offers
(`destinationMembershipOffers`).

### Relevant Endpoints

- [GET All membership switch configurations for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationsForCustomer)
- [GET Membership switch configuration by id for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationForCustomer)
- [POST Preview the membership switch](../openapi/openapi#operation/postMembershipSwitchPreview)
- [POST Perform the membership switch](../openapi/openapi#operation/switchMembership)


### Membership Switching in 

The switching process is strictly governed by studio-side configurations. Operators define specific paths (e.g.,
"Gold Member" can switch to "Platinum", but "Basic" cannot switch to "Corporate"). Therefore, the API does not simply
list all offers; it lists valid **Switch Configurations** for a specific customer.

The flow relies on three specific identifiers:

1. `sourceContractId`: The ID of the customer's *current* contract being replaced.
2. `configId`: The ID of the allowed switch path (e.g., "Upgrade to Platinum").
3. `membershipOfferTermId`: The ID of the specific *new* term selected from the destination offer.


### Display, validation and preview

The switch flow follows this specific sequence:

- **Step 1: Check Eligibility**: Call [GET All membership switch configurations for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationsForCustomer).
  - This returns a list of available switch paths.
  - Each config contains a `sourceContracts` array. You must match these IDs against the customer's active contracts
to show the user which of their contracts can be switched.
  - *Note*: If this endpoint returns an empty list, the customer is not eligible for any switches.
- **Step 2: Fetch Destination Offers**: Call [GET Membership switch configuration by id for a customer](../openapi/openapi#operation/getMembershipSwitchConfigurationForCustomer).
  - This returns the `destinationMembershipOffers` (the new offers available for this specific switch).
  - It also returns `presentation` data (banner text, image URLs) which should be displayed to the user to market the
upgrade.
  - **Modules**: The destination offers contain the same module structure (`includedModules`, `selectableModules`,
`terms.optionalModules`) as standard offers.
- **Step 3: Preview**: Before confirming, call [POST Preview the membership switch](../openapi/openapi#operation/postMembershipSwitchPreview).
  - **Payload**: Requires `configId`, `sourceContractId`, `membershipOfferTermId`, `startDate`, and any module
selections.
  - **Purpose**: Calculates the pro-rated cost or upgrade fees. The `paymentPreview.dueOnSigningAmount` is the
authoritative source for any immediate payment required to finalize the switch.


### Payment Session Orchestration (UPC)

A membership switch often requires an immediate payment (e.g., an upgrade fee or the difference in pro-rated contract
value).

1. **Determine Necessity** Check the `paymentPreview.dueOnSigningAmount` from the preview endpoint.
  - If `0`: No payment session is required.
  - If `> 0`: An **ECOM** payment session is required.
2. **Create Session (ECOM)**
  - **Scope**: `ECOM`
  - **Amount**: Must match the `dueOnSigningAmount`.
  - **Customer ID**: Pass the existing ERP `{customerId}`.
  - **Reference**: "Membership Switch Fee" (or similar).


*Note: Unlike the Signup flow, the Switch API spec primarily focuses on initialPaymentRequestToken for immediate costs.
The recurring payment method usually remains attached to the customer account, or is handled via the existing payment
instrument.*

### Performing the Switch

Once the preview is accepted and payment (if any) is authorized, call [POST Perform the membership switch](../openapi/openapi#operation/switchMembership).

- **Payload Mapping**:
  - `configId`: From the selected configuration.
  - `sourceContractId`: The contract being replaced.
  - `membershipOfferTermId`: The new term selected.
  - `initialPaymentRequestToken`: The token from the ECOM payment session (if a payment was made).
  - `selectedSelectableModuleIds` / `selectedOptionalModuleIds`: Must match the preview.


### Common Integration Challenges

- **Source Contract Selection**: A customer might have multiple active contracts. You must ensure the user selects the
correct `sourceContractId` that corresponds to the `sourceContracts` list returned in the configuration.
- **Immediate vs. Recurring**: The `initialPaymentRequestToken` is strictly for the *immediate* amount due (setup fees,
pro-rata difference). It does not automatically replace the recurring payment method for the *new* contract unless the
studio configuration dictates otherwise.
- **Presentation Data**: Use the `presentation.imageUrl` and `presentation.bannerText` provided in the config response
to ensure the upgrade path is presented exactly as the marketing team intended.
- **Module Logic**: Just like new contracts, verify that selected **Optional Modules** are valid for the chosen **Term
**.