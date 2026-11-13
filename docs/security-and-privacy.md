# Security, privacy and failure boundaries

[← Documentation](README.md) · [← Repository](../README.md)

## Why this matters

The application can hold business records and customer-commerce information for different tenants. Security must be enforced at data access, application routes, integrations, webhooks, background processing and outbound actions.

This document describes **design considerations and recorded implementation work**, not a completed penetration test or compliance certification.

## Principal trust boundaries

| Boundary | Failure mode | Necessary control |
|---|---|---|
| SaaS user → tenant data | Cross-tenant read/write | Membership and RLS tests, server-side authorization |
| Shopify context → business model | Wrong store associated with tenant | Explicit store-to-tenant/source resolution |
| Third-party webhook → database | Forged or replayed event | Verify event signature, replay/idempotency policy |
| Integration secrets → runtime | Token exposure | Server-side secret storage, restricted access, rotation |
| Diagnostic → outbound action | Unapproved customer messaging | Merchant review and authorization |
| Billing → entitlements | Subscription mismatch | Verified Stripe events and authoritative plan state |
| User exports → reports | Data leakage | Tenant-scoped export and redaction |

## Privacy lifecycle: different scopes, different consequences

The October 2026 work described distinct Shopify integration cleanup paths:

- **Uninstall:** detach the Shopify integration and its sessions/secrets without automatically destroying unrelated Cercle 8 history.
- **Customer redaction:** restrict deletion to the targeted Shopify identities/events/metrics covered by the request.
- **Shop redaction:** scope removals to the relevant connected Shopify source.

This distinction matters because an external integration can be removed without being the same thing as deleting the entire SaaS business account.

**Verification requirement:** ensure signed webhook authenticity, scoped deletes, idempotency, failure handling and expected downstream data relationships work in the deployed environment.

## Evidence currently missing from the public record

- Comprehensive cross-tenant negative security tests.
- Real deployed Shopify compliance-webhook acceptance results.
- Authorization and idempotency tests for recommendation execution.
- Production-oriented secrets rotation and logging review.
- Full billing entitlement and webhook replay handling tests.

## Repository publication policy

No proprietary diagnostic source code, customer or payment data, credential material, private endpoints, active webhook secrets, database dumps, application environment variables or sensitive screenshots.

Use synthetic examples for diagrams and explanations. A GitHub case study is not a safe location for raw logs.

[Multi-tenancy](multi-tenancy.md) · [Shopify privacy ADR](../engineering-decisions/0004-scoped-shopify-privacy.md)
