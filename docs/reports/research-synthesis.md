# Research Synthesis

## Summary

This research program treats AI problem solving as a quality-constrained total-cost process rather than a pure capability problem. The central argument is that meaningful evaluation should include both direct cost and indirect cost.

An important clarification is that indirect-cost reduction does not imply removing humans from the loop by default. Human oversight is better modeled as a constrained, priced resource. The relevant optimization question is when to automate, when to escalate selectively, and when human review is itself the cheapest reliable policy.

## What Has Been Established in This Research Cycle

### 1. Conceptual foundation

The repository now defines AI problem solving as a full episode rather than a single model call. This shift makes it possible to account for retries, tool use, verification, human oversight, and failure recovery inside one framework.

### 2. Cost taxonomy

The current framework distinguishes:

- direct cost: model/API usage, inference-time compute, serving and latency, tool usage
- indirect cost: human oversight, retries, recovery, orchestration overhead

### 3. Prior-work structure

The literature is strongest on:

- routing and cascades
- test-time compute allocation
- decoding and serving efficiency

The literature is weaker on:

- workflow-level total cost
- indirect-cost integration
- explicit quality thresholds
- shared reporting conventions across task families

### 4. Evaluation framework

The repository now has a first version of:

- episode-level analysis
- cost vector reporting
- weighted total-cost reporting
- failure taxonomy
- logging schema
- benchmark blueprint

## Main Research Claim Emerging from This Cycle

The strongest candidate contribution for this repository is a workflow-level framework for evaluating AI problem solving under explicit quality constraints, with direct and indirect cost treated as separate but jointly analyzed dimensions.

This includes treating human oversight as part of the optimization target rather than as an external fallback. The mature research direction is not "remove humans everywhere," but "allocate scarce human attention where it has the highest cost-adjusted value."

## Current Recommendation

The first empirical research cycle should focus on:

1. coding
2. classification
3. routing
4. retry policy
5. verification policy

This gives the cleanest path to early results while preserving the larger thesis of total-cost evaluation.
