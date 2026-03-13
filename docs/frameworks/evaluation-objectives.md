# Evaluation Objectives

## Purpose

This document defines the candidate optimization objectives that should be compared in this repository before settling on a default score.

## Why This Matters

The repository already treats AI usage as a quality-constrained total-cost problem. The remaining question is how that decision rule should be operationalized so that policy comparisons are both transparent and decision-ready.

## Objective 1: Threshold-Constrained Cost Minimization

Definition:

- first require that a policy meets the task-level quality threshold
- then choose the policy with the lowest total cost among the feasible set

Strengths:

- matches real deployment behavior
- prevents low-quality cheap policies from looking attractive
- easy to explain to practitioners

Weaknesses:

- loses information about near-threshold policies
- depends heavily on threshold selection

Recommended use:

- default decision rule for benchmark winners

## Objective 2: Explicit Cost Vector Reporting

Definition:

- report quality, direct spend, latency, retries, verification load, and human minutes separately

Strengths:

- maximizes transparency
- avoids hiding tradeoffs inside one scalar
- supports cross-team discussion when priorities differ

Weaknesses:

- does not by itself choose a winner
- harder to summarize in one headline metric

Recommended use:

- default reporting layer for all experiments

## Objective 3: Weighted Total Cost

Definition:

- combine cost components into one declared scalar objective

Example:

`weighted_total_cost = a*money + b*latency + c*human_minutes + d*retries + e*verification`

Strengths:

- useful when a deployment setting has a real preference structure
- produces a crisp ranking
- enables sensitivity analysis

Weaknesses:

- highly assumption-dependent
- can make arbitrary weights look more objective than they are

Recommended use:

- scenario-specific comparison, not the only reporting mode

## Objective 4: Pareto Frontier Analysis

Definition:

- compare policies by whether one dominates another on quality and cost dimensions without forcing a single scalar

Strengths:

- preserves tradeoff structure
- useful when different teams value money, latency, and human load differently

Weaknesses:

- harder to communicate as a final recommendation
- many policies can remain non-dominated

Recommended use:

- secondary analysis for policy pruning and discussion

## Objective 5: Expected Cost Under Failure Risk

Definition:

- estimate total expected cost after including the downstream consequences of failure or escalation

Useful examples:

- customer support misrouting
- bad extraction requiring manual correction
- code generation creating debugging overhead

Strengths:

- closer to operational reality
- highlights hidden costs from low-quality automation

Weaknesses:

- requires more domain assumptions
- harder to benchmark consistently across tasks

Recommended use:

- domain-specific case studies and later-stage applied work

## Recommended Framework for This Repository

The project should use a layered objective stack rather than a single score:

1. explicit quality threshold as a hard gate
2. cost vector reporting as the default presentation
3. weighted total cost as a scenario-specific ranking tool
4. Pareto frontier analysis as a robustness check

## Research Questions Created by This Framework

- How often does weighted total cost disagree with threshold-gated ranking?
- Which task families are most sensitive to weight changes?
- When do human minutes, not API dollars, determine the winner?
