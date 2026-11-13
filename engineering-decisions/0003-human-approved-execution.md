# ADR-0003 — Human approval before external execution

- **Status:** Mandatory V1 design; not independently verified complete

## Problem

A diagnostic recommendation is informational. A marketing send via Klaviyo can affect real customers and requires authorization, traceability and predictable failure handling.

## Decision

**Recommendation → Prepare → Preview → Human approval → Execute → Track.**

Klaviyo email execution is the first V1 delivery target. SMS and WhatsApp are future channel design considerations, not completed capabilities.

## Trade-offs

| Design | Benefit | Drawback |
|---|---|---|
| Automatic execution | Fast | Unintended actions and weaker control |
| Export-only | Simple | Poor integrated workflow |
| Approval gate | Auditable, authorized | More lifecycle states and retries |

## Acceptance criteria

- [ ] No send without approval
- [ ] Tenant and approver checks
- [ ] Preview content matches executed action
- [ ] Duplicate-safe retry behavior
- [ ] Provider errors and outcomes recorded

[Execution flow](../architecture/recommendation-flow.md) · [Klaviyo design](../docs/klaviyo-execution.md)