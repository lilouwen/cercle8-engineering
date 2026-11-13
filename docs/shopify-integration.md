# Shopify integration — embedded app and standalone SaaS

[← Documentation](README.md) · [← Repository](../README.md)

## Engineering problem

Cercle 8 can be reached as a standalone SaaS or as a Shopify app. These contexts do not automatically share identity, browser sessions, application permissions or lifecycle events.

A merchant should not be forced into unrelated workspaces merely because they move between the app and the SaaS experience.

## Domain identity

The recorded architectural mapping is:

**Shop domain → Tenant ID → Data source ID**

This separates the external store identity from Cercle 8's business ownership and from the specific connected ingestion source.

~~~mermaid
sequenceDiagram
    participant M as Merchant
    participant S as Shopify context
    participant A as Cercle 8 application
    participant O as Shopify session store
    participant D as Supabase business data
    M->>S: Open installed app
    S->>A: Authenticated app context
    A->>O: Resolve valid Shopify session
    A->>D: Resolve shop → tenant → source
    D-->>A: Tenant-scoped business context
    A-->>M: Authorized app view
~~~

**Conceptual sequence**, not a claim that every real OAuth/navigation scenario has passed tests.

## Architectural changes recorded in October 2026

- The business-data model was consolidated around Supabase.
- Shopify sessions remained persisted separately through Prisma.
- The Shopify application pages and diagnostic/recommendation/report paths were migrated toward the shared model.
- An embedded app configuration and privacy compliance webhook setup were recorded.
- Static checks (lint, type-check, build, Prisma validation) were reported as passing.

The same October record explicitly noted **no live OAuth test or automated app end-to-end test** at that stage. The Shopify development-store journey, deployment configuration, secrets and edge function behavior were still to be validated.

## Why separate sessions and business data?

| Concern | Why it matters |
|---|---|
| Shopify session | Expiry, OAuth installation state and API authentication |
| Tenant | Persistent ownership of Cercle 8 business resources |
| Data source | Connection-specific ingestion and deletion scope |
| SaaS user | Individual sign-in, workspace membership and roles |

Coupling all four concerns to a single session record creates fragile links between authentication lifetime and business ownership.

## Integration failure scenarios

- OAuth succeeds but tenant/source mapping is absent.
- Store is uninstalled then reinstalled.
- Existing SaaS account connects a previously known shop.
- Store authorization changes while background jobs are pending.
- External API rate limits, pagination or field availability change.
- Connection is removed while reports or data snapshots still exist.

Every scenario requires expected behavior, a reliable source of authority and tests.

## Completion criteria

- [ ] Real development-store install and OAuth flow
- [ ] Reinstall and reconnect without unexpected duplicate tenancy
- [ ] Authorized access across standalone SaaS and embedded context
- [ ] Correct ingestion and error handling for Shopify data
- [ ] Privacy webhook delivery/processing in deployed environment
- [ ] Verified tenant separation, including hostile/mismatched contexts
- [ ] Clear uninstall versus account cancellation behavior

[Decision: sessions](../engineering-decisions/0002-shopify-sessions.md) · [Shopify flow diagram](../architecture/shopify-tenant-flow.md)
