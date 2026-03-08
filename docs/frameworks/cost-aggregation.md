# Cost Aggregation

## Purpose

This document defines how raw episode logs should be aggregated into research metrics.

## Reporting Layers

Research outputs in this repository should report results at three layers:

### 1. Raw Component Layer

Report disaggregated metrics:

- model spend
- tool spend
- token usage
- latency
- retries
- human minutes
- verification count
- recovery steps

### 2. Cost Vector Layer

Report a cost vector per policy:

- average direct monetary cost per episode
- average total latency per episode
- average human minutes per episode
- average retries per episode
- average verification steps per episode
- threshold-satisfying success rate

### 3. Weighted Total-Cost Layer

When scenario-specific comparison is needed, compute:

`WeightedTotalCost = a * direct_cost_usd + b * latency_seconds + c * human_minutes + d * retries + e * tool_cost_usd + f * recovery_steps`

The coefficients must be declared alongside every table or figure that uses this score.

## Aggregation Rules

- failed episodes still count toward average cost
- cost should be reported both per episode and per successful episode
- human escalation should remain visible as both a rate and a cost term
- retries should be counted beyond the first attempt only
- tool cost should be reported separately before inclusion in total direct cost

## Minimum Output Table

Each benchmark comparison should include:

| Policy | Quality threshold met | Success rate | Direct cost / episode | Direct cost / success | Latency / episode | Human minutes / episode | Retries / episode | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Frontier Reporting

The default analytical view should be a frontier rather than a single ranking. A policy is useful when it offers one of the following:

- lower cost at the same quality level
- higher quality at the same cost level
- lower indirect cost at the same direct cost and quality level

## Interpretation Rule

No policy should be called better by default unless it is clear which cost component improved and which constraints remained fixed.
