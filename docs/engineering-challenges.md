# Engineering challenges: problems, decisions, lessons

[← Documentation](README.md) · [← Repository](../README.md)

## Challenge 01 — Duplicate sources of business truth

**Problem.** Shopify integration and standalone SaaS data models risked becoming separate sources of customers, diagnostics and tenant identity.

**Decision.** Use Supabase as the shared business-data store, while keeping Shopify session persistence separate through Prisma.

**Evidence.** October 2026 development notes report migration of relevant application paths and successful static checks.

**Remaining validation.** Deployed store installation, cross-context identity reconciliation and data-source authorization.

**Trade-off.** Centralization improves conceptual consistency but raises the importance of robust shared tenant mapping.

[Full ADR](../engineering-decisions/0001-supabase-source-of-truth.md)

## Challenge 02 — Authentication is not business authorization

**Problem.** Embedded Shopify installation context and SaaS sign-in represent different session models. Neither automatically proves access to a specific tenant's records.

**Approach.** Resolve shop identity, session state, tenant ownership and data-source scope separately.

**Risk.** A convenient default selection could leak data or create duplicate workspaces if authorization is inferred from a store name alone.

**Remaining validation.** Negative tenant tests, stale sessions, reconnect and installation transitions.

[Shopify integration](shopify-integration.md)

## Challenge 03 — Protecting privacy without destroying unrelated history

**Problem.** Shopify uninstall and redaction requests must not indiscriminately delete unrelated SaaS business records.

**Approach.** Model integration/source-scoped cleanup separately from tenant/account deletion.

**Evidence.** October 2026 privacy webhook preparation is documented.

**Remaining validation.** Real signed callbacks, scope correctness, safe retries and production deployment.

[Privacy boundary](security-and-privacy.md)

## Challenge 04 — Diagnostics that remain explainable

**Problem.** Multiple data sources can have inconsistent completeness and event semantics. A recommendation must be explainable and reproducible.

**Approach.** Normalize event/identity data before computing metrics, snapshots and recommendations.

**Evidence.** June 2026 test dataset and diagnostic processing recorded.

**Remaining validation.** Duplicate handling, missing data, historical consistency and quality of customer-level conclusions.

[Diagnostics](diagnostic-engine.md)

## Challenge 05 — A recommendation becomes an external effect

**Problem.** Generating a retention recommendation is low-risk compared with sending customer messages through Klaviyo.

**Approach.** Human approval before any execution, plus tenant ownership checks and an auditable execution lifecycle.

**Status.** V1 implementation/validation priority; not claimed complete.

**Trade-off.** More workflow states add complexity but make unintended outbound actions easier to prevent and investigate.

[Approval workflow](klaviyo-execution.md)

## Challenge 06 — One engineer, coupled subsystems

**Problem.** Identity, data modeling, diagnostics, external APIs and billing must evolve together with limited engineering capacity.

**Response.** Prioritize critical end-to-end paths, record architecture decisions, narrow the scope of each integration and distinguish build success from real behavioral verification.

**Lesson.** Releasing fewer interconnected features reliably is more valuable than adding unvalidated surface area.

[Sole developer responsibilities](solo-development.md)
