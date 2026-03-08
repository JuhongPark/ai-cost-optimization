# Cost Taxonomy

## Purpose

This document divides AI problem-solving cost into two groups:

- direct cost: resources consumed directly by running the AI system
- indirect cost: additional resources caused by making the AI system usable, reliable, or recoverable in practice

This distinction is useful because much of the existing literature focuses on direct inference cost, while the broader workflow cost of AI problem solving remains less unified.

## 1. Direct Cost

Direct cost refers to resources spent directly during inference or execution.

### 1.1 Model or API usage cost

This includes per-token fees, per-request fees, and the cost of selecting a larger or smaller model for a query.

Relevant research:

- **FrugalGPT** studies cost-aware use of multiple LLM APIs through prompt adaptation, approximation, and cascades.
  Source: https://arxiv.org/abs/2305.05176

Implication:

- model selection and routing should be treated as first-class optimization variables

### 1.2 Inference-time compute cost

This includes the compute budget spent at test time, such as longer reasoning, more samples, verifier calls, or search over candidate answers.

Relevant research:

- **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters** studies adaptive allocation of test-time compute by prompt difficulty.
  Source: https://arxiv.org/abs/2408.03314
- **s1: Simple test-time scaling** studies explicit budget control for reasoning through budget forcing.
  Source: https://arxiv.org/abs/2501.19393

Implication:

- direct cost is not only model size; it also depends on how much compute is allocated per query

### 1.3 Serving and latency cost

This includes the infrastructure and efficiency cost of generating tokens, serving requests, and reducing response latency.

Relevant research:

- **Fast Inference from Transformers via Speculative Decoding** accelerates generation by using a smaller model to propose tokens and a larger model to verify them.
  Source: https://arxiv.org/abs/2211.17192
- **Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention** reduces repeated KV-cache computation and end-to-end serving cost for multi-turn workloads.
  Source: https://arxiv.org/abs/2403.19708
- **P/D-Serve: Serving Disaggregated Large Language Model at Scale** optimizes large-scale serving throughput and time-to-first-token.
  Source: https://arxiv.org/abs/2408.08147

Implication:

- some direct-cost reductions preserve output quality and operate purely at the systems layer

### 1.4 Tool and external API usage cost

This includes the direct cost of search calls, calculator calls, retrieval queries, translation APIs, and other external tools.

Relevant research:

- **Toolformer** studies how a model can learn when to call tools and how to integrate the results into generation.
  Source: https://arxiv.org/abs/2302.04761

Implication:

- tool use can increase direct cost per step while reducing the total cost of solving the task if it lowers model requirements or failure rates

## 2. Indirect Cost

Indirect cost refers to resources not captured by a single inference bill, but still required to obtain a usable answer in practice.

### 2.1 Human oversight cost

This includes human review, approval, correction, intervention, and escalation time.

Relevant research:

- **Consistent Estimators for Learning to Defer to an Expert** formalizes when a model should answer and when it should defer to a human expert.
  Source: https://arxiv.org/abs/2006.01862
- **Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints** extends this to multiple experts, cost-sensitive errors, and expert capacity limits.
  Source: https://arxiv.org/abs/2403.06906

Implication:

- human involvement should be modeled as a constrained and priced resource, not as free fallback capacity
- the relevant optimization question is often how to allocate human attention, not how to eliminate it entirely

### 2.2 Retry and self-correction cost

This includes repeated prompting, iterative refinement, self-critique, and multi-trial recovery after an unsatisfactory first answer.

Relevant research:

- **Self-Refine** studies iterative feedback and refinement by the same model at test time.
  Source: https://arxiv.org/abs/2303.17651
- **Reflexion** studies language agents that improve through verbal feedback and repeated trials.
  Source: https://arxiv.org/abs/2303.11366

Implication:

- quality gains from retries or self-correction must be evaluated against their extra cost, not only against their final accuracy

### 2.3 Failure recovery and orchestration cost

This includes the overhead of verification, staged reasoning, control flow, fallback policies, and recovery paths after intermediate errors.

Relevant research:

- **Language Model Cascades** provides a framework for composing repeated interactions, verifiers, tool use, and structured control flow.
  Source: https://arxiv.org/abs/2207.10342

Implication:

- end-to-end problem-solving cost depends on the full execution policy, not just the first model call

## 3. Working View for This Repository

For this repository, the current working split is:

### Direct cost

- model or API usage cost
- inference-time compute cost
- serving and latency cost
- tool or external API usage cost

### Indirect cost

- human oversight cost
- retry and self-correction cost
- failure recovery and orchestration cost

## 4. Research Gap

The literature is relatively mature on direct-cost optimization, especially:

- model routing
- test-time compute allocation
- decoding and serving efficiency

The literature is less unified on indirect cost, especially:

- human oversight under realistic workflows
- retries and recovery as part of total task cost
- shared cost accounting across tools, routing, verification, and fallback

This suggests that a strong contribution for this repository is not only reducing direct inference cost, but also defining a workflow-level cost framework that includes indirect costs explicitly.
