# Lessons learned

[← Documentation](README.md) · [← Repository](../README.md)

## 1. One source of truth is an architectural constraint

The Shopify/SaaS convergence work reinforced that shared business identity and data ownership are more important than preserving the convenience of two separate models.

## 2. Sessions should not own long-lived business state

An integration token and session can expire or be revoked. Customer diagnostics and approved historical reports have a different lifecycle.

## 3. A green build is not an integration acceptance test

In October 2026, static checks were reported as passing while real Shopify OAuth and deployed webhook execution remained to be tested. That distinction is now explicit in the case study.

## 4. Privacy requirements affect the schema

Store uninstall, customer redaction and whole-source redaction represent different scopes. Deletion logic needs accurate entity ownership and explicit non-deletion of unrelated data.

## 5. An outbound action needs stronger guarantees than a recommendation

Human approval, idempotency, traceability and provider error handling are separate engineering responsibilities. Klaviyo execution is treated as a V1 completion requirement, not as an already proven flow.

## 6. Solo development requires aggressive prioritization

Each new integration affects authentication, data models, monitoring and quality assurance. The strongest milestones are coherent verified journeys, not the number of individual features implemented.

## 7. Evidence makes technical storytelling credible

Architecture diagrams explain intent; real tests and dated validation records demonstrate behavior. Both matter, but they should never be confused.

[Validation ledger](validation-status.md) · [Solo engineering](solo-development.md)
