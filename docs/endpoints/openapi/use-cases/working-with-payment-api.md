# Working with Payment API

## Introduction

This documentation describes how to integrate with a unified and secure payment system for initiating payments or tokenizing payment instruments. The approach follows a two-step flow:

1. **Obtain a concludable payment request token** â€“ This token represents either an authorized payment (ready for capture) or an authorized payment instrument for future use. To obtain it, the frontend mounts the Universal Payment Component (UPC) using a short-lived user payment session token securely obtained from the backend.
2. **Post a usage with the obtained payment request token** â€“ The token can be used to create a payment instrument in the customer account, attach it to a contract, or post a usage (e.g., credit top-up, ticket purchase). If the usage involves an amount greater than zero, capture is deferred until the related good or service is booked, minimizing refunds. If unused within its validity period, the authorization is cancelled or refunded.


### Key Concepts

- **Universal Payment Component (UPC)** â€“ Embeddable JavaScript component handling the authorization of a payment request token.
- **Universal Payment Gateway (UPG)** â€“ Public API the UPC communicates with, authorized via a short-lived session token.
- **Payment Instrument** â€“ A user-specific object used to attempt a payment.
- **Payment Method** â€“ The type of payment instrument (e.g., credit card, direct debit, PayPal).
- **Scope** â€“ Defines the payment context (`MEMBER_ACCOUNT` or `ECOM`) to determine available payment methods.


## Important Usage Notes

- Always define **either** `finionPayCustomerId` **or** `customerId` for an existing customer session. When assigning a `paymentRequestToken` to a usage, the system checks that the token belongs to the correct customer. If this check fails, the operation will not succeed.
- **Example:** Selling a contract online and collecting a payment method for the upfront fee requires two `paymentRequestTokens` â€” one for the payment instrument and one for the actual upfront payment. This means creating two separate user payment sessions. If the flow is for a new customer, create the second session using the `finionPayCustomerId` returned by the first.
- While the `paymentRequestToken` is unused for posting a usage, **no funds are captured** (if the payment method allows). Authorizing a token with `amount > 0` only authorizes the payment; capture happens when posting the usage. This prevents unnecessary collections or refunds in case of process errors or user cancellation.
- **Saving payment methods:** If the scope is `ECOM` and the payment method supports saving, the user can choose to store the method for future use.
- **Authorizing saved payment methods:** Stored payment methods are already authorized, so they are not re-authorized when selected via the component. The payment result is returned upon posting the usage.
- Any unused `paymentRequestToken` is automatically cancelled when the related user payment session expires.
- A user payment session is automatically invalidated once one `paymentRequestToken` from that session is used â€” only one token per session can be used.


## Endpoints Using paymentRequestToken

The `paymentRequestToken` returned by the UPC can be used in the following scenarios:

### Creating a Payment Instrument in the Customer

- Create a payment instrument and link it to the customer so it can be used in future payment runs (e.g., membership fees).
- Applies to:
  - Creating a new customer and contract *(work in progress)*
  - Adding a contract to an existing customer *(work in progress)*
  - Offering self-service payment method updates *(work in progress)*
  - Adding a secondary payment method *(planned)*


### Posting a Sellable Entity

If the `paymentRequestToken` is authorized with a payment amount, it can be used for purchasing any sellable entity:

- Upfront payment in contract creation (joining fee or total contract value) *(work in progress)*
- Account balancing for open fees *(work in progress)*
- Purchasing a day ticket *(work in progress)*
- Purchasing a value voucher *(planned)*
- Purchasing a contract voucher *(planned)*
- Purchasing a course contingent *(planned)*
- Purchasing an appointment (e.g., personal training contingent) *(planned)*


## Creating a User Payment Session

To initiate a payment process or capture a payment instrument, you must first create a user payment session.

