# Multi-tenancy and authorization

[← Documentation](README.md) · [← Repository](../README.md)

## Problem

A B2B SaaS handles resources owned by different businesses. Reusing infrastructure does not authorize users from one organization to inspect or change the resources of another organization.

The hard part is not attaching a tenant ID to a table. It is ensuring that **every route, background process, data-source import and external action** has a well-defined tenant boundary.

## Conceptual relationship

~~~mermaid
erDiagram
    TENANT ||--o{ MEMBERSHIP : has
    USER ||--o{ MEMBERSHIP : joins
    TENANT ||--o{ DATA_SOURCE : owns
    DATA_SOURCE ||--o{ CUSTOMER_IDENTITY : imports
    DATA_SOURCE ||--o{ CUSTOMER_EVENT : generates
    TENANT ||--o{ DIAGNOSTIC_SNAPSHOT : receives
    TENANT ||--o{ RECOMMENDATION : owns
    RECOMMENDATION ||--o{ PROPOSED_ACTION : leads_to
~~~

**Illustrative domain diagram.** It is deliberately not an export of the private schema. Real table names, keys and constraints may differ.

## Authentication versus authorization

- **Authentication:** who is the current user or connected Shopify context?
- **Tenant resolution:** which company and connected source does this request represent?
- **Authorization:** may that actor perform this operation on the exact resource?
- **Enforcement:** RLS, server-side checks and scoped integration behavior must agree.

A successful Shopify OAuth response cannot be treated as permission to access arbitrary records in Supabase. Likewise, a logged-in SaaS user may belong to zero, one or several workspaces.

## Historical evidence

A June 2026 test record described an authenticated user mapped to a demo tenant, a tenant-scoped dashboard, one connected source, an import and a small set of imported rows. This supports a historical **scoped-flow test**, not comprehensive cross-tenant isolation coverage.

## Validation plan

| Boundary | Acceptance criterion |
|---|---|
| Tenant A versus Tenant B | A cannot read, update or trigger actions for B |
| Missing membership | Denied by default |
| Invalid tenant identifier | Server rejects instead of silently choosing another tenant |
| Shopify store mapping | Store resolves only to its authorized tenant/data source |
| Data ingestion | Rows remain scoped to the owning source and tenant |
| Background jobs | Privileged execution resolves an explicit tenant, rather than bypassing scope |
| Export / PDF | Generated document contains only authorized tenant data |
| Recommendations | Action belongs to the same tenant as source diagnostic |
| Account or store disconnect | Affects only the intended integration and resources |

Documented implementation work needs a test ledger, not only a schema review. Detailed SQL policies and access tokens are intentionally excluded.

[Shopify identity flow](../architecture/shopify-tenant-flow.md) · [Security](security-and-privacy.md)
