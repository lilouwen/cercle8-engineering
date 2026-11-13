# System architecture

[← Documentation](README.md) · [← Repository](../README.md)

## Architecture objective

Cercle 8 combines a standalone SaaS, a Shopify embedded-app context and external services. The primary architectural task is to maintain **one tenant-aware business identity** across these entry points without turning each integration into its own business database.

## Logical building blocks

| Layer | Responsibility | Technology |
|---|---|---|
| Product UI | Diagnostics, recommendations, review and workflows | Next.js 15, React |
| Authentication | Sessions, identity, connection handoffs | Supabase Auth, Shopify OAuth |
| Authorization | Scoped access to business resources | Supabase RLS and server-side checks |
| Business persistence | Tenant, data source, customer, event, metric and diagnostic data | Supabase / PostgreSQL |
| Shopify runtime state | Installation/session persistence | Prisma session storage |
| Ingestion | Data-source adapters and normalization | Shopify APIs, CSV and server-side logic |
| Diagnostic analysis | Snapshots, segmentation and explainable recommendations | Proprietary business logic (not published) |
| Action execution | Human review, external service orchestration and tracking | Klaviyo integration |
| Billing | Subscription lifecycle and product entitlements | Stripe |
| Hosting | Web delivery and managed backend components | Vercel / Supabase |

## Trust boundaries

~~~mermaid
flowchart TD
    Visitor["User / store merchant"]
    App["Next.js UI and server"]
    Shopify["Shopify OAuth / APIs"]
    Klaviyo["Klaviyo API"]
    Stripe["Stripe webhooks / billing"]
    Auth["Authentication & tenant resolution"]
    DB[("Supabase Postgres")]
    Diag["Diagnostics / recommendations"]
    Exec["Reviewed outbound action"]

    Visitor --> App
    App --> Auth
    Auth --> DB
    Shopify <-->|"Authenticated integration boundary"| App
    App --> DB
    DB --> Diag
    Diag --> Exec
    Exec -->|"Approved external action"| Klaviyo
    Stripe -->|"Verified event boundary"| App

    classDef boundary fill:#302b63,stroke:#818cf8,color:#fff
    classDef external fill:#17213a,stroke:#64748b,color:#fff
    classDef internal fill:#153b57,stroke:#38bdf8,color:#fff
    class Auth,App boundary
    class Visitor,Shopify,Klaviyo,Stripe external
    class DB,Diag,Exec internal
~~~

The diagram illustrates **intended controls**. A server-side API or webhook still requires authorization, replay protection, scoped data access and operational validation; the diagram is not proof that these controls are implemented correctly.

## Significant architectural evolution

An October 2026 development record describes the move toward **Supabase as the single source of truth for business data**. Prisma remained for Shopify sessions instead of becoming a second, competing customer/diagnostic database.

This decision reduces duplication of business entities and makes cross-context reporting easier to reason about. The trade-off is that **tenant resolution and permission checks become critical shared infrastructure**.

[Architecture decision: source of truth](../engineering-decisions/0001-supabase-source-of-truth.md) · [Session separation](../engineering-decisions/0002-shopify-sessions.md)

## Open verification concerns

- End-to-end Shopify authentication from an authorized development store.
- Tenant authorization checks for every data and action route.
- Stripe lifecycle handling and entitlement enforcement.
- Klaviyo approval and execution failure/retry behavior.
- Reliable diagnostics and consistent snapshots across data sources.
- Deployment-specific secrets, webhook endpoints and monitoring.

**Validation state:** logical design and historical implementation notes; not a claim of production certification.
