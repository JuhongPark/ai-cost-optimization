# ai4-cost-optimization

## Philosophy

This research starts from a working assumption: AI's problem-solving capability is already strong enough for many practical tasks, and it will likely continue to improve.

Given that assumption, the central question is not AI's problem-solving capability itself, but how to evaluate AI problem solving from a cost perspective and optimize it. This repository evaluates AI usage primarily through a cost lens rather than a capability lens, treating problem solving itself as a cost question measured by the total resources required to reach an acceptable answer, and focuses on methods, frameworks, and experiments that optimize the cost of applying AI in real-world settings.

## Start Here

If you are new to the repository, start with these three documents in order:

1. [`docs/research-plan.md`](docs/research-plan.md) — the research question, thesis, and three-month program.
2. [`docs/frameworks/cost-taxonomy.md`](docs/frameworks/cost-taxonomy.md) — the direct-cost vs indirect-cost split that everything else builds on.
3. [`docs/experiments/first-empirical-cycle-plan.md`](docs/experiments/first-empirical-cycle-plan.md) — what is actually being run in the first empirical cycle.

Then [`docs/README.md`](docs/README.md) is the full documentation navigation hub.

## Structure

- [`docs/`](docs/README.md) — research documentation (plan, frameworks, experiments, references, reports).
- [`configs/`](configs/README.md) — YAML configs for benchmarks, policies, providers, scenarios, and studies.
- [`benchmarks/`](benchmarks/README.md) — benchmark task data for the real execution layer.
- [`schemas/`](schemas/README.md) — canonical episode log schema.
- [`scripts/`](scripts/README.md) — validation, stub execution, aggregation, and synthesis helpers.
- [`results/`](results/README.md) — raw logs, aggregate tables, figures, and benchmark reports.

## Local Cycle

The repository can run a full local first-cycle prototype:

1. generate deterministic stub episode logs from benchmark and policy configs
2. validate raw logs against the episode schema
3. aggregate results into tables and benchmark summaries
4. synthesize a cross-benchmark final summary

It also includes a provider-backed execution layer with:

1. benchmark task loading from `benchmarks/`
2. provider adapters from `configs/providers/`
3. a real runner that can execute through an offline heuristic provider or an OpenAI-compatible endpoint
