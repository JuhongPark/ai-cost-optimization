# Logging Schema

## Purpose

This document defines the minimum logging schema for benchmark episodes in this repository.

## Principles

- logging should happen at the episode level
- repeated attempts within one task must remain visible
- direct cost and indirect cost must be separable
- failure should be explicit, not inferred from missing success

## Episode Record

Each problem-solving episode should include the following fields.

| Field | Type | Description |
| --- | --- | --- |
| `episode_id` | string | Unique identifier for the full problem-solving episode. |
| `task_family` | string | High-level family such as `coding`, `classification`, `extraction`, or `agent_workflow`. |
| `task_id` | string | Unique identifier for the task instance. |
| `policy_id` | string | Identifier for the execution policy. |
| `model_id` | string | Primary model used in the episode. |
| `prompt_version` | string | Prompt or policy version identifier. |
| `started_at` | timestamp | Episode start time. |
| `ended_at` | timestamp | Episode end time. |
| `duration_seconds` | float | Total elapsed episode duration. |
| `final_status` | enum | `success`, `failure`, `human_escalation`, or `budget_exhausted`. |
| `failure_category` | enum or null | Failure reason if not successful. |
| `quality_score` | float or null | Task-specific quality score where applicable. |
| `quality_threshold_met` | boolean | Whether the predefined threshold was satisfied. |

## Attempt-Level Fields

An episode may contain one or more attempts. Each attempt should capture:

| Field | Type | Description |
| --- | --- | --- |
| `attempt_index` | integer | Attempt number within the episode. |
| `attempt_model_id` | string | Model used in this attempt. |
| `input_tokens` | integer | Input tokens consumed in the attempt. |
| `output_tokens` | integer | Output tokens generated in the attempt. |
| `attempt_latency_seconds` | float | Latency for this attempt. |
| `attempt_cost_usd` | float | Direct monetary cost for this attempt. |
| `verification_count` | integer | Number of verification steps used in this attempt. |
| `tool_call_count` | integer | Number of external tool calls in this attempt. |
| `tool_cost_usd` | float | External tool/API cost in this attempt. |
| `attempt_outcome` | enum | `accepted`, `rejected`, `failed`, or `escalated`. |

## Indirect-Cost Fields

Indirect-cost accounting should include:

| Field | Type | Description |
| --- | --- | --- |
| `retry_count` | integer | Number of retries beyond the first attempt. |
| `human_review_count` | integer | Number of human review events. |
| `human_review_minutes` | float | Estimated human review time. |
| `human_intervention_count` | integer | Number of explicit interventions or handoffs. |
| `recovery_step_count` | integer | Number of recovery or fallback steps. |
| `routing_decision_count` | integer | Number of routing decisions. |
| `fallback_path_used` | boolean | Whether any fallback path was activated. |

## Derived Fields

The following should be computed from raw logs:

- `total_direct_cost_usd`
- `total_tool_cost_usd`
- `total_token_count`
- `total_latency_seconds`
- `total_human_minutes`
- `total_retry_count`
- `total_verification_count`
- `total_recovery_steps`

## Failure Categories

The default failure taxonomy is:

- `wrong_answer`
- `quality_below_threshold`
- `timeout`
- `budget_exhausted`
- `tool_failure`
- `verification_failure`
- `routing_failure`
- `unrecovered_workflow_failure`
- `human_escalation`

## Recommended Storage Format

The simplest recommended format is one JSON object per episode with nested attempt records. A tabular export can then be derived for analysis.
