# Strategy Taxonomy

## Purpose

This document organizes the main optimization strategies that should be studied in this repository.

## Strategy Families

### 1. Model Selection

Choose a stronger or cheaper model before solving the task.

What it primarily affects:

- direct model cost
- baseline quality
- need for later retries or escalation

Best suited for:

- coding
- classification
- extraction

### 2. Difficulty-Based Routing

Route easier tasks to cheaper paths and harder tasks to stronger paths.

What it primarily affects:

- direct cost
- success rate at fixed average budget

Main risk:

- routing errors can increase indirect cost through failed recoveries

### 3. Retry Policy

Allow repeated attempts after an initial failure or low-confidence output.

What it primarily affects:

- quality recovery
- retry overhead
- latency

Main risk:

- direct cost may rise faster than quality

### 4. Verification Policy

Use tests, judges, heuristics, or external checks before accepting an answer.

What it primarily affects:

- failure rate
- hidden error reduction
- indirect recovery cost

Main risk:

- verification may cost more than the errors it prevents

### 5. Tool-Use Policy

Choose when to call external tools instead of relying on free-form model inference.

What it primarily affects:

- tool cost
- reasoning burden
- completion reliability

Main risk:

- tool use can shift rather than reduce cost

### 6. Human Escalation Policy

Choose when a task should be reviewed or completed by a human.

What it primarily affects:

- indirect human cost
- final quality assurance
- recovery after model failure

Main risk:

- cheap AI paths can become expensive if they overuse human fallback

### 7. Serving Optimization

Improve efficiency of token generation or response handling without changing the task policy.

What it primarily affects:

- latency
- serving cost
- throughput

Main risk:

- may improve infrastructure cost without changing end-to-end workflow cost

## Priority Order for This Repository

The recommended research order is:

1. model selection
2. difficulty-based routing
3. retry policy
4. verification policy
5. tool-use policy
6. human escalation policy
7. serving optimization

This order follows the current thesis that workflow-level cost optimization should be analyzed before lower-level serving refinements dominate the agenda.
