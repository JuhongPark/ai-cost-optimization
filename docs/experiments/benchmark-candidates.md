# Benchmark Candidates

## Purpose

This document proposes initial benchmark candidates for the first research cycle.

## Selection Criteria

Each candidate benchmark should satisfy most of the following:

- reproducible task instances
- measurable success criteria
- practical relevance
- support for cost-sensitive policy variation
- manageable setup cost for early experiments

## 1. Coding

### Primary candidates

- **HumanEval**
  - fit: clean correctness signal through tests
  - good for: model selection, retry policy, verification policy
- **MBPP**
  - fit: broader coding task variety with runnable tests
  - good for: baseline comparisons and retry analysis

### Why this family should start first

- correctness is relatively objective
- pass/fail thresholds are easy to communicate
- retries and verification naturally matter

## 2. Classification

### Primary candidates

- **MMLU subsets**
  - fit: broad subject coverage and controlled evaluation
  - good for: strong-vs-cheap model routing and selective escalation
- **Domain-specific label classification tasks**
  - fit: practical task framing with measurable accuracy or F1
  - good for: deferral and review policy analysis

### Why this family should come early

- easy to compare direct cost against quality
- low workflow complexity makes policy effects easier to isolate

## 3. Information Extraction

### Primary candidates

- **Structured extraction from documents or web pages**
  - fit: precision/recall style evaluation
  - good for: tool use, verification, cleanup policy
- **Relation or field extraction benchmarks**
  - fit: measurable field-level accuracy
  - good for: cheap-vs-strong model comparisons and review thresholds

### Why this family matters

- closer to real business workflows
- useful for evaluating cleanup and review overhead

## 4. Multi-step Agent Workflows

### Primary candidates

- **GAIA**
  - fit: multi-step, tool-using assistant tasks
  - good for: routing, tool use, retries, failure recovery
- **MiniWoB++ or workflow-style sandbox tasks**
  - fit: explicit sequence of decisions and environment interaction
  - good for: orchestration cost and fallback analysis

### Why this family should come later

- richer orchestration and recovery behaviors
- harder to evaluate cleanly
- best used after the logging and failure taxonomy are stable

## Recommended First-Cycle Benchmark Set

For the first cycle, the most practical benchmark set is:

1. HumanEval
2. MBPP
3. one classification benchmark or MMLU subset
4. one structured extraction task set
5. one multi-step agent benchmark such as GAIA

## Policy Priorities by Benchmark Family

### Coding

- strong-model single pass
- cheap-model single pass
- retry-enabled policy
- verification-enabled policy

### Classification

- strong-model single pass
- cheap-model single pass
- difficulty-based routing
- defer-to-review policy

### Extraction

- strong-model single pass
- cheap-model single pass
- tool-assisted extraction
- verification and cleanup policy

### Agent Workflows

- strong-model single pass
- routing policy
- tool policy
- retry and fallback policy
- human escalation policy

## Recommendation

The first operational research cycle should begin with coding and classification, then expand to extraction and agent workflows once the measurement stack is stable.
