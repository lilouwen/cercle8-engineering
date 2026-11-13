# System overview

[← Architecture index](README.md)

~~~mermaid
flowchart LR
    Merchant["Merchant"] --> Web["Next.js SaaS / Shopify context"]
    Shopify["Shopify"] --> Web
    Web --> Auth["Authentication and tenant resolution"]
    Auth --> Data[("Supabase: business source of truth")]
    Web --> Session[("Prisma: Shopify sessions")]
    Web --> Ingest["Ingestion and normalization"]
    Ingest --> Data
    Data --> Diagnostic["Diagnostic snapshots"]
    Diagnostic --> Review["Recommendations and review"]
    Review --> Approval["Human approval"]
    Approval --> Klaviyo["Klaviyo API"]
    Stripe["Stripe"] -->|"Billing events"| Web

    classDef e fill:#17213a,stroke:#64748b,color:#fff
    classDef c fill:#302b63,stroke:#818cf8,color:#fff
    classDef d fill:#153b57,stroke:#38bdf8,color:#fff
    class Merchant,Shopify,Stripe,Klaviyo e
    class Web,Auth,Session,Ingest c
    class Data,Diagnostic,Review,Approval d
~~~

**Design diagram only.** Validation of real Shopify OAuth, Stripe subscription lifecycle, full tenant isolation and outbound execution remains part of V1 testing.

[System architecture](../docs/system-architecture.md) · [Evidence status](../docs/validation-status.md)