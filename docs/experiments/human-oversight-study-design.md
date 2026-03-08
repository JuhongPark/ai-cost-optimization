# Human Oversight Study Design

## Purpose

This document defines the first study design for comparing automation and human-oversight allocation policies.

## Policy Classes

### 1. Full Automation

Description:

- the system attempts to solve the task end to end without planned human review

Typical triggers:

- no escalation until final failure or budget exhaustion

What it tests:

- the lowest-human-cost path
- the risk of hidden recovery cost

### 2. Selective Human-in-the-Loop

Description:

- the system escalates only under explicit policy triggers

Example triggers:

- low confidence
- verifier rejection
- repeated retry failure
- high predicted task difficulty

What it tests:

- whether targeted human review lowers total cost
- whether a small amount of human time prevents expensive retries or failures

### 3. Human-First

Description:

- a human reviews or completes the task at the start or immediately after generation

What it tests:

- whether high-risk or high-value tasks are cheaper with early human involvement

## Core Comparison Questions

1. Which policy class achieves the quality threshold with the lowest total cost?
2. How much direct cost is saved by more automation?
3. How much indirect cost is created by more automation?
4. Which escalation triggers are most cost-effective?
5. Which task families benefit most from selective oversight?

## Minimum Metrics

- success rate
- threshold-satisfying success rate
- direct cost per episode
- human minutes per episode
- retries per episode
- verification count per episode
- failure rate
- cost per successful episode

## Task-Family Expectations

### Coding

Likely useful comparison:

- full automation vs selective HITL after failed verification

### Classification

Likely useful comparison:

- full automation vs confidence-based escalation

### Information Extraction

Likely useful comparison:

- automation with cleanup vs selective human review on low-precision outputs

### Agent Workflows

Likely useful comparison:

- automation with fallback vs staged human intervention after tool or recovery failure

## Initial Hypothesis

Selective human oversight will often dominate both extremes:

- cheaper than human-first on easy or medium tasks
- more reliable and sometimes cheaper than full automation on hard or high-recovery-cost tasks
