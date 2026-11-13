# Engineering a complex SaaS as the sole developer

[← Documentation](README.md) · [← Repository](../README.md)

## Scope of responsibility

Cercle 8 is a co-founded business. Its software engineering work has been driven by **one developer**.

That means there is no separate engineering team to independently own frontend, backend, infrastructure, data modeling, integrations, debugging, release validation or maintenance.

## The coordination problem

At individual feature level, a new screen or API route may appear straightforward. At product level, it can affect several connected systems:

**A change to the tenant model** can affect Shopify OAuth, data-source ownership, diagnostic history, PDF exports and recommendation authorization.

**A change to Shopify data ingestion** can alter customer metrics, classification, diagnostics and lifecycle communications.

**A change to recommendation execution** requires decisions about approval state, retries, API credentials, audit logs and customer impact.

The engineering constraint is **managing these dependencies with limited development capacity**.

## Three practical trade-offs

### 1. Shipping a feature versus stabilizing the underlying model

A feature implemented against an unstable business identity model creates rework. The historical move toward a Supabase business source of truth illustrates why consolidation may matter more than another UI milestone.

### 2. An abstraction too early versus duplication too late

A multi-channel orchestration layer is valuable, but email execution via Klaviyo must first be reliable and testable. Abstraction should reflect demonstrated needs, not speculative future channels.

### 3. Static code quality versus end-to-end correctness

Passing lint, type-check, build and schema validation is valuable, but it cannot validate a live OAuth redirect, store installation, Stripe billing lifecycle or real provider callback.

A solo developer must deliberately budget time for those integration boundaries rather than treating green builds as full readiness.

## How I document engineering decisions

Each technical case study includes:

1. **Problem:** what broke or what constraint was introduced.
2. **Alternatives:** which plausible designs could have solved it.
3. **Decision:** what was chosen and why.
4. **Implementation boundary:** what changed, at a non-proprietary level.
5. **Validation:** what was actually tested versus still unverified.
6. **Trade-offs:** costs, risks and follow-up work.

This repository avoids inflated numerical claims about users, revenue, uptime, performance or production traffic.

## What being a solo developer does not mean

It does not imply owning the entire company alone, having every specialized discipline mastered, or having independently audited all security controls. It means taking responsibility for the technical delivery and for honestly identifying what has not yet been proven.

[Engineering challenges](engineering-challenges.md) · [Architecture decisions](../engineering-decisions/README.md)
