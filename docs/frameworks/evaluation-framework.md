# Evaluation Framework

## Purpose

This document defines the first version of the evaluation framework for AI cost optimization research in this repository.

## Core Principle

AI problem solving should be evaluated as a quality-constrained total-cost process. A system is better when it reaches the required level of task quality with lower total cost.

## Unit of Analysis

The primary unit of analysis is a **problem-solving episode**.

A problem-solving episode begins when a task instance is given to the system and ends when one of the following occurs:

- the system reaches an acceptable answer
- the system fails and stops
- the task is escalated to a human
- the cost budget is exhausted

This definition is important because a single answer may involve multiple model calls, retries, tools, verifiers, and human checks.

## Evaluation Dimensions

Each episode should be evaluated along four dimensions:

### 1. Quality

Quality measures whether the outcome satisfies the task requirement.

Representative quality metrics:

- correctness
- success rate
- pass@k
- precision, recall, or F1
- human acceptance rate

### 2. Direct Cost

Direct cost measures the resources spent directly while executing the system.

Primary direct-cost metrics:

- model or API spend
- input tokens
- output tokens
- tool or external API spend
- latency

### 3. Indirect Cost

Indirect cost measures the resources required to make the episode usable and reliable in practice.

Primary indirect-cost metrics:

- human intervention count
- human review time
- retry count
- verification count
- recovery overhead

### 4. Policy Complexity

Policy complexity measures how complicated the execution strategy is.

Representative complexity indicators:

- number of decision points
- number of routing branches
- number of tool types
- number of fallback paths

This is a secondary measure, but it matters because some cost-saving policies may be difficult to maintain operationally.

## Reporting Modes

The framework supports two reporting modes.

### Mode A: Explicit Cost Vector

Report cost as a vector rather than forcing a single scalar.

Example:

- quality = 0.91 success rate
- model spend = $0.018 per task
- latency = 6.4 seconds
- human touches = 0.07 per task
- retries = 1.3 per task

This mode is best for transparency.

### Mode B: Weighted Total Cost

When needed, report a weighted total cost using an explicitly declared function:

`TotalCost = a(MonetaryCost) + b(Latency) + c(HumanOversight) + d(Retries) + e(ToolCost)`

This mode is best for comparing policies under a chosen deployment setting.

## Quality Constraint Rule

No system should be treated as cost-efficient unless it satisfies a predefined minimum quality threshold for the task category.

Example thresholds:

- coding: must pass the test suite
- information extraction: must exceed target precision and recall
- classification: must exceed target accuracy or F1
- agent workflow: must exceed target completion rate

## Comparison Template

Each comparison should be structured around the same questions:

1. What quality threshold must be met?
2. What direct cost is required to meet it?
3. What indirect cost is required to meet it?
4. Which strategy reaches the threshold at the lowest total cost?
5. Which cost component dominates the final result?

## Baseline Policies

All benchmark comparisons should include at least the following policies:

- strong-model single pass
- cheap-model single pass
- routed policy
- retry-enabled policy
- verification-enabled policy

In addition, the framework should explicitly compare three policy classes:

- full automation
- selective human-in-the-loop
- human-first or immediate escalation

This comparison is necessary because indirect-cost optimization is not equivalent to eliminating human oversight.

## Human Oversight Allocation Rule

Human review should be treated as a decision variable inside the policy, not as an external exception. For any task family, the evaluation should ask:

1. When is automation sufficient?
2. When does selective escalation reduce total cost?
3. When does human-first handling outperform repeated AI failure and recovery?

## Failure Accounting

Failure should not disappear inside averages. Episodes that fail must still be counted and categorized.

Minimum failure categories:

- wrong final answer
- timeout or budget exhaustion
- tool failure
- verifier failure
- human escalation
- unrecovered multi-step failure

## Decision Rule for This Repository

The repository should prefer cost-quality frontiers over single-score leaderboards. Weighted total-cost scores can be added later for specific deployment scenarios, but the default reporting mode should preserve visibility into direct versus indirect costs.
