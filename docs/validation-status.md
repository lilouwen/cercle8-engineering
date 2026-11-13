# Evidence and validation ledger

[← Documentation](README.md) · [← Repository](../README.md)

> **As of 13 November 2026:** This ledger describes historical notes and remaining V1 checks. It is not a live deployment audit. "Reported" means discussed in earlier development work, not independently reproduced by this public repository.

| Subsystem / event | Historical evidence | Current confidence | Still needed |
|---|---|---|---|
| Supabase tenant-scoped demo | June 2026 user/tenant/source and import notes | Historical scoped test reported | Negative isolation tests across independent tenants |
| Shopify ingestion and diagnostics | June 2026: 76 test customers, 277 events, 76 metrics | Historical test environment result | Repeatable dataset + current integration verification |
| Shopify/SaaS business-data convergence | 20 Oct 2026 development notes | Implementation and static checks reported | Deployment + cross-context end-to-end flow |
| Prisma Shopify sessions | October architectural separation | Implementation/configuration reported | Real session expiry/reconnect validation |
| Shopify privacy webhooks | October configuration and code preparation | Static checks reported | Real signed delivery, scoped cleanup and retry tests |
| Embedded Shopify OAuth | October configuration prepared | **Not live-tested at that checkpoint** | Real dev-store OAuth, reinstallation, app-bridge context |
| Diagnostic review and recurring tracking | V1 product scope | Partial / requires inspection | Complete diagnostic-to-review-to-follow-up journey |
| Klaviyo human-approved email actions | V1 mandatory requirement | **Not independently verified complete** | Authorization, provider execution, duplicates and failures |
| Stripe subscriptions | Test pricing/integration scope | Production readiness unverified | Real billing entitlements and webhook lifecycle |
| Multi-tenant RLS across all routes | Architectural requirement and early scoped testing | Incomplete negative-security evidence | Cross-tenant tests for APIs, exports, jobs and actions |
| FR/EN and PDF outputs | V1 feature scope | Current completion not established here | Language, PDF content and localization acceptance checks |
| Operational readiness | Deployment and security roadmap | Not certified | Monitoring, logging, secrets and incident procedures |

## Status terminology

- **Reported implementation** — prior engineering record says work was completed, but this public portfolio is not a code audit.
- **Historical test** — a specific test observation was recorded at the time; not representative of present production.
- **Pending validation** — a real behavioral or deployment test is still needed.
- **Planned** — feature or engineering control is part of the design but not claimed operational.

## Minimum next acceptance journey

1. Install Shopify on a development store.
2. Complete authenticated onboarding and resolve the correct tenant/source.
3. Ingest customer/order events; review normalized counts and diagnostic results.
4. Preserve the initial snapshot and complete diagnostic review.
5. Prepare a Klaviyo recommendation action and require human approval.
6. Execute and confirm external status without duplicates.
7. Validate Stripe plan entitlements, tenant isolation and cancellation/reconnection paths.
8. Record reproducible results, failure cases and deployment scope.

A **successful build** is only one input into this journey.

[Development journal](../development-journal/README.md) · [Engineering challenges](engineering-challenges.md)
