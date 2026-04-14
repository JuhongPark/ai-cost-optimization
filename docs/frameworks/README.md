# Frameworks

This directory stores evaluation frameworks, metric definitions, and cost models used in the research.

Suggested reading order: cost taxonomy → evaluation framework → evaluation objectives → policy design space → strategy taxonomy → logging schema → cost aggregation → failure taxonomy → scenario cost assumptions.

## Foundations

- [`cost-taxonomy.md`](cost-taxonomy.md): direct-cost vs indirect-cost framework for AI problem solving.
- [`evaluation-framework.md`](evaluation-framework.md): quality-constrained total-cost evaluation framework.
- [`evaluation-objectives.md`](evaluation-objectives.md): candidate optimization objectives and when to use them.

## Policy and Strategy Space

- [`policy-design-space.md`](policy-design-space.md): explicit design axes for model, routing, verification, retry, tools, and oversight.
- [`strategy-taxonomy.md`](strategy-taxonomy.md): categories of optimization strategies compared across experiments.

## Operational Schemas

- [`logging-schema.md`](logging-schema.md): episode-level logging schema for benchmark runs.
- [`cost-aggregation.md`](cost-aggregation.md): aggregation and reporting rules for cost metrics.
- [`failure-taxonomy.md`](failure-taxonomy.md): shared failure classes for episode analysis.

## Applied Assumptions

- [`scenario-cost-assumptions.md`](scenario-cost-assumptions.md): scenario-specific assumptions for weighted cost comparisons.
