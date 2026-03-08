# classification_mmlu_subset_v1 Summary

| policy_id | policy_class | episodes | success_rate | avg_quality_score | avg_direct_cost_usd | avg_latency_seconds | avg_human_minutes | avg_retry_count | avg_verification_count | avg_weighted_total_cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cheap_model_single_pass | full_automation | 3 | 0.0 | 0.75 | 0.000924 | 2.25 | 0.0 | 0.0 | 0.0 | 0.001149 |
| confidence_gated_hitl | selective_hitl | 3 | 1.0 | 0.86 | 0.00198 | 5.4 | 2.0 | 1.0 | 0.0 | 0.00702 |
| difficulty_routing | full_automation | 3 | 1.0 | 0.88 | 0.001848 | 2.75 | 0.0 | 0.0 | 0.0 | 0.002123 |
| human_first | human_first | 3 | 1.0 | 0.98 | 0.001188 | 2.75 | 5.0 | 0.0 | 0.0 | 0.011463 |
| strong_model_single_pass | full_automation | 3 | 1.0 | 0.96 | 0.003432 | 3.5 | 0.0 | 0.0 | 0.0 | 0.003782 |

Weighted total-cost formula: `direct + 0.0001*latency + 0.002*human_minutes + 0.0005*retries + 0.00025*verification`.

Leading stub policy by weighted total cost among threshold-satisfying policies: `difficulty_routing` (full_automation) with weighted total cost 0.002123.
