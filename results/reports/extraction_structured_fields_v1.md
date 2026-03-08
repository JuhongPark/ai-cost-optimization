# extraction_structured_fields_v1 Summary

| policy_id | policy_class | episodes | success_rate | avg_quality_score | avg_direct_cost_usd | avg_latency_seconds | avg_human_minutes | avg_retry_count | avg_verification_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cheap_model_single_pass | full_automation | 3 | 0.0 | 0.78 | 0.001764 | 4.05 | 0.0 | 0.0 | 0.0 |
| strong_model_single_pass | full_automation | 3 | 1.0 | 0.99 | 0.006552 | 6.3 | 0.0 | 0.0 | 0.0 |
| tool_assisted_extraction | full_automation | 3 | 1.0 | 0.91 | 0.008158 | 9.315 | 0.0 | 1.0 | 2.0 |
| verifier_gated_hitl | selective_hitl | 3 | 1.0 | 0.93 | 0.004536 | 10.935 | 1.5 | 1.0 | 2.0 |

Leading stub policy by threshold-satisfying success rate: `verifier_gated_hitl` (selective_hitl) with success rate 1.0.
