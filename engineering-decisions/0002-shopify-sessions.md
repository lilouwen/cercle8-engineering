# ADR-0002 — Shopify session persistence is not business ownership

- **Recorded:** 20 October 2026
- **Status:** Historical design/implementation reported; real session tests outstanding

## Problem

Shopify sessions can expire, be revoked or be reissued. A SaaS tenant and historical diagnostics have longer lifecycles. Using a session record as the main business record would create fragile coupling.

## Decision

Keep Shopify Session persistence through Prisma while Supabase remains the source of truth for tenants and business data.

## Consequences

- A session authenticates a Shopify integration context but does not authorize arbitrary tenant access.
- The app must resolve and validate shop-to-tenant-to-source ownership.
- Reinstallation, disconnection, stale sessions and standalone-to-embedded transitions require explicit tests.

## Acceptance criteria

- [ ] Development-store OAuth
- [ ] Expired and revoked sessions handled correctly
- [ ] Reconnect without unexpected duplicate tenant
- [ ] Invalid or mismatched tenant mapping denied
- [ ] Store uninstall does not indiscriminately remove unrelated SaaS history

[Identity sequence](../architecture/shopify-tenant-flow.md) · [Tenant security](../docs/multi-tenancy.md)