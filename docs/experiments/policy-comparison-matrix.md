# Policy Comparison Matrix

## Purpose

This document turns the first empirical cycle into a benchmark-by-benchmark comparison matrix.

## Comparison Matrix

| Benchmark family | Scenario | Must-compare policies | Main decision question | Expected dominant cost |
| --- | --- | --- | --- | --- |
| coding | code generation and repair | strong single pass, cheap single pass, cheap verifier HITL, verifier-gated HITL, human-first | is upfront verification cheaper than strong-first generation or human-heavy handling? | debugging and recovery |
| classification | classification and routing ops | strong single pass, cheap single pass, difficulty routing, confidence-gated HITL, human-first | do routing and selective deferral lower cost without queue overload? | escalation load and latency |
| extraction | document extraction ops | strong single pass, cheap single pass, tool-assisted extraction, verifier-gated HITL, human-first | is structured validation cheaper than stronger first-pass generation or blanket review? | cleanup burden and silent error risk |

## Policy Roles

### Baseline policies

- `cheap_model_single_pass`: lowest-direct-cost baseline
- `strong_model_single_pass`: highest-quality simple baseline
- `human_first`: oversight-heavy reference point

### Frontier-shifting policies

- `difficulty_routing`: tests whether adaptive model selection shifts the frontier
- `cheap_model_verifier_hitl`: tests whether verification plus selective escalation beats stronger default models
- `confidence_gated_hitl`: tests whether confidence-aware triage lowers total cost
- `verifier_gated_hitl`: tests whether explicit rejection signals produce cheaper oversight allocation
- `tool_assisted_extraction`: tests whether tool usage reduces total extraction burden

## Decision Rules By Benchmark

### Coding

Prefer the policy that:

- satisfies the test-based quality gate
- minimizes recovery and debugging burden
- keeps human escalation limited to hard failures

### Classification

Prefer the policy that:

- satisfies the accuracy threshold
- keeps escalation rate operationally manageable
- preserves low latency for routine cases

### Extraction

Prefer the policy that:

- satisfies F1 and secondary precision-recall thresholds
- reduces silent structured-output errors
- avoids large cleanup queues

## Research Use

This matrix should be treated as the operational checklist for the first empirical cycle. If a policy is not in this table, it is out of scope unless the study manifest is revised.
