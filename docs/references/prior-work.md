# Prior Work

## Scope

This note reviews prior work most relevant to AI cost optimization research. The focus is not general capability improvement, but methods that change the cost of obtaining useful problem-solving performance.

## Key Themes

### 1. Cost-aware model selection and cascades

**FrugalGPT (Chen et al., 2023)**  
Source: https://arxiv.org/abs/2305.05176

FrugalGPT is one of the clearest starting points for this repository. It frames LLM usage as an inference cost problem and proposes three families of cost-reduction strategies: prompt adaptation, model approximation, and LLM cascades. Its central result is that routing across models can drastically reduce cost while maintaining or even improving quality on some tasks.

Relevance to this project:

- establishes cost-aware model routing as a primary optimization axis
- treats the best model as a reference point rather than the default answer
- supports the idea that AI usage should be evaluated at the workflow level, not just at the single-model level

### 2. Cascaded problem solving as a general framework

**Language Model Cascades (Dohan et al., 2022)**  
Source: https://arxiv.org/abs/2207.10342

Language Model Cascades provides a broader conceptual frame for chaining models, verifiers, and tools. It does not focus narrowly on cost, but it is important because it formalizes multi-step LM systems as structured programs with control flow. That matters for cost optimization because most meaningful savings will likely come from system design choices rather than from a single model call.

Relevance to this project:

- gives a language for thinking about tool use, verification, and staged reasoning
- supports evaluating the cost of a full problem-solving process
- suggests that optimization should target policies over sequences of actions, not isolated prompts

### 3. Test-time compute as a substitute for larger models

**Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (Snell et al., 2024)**  
Source: https://arxiv.org/abs/2408.03314

This paper studies how extra inference-time compute can improve performance, and argues that the best strategy depends on prompt difficulty. The key result is that adaptive allocation of test-time compute can outperform simpler baselines and, in some FLOPs-matched settings, outperform a much larger model.

Relevance to this project:

- directly supports the idea that cost optimization is partly a budget-allocation problem
- shows that prompt difficulty should influence how much compute is spent
- suggests that fixed policies are likely suboptimal relative to adaptive ones

### 4. Simple mechanisms for test-time budget control

**s1: Simple test-time scaling (Muennighoff et al., 2025)**  
Source: https://arxiv.org/abs/2501.19393

s1 is important because it shows that test-time scaling does not necessarily require a complicated reinforcement learning pipeline. The paper introduces budget forcing as a way to explicitly control how long a model reasons at inference time, and reports gains on reasoning-heavy tasks.

Relevance to this project:

- provides a concrete mechanism for controlling inference budget
- supports explicit test-time budget policies as an experimental variable
- is especially relevant for reasoning tasks where "think longer" may trade cost for quality

### 5. Decoding acceleration without changing outputs

**Fast Inference from Transformers via Speculative Decoding (Leviathan et al., 2022; ICML 2023)**  
Source: https://arxiv.org/abs/2211.17192

Speculative decoding addresses a different layer of the cost stack: system-side decoding efficiency. It speeds up generation by using a smaller approximation model to propose tokens and a larger model to verify them, while preserving the output distribution.

Relevance to this project:

- shows that cost optimization can happen below the workflow level
- separates quality-preserving acceleration from quality-cost tradeoff strategies
- is useful when latency and serving efficiency are part of the objective

### 6. Online multi-model routing under demand constraints

**Efficient Training-Free Online Routing for High-Volume Multi-LLM Serving (Wu and Silwal, 2025)**  
Source: https://arxiv.org/abs/2509.02718

This work extends the routing idea into an online setting with token budgets and throughput constraints. It is especially relevant for production scenarios where decisions must be made under sustained traffic rather than offline evaluation only.

Relevance to this project:

- highlights the difference between offline cost optimization and online serving optimization
- suggests that routing policies should be evaluated under throughput constraints
- motivates separating research tracks for offline experimental quality-cost tradeoffs and online deployment efficiency

## Synthesis

These papers suggest that prior work on AI cost optimization can be grouped into four main directions:

- **routing and cascades**: choose different models or stages for different queries
- **test-time budget allocation**: spend more or less reasoning compute depending on difficulty
- **verification-based acceleration**: use cheap models to propose and expensive models to verify
- **systems-level serving optimization**: reduce latency and serving cost without changing task policies

## Gaps Relative to This Repository

The existing literature is strong on inference cost reduction, routing, and test-time compute, but weaker on a unified definition of problem-solving cost at the workflow level. In particular, the papers above do not fully cover:

- human intervention cost
- retry and recovery cost across full workflows
- task-level acceptance thresholds as explicit optimization constraints
- cross-task evaluation under a shared cost-quality framework
- integration of tool use, routing, retries, and verification into one total-cost metric

This gap supports the direction of this repository: define AI problem solving itself as a cost-sensitive process, then evaluate and optimize that process under explicit quality constraints.

## Immediate Implications for Our Research Plan

The first experimental track should focus on the strongest and most mature prior-work directions:

1. model selection and routing
2. test-time budget control
3. verification and retry policy

System-level serving optimizations should be treated as a separate layer that can later be integrated into total-cost accounting.
