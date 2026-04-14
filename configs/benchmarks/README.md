# Benchmark Configs

This directory stores benchmark-level configuration files. Each file declares task metadata, acceptance thresholds, and links to the underlying task data in [`../../benchmarks/`](../../benchmarks/README.md).

- [`coding-human-eval.yaml`](coding-human-eval.yaml): coding benchmark with test-based correctness for early cost experiments.
- [`classification-mmlu-subset.yaml`](classification-mmlu-subset.yaml): classification-style benchmark for routing and confidence-based escalation studies.
- [`extraction-structured-fields.yaml`](extraction-structured-fields.yaml): structured extraction benchmark for tool use and selective review policies.
