# Final Cycle Summary
## Scope
This report summarizes the completed local first-cycle experiment pipeline. The results are generated from deterministic stub executions, so they validate the framework and execution flow rather than prove live-model empirical claims.
## Benchmark Findings
### Classification
- Lowest-cost successful policy: `difficulty_routing` (`full_automation`) with weighted total cost 0.002123, direct cost 0.001848, and human minutes 0.0.
- Success rate: 1.0; latency: 2.75; retries: 0.0.
### Coding
- Lowest-cost successful policy: `strong_model_single_pass` (`full_automation`) with weighted total cost 0.007808, direct cost 0.006968, and human minutes 0.0.
- Success rate: 1.0; latency: 8.4; retries: 0.0.
### Extraction
- Lowest-cost successful policy: `strong_model_single_pass` (`full_automation`) with weighted total cost 0.007182, direct cost 0.006552, and human minutes 0.0.
- Success rate: 1.0; latency: 6.3; retries: 0.0.

## Cross-Benchmark Interpretation
- Weighted total-cost formula used in this local cycle: `direct + 0.0001*latency + 0.002*human_minutes + 0.0005*retries + 0.00025*verification`.
- classification: full automation reached the threshold at the lowest weighted total cost
- coding: full automation reached the threshold at the lowest weighted total cost
- extraction: full automation reached the threshold at the lowest weighted total cost
- Inference from the local cycle: the optimal policy class depends on task family rather than admitting a single universal winner.
- The local cycle shows that winner selection can vary across task families once weighted total cost and quality thresholds are applied.
- This supports the repository thesis that direct cost alone is not sufficient; policy choice must be evaluated under explicit quality thresholds and with indirect-cost visibility.

## Conclusion Boundary
- Completed: measurement freeze, benchmark freeze, stub-backed policy comparison run, cross-benchmark summary, and repository-level synthesis.
- Not yet completed: live model execution against real benchmark data. The current conclusion is therefore structural and procedural, not a final empirical claim about production models.

## Next Step
- Replace the stub benchmark runner with a real benchmark execution layer while preserving the same schema, configs, and aggregation pipeline.
