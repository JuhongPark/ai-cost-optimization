# Documentation

This directory holds the research documentation for the AI cost optimization project. The spine is [`research-plan.md`](research-plan.md); every other document supports it.

## Layout

- [`research-plan.md`](research-plan.md) — objective, thesis, scope, research questions, and the three-month program.
- [`frameworks/`](frameworks/README.md) — cost model, evaluation framework, logging schema, policy design space, and optimization strategy taxonomy.
- [`experiments/`](experiments/README.md) — benchmark design, reusable policy templates, and the first empirical cycle plan.
- [`references/`](references/README.md) — prior work, gap analysis, human-oversight notes, and MIT and industry reading notes.
- [`reports/`](reports/README.md) — synthesis documents, reporting templates, and the forward-looking research backlog.

## Reading Order for a New Reader

1. Top-level [`README.md`](../README.md) for philosophy and repo shape.
2. [`research-plan.md`](research-plan.md) for the research question and the three-month program.
3. [`frameworks/cost-taxonomy.md`](frameworks/cost-taxonomy.md) and [`frameworks/evaluation-framework.md`](frameworks/evaluation-framework.md) for the working definitions.
4. [`experiments/first-empirical-cycle-plan.md`](experiments/first-empirical-cycle-plan.md) and [`experiments/policy-comparison-matrix.md`](experiments/policy-comparison-matrix.md) for what is actually being run.
5. [`reports/research-synthesis.md`](reports/research-synthesis.md) and [`reports/practitioner-guidance.md`](reports/practitioner-guidance.md) for the current synthesis and the operational takeaways.
6. [`references/industry-trends-2026.md`](references/industry-trends-2026.md) and [`references/industry-updates-2026-04.md`](references/industry-updates-2026-04.md) for the most recent external context.

## Where Related Code and Data Live

- [`../configs/`](../configs/README.md) — benchmark, policy, provider, scenario, and study configuration files.
- [`../benchmarks/`](../benchmarks/README.md) — benchmark task data for the real execution layer.
- [`../schemas/`](../schemas/README.md) — canonical episode log schema.
- [`../scripts/`](../scripts/README.md) — validators, stub runners, aggregators, and synthesis helpers.
- [`../results/`](../results/README.md) — raw logs, aggregate tables, figures, and benchmark reports.
