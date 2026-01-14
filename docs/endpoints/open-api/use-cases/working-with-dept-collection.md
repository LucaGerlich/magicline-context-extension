# Working with debt collection endpoints

## Intro

Use case description on how to receive and update debt collection cases via the   Open API.

## General

### Relevant Endpoints

- [GET Debtors](../openapi/openapi#operation/getDebtors)
- [GET Transfer Details](../openapi/openapi#operation/getTransferDetails)
- [POST Confirm transfer retrieval](../openapi/openapi#operation/confirmTransfer)
- [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection)
- [GET debt collection cases](../openapi/openapi#operation/getDebtCollectionCases)
- [GET Blocked Debtors](../openapi/openapi#operation/getDebtCollectionBlockedDebtors)
- [GET Blocked Debts](../openapi/openapi#operation/getDebtCollectionBlockedDebts)


### Receiving and accepting an integration request

Please refer to [Managing Activations](../../../products/developer-portal/managing-activations).

### Retrieving Debt Collection Cases

Once a debt collection run is verified by a studio, the `FINANCE_DEBT_COLLECTION_RUN_CREATED` webhook is triggered (see [Event types](../webhooks/event-types)). This event contains an ID (`entityId`), referring to the unique debt collection run, containing all cases. However, it won't include the actual debt cases.

Developers are required to fetch information about debtors and debt cases using the following endpoints:

- [GET Debtors](../openapi/openapi#operation/getDebtors): Returns debtors for specified debtCollectionRunId in slices
- [GET Transfer Details](../openapi/openapi#operation/getTransferDetails): Provides holistic data about the transfer including current status, date, client information, etc.


Important information:

- `debtorId`: A unique identifier for the debtor. Note: The ID is unique per studio and not globally.
- `collectionCaseId`: The ID of a debtor in a single transfer. Multiple IDs for the same debtor indicates individual debt collection transfers.
- `debtId`: An ID of a single debt of a debtor. Necessary for sending case updates.


Both these endpoints utilize the `debtCollectionRunId` parameter for reference, which was obtained from the `FINANCE_DEBT_COLLECTION_RUN_CREATED` webhook event's field `entityId`.

### Confirming Debt Collection Case Retrieval

After case retrieval, partners **must** confirm this action by leveraging the [POST Confirm transfer retrieval](../openapi/openapi#operation/confirmTransfer) endpoint. This will inform the studio about a successful data transfer to the partner.

It is highly recommended to confirm the transfer immediately after having received the debt collection cases.

### Updating Debt Collection Cases

The handling of updates on cases is carried out via the [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection) endpoint. The `Open Api Token` assigned during registration is required to authenticate.

Important:

- Updates imply the entirety of a debtor's current state, not the difference from the prior state.
- `collectionCaseIds` must include all   case IDs related to the partner's case.
- Payments cumulate. For instance, receiving two payments, one for €10 and another for €15, equates to a total paid amount of €25, not two separate payments.


Additional parameters which can be used by partners:

- `agencyCollectionCaseId`: A partner's case ID used by   for reference.
- `publicCollectionCaseId`: An optional public case ID that varies from the `agencyCollectionCaseId`, used for client communication.


All debts relating to the partner's case should be provided in `debts` (At least one is required, regardless of changes).

### Closing a Debt Collection Case

Case closure necessitates setting a `closure` type. On applying a `POSITIVE`, `NEGATIVE`, or `REVERSAL` type, the debtor's debt collection status in   is removed, facilitating regular collection processes for future or open debts if the debtor maintains studio membership.

For uncollectible debts due to bankruptcy or special agreements, the partner can optionally employ the `WRITE_OFF_REMAINING_DEBTS` closure type.

In the case of `REJECTION`, the debtor stays in the debt collection status and all restrictions persist in  . It is mandatory to provide a valid value for `rejectionReason` in this case. (see the Open API Documentation for a description of the various reasons: [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection) endpoint)

If a case has been closed by the partner via `closure`, partners can still report payments, increasing the `paidAmount` accordingly for   to create a payment in the member account.

Caution: closing a case is considered final! E.g. if one update contains a `closure` element with type `POSITIVE` the case is closed in  . If a subsequent update doesn't contain a `closure` element anymore, the case isn't reopened in  . The member will not be put back into debt collection, until the studio initiates this. This also applies to the `WRITE_OFF_REMAINING_DEBTS` parameter: if an update contains a closure without `WRITE_OFF_REMAINING_DEBTS` parameter, and a subsequent update contains a closure with this parameter it will not be handled, since the case is already closed on  s side!

### Using  side Updates to Debt Collection Cases

This feature enables studio users to directly update the status of debt collection cases (e.g., closing or reverting a case) via the  UI. The purpose of this functionality is to ensure that the studio’s actions are automatically synchronized with the debt collection partner’s system, without requiring the studio to contact the partner manually.

When a user performs an update,  triggers a webhook event to the partner’s configured webhook URL. This event signals the partner to fetch the latest state of the case and adjust their records accordingly, ensuring data consistency between the studio and the debt collection partner.

#### Permissions

In order to allow studio users to change the case status, the permission to update debt collection cases must be explicitly enabled for the debt collection partner in the developer portal.

#### Webhook Event

The webhook event contains the `caseAdjustmentRequestId` as the `entityId`.
Depending on the partner’s configuration, it will also include either:

- an `agencyCollectionCaseId` (if the partner has assigned one), or
- a `collectionCaseId`.


#### Partner Action

Upon receiving the webhook event, the partner must fetch the updated case details via the [GET debt collection cases](../openapi/openapi#operation/getDebtCollectionCases) endpoint, using one of the IDs provided in the webhook event.
This design ensures that the debt collection partner’s dataset always matches the studio’s dataset, reducing manual communication overhead and improving synchronization.

### Contract Termination Between Studio and Partner

There are two distinguishable scenarios:

- A studio may switch to a new debt collection partner, but the old partner keeps handling the cases it already received. The old partner is still able to send updates via Open API to report payments, case closings, etc. as usual. The only difference is that the old partner doesn’t receive any new cases.
- Contract termination initiated by the studio or the partner.
In this case, the following steps might be taken, utilizing the [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection)
endpoint:
- If initiated by the studio, partners should close the debt collection cases with type as `REJECTION` and `rejectionReason` as `WITHDRAWN_BY_STUDIO`.
- If initiated by the partner, case closure should happen using `REVERSAL` type.


### Procedure for Direct Customer Payment to Studio

Presently, automatic forwarding of payments from the studio to the partner is unavailable.

If a customer pays directly to the studio, the studio must inform the partner and avoid booking payments in  . Instead, partners should report the payment via Open API as if the payment was received directly. Money transfer arrangements between the studio and the partner are at their discretion.

### Blocking and Unblocking Debt Collection Cases

A customer or only a specific debt can be excluded from future debt collection runs by adding a block property to a debtor or a debt on  [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection).

By sending an update to the debtor or debt without the block property the block will be removed.

## Use case examples

The following examples are intended to illustrate some cases and in which situation which data must be sent as an update.

### Preconditions

Each example assumes the following as preconditions:

- The studio has performed 2 debt collection runs, and you as partner have fetched the included member
- Both debt collection runs contained exactly one member, with [debtorId](../openapi/openapi#operation/getDebtors) `debtorid` (usually the debtorId is either a UUID or a number, but for better readability we use this)
- The first debt collection run:
  - Contains as [collectionCaseId](../openapi/openapi#operation/getDebtors) `collection-caseid-1` (The collectionCaseId is normally a UUID, but this is used for better readability)
  - A single [debt](../openapi/openapi#operation/getDebtors) with [debtId](../openapi/openapi#operation/getDebtors) `debtid-1` of 10€ (debtIds are normally a UUID)
- The second debt collection run:
  - contained as [collectionCaseId](../openapi/openapi#operation/getDebtors) `collection-caseid-2`
  - A single [debt](../openapi/openapi#operation/getDebtors) with [debtId](../openapi/openapi#operation/getDebtors) `debtid-2` of 20€


### Single payment with case closure

(See [preconditions](#preconditions))

Lets assume you have received a single payment on the full amount and want to report the payment with a successful case closure.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "closure": {
            "type": "POSITIVE",
            "options": [],
            "date": "2024-10-14",
            "closureReason": "Optional, e.g. 'Member has fully paid'"
          },
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 10,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 20,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

**Consequences**

-  will create a payment of 30€ (since this is your first update and the `paidAmount` is 30€ in total)
- The debt collection case is closed in
- Assuming that the Member has no other debt collection cases or open debts, the debt collection level is removed from the member and he may enter the Gym again


### Partial payment with case closure

(See [preconditions](#preconditions))

There was a negotiation with the debtor, and you and the debtor agreed upon that he must only pay 50% of the total value to close the case.

You received the money and want to report to  the payment of 50% (15€) and close the case.

Its up to you how the partial payment is distributed among the open debts. In this example we assume that the paid amount is distributed equally among the debts.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "closure": {
            "type": "POSITIVE",
            "options": [],
            "date": "2024-10-14",
            "closureReason": "Optional, e.g. 'Negotiated case closure with partial payment'"
          },
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 5,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 10,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

**Consequences**

-  will create a payment of 15€ (since this is your first update and the `paidAmount` is 15€ in total)
- The debt collection case is closed in
- If the studio has a setting enabled to write off remaining debts, the 2 debts will be reduced by the still open amount, so the debtor then has no open debts anymore
  - If the remaining debts are written off the debt collection level of the debtor is removed and he may enter the Gym again, if he is still a member with active contract


### Intermediate payment

(See [preconditions](#preconditions))

You received a partial payment of 5€ by the debtor. You assign this payment to one debt (`debtid`) and want to report this payment to  , without closing the case.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 5,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

**Consequences**

-  will create a payment of 5€


Note that as in every update, both `collectionCaseIds` are added, and also both `debts`, also the one that didn't change. The update always must contain the whole case, including all case ids and debts.

### Reversal of payment

(See [preconditions](#preconditions))

Lets assume you first reported by mistake a payment of 5€ on debt `debtid-1`. Actually you only received 2€ by the debtor and want to correct this.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 2,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

**Consequences**

-  will reduce the previously created payment of 5€ down to 2€


### Reversal of Case

(See [preconditions](#preconditions))

Lets assume the studio you are working with has submitted a member to debt collection by mistake. The studio sends and email to you, asking to close the case without any processing.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "closure": {
            "type": "REJECTION",
            "rejectionReason": "WITHDRAWN_BY_STUDIO",
            "options": [],
            "date": "2024-10-14",
            "closureReason": "Optional, e.g. 'Studio asked for case closure on 2024-10-14 as transfer made by mistake'"
          },
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

### Rejection by Partner

(See [preconditions](#preconditions))

Lets assume your received a debtor but with the given address information it is not possible to contact the debtor, and any address search was also unsuccessuful.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "closure": {
            "type": "REJECTION",
            "rejectionReason": "POSTAL_DELIVERY_NOT_POSSIBLE",
            "options": [],
            "date": "2024-10-14",
            "closureReason": "Optional: "
          },
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

### Adjustments of debts by the Studio

The studio wants to adjust a debt that was sent to you as part of a debt collection handover. Currently this is only possible by performing these steps:

- You need to reject the case with a rejection reason of `WITHDRAWN_BY_STUDIO` (see [Reversal of Case](#reversal-of-case))
- The studio adjusts the debt via
- The studio performs a new debt collection run


(A feature which is currently in development will adjust this process. The studio then will be able to adjust a debt that is currently in debt collection, you will receive a Notification about this adjustment and the option to either accept or reject this change)

### Blocking and Unblocking Debt Collection Cases

(See [preconditions](#preconditions))

Let's assume you want to block the debtor from future debt collection runs, you have sent an update with a block for the debtor.

You would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "block": {
            "limitType": "LIMITED",
            "endDate": "2024-09-20"
          },
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

Because there are no blocks in the json at the specific debts, eventually existing blocks will be removed.

If you later on want to enable the debtor but block `debtid-2` forever, you would send the following update to [POST Update debt collection](../openapi/openapi#operation/updateDebtCollection):


```json
{
  "debtors": [
    {
      "debtorId": "debtorid",
      "agencyCollectionCases": [
        {
          "agencyCollectionCaseId": "your-case-id",
          "publicCollectionCaseId": "optional-your-customer-facing-id",
          "collectionCaseIds": [
            "collection-caseid-1",
            "collection-caseid-2"
          ],
          "debts": [
            {
              "debtId": "debtid-1",
              "originalAmount": 10,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR"
            },
            {
              "debtId": "debtid-2",
              "originalAmount": 20,
              "canceledAmount": 0,
              "paidAmount": 0,
              "currency": "EUR",
              "block": {
                "limitType": "UNLIMITED"
              }
            }
          ]
        }
      ]
    }
  ],
  "requestId": "your-request-id"
}
```

### Closing a case related to rest maturity with reversing the rest maturity (Planned)

This is a planned feature and currently not supported.

### Payment within the studio (Planned)

This is a planned feature and currently not supported.

### Reduce debt claim amount without removing the entrance restriction (Planned)

This is a planned feature and currently not supported.

### Send activity updates to the studio (Planned)

This is a planned feature and currently not supported.