# ai-cost-optimization

## Philosophy

This research starts from a working assumption: AI's problem-solving capability is already strong enough for many practical tasks, and it will likely continue to improve.

Given that assumption, the central question is not AI's problem-solving capability itself, but how to evaluate AI problem solving from a cost perspective and optimize it. This repository evaluates AI usage primarily through a cost lens rather than a capability lens, treating problem solving itself as a cost question measured by the total resources required to reach an acceptable answer, and focuses on methods, frameworks, and experiments that optimize the cost of applying AI in real-world settings.

## Structure

- `docs/research-plan.md`: core research plan
- `docs/frameworks/`: evaluation frameworks and cost models
- `docs/experiments/`: experiment designs and results
- `docs/references/`: references and reading notes
- `docs/reports/`: synthesis documents and practical guidance
- `schemas/`: machine-readable schemas for experiment artifacts
- `configs/`: benchmark and policy configurations
- `scripts/`: validation, stub execution, and aggregation helpers
- `results/`: raw logs, aggregate tables, figures, and summaries

## Local Cycle

The repository can run a full local first-cycle prototype:

1. generate deterministic stub episode logs from benchmark and policy configs
2. validate raw logs against the episode schema
3. aggregate results into tables and benchmark summaries
4. synthesize a cross-benchmark final summary
