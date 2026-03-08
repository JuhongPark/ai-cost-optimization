# Failure Taxonomy

## Purpose

This document defines a shared failure taxonomy for episode-level analysis.

## Failure Classes

### Quality Failures

- `wrong_answer`: the final answer is incorrect
- `quality_below_threshold`: output exists but does not satisfy the minimum quality rule

### Budget Failures

- `timeout`: the episode exceeds the allowed time budget
- `budget_exhausted`: the episode exhausts the allowed cost or attempt budget

### Tool and Verification Failures

- `tool_failure`: an external tool or API call fails
- `verification_failure`: the verifier rejects the answer or the verification path breaks

### Policy Failures

- `routing_failure`: the routing decision sends the task to an inadequate path
- `fallback_failure`: a fallback path is triggered but still fails to recover the episode
- `unrecovered_workflow_failure`: a multi-step execution fails without successful recovery

### Human-Related Outcomes

- `human_escalation`: the task is escalated to a human before acceptable completion
- `human_rejection`: human review rejects the answer after generation

## Usage Rule

Every unsuccessful episode should be assigned one primary failure category, even if multiple things went wrong. Secondary notes can be kept separately if needed.
