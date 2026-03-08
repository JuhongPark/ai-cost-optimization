# Final Cycle Summary
## Scope
This report summarizes the completed local first-cycle experiment pipeline. The results are generated from deterministic stub executions, so they validate the framework and execution flow rather than prove live-model empirical claims.
## Benchmark Findings
### Classification
- Lowest-cost successful policy: `difficulty_routing` (`full_automation`) with direct cost 0.001848 and human minutes 0.0.
- Success rate: 1.0; latency: 2.75; retries: 0.0.
### Coding
- Lowest-cost successful policy: `strong_model_single_pass` (`full_automation`) with direct cost 0.006968 and human minutes 0.0.
- Success rate: 1.0; latency: 8.4; retries: 0.0.
### Extraction
- Lowest-cost successful policy: `verifier_gated_hitl` (`selective_hitl`) with direct cost 0.004536 and human minutes 1.5.
- Success rate: 1.0; latency: 10.935; retries: 1.0.

## Cross-Benchmark Interpretation
- classification: full automation reached the threshold at the lowest direct cost
- coding: full automation reached the threshold at the lowest direct cost
- extraction: selective HITL was cost-competitive and threshold-satisfying
- Inference from the local cycle: the optimal policy class depends on task family rather than admitting a single universal winner.
- Coding favored a strong automated baseline in the current stub setup, classification favored routing, and extraction admitted a selective HITL winner.
- This supports the repository thesis that direct cost alone is not sufficient; policy choice must be evaluated under explicit quality thresholds and with indirect-cost visibility.

## Conclusion Boundary
- Completed: measurement freeze, benchmark freeze, stub-backed policy comparison run, cross-benchmark summary, and repository-level synthesis.
- Not yet completed: live model execution against real benchmark data. The current conclusion is therefore structural and procedural, not a final empirical claim about production models.

## Next Step
- Replace the stub benchmark runner with a real benchmark execution layer while preserving the same schema, configs, and aggregation pipeline.
