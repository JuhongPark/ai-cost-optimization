# Scenario Configs

This directory stores scenario-level assumptions for applied cost comparisons. Each scenario declares a quality gate, cost assumptions (human review minutes, latency sensitivity, downstream failure cost, verification cost), and a weighting profile used by the comparison scripts.

- [`code-generation-repair.yaml`](code-generation-repair.yaml): reliability-critical coding workflow where failed outputs create debugging and developer interruption cost.
- [`document-extraction-ops.yaml`](document-extraction-ops.yaml): high-volume structured extraction workflow with cleanup queues and selective review.
- [`classification-routing-ops.yaml`](classification-routing-ops.yaml): fast, high-volume routing workflow where queue load and escalation rate can dominate spend.
