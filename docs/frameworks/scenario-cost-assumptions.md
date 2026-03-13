# Scenario Cost Assumptions

## Purpose

This document translates the repository's general cost framework into scenario-specific assumptions that can support applied comparisons.

## Why Assumptions Need To Be Explicit

Weighted cost comparisons are only meaningful if the repository states what each unit of delay, human time, or downstream failure is assumed to cost. The goal is not perfect realism. The goal is transparent, revisable assumptions.

## Shared Assumption Types

Every scenario should declare assumptions for:

- direct model spend
- latency sensitivity
- human review minutes
- escalation capacity
- downstream failure cost
- acceptable quality threshold

## Scenario A: Code Generation and Repair

### Operational assumption

- each failed code output can create nontrivial debugging overhead
- executable verification is available
- human review is relatively expensive but high value

### Suggested initial assumptions

- quality gate: test pass required
- one human review event: 8 to 15 minutes
- unresolved failed episode: high downstream cost
- latency penalty: medium
- verification cost: low relative to debugging cost

### Interpretation

This scenario should usually favor policies that spend more upfront on verification if they sharply reduce debugging and failed handoff burden.

## Scenario B: Document Extraction and Back-Office Processing

### Operational assumption

- large task volume
- partial errors are common
- cleanup queues exist
- some fields may have compliance or audit sensitivity

### Suggested initial assumptions

- quality gate: target precision and recall or field-level F1
- one human review event: 2 to 6 minutes
- unresolved failed episode: medium to high downstream cost
- latency penalty: low to medium
- validation cost: low to medium

### Interpretation

This scenario often makes selective review attractive because blanket human QA is expensive at scale, but silent extraction errors can also accumulate hidden correction cost.

## Scenario C: Classification and Routing Operations

### Operational assumption

- episodes are short
- model spend is low relative to volume
- queue load from escalation can quickly become the bottleneck

### Suggested initial assumptions

- quality gate: target accuracy or F1 above operating threshold
- one human review event: 1 to 4 minutes
- unresolved failed episode: medium downstream cost with some high-priority outliers
- latency penalty: medium to high for urgent routing contexts
- verification cost: usually low unless human confirmation is required

### Interpretation

This scenario is often most sensitive to escalation rate and queue saturation rather than per-call API spend.

## Suggested Weighting Profiles

The repository should not use one universal weighted-cost function. It should compare a small number of scenario-aligned profiles.

### Profile 1: Automation-Heavy Volume Setting

Best match:

- classification
- high-volume extraction

Emphasis:

- API spend
- latency
- escalation rate

De-emphasis:

- per-episode review depth

### Profile 2: Reliability-Critical Knowledge Work

Best match:

- code generation
- compliance-sensitive extraction

Emphasis:

- failure recovery cost
- human review value
- verification effectiveness

De-emphasis:

- small differences in first-pass latency

### Profile 3: Mixed Operations Setting

Best match:

- teams balancing throughput and correctness

Emphasis:

- direct spend
- human minutes
- retries
- moderate failure penalty

## Sensitivity Analysis Rule

Every scenario-weighted result should be accompanied by at least one sensitivity check:

- faster vs slower human review
- lower vs higher downstream failure penalty
- narrower vs wider quality threshold

If rankings change under small assumption shifts, the project should report that instability explicitly.

## Recommended Research Use

This document should be used alongside cost-vector reporting. It should inform weighted comparisons, not replace transparent raw metrics.