**Endpoint:** [POST /v1/payments/user-session](/apis/magicline/openapi/openapi#operation/userSession)

**Required Scope:** `PAYMENT_WRITE`

**Description:** This request generates a short-lived token used by the UPC to authenticate payment flows. It can be for immediate transactions or for storing payment instruments for future recurring payments.

### Request Body Parameters

### Example Request

### Response body

The `token` returned is the `userSessionToken` required to initialize the UPC in your frontend integration.

## Payment Widget Integration Guide

An embeddable payment interface that can be integrated into any web application.

The following URIs are available:

- [https://widget.dev.payment.sportalliance.com/widget.js](https://widget.dev.payment.sportalliance.com/widget.js) - Preview version
- [https://widget.payment.sportalliance.com/widget.js](https://widget.payment.sportalliance.com/widget.js) - Stable version


### Quick Start


```html
<script src="INSERT_WIDGET_URI_HERE"></script>
<div id="payment-widget"></div>

<script>
    const widget = window.paymentWidget.init({
        userSessionToken: 'your-session-token',
        environment: 'live',
        countryCode: 'US',
        locale: 'en',
        container: 'payment-widget'
    });

    // Clean up when done
    widget.destroy();
</script>
```

### Configuration

| Parameter | Type | Description |
|  --- | --- | --- |
| `userSessionToken` | `string` | User session token |
| `environment` | `'test' | 'sandbox' | 'live'` | Payment environment |
| `countryCode` | `string` | ISO country code (e.g., 'US') |
| `locale` | `string` | Locale (e.g., 'en') |
| `container` | `string | HTMLElement` | Element ID or element reference |


**Optional:**

- `styling` - Custom theme colors and styling
- `i18n` - Translation overrides
- `featureFlags` - Enable experimental or alternative features
- `onSuccess` - Success callback function that receives the payment request token, payment instrument details, and payment instrument token
- `devMode` - Show i18n keys instead of translated text (development only)
- `hidePaymentButton` - Hide widget's internal payment buttons for custom button control
- `onPaymentStateChange` - Callback for payment button state changes (processing, canSubmit)
- `customerData` - Pre-fill payment forms with customer information (name, email, address)


### Customization

The payment widget supports two levels of styling customization:

1. **Widget Styling** - Basic widget appearance (colors, borders, shadows)
2. **Payment Provider Styling** - Advanced styling for Stripe and Adyen payment forms


#### 1. Widget Styling

Customize the widget's appearance through basic styling properties:


```javascript
styling: {
    primaryColor: '#007bff',
    secondaryColor: '#6c757d',
    textColorMain: '#333333',
    textColorSecondary: '#6c757d',
    borderColor: '#dee2e6',
    borderRadius: '4px',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
}
```

**Available styling options:**

- `primaryColor` - Primary color for buttons, links, and key UI elements
- `secondaryColor` - Secondary color for less prominent UI elements
- `textColorMain` - Main text color for headings and primary content
- `textColorSecondary` - Secondary text color for descriptions and muted content
- `borderColor` - Border color for inputs, containers, and dividers
- `borderRadius` - Border radius for rounded corners (e.g., '4px', '8px')
- `boxShadow` - Box shadow for depth and elevation effects


#### 2. Payment Provider Styling

For advanced styling of payment forms, you can customize the appearance of Stripe and Adyen payment elements directly through their respective APIs.

##### Stripe Appearance API

Stripe Elements can be customized using the [Appearance API](https://docs.stripe.com/elements/appearance-api). Configure the appearance object in your styling options:


```javascript
styling: {
    primaryColor: '#007bff',
    stripe: {
        appearance: {
            theme: 'stripe',
            variables: {
                colorPrimary: '#0570de',
                colorBackground: '#ffffff',
                colorText: '#30313d',
                colorDanger: '#df1b41',
                fontFamily: 'Ideal Sans, system-ui, sans-serif',
                spacingUnit: '4px',
                borderRadius: '4px'
            },
            rules: {
                '.Input': {
                    border: '1px solid #e6e6e6',
                    boxShadow: 'none'
                },
                '.Input:focus': {
                    border: '1px solid #0570de'
                }
            }
        }
    }
}
```

##### Adyen CSS Variables

Adyen Drop-in can be styled using [CSS variable overrides](https://github.com/Adyen/adyen-web?tab=readme-ov-file#styling). Add custom CSS to your page:


```css
:root {
    --adyen-checkout-primary-color: #007bff;
    --adyen-checkout-primary-color-hover: #0056b3;
    --adyen-checkout-background-color: #ffffff;
    --adyen-checkout-text-color: #333333;
    --adyen-checkout-border-color: #e6e6e6;
    --adyen-checkout-border-radius: 4px;
    --adyen-checkout-input-background-color: #ffffff;
    --adyen-checkout-input-border-color: #d9d9d9;
    --adyen-checkout-input-focus-border-color: #007bff;
    --adyen-checkout-error-color: #d32f2f;
    ...
}
```

#### Translations


```javascript
i18n: {
    'upc.my.payment.instruments': 'My Payment Methods',
    'upc.payment.methods.add.new': 'Add New Payment Method'
}
```

#### Feature Flags

Enable experimental or alternative features:


```javascript
featureFlags: {
    useRubiksUI: true; // Enable Rubiks Styleguide components (default: false)
}
```

The `useRubiksUI` flag switches the payment forms to use the Rubiks design system instead of the default Tailwind-based UI. This provides a more modern and consistent look aligned with the Rubiks component library.

#### Development Mode

Enable development mode to display i18n keys instead of translated text:


```javascript
devMode: true; // Shows i18n keys instead of translations for development
```

#### Success Callback

Handle successful payment completion:


```javascript
onSuccess: (
    paymentRequestToken,
    paymentInstrumentDetails,
    paymentInstrumentToken
) => {
    // paymentRequestToken: string - The payment request token
    // paymentInstrumentDetails: object - Payment instrument details (card info, bank details, etc.)
    // paymentInstrumentToken: string - The payment instrument token for future use
};
```

### Integration Examples

#### React Integration


```tsx
import React, { useEffect, useRef } from 'react';

export const PaymentWidget = ({ userToken, onPaymentSuccess }) => {
    const containerRef = useRef(null);
    const widgetRef = useRef(null);

    useEffect(() => {
        if (containerRef.current && window.paymentWidget) {
            widgetRef.current = window.paymentWidget.init({
                userSessionToken: userToken,
                environment: 'live',
                countryCode: 'US',
                locale: 'en',
                container: containerRef.current,
                featureFlags: {
                    useRubiksUI: true
                },
                onSuccess: (token, details, instrumentToken) => {
                    onPaymentSuccess(token, details, instrumentToken);
                }
            });
        }

        return () => widgetRef.current?.destroy();
    }, [userToken, onPaymentSuccess]);

    return <div ref={containerRef} />;
};
```

#### Angular Integration


```typescript
import { Component, ElementRef, ViewChild, OnDestroy } from '@angular/core';

@Component({
    selector: 'app-payment-widget',
    template: '<div #paymentContainer></div>'
})
export class PaymentWidgetComponent implements OnDestroy {
    @ViewChild('paymentContainer', { static: true }) containerRef!: ElementRef;
    private widget: any;

    ngAfterViewInit() {
        const sessionToken =
            sessionStorage.getItem('paymentSessionToken') ||
            this.getUserToken();
        sessionStorage.setItem('paymentSessionToken', sessionToken);

        this.widget = window.paymentWidget.init({
            userSessionToken: sessionToken,
            environment: 'live',
            countryCode: 'US',
            locale: 'en',
            container: this.containerRef.nativeElement,
            onSuccess: (
                token,
                paymentInstrumentDetails,
                paymentInstrumentToken
            ) => {
                sessionStorage.removeItem('paymentSessionToken');
                this.handlePaymentSuccess(
                    token,
                    paymentInstrumentDetails,
                    paymentInstrumentToken
                );
            }
        });
    }

    ngOnDestroy() {
        this.widget?.destroy();
    }
}
```

#### Vue.js Integration


```vue
<template>
    <div ref="paymentContainer"></div>
</template>

<script>
export default {
    name: 'PaymentWidget',
    props: ['userToken'],
    mounted() {
        const sessionToken =
            sessionStorage.getItem('paymentSessionToken') || this.userToken;
        sessionStorage.setItem('paymentSessionToken', sessionToken);

        this.widget = window.paymentWidget.init({
            userSessionToken: sessionToken,
            environment: 'live',
            countryCode: 'US',
            locale: 'en',
            container: this.$refs.paymentContainer,
            onSuccess: (
                token,
                paymentInstrumentDetails,
                paymentInstrumentToken
            ) => {
                sessionStorage.removeItem('paymentSessionToken');
                this.$emit('paymentSuccess', {
                    token,
                    paymentInstrumentDetails,
                    paymentInstrumentToken
                });
            }
        });
    },
    beforeUnmount() {
        this.widget?.destroy();
    }
};
</script>
```

### Custom Payment Button Control

The widget supports hiding its internal payment buttons, allowing host applications to use custom buttons while maintaining full control over styling and placement.

**Multiple Widget Instances**: The widget fully supports mounting multiple instances on the same page. Each instance maintains its own isolated state and API reference.


```javascript
// Example: Multiple widget instances on the same page
const widget1 = window.paymentWidget.init({
    userSessionToken: 'token-1',
    container: 'payment-widget-1'
    // ... other config
});

const widget2 = window.paymentWidget.init({
    userSessionToken: 'token-2',
    container: 'payment-widget-2'
    // ... other config
});

// Each widget operates independently
await widget1.submitPayment(); // Only affects widget1
const state2 = widget2.getPaymentState(); // Only returns widget2 state
```

#### Basic Usage


```javascript
const widget = window.paymentWidget.init({
    userSessionToken: 'user-session-token',
    environment: 'live',
    countryCode: 'US',
    locale: 'en',
    container: 'payment-widget',
    hidePaymentButton: true,
    onPaymentStateChange: (state) => {
        // Update custom button based on payment state
        const button = document.getElementById('custom-pay-button');
        button.disabled = !state.canSubmit;
        button.textContent = state.isProcessing ? 'Processing...' : 'Pay Now';
    }
});

// Custom button handler
document
    .getElementById('custom-pay-button')
    .addEventListener('click', async () => {
        try {
            await widget.submitPayment();
        } catch (error) {
            console.error('Payment failed:', error);
        }
    });
```

#### Widget API Methods

When you initialize the widget, it returns an instance with the following methods:


```typescript
interface PaymentWidgetInstance {
    destroy(): void; // Clean up widget
    submitPayment(): Promise<void>; // Trigger payment submission
    getPaymentState(): PaymentButtonState; // Get current payment state
    updateCustomerData(data: CustomerData): void; // Update customer data dynamically
}

interface PaymentButtonState {
    isProcessing: boolean; // Payment is being processed
    canSubmit: boolean; // Payment can be submitted (see Payment Method Behavior below)
}

interface CustomerData {
    name?: string;
    email?: string;
    address?: CustomerAddress;
}

interface CustomerAddress {
    line1?: string;
    line2?: string;
    city?: string;
    postalCode?: string;
    state?: string;
    country?: string;
}
```

#### Payment Method Behavior

The `canSubmit` state varies by payment method when using custom buttons:

**Provider-based payments (Stripe/Adyen - Credit Card, PayPal, etc.)**:

- `canSubmit` becomes `true` immediately when the payment provider loads
- The provider's internal validation will handle form completeness during submission


**Form-based payments (SEPA, CH_DD, LSV Direct Debit)**:

- `canSubmit` starts as `false`
- Becomes `true` only when required checkboxes are checked
- Ensures mandate acceptance before allowing submission



```typescript
// Example: Handling different payment methods
onPaymentStateChange: (state) => {
    // For SEPA: Button disabled until checkbox checked
    // For Stripe/Adyen: Button enabled when provider loads
    customButton.disabled = !state.canSubmit || state.isProcessing;
};
```

#### React Example


```tsx
import React, { useState, useEffect } from 'react';

export const CustomPaymentButton = ({ userToken }) => {
    const [widget, setWidget] = useState(null);
    const [buttonState, setButtonState] = useState({
        disabled: true,
        text: 'Pay Now'
    });

    useEffect(() => {
        const widgetInstance = window.paymentWidget.init({
            userSessionToken: userToken,
            environment: 'live',
            countryCode: 'US',
            locale: 'en',
            container: 'payment-widget',
            hidePaymentButton: true,
            onPaymentStateChange: (state) => {
                setButtonState({
                    disabled: !state.canSubmit,
                    text: state.isProcessing ? 'Processing...' : 'Pay Now'
                });
            }
        });

        setWidget(widgetInstance);
        return () => widgetInstance?.destroy();
    }, [userToken]);

    const handlePayment = async () => {
        try {
            await widget?.submitPayment();
        } catch (error) {
            console.error('Payment failed:', error);
        }
    };

    return (
        <div>
            <div id="payment-widget" />
            <button
                onClick={handlePayment}
                disabled={buttonState.disabled}
                className="custom-pay-button"
            >
                {buttonState.text}
            </button>
        </div>
    );
};
```

#### Angular Example


```typescript
import { Component, ElementRef, ViewChild, OnDestroy } from '@angular/core';

@Component({
    selector: 'app-payment-with-custom-button',
    template: `
        <div #paymentContainer></div>
        <button
            (click)="handlePayment()"
            [disabled]="!canSubmit"
            class="custom-pay-button"
        >
            {{ buttonText }}
        </button>
    `
})
export class PaymentWithCustomButtonComponent implements OnDestroy {
    @ViewChild('paymentContainer', { static: true }) containerRef!: ElementRef;
    private widget: any;
    canSubmit = false;
    buttonText = 'Pay Now';

    ngAfterViewInit() {
        this.widget = window.paymentWidget.init({
            userSessionToken: this.getUserToken(),
            environment: 'live',
            countryCode: 'US',
            locale: 'en',
            container: this.containerRef.nativeElement,
            hidePaymentButton: true,
            onPaymentStateChange: (state) => {
                this.canSubmit = state.canSubmit;
                this.buttonText = state.isProcessing
                    ? 'Processing...'
                    : 'Pay Now';
            }
        });
    }

    async handlePayment() {
        try {
            await this.widget?.submitPayment();
        } catch (error) {
            console.error('Payment failed:', error);
        }
    }

    ngOnDestroy() {
        this.widget?.destroy();
    }
}
```

### Customer Data Prefilling

The widget supports pre-filling payment forms with customer information to improve the user experience. Customer data can be provided during initialization or updated dynamically at any time.

#### Initial Configuration

Provide customer data when initializing the widget:


```javascript
const widget = window.paymentWidget.init({
    userSessionToken: 'user-session-token',
    environment: 'live',
    countryCode: 'US',
    locale: 'en',
    container: 'payment-widget',
    customerData: {
        name: 'John Doe',
        email: 'john.doe@example.com',
        address: {
            line1: '123 Main Street',
            line2: 'Apt 4B',
            city: 'New York',
            postalCode: '10001',
            state: 'NY',
            country: 'US'
        }
    }
});
```

#### Dynamic Updates

Update customer data after the widget is initialized:


```javascript
// Update customer data dynamically
widget.updateCustomerData({
    name: 'Jane Smith',
    email: 'jane.smith@example.com',
    address: {
        line1: '456 Oak Avenue',
        city: 'Los Angeles',
        postalCode: '90001',
        state: 'CA',
        country: 'US'
    }
});
```

#### React Example with State Management


```tsx
import React, { useState, useEffect, useRef } from 'react';

export const PaymentWithCustomerData = () => {
    const widgetRef = useRef(null);
    const [customerData, setCustomerData] = useState({
        name: '',
        email: '',
        address: {
            line1: '',
            city: '',
            postalCode: '',
            country: 'US'
        }
    });

    useEffect(() => {
        widgetRef.current = window.paymentWidget.init({
            userSessionToken: 'user-session-token',
            environment: 'live',
            countryCode: 'US',
            locale: 'en',
            container: 'payment-widget',
            customerData: customerData
        });

        return () => widgetRef.current?.destroy();
    }, []);

    // Update customer data dynamically
    useEffect(() => {
        if (widgetRef.current && customerData.name) {
            widgetRef.current.updateCustomerData(customerData);
        }
    }, [customerData]);

    const handleFormChange = (field, value) => {
        setCustomerData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    return (
        <div>
            <h3>Customer Information</h3>
            <input
                type="text"
                placeholder="Name"
                value={customerData.name}
                onChange={(e) => handleFormChange('name', e.target.value)}
            />
            <input
                type="email"
                placeholder="Email"
                value={customerData.email}
                onChange={(e) => handleFormChange('email', e.target.value)}
            />

            <div id="payment-widget" />
        </div>
    );
};
```

#### Angular Example with Form Binding


```typescript
import { Component, OnInit, OnDestroy, ViewChild, ElementRef } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
    selector: 'app-payment-with-customer-data',
    template: `
        <form [formGroup]="customerForm">
            <input formControlName="name" placeholder="Name" />
            <input formControlName="email" placeholder="Email" />
            <input formControlName="line1" placeholder="Address Line 1" />
            <input formControlName="city" placeholder="City" />
            <input formControlName="postalCode" placeholder="Postal Code" />
        </form>
        <div #paymentContainer></div>
    `
})
export class PaymentWithCustomerDataComponent implements OnInit, OnDestroy {
    @ViewChild('paymentContainer', { static: true }) containerRef!: ElementRef;
    private widget: any;
    customerForm: FormGroup;

    constructor(private fb: FormBuilder) {
        this.customerForm = this.fb.group({
            name: [''],
            email: [''],
            line1: [''],
            city: [''],
            postalCode: [''],
            country: ['US']
        });
    }

    ngOnInit() {
        this.widget = window.paymentWidget.init({
            userSessionToken: this.getUserToken(),
            environment: 'live',
            countryCode: 'US',
            locale: 'en',
            container: this.containerRef.nativeElement,
            customerData: this.customerForm.value
        });

        // Update widget when form changes
        this.customerForm.valueChanges.subscribe(data => {
            this.widget.updateCustomerData({
                name: data.name,
                email: data.email,
                address: {
                    line1: data.line1,
                    city: data.city,
                    postalCode: data.postalCode,
                    country: data.country
                }
            });
        });
    }

    ngOnDestroy() {
        this.widget?.destroy();
    }
}
```

#### Supported Payment Methods

Customer data prefilling is supported by the following payment providers:

- **Stripe**: Pre-fills name, email, and full billing address in payment forms
- **Adyen**: Pre-fills cardholder name, email, and address fields for card payments


**Note**: All customer data fields are optional. The widget will pre-fill only the fields that are provided.

### Handling Redirects

For 3D Secure authentication, users may be redirected to their bank. The widget automatically detects and resumes payment processing after redirect.

**Store session token to ensure continuity:**


```javascript
function initializeWidget() {
    // Get token from storage or current session
    const userSessionToken =
        sessionStorage.getItem('paymentSessionToken') || getCurrentUserToken();

    // Store for redirect continuity
    if (!sessionStorage.getItem('paymentSessionToken')) {
        sessionStorage.setItem('paymentSessionToken', userSessionToken);
    }

    const widget = window.paymentWidget.init({
        userSessionToken: userSessionToken,
        environment: 'live',
        countryCode: 'US',
        locale: 'en',
        container: 'payment-widget',
        onSuccess: (
            token,
            paymentInstrumentDetails,
            paymentInstrumentToken
        ) => {
            sessionStorage.removeItem('paymentSessionToken');
            handlePaymentSuccess(
                token,
                paymentInstrumentDetails,
                paymentInstrumentToken
            );
        }
    });
}

// Initialize widget on page load
initializeWidget();
```

### Error Handling

Common validation errors:

- Container element not found
- Missing required parameters
- Invalid environment value



```javascript
try {
    const widget = window.paymentWidget.init(config);
} catch (error) {
    console.error('Widget initialization failed:', error.message);
}
```

### API Reference


```typescript
interface PaymentWidget {
    init(config: PaymentConfig): PaymentWidgetInstance;
}

interface PaymentWidgetInstance {
    destroy(): void;
    submitPayment(): Promise<void>;
    getPaymentState(): PaymentButtonState;
    updateCustomerData(data: CustomerData): void;
}

interface PaymentButtonState {
    isProcessing: boolean;
    canSubmit: boolean;
}

interface PaymentConfig {
    userSessionToken: string;
    environment: 'test' | 'sandbox' | 'live';
    countryCode: string;
    locale: string;
    container: string | HTMLElement;
    styling?: {
        primaryColor?: string;
        secondaryColor?: string;
        textColorMain?: string;
        textColorSecondary?: string;
        borderColor?: string;
        borderRadius?: string;
        boxShadow?: string;
        stripe?: {
            appearance?: {
                theme?: 'stripe' | 'night' | 'flat';
                variables?: Record<string, string>;
                rules?: Record<string, Record<string, string>>;
            };
        };
    };
    i18n?: Record<string, string>;
    featureFlags?: PaymentFeatureFlags;
    hidePaymentButton?: boolean;
    customerData?: CustomerData;
    onSuccess?: (
        paymentRequestToken: string,
        paymentInstrumentDetails?: PaymentInstrumentDetails,
        paymentInstrumentToken?: string
    ) => void;
    onPaymentStateChange?: (state: PaymentButtonState) => void;
    devMode?: boolean;
}

interface PaymentFeatureFlags {
    useRubiksUI?: boolean; // Enable Rubiks Styleguide components
}

interface CustomerData {
    name?: string;
    email?: string;
    address?: CustomerAddress;
}

interface CustomerAddress {
    line1?: string;
    line2?: string;
    city?: string;
    postalCode?: string;
    state?: string;
    country?: string;
}

interface BankAccountDetails {
    accountHolder: string;
    bankName: string;
    bic: string;
    iban: string;
    signature?: string;
}

interface PaymentInstrumentDetails {
    creditCard?: {
        brand?: string;
        cardHolder: string;
        cardNumber: string;
        expiry: string;
        issuerCountry?: string;
    };
    sepa?: {
        bankAccountDetails: BankAccountDetails;
    };
    bacs?: {
        accountHolder: string;
        bankAccountNumber: string;
        bankLocationId: string;
        directDebitPdfFormUrl: string;
        mandateId: string;
        shopperEmail: string;
    };
    chDD?: {
        bankAccountDetails: BankAccountDetails;
    };
    lsvDD?: {
        bankAccountDetails: BankAccountDetails;
    };
    ideal?: {
        issuer: string;
    };
    banContactCard?: {
        cardHolder: string;
        cardNumber: string;
        expiry: string;
    };
    paypal?: {};
    twint?: {};
    cash?: {};
    bankTransfer?: {};
}
```