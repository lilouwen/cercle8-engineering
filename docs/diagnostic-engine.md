# Customer diagnostics and explainable decisions

[← Documentation](README.md) · [← Repository](../README.md)

## Engineering objective

Turn heterogeneous customer-commerce inputs into a stable, explainable analysis a merchant can review before taking action.

The product scope includes customer health, retention-risk segmentation, dormant/VIP customers, a layered decision structure, early signals, diagnostic snapshots and follow-up reporting.

## Conceptual processing stages

~~~mermaid
flowchart LR
    Sources["Shopify / Klaviyo / CSV"] --> Normalize["Normalize events and identities"]
    Normalize --> Metrics["Customer metrics"]
    Metrics --> Snapshot["Diagnostic snapshot"]
    Snapshot --> Segments["Segments and signals"]
    Segments --> Recommendations["Explainable recommendations"]
    Recommendations --> Human["Merchant review"]
    Human --> Action["Proposed action"]
~~~

The diagram represents **design intent**, not a publication of proprietary scoring thresholds, full business logic or a current production workflow.

## Difficult questions

**Data completeness.** A CSV test import is not the same as a connected store with order histories, missing values, refunds or duplicate identities.

**Repeatability.** Recomputing a diagnostic should not silently rewrite the meaning of a previous approved report. Snapshots provide a historical boundary.

**Explainability.** Users should understand which signals informed a recommendation without exposing sensitive implementation rules.

**Review and activation.** Initial diagnostic, human review, activation of recurring analysis and subsequent updates are separate lifecycle events.

**Action separation.** A recommendation is an analysis result. Sending an email or message is a privileged external operation that should be handled separately.

## Historical test observations

A June 2026 development note recorded a Shopify-ingestion test dataset with **76 customers**, **277 customer events** and **76 customer metrics**, followed by diagnostic processing. One normalized sample purchase event was also noted.

This is a **historical test-environment observation**, not a claim of live commercial traffic, scale, stability or customer outcomes.

## Validation criteria

- [ ] Controlled, repeatable inputs lead to traceable diagnostic outputs.
- [ ] Empty, partial and inconsistent datasets have defined behaviors.
- [ ] Duplicate event imports do not silently skew counts.
- [ ] Tenant/source scope is preserved throughout calculation.
- [ ] Report snapshots remain immutable or explicitly versioned.
- [ ] Recommendations can be explained and reviewed.
- [ ] Monthly updates preserve history, rather than replacing the initial result.
- [ ] The execution layer cannot run an action before authorization.

The proprietary algorithm remains private. A strong technical portfolio explains interfaces, failure handling and reproducibility without disclosing intellectual property.

[Action execution](klaviyo-execution.md) · [Validation ledger](validation-status.md)
