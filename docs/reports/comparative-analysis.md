# Comparative Analysis

## Purpose

This document compares the main optimization strategy families through the lens of direct cost, indirect cost, and quality risk.

## Comparison Table

| Strategy | Direct-cost impact | Indirect-cost impact | Main quality risk | Best initial task families |
| --- | --- | --- | --- | --- |
| Model selection | High | Medium | weak model underperforms | coding, classification |
| Difficulty-based routing | High | Medium to high | routing errors | classification, coding |
| Retry policy | Low to medium | High | repeated low-value attempts | coding, agent workflows |
| Verification policy | Medium | Medium | over-verification overhead | coding, extraction |
| Tool-use policy | Medium | Medium | tool dependence and failure | extraction, agent workflows |
| Human escalation policy | Low direct savings | High indirect impact | over-escalation | classification, extraction, agent workflows |
| Serving optimization | High infrastructure savings | Low | minimal task-policy risk | all at deployment stage |

## Main Takeaways

### Highest immediate research value

- model selection
- difficulty-based routing
- retry policy
- verification policy

These four strategies are the strongest starting point because they directly affect whether a task reaches the quality threshold at acceptable total cost.

### Direct-cost-heavy strategies

- model selection
- routing
- serving optimization

These strategies usually produce the clearest near-term savings, but they can hide downstream indirect-cost increases if failure recovery is ignored.

### Indirect-cost-heavy strategies

- retry policy
- human escalation policy
- verification policy

These strategies are central to the repository because they expose the gap between inference bill reduction and full workflow efficiency.

Human escalation should be interpreted as an allocation problem rather than a failure of automation. In some task families, selective review may be the lowest-total-cost strategy.

## Recommended First Comparison Set

The first comparative research cycle should test:

1. strong-model single pass
2. cheap-model single pass
3. difficulty-based routing
4. cheap-model plus retry
5. cheap-model plus verification

This set makes it possible to compare direct-cost savings against indirect-cost burdens without needing a large orchestration stack at the start.
