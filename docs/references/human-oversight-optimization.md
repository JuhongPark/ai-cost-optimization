# Human Oversight Optimization

## Purpose

This note summarizes the research direction most relevant to a key clarification in this repository: reducing indirect cost does not mean eliminating humans by default. It means optimizing when and how human oversight is used.

## Core Question

The main question is not:

- how to remove humans from the workflow entirely

The main question is:

- when is full automation cheapest?
- when is selective human oversight cheapest?
- when is human-first handling cheaper than repeated AI failure and recovery?

## Relevant Research Directions

### 1. Learning to Defer

**Consistent Estimators for Learning to Defer to an Expert**  
Source: https://arxiv.org/abs/2006.01862

This paper formalizes a setting where a model either answers or defers to an expert. The main contribution is to frame this as a prediction-plus-rejection problem rather than a pure automation problem.

Why it matters here:

- human oversight is treated as part of the decision rule
- the model is allowed to decide that it should not answer
- selective deferral is a first-class optimization mechanism

### 2. Cost-sensitive deferral with workload constraints

**Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints**  
Source: https://arxiv.org/abs/2403.06906

This paper is especially relevant because it adds two ingredients that matter directly for this repository: different error costs and limited expert capacity. The paper proposes a framework that globally minimizes error cost subject to workload limits.

Why it matters here:

- human review is modeled as scarce capacity
- not all mistakes have equal cost
- the best allocation of human attention depends on both error risk and resource limits

### 3. Scalable oversight using weaker judges

**On scalable oversight with weak LLMs judging strong LLMs**  
Source: https://arxiv.org/abs/2407.04622

This paper studies whether weaker models can help oversee stronger ones under structured protocols. It is not the same problem as human oversight, but it matters because it suggests that some oversight load can be shifted from expensive humans to weaker AI judges.

Why it matters here:

- oversight itself can have layers
- weak overseers may substitute for part of human review
- indirect-cost reduction can come from changing who performs oversight, not only from removing oversight

### 4. AI feedback as a substitute for some human labeling effort

**RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback**  
Source: https://arxiv.org/abs/2309.00267

This paper shows that some forms of expensive human feedback can be partially substituted with AI feedback while maintaining strong performance in the studied tasks.

Why it matters here:

- part of human oversight cost may be replaceable
- the relevant question is not only whether humans are used, but where in the pipeline they are still necessary

## Working Interpretation for This Repository

The literature suggests three distinct indirect-cost strategies:

1. reduce unnecessary human involvement
2. allocate human review selectively
3. substitute some oversight with weaker or cheaper overseers

This is materially different from full human removal. In many realistic workflows, the total-cost-optimal policy may still include humans, but only on the hardest, riskiest, or highest-value cases.

## Implications for Our Research

The repository should explicitly compare three policy classes:

- full automation
- selective human-in-the-loop
- human-first or human-escalated handling

The main evaluation question should be:

- which policy reaches the quality threshold at the lowest total cost for a given task family?

## Practical Hypothesis

For many workflows, the likely best policy is not zero human oversight but selective human oversight combined with routing, verification, and confidence-aware escalation.
