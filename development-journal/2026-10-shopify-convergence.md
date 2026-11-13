# 20 October 2026 — Shopify architecture convergence

**Evidence class:** Historical development record and static checks

## Problem

Unify Shopify embedded application identity with the standalone SaaS business model without competing copies of customer and diagnostic data.

## Work described

- Supabase adopted as the shared business source of truth.
- Shop domain → tenant ID → data source ID mapping documented.
- Prisma retained for Shopify Session records.
- Application, diagnostics, recommendation and report paths migrated toward the common model.
- Shopify compliance webhook handling prepared.

## Reported checks

- Lint: PASS
- Type-check: PASS
- Build: PASS
- Prisma validation: PASS

These checks were reported at the time; no code from the private commercial repository was executed to create this public case study.

## Remaining at that checkpoint

Real OAuth, development-store end-to-end flows, deployment secrets, webhook callback validation and cross-context access testing.

[← Journal](README.md) · [ADR-0001](../engineering-decisions/0001-supabase-source-of-truth.md)