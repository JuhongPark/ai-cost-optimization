# Policy Templates

## Purpose

This document defines reusable policy templates for early benchmark studies.

## Template A: Full Automation Baseline

- `policy_class`: `full_automation`
- `routing`: off or optional
- `verification`: optional
- `human_escalation`: only on terminal failure

## Template B: Confidence-Gated HITL

- `policy_class`: `selective_hitl`
- `routing`: optional
- `verification`: on
- `human_escalation`: trigger when confidence falls below threshold

## Template C: Verifier-Gated HITL

- `policy_class`: `selective_hitl`
- `routing`: optional
- `verification`: on
- `human_escalation`: trigger when verifier rejects or repeated retries fail

## Template D: Human-First

- `policy_class`: `human_first`
- `routing`: optional
- `verification`: optional
- `human_escalation`: default at start or after first output

## Template E: Cheap Model with Selective Escalation

- `policy_class`: `selective_hitl`
- `model_strategy`: cheap-first
- `retry_policy`: limited
- `human_escalation`: on low confidence or failed verification

## Template F: Strong Model with Minimal Oversight

- `policy_class`: `full_automation`
- `model_strategy`: strong-first
- `retry_policy`: minimal
- `human_escalation`: only on final failure
