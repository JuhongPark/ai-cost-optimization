# Benchmark Report Template

## Purpose

This template defines the minimum structure for a single-benchmark result report in the first empirical cycle.

## 1. Benchmark Context

- benchmark id
- task family
- linked industry scenario
- declared quality threshold
- in-scope policies

## 2. Key Result

State the main outcome in one sentence:

- which policy won under threshold-constrained comparison
- whether weighted ranking agreed or disagreed

## 3. Threshold Feasibility

Report:

- which policies met the threshold
- which policies failed it
- which quality metric was binding

## 4. Cost Vector Comparison

For each in-scope policy, report:

- direct cost
- latency
- human minutes
- retries
- verification count
- tool usage

## 5. Weighted Scenario Comparison

Report weighted ranking under the linked scenario profile.

Required note:

- whether the ranking changed under sensitivity analysis

## 6. Interpretation

Answer:

- what cost component decided the winner
- whether selective HITL was competitive
- whether routing, retry, verification, or stronger models had the highest leverage

## 7. Risks and Validity Limits

- benchmark-specific grading limitations
- places where assumptions may dominate the result
- open questions for the next cycle
