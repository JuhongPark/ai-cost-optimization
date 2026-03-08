# Literature Map

## Purpose

This document organizes the prior work most relevant to AI cost optimization by cost category, optimization mechanism, and open limitation.

## Map by Cost Category

| Cost category | Representative work | Main contribution | Limitation relative to this repository |
| --- | --- | --- | --- |
| Model or API usage cost | FrugalGPT (https://arxiv.org/abs/2305.05176) | Shows that prompt adaptation, approximation, and LLM cascades can reduce inference cost while preserving quality. | Focuses on inference-time API cost more than workflow-level total cost. |
| Inference-time compute cost | Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (https://arxiv.org/abs/2408.03314) | Shows that adaptive test-time compute allocation can outperform fixed compute strategies. | Does not unify test-time compute with human oversight or recovery cost. |
| Inference-time compute cost | s1: Simple test-time scaling (https://arxiv.org/abs/2501.19393) | Introduces simple budget forcing for reasoning-time control. | Strong on reasoning budget control, weaker on end-to-end workflow accounting. |
| Serving and latency cost | Fast Inference from Transformers via Speculative Decoding (https://arxiv.org/abs/2211.17192) | Reduces generation cost and latency while preserving output distribution. | Operates at the systems layer rather than the full task-policy layer. |
| Serving and latency cost | Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention (https://arxiv.org/abs/2403.19708) | Optimizes repeated serving cost in multi-turn settings through caching. | Focuses on serving efficiency, not task-level cost-quality tradeoffs. |
| Serving and latency cost | P/D-Serve: Serving Disaggregated Large Language Model at Scale (https://arxiv.org/abs/2408.08147) | Improves throughput and time-to-first-token in large-scale deployment. | Primarily infrastructure-oriented. |
| Tool or external API usage cost | Toolformer (https://arxiv.org/abs/2302.04761) | Studies when and how models should call tools. | Does not explicitly frame tool use as part of a total-cost objective. |
| Human oversight cost | Consistent Estimators for Learning to Defer to an Expert (https://arxiv.org/abs/2006.01862) | Formalizes answer-versus-defer decisions under expert fallback. | Not designed specifically for LLM workflows with retries and tools. |
| Human oversight cost | Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints (https://arxiv.org/abs/2403.06906) | Models multiple experts, workload limits, and cost-sensitive deferral. | Strong on deferral, but not on full AI workflow orchestration. |
| Retry and self-correction cost | Self-Refine (https://arxiv.org/abs/2303.17651) | Uses iterative feedback and revision to improve final outputs. | Improves quality, but usually reports gains more than total retry cost. |
| Retry and self-correction cost | Reflexion (https://arxiv.org/abs/2303.11366) | Uses verbal feedback and repeated trials to improve agent performance. | Makes retries central, but does not provide a general total-cost framework. |
| Failure recovery and orchestration cost | Language Model Cascades (https://arxiv.org/abs/2207.10342) | Frames multi-step problem solving as cascaded programs with control flow, verifiers, and tools. | Conceptually strong, but not fully tied to a direct-versus-indirect cost taxonomy. |

## Map by Optimization Mechanism

### Routing and Cascades

- FrugalGPT: https://arxiv.org/abs/2305.05176
- Language Model Cascades: https://arxiv.org/abs/2207.10342

What this line of work establishes:

- not every query should use the strongest model
- staged decision policies can reduce cost substantially
- system-level control flow matters for efficiency

What remains open:

- how to account for retries, human review, and tool usage in the same objective

### Test-Time Budget Allocation

- Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters: https://arxiv.org/abs/2408.03314
- s1: Simple test-time scaling: https://arxiv.org/abs/2501.19393

What this line of work establishes:

- inference budget should vary with task difficulty
- compute allocation can substitute for larger models in some cases

What remains open:

- how test-time budget interacts with workflow-level acceptance thresholds and total cost

### Systems and Serving Efficiency

- Fast Inference from Transformers via Speculative Decoding: https://arxiv.org/abs/2211.17192
- Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention: https://arxiv.org/abs/2403.19708
- P/D-Serve: Serving Disaggregated Large Language Model at Scale: https://arxiv.org/abs/2408.08147

What this line of work establishes:

- large savings can come from the serving stack itself
- some cost improvements preserve output quality exactly or nearly exactly

What remains open:

- how to compare systems gains with policy-level gains inside one total-cost framework

### Tool Use and External Resource Calls

- Toolformer: https://arxiv.org/abs/2302.04761
- ReAct: https://arxiv.org/abs/2210.03629

What this line of work establishes:

- tool use can improve quality or reduce reasoning burden
- action decisions should be part of the task policy

What remains open:

- when tool use lowers total cost versus merely shifting cost to external APIs or longer execution paths

### Human Oversight and Deferral

- Consistent Estimators for Learning to Defer to an Expert: https://arxiv.org/abs/2006.01862
- Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints: https://arxiv.org/abs/2403.06906
- On scalable oversight with weak LLMs judging strong LLMs: https://arxiv.org/abs/2407.04622

What this line of work establishes:

- oversight can be modeled as a resource allocation problem
- weaker judges or experts can sometimes supervise stronger systems in structured ways

What remains open:

- how to price human or judge oversight as part of practical workflow cost

### Retry, Reflection, and Recovery

- Self-Refine: https://arxiv.org/abs/2303.17651
- Reflexion: https://arxiv.org/abs/2303.11366
- Large Language Models have Intrinsic Self-Correction Ability: https://arxiv.org/abs/2406.15673

What this line of work establishes:

- retries and self-correction can improve outcomes
- recovery policies may be query-dependent

What remains open:

- whether retry gains justify their cost once latency, token use, and human review are included

## Preliminary Reading Order for This Repository

The most important reading order for this repository is:

1. FrugalGPT
2. Language Model Cascades
3. Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
4. Self-Refine and Reflexion
5. Learning to Defer papers
6. Speculative Decoding and serving papers

This order follows the current research thesis: first define the problem as a cost-sensitive workflow, then understand the strongest cost optimization mechanisms, then expand to indirect-cost accounting.
