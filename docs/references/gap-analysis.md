# Gap Analysis

## Purpose

This note identifies the main research gaps between existing literature and the goals of this repository.

## Gap 1: Workflow-level total cost is underdefined

Many papers optimize one cost component at a time, such as API price, latency, routing, or test-time compute. Fewer papers define the full cost of solving a task from start to finish, including retries, orchestration, oversight, and failure recovery.

Why it matters:

- a cheaper first attempt may create a more expensive full workflow
- local optimization can increase global cost
- task completion should be evaluated as an end-to-end process

## Gap 2: Indirect cost is fragmented across separate literatures

Human oversight, deferral, self-correction, and recovery are studied in different research traditions. These literatures are informative, but they are not yet unified into a single framework for AI problem-solving cost.

Why it matters:

- indirect cost can dominate practical usage even when direct inference cost falls
- the same system may look cost-efficient on API bills but expensive in operational practice

## Gap 3: Quality constraints are often implicit

A large share of cost-optimization work shows accuracy retention or benchmark gains, but the minimum acceptable quality threshold is often not treated as an explicit optimization constraint.

Why it matters:

- cost reduction without a predefined quality floor is ambiguous
- practical deployments care about acceptable quality, not just relative score changes

## Gap 4: Cross-task comparability remains weak

Different papers optimize coding, QA, reasoning, or serving workloads with different metrics and assumptions. This makes it difficult to compare strategies across task classes.

Why it matters:

- the best policy for coding may not be the best policy for extraction or planning
- a general AI cost framework needs common reporting conventions

## Gap 5: Direct-cost and indirect-cost strategies are rarely analyzed together

Existing work often studies routing, speculative decoding, tool use, or self-correction separately. But practical systems combine these mechanisms in one workflow.

Why it matters:

- cost interactions may be nonlinear
- direct-cost savings may increase indirect-cost burden
- a useful framework should expose these tradeoffs explicitly

## Gap 6: Human oversight is usually treated as a fallback, not as a priced resource

Learning-to-defer and scalable-oversight work offers useful theory, but many practical AI workflow discussions still treat human review as an unpriced safety net.

Why it matters:

- human time is often the highest-value resource in deployment
- escalation policy is one of the central cost questions in real workflows

## Implications for This Repository

The repository should prioritize research outputs that directly address these gaps:

- a direct-versus-indirect cost taxonomy
- a workflow-level total-cost definition
- explicit quality thresholds by task type
- shared reporting conventions across tasks
- comparative analysis of routing, retries, tool use, and oversight under one framework

## Immediate Research Priorities

1. Formalize workflow-level total cost.
2. Define acceptance criteria by task category.
3. Define shared reporting units for direct and indirect costs.
4. Compare the most mature optimization strategies under the same conceptual framework.
5. Build benchmark-ready experimental blueprints that reflect end-to-end task solving rather than isolated inference calls.
