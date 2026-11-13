# Human-controlled recommendation execution

[← Documentation](README.md) · [← Repository](../README.md)

## The difficult boundary

**Analyzing customer data is not the same as acting on customers.** Once a SaaS sends information to a third-party messaging service, its operations can affect real recipients.

Cercle 8's V1 requirement therefore includes **human approval before any recommendation execution**.

## Intended lifecycle

~~~mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Prepared: audience / channel / message / timing
    Prepared --> AwaitingApproval
    AwaitingApproval --> Rejected: merchant rejects
    AwaitingApproval --> Approved: merchant approves
    Approved --> Queued
    Queued --> Executing
    Executing --> Succeeded: provider confirms
    Executing --> Failed: provider error
    Failed --> ReviewRequired
    ReviewRequired --> Queued: explicit authorized retry
    Succeeded --> [*]
    Rejected --> [*]
~~~

This is a **design model**, not proof that these states or transitions are implemented exactly this way in the private codebase.

## Engineering constraints

- **Tenant binding:** the source recommendation, audience, approval and connected Klaviyo account must agree on ownership.
- **Approver identity:** the SaaS must record who authorized which proposed action.
- **Preview:** a merchant must see audience, content, channel and timing before execution.
- **Idempotency:** retrying after an uncertain API response must not accidentally send duplicates.
- **Provider errors:** rate limits, expired tokens and partial failures need recoverable states.
- **Traceability:** the system should preserve planned versus actual execution status.
- **Channel abstraction:** email is the priority; SMS/WhatsApp are architectural considerations, not claims of implemented delivery.

## V1 boundary

The human-approved Klaviyo email flow is a V1 feature to **finish and validate before launch**, not a distant optional enhancement. Do not label outbound execution production-ready until the complete path and error cases have been tested.

## Acceptance tests

| Case | Expected result |
|---|---|
| No approval | No external send |
| Different tenant | Rejected |
| Approval after audience changed | Requires explicit review of changed action |
| Token expired | Failed and reported without unauthorized retry |
| Provider timeout | Retry strategy avoids duplicate effects |
| Successful send | Persist provider reference/status and audit context |
| Rejected action | Never sent |
| Future additional channel | Does not bypass existing authorization boundary |

[Recommendation sequence](../architecture/recommendation-flow.md) · [Decision record](../engineering-decisions/0003-human-approved-execution.md)
