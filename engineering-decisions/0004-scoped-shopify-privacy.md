# ADR-0004 — Privacy deletion must respect data-source boundaries

- **Recorded:** October 2026
- **Status:** Implementation notes and static checks reported; deployed callback verification pending

## Problem

Shopify uninstallation or privacy requests must not result in arbitrary destruction of unrelated Cercle 8 tenants, data sources or diagnostic history.

## Documented design

- **Uninstall:** disconnect the Shopify integration and its associated session/secrets.
- **Customer redaction:** scope deletion to the requested Shopify customer identities and related records.
- **Shop redaction:** scope deletion to the relevant Shopify source.
- **Data request:** handle a customer data request with appropriate source ownership.

## Technical consequences

Deletion logic spans shop identity, tenant ownership, source, customer events and metrics, sessions and downstream analysis. Correctly verifying request authenticity, replay/idempotency and relationship cleanup is essential.

A completed lint/build does not prove production webhook security.

[Security and privacy](../docs/security-and-privacy.md) · [Shopify integration](../docs/shopify-integration.md)