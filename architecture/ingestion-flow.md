# Data ingestion → diagnostics

[← Architecture index](README.md)

~~~mermaid
flowchart LR
    Sources["Shopify / CSV / connected source"] --> Normalize["Source adapter and normalization"]
    Normalize --> Scope["Resolve tenant and data source"]
    Scope --> Events["Customer events / identities"]
    Events --> Metrics["Derived customer metrics"]
    Metrics --> Snapshot["Diagnostic snapshot"]
    Snapshot --> Segments["Segments and signals"]
    Segments --> Rec["Recommendations"]
    Rec --> Review["Merchant review"]
~~~

The model must address duplicate events, inconsistent identifiers, missing data, historical snapshots and authorization.

**Historical test record (June 2026):** 76 test customers, 277 customer events and 76 customer metrics. These are not production traffic statistics or an independently reproduced benchmark.

[Diagnostics guide](../docs/diagnostic-engine.md) · [Journal](../development-journal/2026-06-data-and-tenant-tests.md)