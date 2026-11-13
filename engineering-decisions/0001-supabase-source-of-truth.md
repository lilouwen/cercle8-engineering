# ADR-0001 — Business data has one source of truth

- **Recorded:** 20 October 2026
- **Status:** Architectural migration reported; complete live validation outstanding

## Context

Shopify embedded application and standalone SaaS were at risk of maintaining competing models for tenants, customers, data sources and diagnostics.

## Options

| Option | Benefit | Cost |
|---|---|---|
| Separate business databases | Independent integration development | Synchronization ambiguity and duplication |
| Supabase for business data | Unified business history and tenant ownership | Shared authorization must be correct |
| Read directly from third-party APIs | Lower initial data replication | Availability and external API constraints |

These are a comparison of plausible designs, not a claim that a formal alternatives meeting occurred.

## Decision

Consolidate business entities and reporting in Supabase/PostgreSQL. Resolve incoming Shopify store identity through the shop-to-tenant-to-data-source association.

## Evidence and trade-offs

October notes describe migration of relevant application paths and passing lint, type-check, build and Prisma validation. Centralization removes one kind of synchronization burden but amplifies the importance of correct access checks.

**Missing:** development-store OAuth and complete end-to-end Shopify/SaaS behavior at that historical checkpoint.

[Architecture](../docs/system-architecture.md) · [Shopify integration](../docs/shopify-integration.md)