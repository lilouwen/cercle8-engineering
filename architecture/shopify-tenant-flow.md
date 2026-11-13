# Shopify context → tenant → data source

[← Architecture index](README.md)

~~~mermaid
sequenceDiagram
    actor Merchant
    participant Shopify
    participant Web as Next.js application
    participant Sessions as Shopify Session store
    participant Data as Supabase business data
    Merchant->>Shopify: Open embedded app
    Shopify->>Web: Authenticated installation context
    Web->>Sessions: Resolve valid session
    Sessions-->>Web: Session state
    Web->>Data: Resolve shop → tenant → data source
    Data-->>Web: Authorized tenant scope
    Web-->>Merchant: Render scoped application
~~~

Shop identity, SaaS tenant and connected data source are **different resources**. A valid external session must not grant arbitrary access to business data.

**Implementation notes:** October 2026 records report this design and the business-data migration. At that point no live development-store OAuth test had been documented.

[Shopify engineering guide](../docs/shopify-integration.md) · [Session decision](../engineering-decisions/0002-shopify-sessions.md)