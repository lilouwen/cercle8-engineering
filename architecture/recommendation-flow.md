# Approval-gated outbound actions

[← Architecture index](README.md)

~~~mermaid
sequenceDiagram
    actor Merchant
    participant App as Cercle 8 application
    participant DB as Tenant-scoped records
    participant Gate as Approval workflow
    participant Provider as Klaviyo
    Merchant->>App: Select recommendation
    App->>DB: Verify tenant ownership
    Merchant->>App: Prepare audience, message, channel, timing
    App->>Gate: Submit proposed action
    Gate-->>Merchant: Display action preview
    alt Authorized approval
        Merchant->>Gate: Approve exact action
        Gate->>DB: Save approval and execution intent
        Gate->>Provider: Execute approved request
        Provider-->>Gate: Provider outcome
        Gate->>DB: Persist outcome and reference
    else Rejected or pending
        Gate-->>App: Do not execute
    end
~~~

This is the **V1 target workflow**, not proof that external delivery is already operational. Required safeguards include tenant checks, an approved immutable payload or revision, safe retries and an auditable outcome.

[Action execution](../docs/klaviyo-execution.md) · [Approval decision](../engineering-decisions/0003-human-approved-execution.md)