# First Empirical Cycle Plan

## Purpose

This document converts the repository's investigation framework into a concrete first empirical cycle.

## Goal

The first empirical cycle should not try to answer every research question at once. It should answer a small number of high-value questions with a stable, repeatable comparison set.

## Core Questions

### Question 1

Under a fixed quality threshold, which baseline policy class is cheapest for each benchmark family?

Why this comes first:

- it directly tests the main thesis of the repository
- it produces an interpretable result even with a small benchmark suite

Policies to compare:

- cheap-model single pass
- strong-model single pass
- selective HITL baseline
- human-first baseline

Benchmarks:

- coding
- classification
- extraction

## Question 2

Which policy lever changes the cost-quality frontier most: stronger models, routing, retry, or verification?

Why this comes second:

- it identifies where later research effort should go
- it helps avoid premature complexity

Policies to compare:

- strong-model single pass
- cheap-model single pass
- difficulty-based routing
- cheap-model retry
- cheap-model verifier HITL

Primary outputs:

- threshold-satisfying success rate
- direct cost
- human minutes
- retries
- weighted total cost under declared scenarios

## Question 3

When does selective human oversight become cheaper than either full automation or human-first handling?

Why this comes third:

- this is the strongest distinctive contribution of the repository
- it links the cost framework to realistic deployment decisions

Policies to compare:

- full automation
- confidence-gated HITL
- verifier-gated HITL
- human-first

Sensitivity variables:

- human review time
- escalation rate
- failure-recovery burden
- downstream failure cost

## Scope Boundaries

The first empirical cycle should exclude:

- serving-optimization-only comparisons
- large open-ended agent benchmarks
- training-time efficiency claims
- deployment-wide infrastructure allocation

These can be revisited after the workflow-level comparison frame is stable.

## Benchmark-by-Benchmark Focus

### Coding

Primary comparison:

- strong single pass vs cheap plus verification vs verifier-gated HITL

Main research concern:

- whether test-backed verification reduces total cost enough to beat stronger first-pass generation

### Classification

Primary comparison:

- cheap single pass vs strong single pass vs difficulty routing vs confidence-gated HITL

Main research concern:

- whether routing and selective deferral reduce cost without excessive escalation load

### Extraction

Primary comparison:

- strong single pass vs tool-assisted extraction vs verifier-gated or selective review policies

Main research concern:

- whether structured validation and cleanup-aware escalation outperform pure stronger-model usage

## Required Outputs

Each benchmark report should answer:

1. What threshold was applied?
2. Which policies met it?
3. What direct costs did they incur?
4. What indirect costs did they incur?
5. Which policy won under threshold-constrained comparison?
6. Which policy won under the scenario-specific weighted objective?

## Cross-Benchmark Synthesis Questions

At the end of the cycle, the repository should be able to state:

- whether optimal policies differ across benchmark families
- whether indirect cost changes winner selection
- whether selective HITL is consistently competitive
- which policy lever deserves the second empirical cycle

## Recommended Deliverables

- benchmark-level result tables
- cost-vector summaries
- scenario-specific weighted rankings
- one cross-benchmark narrative focused on policy choice, not raw capability
