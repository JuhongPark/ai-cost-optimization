# Benchmark Blueprint

## Purpose

This document defines the initial benchmark blueprint for evaluating AI cost optimization strategies.

## Benchmark Design Principles

The first benchmark set should satisfy five conditions:

- tasks must have measurable success criteria
- tasks must differ in difficulty
- tasks must expose meaningful cost tradeoffs
- tasks must be reproducible
- tasks must support logging at the episode level

## Initial Task Families

### 1. Coding Tasks

Why include them:

- they have clear correctness signals
- retries and verification are common
- model quality differences are often meaningful

Primary acceptance rule:

- pass the test suite or meet a fixed correctness threshold

Useful cost-sensitive variables:

- model choice
- retry policy
- verification policy
- human escalation for failed outputs

### 2. Information Extraction Tasks

Why include them:

- they are common in practical workflows
- tool use and structured validation can matter
- quality can be measured with precision and recall

Primary acceptance rule:

- satisfy a predefined precision and recall target

Useful cost-sensitive variables:

- model size
- extraction with or without tools
- verification and cleanup policy

### 3. Classification Tasks

Why include them:

- they provide controlled, relatively low-cost comparisons
- routing and deferral policies can be tested cleanly

Primary acceptance rule:

- satisfy a target accuracy or F1 threshold

Useful cost-sensitive variables:

- strong versus cheap model
- selective escalation
- deferred review policy

### 4. Multi-step Agent Workflows

Why include them:

- they expose orchestration and recovery costs clearly
- they make retries, tool use, and failure paths visible

Primary acceptance rule:

- satisfy a target completion rate with bounded failure modes

Useful cost-sensitive variables:

- routing
- tool policy
- retry policy
- human handoff policy

## Priority Order

The recommended starting order is:

1. coding tasks
2. classification tasks
3. information extraction tasks
4. multi-step agent workflows

This order starts with cleaner evaluation settings before moving into more orchestration-heavy workflows.

## Standard Policy Set

Each task family should be evaluated under the same initial policy set:

- strong-model single pass
- cheap-model single pass
- difficulty-based routing
- retry-enabled policy
- verification-enabled policy

## Policy-Class Comparison

Each benchmark family should also be evaluated across three oversight classes:

1. **Full automation**
   - the system completes the episode without human review unless it fails completely
2. **Selective human-in-the-loop**
   - the system escalates only on predefined triggers such as low confidence, verifier failure, or repeated retry failure
3. **Human-first or immediate escalation**
   - a human reviews or completes the task at the start or after the first model output by policy

This comparison is required because a lower-AI-cost policy may still have higher total cost once human review and recovery are included.

## Episode Logging Requirements

Each benchmark run should log:

- task family
- task instance id
- policy id
- model id
- prompt version
- start and end timestamps
- token usage
- tool usage
- retry count
- verification count
- human escalation count
- direct monetary cost
- final quality outcome
- failure category

## Initial Research Questions for Benchmarks

1. Which task family shows the largest gains from routing?
2. Which task family is most sensitive to retry overhead?
3. When does verification lower total cost instead of increasing it?
4. Which task family creates the largest indirect-cost burden?
5. Which policy reaches the quality threshold at the lowest total cost?
6. When is selective human oversight cheaper than full automation?
7. For which task families is human-first handling competitively priced?
