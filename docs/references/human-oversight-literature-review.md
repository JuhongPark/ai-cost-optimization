# Human Oversight Literature Review

## Purpose

This document expands the existing human-oversight note into a more investigation-oriented literature synthesis.

## Central Framing

The most useful literature for this repository does not ask whether humans should disappear from AI workflows. It asks how scarce oversight capacity should be allocated under cost, error, and workload constraints.

## Cluster 1: Learning to Defer

Representative papers:

- Consistent Estimators for Learning to Defer to an Expert
- Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints

Why this cluster matters:

- it formalizes the choice between answering and deferring
- it treats expert review as capacity-limited
- it supports the repository's view that escalation is a policy decision, not an exception

Main takeaway for this project:

- selective HITL should be modeled as an optimization strategy with explicit workload and error-cost assumptions

## Cluster 2: Scalable Oversight

Representative papers:

- On scalable oversight with weak LLMs judging strong LLMs
- RLAIF vs. RLHF

Why this cluster matters:

- it suggests that not all oversight must come from expensive humans
- it opens a layered oversight model: cheap model, stronger model, weak judge, human

Main takeaway for this project:

- the design space should include non-human overseers when comparing total cost

## Cluster 3: Confidence, Verification, and Triage

Relevant idea family:

- confidence-based gating
- verifier-triggered escalation
- test-backed acceptance rules

Why this cluster matters:

- many practical workflows do not escalate randomly; they escalate when confidence is low or verification fails
- this is where operational policies become measurable

Main takeaway for this project:

- the repository should compare escalation triggers, not just escalation rates

## Cluster 4: Human Factors and Queue Economics

This literature is less unified in the repo today, but it is important.

Key themes:

- reviewer fatigue
- throughput constraints
- error correlation between model and reviewer
- turnaround-time effects on downstream value

Main takeaway for this project:

- human review cost should not be modeled only as minutes per task; it may also include queue delay and capacity saturation effects

## Research Gaps Most Relevant Here

- Many papers optimize error under deferral but not full workflow cost.
- Many practical systems mention human review without pricing it explicitly.
- Few benchmark setups compare full automation, selective HITL, and human-first using one shared reporting frame.

## Implications for This Repository

The first oversight-focused study should answer:

1. Which escalation trigger best preserves quality at low human load?
2. At what review-time assumption does selective HITL stop being cost-effective?
3. When does human-first handling dominate because model failure is too expensive?
4. Can cheap verifiers or weak judges absorb part of the review burden?

## Recommended Literature Position

The repository should position itself as workflow-level cost research that connects three threads:

- learning to defer
- scalable oversight
- operational cost accounting for retries, verification, and recovery
