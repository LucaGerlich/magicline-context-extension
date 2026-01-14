# Working with leads

## Introduction

Use case description of how to use the lead collection:

- Fetching details about mandatory data
- Save lead data


## Relevant Endpoints

- [GET Config of the lead](../openapi/openapi#operation/getLeadConfig)
- [POST Validate for lead creation](../openapi/openapi#operation/validateForLeadCreation)
- [POST Create lead](../openapi/openapi#operation/createLead)


## Lead Creation in  World

The Lead creation process is designed to be dynamic. Instead of hardcoding form fields in your application,
you must first ask the API what information the specific studio requires. This ensures compliance with local regulations
(e.g., mandatory phone numbers in some regions) and studio-specific business rules (e.g., custom marketing questions).

## Step 1: Dynamic Form Configuration

The process begins with the [GET Config of the lead](../openapi/openapi#operation/getLeadConfig) endpoint. This response acts as the blueprint for your frontend form.
It categorizes data requirements into three areas:

- **Standard Attributes**: Basic profile fields (Name, Email, Mobile, etc.).
- **Additional Information**: Custom fields defined by the studio (e.g., "How did you hear about us?").
- **Communication Preferences**: A privacy matrix for marketing consents.


**Field Modes** (`OpenApiV1InputFieldMode`) For both Attributes and Additional Information, the API assigns a mode to
tell you how to render the input:

- `MANDATORY`: The field must be displayed and a value is required.
- `OPTIONAL`: The field should be displayed, but the user can leave it empty.
- (*Implicit* `HIDDEN`): If a field is not returned in the config, it should not be requested.


**Communication Preferences Matrix** The configuration returns a list of available **Categories** (e.g., "Marketing",
"Contract") and the available **Channels** within them (e.g., "Email", "SMS"). Your UI should generate the appropriate
checkboxes to allow the user to opt-in or opt-out per category and channel.

## Step 2: Validation (Optional but Recommended)

Before submitting the final creation request, you can use the [POST Validate for lead creation](../openapi/openapi#operation/validateForLeadCreation) endpoint.

- **Payload**: Identical to the creation endpoint.
- **Purpose**: It performs a "dry run" of the creation logic to check for data integrity (e.g., "Is this email already in use?", "Is the postal code valid?").
- **Response**: Instead of a generic HTTP 400 error, this endpoint returns a structured `validationStatus` containing specific **Validation Codes**.


*Note: Usage of this endpoint is optional. You may choose to skip it and handle validation errors directly from the final creation response if preferred.*

## Step 3: Create Lead

Once the data is collected (and optionally validated), send it to the [POST Create lead](../openapi/openapi#operation/createLead) endpoint. This creates the Lead
entity in the ERP with all the provided attributes, custom answers, and communication preferences.

## Common Integration Challenges

- **Hardcoding Fields**: Avoid assuming which fields are mandatory. Always render your form based on the `OpenApiV1InputFieldMode` returned by the GET Config endpoint.
- **Communication Matrix Structure**: Ensure you send the preferences back in the correct nested structure (Category → Channel → Active Boolean) as defined by the config. For the displaying part you can flatten the view so that a checkmark for marketing means for all channels.