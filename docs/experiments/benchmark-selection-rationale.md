# Benchmark Selection Rationale

## Purpose

This document explains why the repository's initial benchmark families are reasonable for a first research cycle focused on AI cost optimization.

## Selection Criteria

A benchmark is a good fit for this project when it satisfies most of the following:

- quality can be measured clearly
- failure has a meaningful downstream cost
- different policy choices plausibly change total cost
- the task can be logged at the episode level
- human review is at least conceptually realistic

## Why Coding Belongs

Strengths:

- correctness can be measured with tests
- retry and verification are natural policy levers
- stronger models often improve first-pass quality
- failure recovery cost is realistic and visible

Why it matters for this repository:

- coding is a strong setting for studying verifier-heavy policies and the tradeoff between stronger first-pass models and cheaper retry-based pipelines

Primary caveat:

- some benchmark tasks are cleaner than real software work, so later phases should include messier repair or editing tasks

## Why Classification Belongs

Strengths:

- low-cost, repeatable episodes
- clear acceptance thresholds such as accuracy or F1
- routing and deferral policies are easy to study
- human escalation can be modeled cleanly

Why it matters for this repository:

- classification is the simplest place to test whether cheap automation plus selective review beats stronger default models

Primary caveat:

- some classification benchmarks understate real-world ambiguity and downstream error cost

## Why Information Extraction Belongs

Strengths:

- common enterprise workflow
- precision and recall are measurable
- tool use and validation are plausible
- human cleanup cost is easy to imagine operationally

Why it matters for this repository:

- extraction is a strong testbed for tool-assisted and validator-assisted policies where direct spend may be small but correction burden may be large

Primary caveat:

- exact-match evaluation can be too brittle, so benchmark design must reflect realistic structured-output quality

## Why Agent Workflows Are Deferred

Agent workflows matter to the thesis, but they should not lead the first cycle.

Reasons to defer:

- grading is noisier
- failure paths are more complex
- policy interactions become harder to attribute
- early research benefits from cleaner benchmark families first

Recommended stance:

- keep agent workflow as a second-wave benchmark family after the first three produce stable reporting conventions

## Cross-Benchmark Justification

Taken together, coding, classification, and extraction create a useful spread:

- coding emphasizes correctness and verification
- classification emphasizes routing and selective escalation
- extraction emphasizes structured quality and cleanup burden

This mix is enough to test the central hypothesis that optimal policies are task-dependent.

## Recommended Expansion Order

1. coding with stronger executable evaluation
2. classification with deferral-focused policies
3. extraction with structured validation and cleanup accounting
4. agent workflows with richer orchestration cost logging
