<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,48:302b63,100:24243e&height=220&section=header&text=CERCLE%208&fontSize=48&fontColor=ffffff&animation=fadeIn" width="100%" alt="Cercle 8 engineering case study" />
</p>

<h3 align="center">ENGINEERING A MULTI-TENANT SAAS AS A SOLO DEVELOPER</h3>

<p align="center">
  Architecture · Integrations · Security · Reliability · Engineering Trade-offs
</p>

<p align="center">
  <a href="docs/system-architecture.md"><img src="https://img.shields.io/badge/Next.js-15-181717?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js"/></a>
  <a href="docs/multi-tenancy.md"><img src="https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"/></a>
  <a href="docs/shopify-integration.md"><img src="https://img.shields.io/badge/Shopify-Integration-95BF47?style=for-the-badge&logo=shopify&logoColor=white" alt="Shopify"/></a>
  <a href="docs/klaviyo-execution.md"><img src="https://img.shields.io/badge/Klaviyo-Engagement-222222?style=for-the-badge" alt="Klaviyo"/></a>
  <a href="docs/system-architecture.md"><img src="https://img.shields.io/badge/Stripe-Billing-635BFF?style=for-the-badge&logo=stripe&logoColor=white" alt="Stripe"/></a>
</p>

<p align="center">
  <strong>Owen-Junior Jean</strong> · Co-founder & Sole Software Developer
</p>

---

## Beyond the dashboard

**Cercle 8** is a B2B customer-retention intelligence platform for e-commerce businesses. It is designed to connect customer data, generate diagnostics, explain retention risks and translate recommendations into controlled actions.

This repository is not the SaaS source code. It is a public **software-engineering case study**: architectural evolution, real technical constraints, integration failures and risks, decisions, test boundaries and lessons from building a complex product as its sole software developer.

> **Engineering scope:** "Solo developer" describes technical implementation responsibility, not sole ownership of the business. Cercle 8 is a co-founded product.

## System at a glance

~~~mermaid
flowchart LR
    Store["Shopify store"] --> Ingest["Data ingestion and normalization"]
    CSV["CSV source"] --> Ingest
    CRM["Klaviyo integration"] <--> Ops["Approved actions"]
    Ingest --> DB[("Supabase / PostgreSQL<br/>tenant-aware business data")]
    DB --> Engine["Customer diagnostic<br/>and segmentation"]
    Engine --> Review["Review and recommendations"]
    Review --> Approve["Human approval"]
    Approve --> Ops
    Billing["Stripe"] --> App["Next.js SaaS + Shopify context"]
    App <--> DB
    App --> Review

    classDef input fill:#17213a,stroke:#64748b,color:#fff
    classDef core fill:#302b63,stroke:#818cf8,color:#fff
    classDef action fill:#153b57,stroke:#38bdf8,color:#fff
    class Store,CSV,CRM,Billing input
    class DB,Ingest,App,Engine core
    class Review,Approve,Ops action
~~~

**Architectural intent, not a live-production topology.** Some steps are implemented or previously tested; others are still part of V1 validation. The diagram deliberately omits secret handling and proprietary diagnostic rules.

[Full architecture](docs/system-architecture.md) · [Trust boundaries](docs/security-and-privacy.md) · [Data-source identity](architecture/shopify-tenant-flow.md)

## The engineering challenges

| Engineering problem | What made it difficult | Case study |
|---|---|---|
| **Tenant isolation** | One backend serving multiple businesses without cross-tenant data access | [Multi-tenancy](docs/multi-tenancy.md) |
| **One business identity across contexts** | Shopify embedded app, standalone SaaS, sessions and tenant mapping | [Shopify integration](docs/shopify-integration.md) |
| **A single source of truth** | Avoiding competing data models and synchronization ambiguity | [ADR 0001](engineering-decisions/0001-supabase-source-of-truth.md) |
| **Meaningful diagnostics** | Turning heterogeneous activity data into explainable results | [Diagnostic engine](docs/diagnostic-engine.md) |
| **Safe external actions** | Human authorization, API failures, retry behavior and auditability | [Klaviyo execution](docs/klaviyo-execution.md) |
| **Operating with one developer** | Architecture, implementation, testing and scope competing for time | [Solo engineering](docs/solo-development.md) |

## Technical stack

| Area | Technology / design |
|---|---|
| User-facing application | Next.js 15, React, TypeScript |
| Business data | PostgreSQL, Supabase, tenant-aware data model |
| Authentication and authorization | Supabase Auth, Shopify OAuth, Row Level Security |
| Shopify session persistence | Prisma, separated from business records |
| Commerce and engagement APIs | Shopify, Klaviyo |
| Payments | Stripe |
| Hosting and server-side integration | Vercel, API routes, Supabase Edge Functions |
| Product logic | Diagnostic snapshots, segmentation, recommendations, action planning |

## Selected engineering evidence

These are **historical development records**, not current production metrics.

- **June 2026:** a test environment recorded tenant-scoped access and an initial connected source/import.
- **12 June 2026:** a recorded ingestion exercise included **76 test customers, 277 customer events and 76 customer metrics**, with downstream diagnostic processing.
- **20 October 2026:** a documented architecture consolidation aligned Shopify business data with Supabase, while reserving Prisma for session persistence. Lint, type-check, build and Prisma schema validation were reported as passing.
- **October 2026:** the Shopify embedded-app/session and privacy-webhook configuration was prepared; **real OAuth, production secrets, deployment and end-to-end acceptance were not established by those static checks**.

See [Evidence & validation ledger](docs/validation-status.md) and [Development journal](development-journal/README.md). Tests and dates here reflect development notes, not independently reproduced evidence.

## Read the engineering story

<details open>
<summary><strong>Architecture and integrations</strong></summary>

- [System architecture](docs/system-architecture.md)
- [Multi-tenancy and RLS](docs/multi-tenancy.md)
- [Shopify integration: embedded and standalone](docs/shopify-integration.md)
- [Diagnostic engine](docs/diagnostic-engine.md)
- [Human-controlled Klaviyo execution](docs/klaviyo-execution.md)
- [Security and privacy](docs/security-and-privacy.md)

</details>

<details>
<summary><strong>Technical difficulties and decisions</strong></summary>

- [Engineering challenges](docs/engineering-challenges.md)
- [Architecture decision records](engineering-decisions/README.md)
- [Data-flow and sequence diagrams](architecture/README.md)
- [Solo development and constraints](docs/solo-development.md)
- [Lessons learned](docs/lessons-learned.md)

</details>

<details>
<summary><strong>Evidence and project evolution</strong></summary>

- [Validation status](docs/validation-status.md)
- [Historical development journal](development-journal/README.md)
- [Documentation index](docs/README.md)

</details>

## Publication boundary

This public repository contains **sanitized documentation only**. It does **not** contain source code for the commercial application, tenant data, API keys, Shopify tokens, diagnostic formulas, webhook signatures, customer exports or private operational endpoints.

A completed lint/build check is not the same as a passing OAuth, billing, multi-tenant security or external-execution test. The V1 status is tracked explicitly rather than described as production-ready.

---

<p align="center">
  <strong>Owen-Junior Jean</strong><br/>
  Co-founder & Solo Software Developer · Cercle 8<br/>
  <a href="https://github.com/lilouwen">GitHub</a> · <a href="https://www.linkedin.com/in/owen-junior-jean/">LinkedIn</a>
</p>

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=110&section=footer" width="100%" alt="Footer" /></p>
