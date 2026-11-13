<div class="hero-kicker">SOLO ENGINEERING · B2B SAAS · SYSTEM DESIGN</div>

# Cercle 8
## One developer. Several systems. Real architectural trade-offs.

**Co-founder & Sole Software Developer — Owen-Junior Jean**

Cercle 8 is a multi-tenant customer-retention intelligence platform for e-commerce businesses. This website focuses on what is technically difficult about building a product like this without a separate engineering team.

[Engineering problems](docs/engineering-challenges.md){ .md-button .md-button--primary }
[System architecture](docs/system-architecture.md){ .md-button }
[Validation evidence](docs/validation-status.md){ .md-button }

<div class="grid cards" markdown>

- **01 / Multi-tenant architecture**

    ---

    A shared Supabase backend must protect each business's data, including from requests that appear correctly authenticated but target the wrong tenant.

    [Access-control decisions](docs/multi-tenancy.md)

- **02 / Shopify + SaaS identity**

    ---

    An embedded Shopify app and standalone SaaS have different session lifecycles. One merchant still needs one coherent business identity.

    [Shopify integration case study](docs/shopify-integration.md)

- **03 / Explainable diagnostics**

    ---

    Customer and order data must be normalized, scoped and historically reproducible before it becomes a diagnosis and recommendation.

    [Diagnostic engine](docs/diagnostic-engine.md)

- **04 / Controlled automation**

    ---

    Recommendations must not silently become external messages. Human approval, provider failure handling and auditability are engineering requirements.

    [Klaviyo execution design](docs/klaviyo-execution.md)

</div>

## The system boundary

~~~mermaid
flowchart LR
    Shopify["Shopify"] --> Ingest["Ingestion and normalization"]
    CSV["CSV"] --> Ingest
    Ingest --> Data[("Supabase: tenant-scoped business data")]
    App["Next.js SaaS + Shopify context"] <--> Data
    Data --> Dx["Diagnostics and snapshots"]
    Dx --> Review["Merchant review"]
    Review --> Approval["Human authorization"]
    Approval --> Send["Klaviyo action"]
    Stripe["Stripe"] --> App
    classDef ext fill:#15233a,stroke:#64748b,color:#fff
    classDef core fill:#302b63,stroke:#818cf8,color:#fff
    classDef edge fill:#12394e,stroke:#38bdf8,color:#fff
    class Shopify,CSV,Stripe ext
    class Ingest,Data,App,Dx core
    class Review,Approval,Send edge
~~~

**Conceptual architecture**, not proof every integration is ready for production. Private business logic and customer data are excluded.

## Engineering journey

| Period | What changed | Why it matters |
|---|---|---|
| June 2026 | Tenant-scoped test and commerce data ingestion | An early path from events to diagnostics |
| October 2026 | Shared Shopify/SaaS business state in Supabase | Reduced duplicate sources of truth |
| October 2026 | Shopify sessions separated from business records | Authentication lifetime no longer defines business identity |
| V1 in progress | Human-reviewed Klaviyo execution | Moving from analysis to controlled external effects |

[Historical journal](development-journal/README.md) · [Architecture decisions](engineering-decisions/README.md)

## Why solo engineering changes the trade-offs

A single design change can affect authentication, tenancy, customer data, recommendations, billing and external APIs simultaneously. There is no separate frontend, backend, DevOps or QA team to absorb this coordination.

[Engineering trade-offs](docs/solo-development.md) · [Lessons learned](docs/lessons-learned.md)

---

!!! info "Evidence boundary"
    This is a public technical case study. Historical results are labeled; production readiness is not assumed. Proprietary application code, credentials and customer data are excluded.

**Owen-Junior Jean** · [GitHub](https://github.com/lilouwen) · [LinkedIn](https://www.linkedin.com/in/owen-junior-jean/)
