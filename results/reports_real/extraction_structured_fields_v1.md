# extraction_structured_fields_v1 Summary

| policy_id | policy_class | episodes | success_rate | avg_quality_score | avg_direct_cost_usd | avg_latency_seconds | avg_human_minutes | avg_retry_count | avg_verification_count | avg_weighted_total_cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cheap_model_single_pass | full_automation | 2 | 0.0 | 0.5 | 0.0 | 0.9 | 0.0 | 0.0 | 0.0 | 9e-05 |
| human_first | human_first | 2 | 1.0 | 1.0 | 0.0 | 1.8 | 5.0 | 0.0 | 1.0 | 0.01043 |
| strong_model_single_pass | full_automation | 2 | 1.0 | 1.0 | 0.0 | 1.8 | 0.0 | 0.0 | 0.0 | 0.00018 |
| tool_assisted_extraction | full_automation | 2 | 0.0 | 0.5 | 0.001 | 0.9 | 0.0 | 1.0 | 1.0 | 0.00184 |
| verifier_gated_hitl | selective_hitl | 2 | 0.0 | 0.5 | 0.0 | 0.9 | 1.5 | 1.0 | 1.0 | 0.00384 |

Weighted total-cost formula: `direct + 0.0001*latency + 0.002*human_minutes + 0.0005*retries + 0.00025*verification`.

Leading policy by weighted total cost among threshold-satisfying policies: `strong_model_single_pass` (full_automation) with weighted total cost 0.00018.
