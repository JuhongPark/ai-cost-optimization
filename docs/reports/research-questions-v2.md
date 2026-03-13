# Research Questions V2

## Purpose

This document narrows the repository's broad thesis into a smaller set of investigation-ready research questions.

## Primary Research Question

Under explicit quality thresholds, which AI execution policy achieves the lowest total cost for a given task family?

This question keeps the repository focused on decision-making rather than generic capability comparison. It also matches the episode-level logging and benchmark structure already present in the project.

## Secondary Research Questions

### 1. When does selective human oversight beat full automation?

This question tests the repository's core claim that human involvement should be treated as a priced resource rather than a binary design preference.

Key sub-questions:

- At what failure rate does selective escalation become cheaper than repeated AI retries?
- How sensitive is the answer to human review time and queue constraints?
- Which escalation trigger works best: confidence, verifier failure, retry exhaustion, or policy default?

### 2. Which indirect-cost components dominate in practice?

This question distinguishes between workflows where API spend is the main issue and workflows where retries, verification, or human review become the real bottleneck.

Key sub-questions:

- When do retries erase the savings of a cheaper model?
- When does verification prevent enough downstream failure to pay for itself?
- Which task families create the largest human-minute burden?

### 3. How task-specific is the optimal policy?

This question asks whether a single policy family can generalize across tasks or whether each task family needs its own cost strategy.

Key sub-questions:

- Does coding favor verifier-heavy policies more than classification?
- Does extraction benefit more from tools and structured validation than from stronger base models?
- Do low-latency classification tasks justify routing more cleanly than high-variance workflows?

### 4. What is the right optimization objective?

This question evaluates whether weighted total cost should be the default objective or only one view among several reporting modes.

Key sub-questions:

- When is a cost vector better than a scalar score?
- When should the project use threshold-constrained optimization instead of weighted aggregation?
- How much do policy rankings change under different weight assumptions?

## Working Hypotheses

The current investigation should treat the following as hypotheses to test rather than conclusions:

- Selective HITL will often outperform both full automation and human-first handling on medium-difficulty, medium-risk tasks.
- The best policy will vary by task family; there will not be a single universal winner.
- Indirect cost will often change the ranking produced by direct cost alone.
- Verification and routing will be higher-leverage early policy levers than complex multi-step orchestration.

## Questions to Deprioritize for Now

These are valid but should not lead the first research cycle:

- pure serving-efficiency optimization
- model pretraining efficiency
- frontier-model capability scaling
- organization-wide platform cost allocation

They matter, but they are downstream of the workflow-level decision framework this repository is trying to establish.

## Recommended Decision Rule

The first empirical cycle should answer four concrete questions for each benchmark:

1. What quality threshold must the policy satisfy?
2. Which policy classes satisfy it?
3. What direct and indirect costs do they incur?
4. Which policy is cheapest under the declared objective?
