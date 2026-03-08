# coding_humaneval_v1 Summary

| policy_id | policy_class | episodes | success_rate | avg_quality_score | avg_direct_cost_usd | avg_latency_seconds | avg_human_minutes | avg_retry_count | avg_verification_count | avg_weighted_total_cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cheap_model_retry | full_automation | 3 | 0.0 | 0.86 | 0.00402 | 13.5 | 0.0 | 1.0 | 0.0 | 0.00587 |
| cheap_model_single_pass | full_automation | 3 | 0.0 | 0.79 | 0.001876 | 5.4 | 0.0 | 0.0 | 0.0 | 0.002416 |
| cheap_model_verifier_hitl | selective_hitl | 3 | 0.0 | 0.96 | 0.004623 | 14.04 | 1.0 | 1.0 | 2.0 | 0.009027 |
| human_first | human_first | 3 | 1.0 | 1.0 | 0.002412 | 6.6 | 5.0 | 0.0 | 0.0 | 0.013072 |
| strong_model_single_pass | full_automation | 3 | 1.0 | 1.0 | 0.006968 | 8.4 | 0.0 | 0.0 | 0.0 | 0.007808 |

Weighted total-cost formula: `direct + 0.0001*latency + 0.002*human_minutes + 0.0005*retries + 0.00025*verification`.

Leading stub policy by weighted total cost among threshold-satisfying policies: `strong_model_single_pass` (full_automation) with weighted total cost 0.007808.
