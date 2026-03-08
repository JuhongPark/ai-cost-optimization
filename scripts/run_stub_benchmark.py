#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def slug_to_filename(policy_id: str) -> str:
    return policy_id.replace("_", "-") + ".yaml"


def recommended_policy_paths(benchmark_config: dict) -> list[Path]:
    return [
        REPO_ROOT / "configs" / "policies" / slug_to_filename(policy_id)
        for policy_id in benchmark_config["recommended_policies"]
    ]


def benchmark_base_metrics(task_family: str) -> dict:
    if task_family == "coding":
        return {"quality": 0.82, "input_tokens": 700, "output_tokens": 320, "latency": 6.0}
    if task_family == "classification":
        return {"quality": 0.78, "input_tokens": 500, "output_tokens": 80, "latency": 2.5}
    if task_family == "extraction":
        return {"quality": 0.81, "input_tokens": 900, "output_tokens": 180, "latency": 4.5}
    return {"quality": 0.55, "input_tokens": 1100, "output_tokens": 260, "latency": 8.5}


def policy_adjustments(policy_id: str, policy_class: str) -> dict:
    adjustments: dict[str, float | int | str | bool] = {
        "quality_delta": 0.0,
        "cost_multiplier": 1.0,
        "latency_multiplier": 1.0,
        "retry_count": 0,
        "verification_count": 0,
        "tool_call_count": 0,
        "human_review_count": 0,
        "human_review_minutes": 0.0,
        "human_intervention_count": 0,
        "routing_decision_count": 0,
        "recovery_step_count": 0,
        "fallback_path_used": False,
        "escalation_trigger": None,
    }

    if policy_id == "strong_model_single_pass":
        adjustments["quality_delta"] = 0.18
        adjustments["cost_multiplier"] = 2.6
        adjustments["latency_multiplier"] = 1.4
    elif policy_id == "cheap_model_single_pass":
        adjustments["quality_delta"] = -0.03
        adjustments["cost_multiplier"] = 0.7
        adjustments["latency_multiplier"] = 0.9
    elif policy_id == "cheap_model_retry":
        adjustments["quality_delta"] = 0.04
        adjustments["cost_multiplier"] = 1.0
        adjustments["latency_multiplier"] = 1.25
        adjustments["retry_count"] = 1
    elif policy_id == "difficulty_routing":
        adjustments["quality_delta"] = 0.1
        adjustments["cost_multiplier"] = 1.4
        adjustments["latency_multiplier"] = 1.1
        adjustments["routing_decision_count"] = 1
    elif policy_id == "cheap_model_verifier_hitl":
        adjustments["quality_delta"] = 0.14
        adjustments["cost_multiplier"] = 1.15
        adjustments["latency_multiplier"] = 1.3
        adjustments["retry_count"] = 1
        adjustments["verification_count"] = 1
        adjustments["human_review_count"] = 1
        adjustments["human_review_minutes"] = 1.0
        adjustments["human_intervention_count"] = 1
        adjustments["recovery_step_count"] = 1
        adjustments["escalation_trigger"] = "verifier_failure_or_retry_exhaustion"
    elif policy_id == "confidence_gated_hitl":
        adjustments["quality_delta"] = 0.08
        adjustments["cost_multiplier"] = 1.0
        adjustments["latency_multiplier"] = 1.2
        adjustments["retry_count"] = 1
        adjustments["human_review_count"] = 1
        adjustments["human_review_minutes"] = 2.0
        adjustments["human_intervention_count"] = 1
        adjustments["escalation_trigger"] = "confidence_below_threshold"
    elif policy_id == "verifier_gated_hitl":
        adjustments["quality_delta"] = 0.12
        adjustments["cost_multiplier"] = 1.2
        adjustments["latency_multiplier"] = 1.35
        adjustments["retry_count"] = 1
        adjustments["verification_count"] = 1
        adjustments["human_review_count"] = 1
        adjustments["human_review_minutes"] = 1.5
        adjustments["human_intervention_count"] = 1
        adjustments["recovery_step_count"] = 1
        adjustments["escalation_trigger"] = "verifier_failure_or_retry_exhaustion"
    elif policy_id == "tool_assisted_extraction":
        adjustments["quality_delta"] = 0.1
        adjustments["cost_multiplier"] = 1.1
        adjustments["latency_multiplier"] = 1.15
        adjustments["retry_count"] = 1
        adjustments["verification_count"] = 1
        adjustments["tool_call_count"] = 2
    elif policy_id == "human_first" or policy_class == "human_first":
        adjustments["quality_delta"] = 0.2
        adjustments["cost_multiplier"] = 0.9
        adjustments["latency_multiplier"] = 1.1
        adjustments["human_review_count"] = 1
        adjustments["human_review_minutes"] = 5.0
        adjustments["human_intervention_count"] = 1
        adjustments["escalation_trigger"] = "policy_default"

    return adjustments


def quality_threshold(benchmark_config: dict) -> float:
    threshold = benchmark_config["acceptance_criteria"]["threshold_value"]
    return float(threshold)


def quality_metrics(task_family: str, quality: float, policy_class: str) -> dict:
    if task_family == "coding":
        return {
            "accuracy": None,
            "pass_rate": quality,
            "f1": None,
            "precision": None,
            "recall": None,
        }
    if task_family == "classification":
        return {
            "accuracy": quality,
            "pass_rate": None,
            "f1": quality - 0.01,
            "precision": None,
            "recall": None,
        }
    if task_family == "extraction":
        precision = min(1.0, quality + (0.03 if policy_class == "selective_hitl" else 0.01))
        recall = max(0.0, quality - 0.02)
        return {
            "accuracy": None,
            "pass_rate": None,
            "f1": quality,
            "precision": round(precision, 4),
            "recall": round(recall, 4),
        }
    return {
        "accuracy": None,
        "pass_rate": None,
        "f1": quality,
        "precision": None,
        "recall": None,
    }


def threshold_met_for_benchmark(benchmark_config: dict, metrics: dict) -> bool:
    metric_name = benchmark_config["acceptance_criteria"]["metric"]
    primary_threshold = float(benchmark_config["acceptance_criteria"]["threshold_value"])
    primary_value = metrics.get(metric_name)
    if primary_value is None or float(primary_value) < primary_threshold:
        return False

    secondary = benchmark_config.get("secondary_criteria", {})
    for key, threshold in secondary.items():
        metric_key = key.removesuffix("_min")
        metric_value = metrics.get(metric_key)
        if metric_value is None or float(metric_value) < float(threshold):
            return False
    return True


def metric_cost_usd(base_input: int, base_output: int, multiplier: float) -> float:
    token_cost = (base_input * 0.000002) + (base_output * 0.000004)
    return round(token_cost * multiplier, 6)


def make_attempt(index: int, model_id: str, input_tokens: int, output_tokens: int, latency: float, cost: float, verification_count: int, tool_call_count: int) -> dict:
    return {
        "attempt_index": index,
        "attempt_model_id": model_id,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "attempt_latency_seconds": round(latency, 3),
        "attempt_cost_usd": round(cost, 6),
        "verification_count": verification_count,
        "tool_call_count": tool_call_count,
        "tool_cost_usd": round(tool_call_count * 0.001, 6),
        "attempt_outcome": "accepted",
    }


def build_episode(benchmark_config: dict, policy_config: dict, episode_index: int) -> dict:
    task_family = benchmark_config["task_family"]
    base = benchmark_base_metrics(task_family)
    adjustments = policy_adjustments(policy_config["policy_id"], policy_config["policy_class"])

    quality = min(1.0, max(0.0, base["quality"] + float(adjustments["quality_delta"])))
    input_tokens = int(base["input_tokens"])
    output_tokens = int(base["output_tokens"])
    latency = float(base["latency"]) * float(adjustments["latency_multiplier"])
    cost = metric_cost_usd(input_tokens, output_tokens, float(adjustments["cost_multiplier"]))
    verification_count = int(adjustments["verification_count"])
    tool_call_count = int(adjustments["tool_call_count"])
    retry_count = int(adjustments["retry_count"])
    attempts = [
        make_attempt(0, policy_config["model_strategy"]["primary_model"], input_tokens, output_tokens, latency, cost, verification_count, tool_call_count)
    ]

    if retry_count:
        attempts.append(
            make_attempt(
                1,
                policy_config["model_strategy"].get("secondary_model", policy_config["model_strategy"]["primary_model"]),
                input_tokens // 2,
                output_tokens // 2,
                latency * 0.8,
                cost * 0.5,
                verification_count,
                tool_call_count,
            )
        )

    start_time = datetime(2026, 3, 8, 12, 0, 0, tzinfo=UTC) + timedelta(minutes=episode_index)
    total_direct_cost = round(sum(attempt["attempt_cost_usd"] + attempt["tool_cost_usd"] for attempt in attempts), 6)
    total_tokens = sum(attempt["input_tokens"] + attempt["output_tokens"] for attempt in attempts)
    total_latency = round(sum(attempt["attempt_latency_seconds"] for attempt in attempts), 3)
    total_verification = sum(attempt["verification_count"] for attempt in attempts)
    total_tool_cost = round(sum(attempt["tool_cost_usd"] for attempt in attempts), 6)
    metrics = quality_metrics(task_family, quality, policy_config["policy_class"])
    threshold_met = threshold_met_for_benchmark(benchmark_config, metrics)
    final_status = "success" if threshold_met else ("human_escalation" if policy_config["policy_class"] != "full_automation" else "failure")
    failure_category = None if threshold_met else ("human_escalation" if final_status == "human_escalation" else "quality_below_threshold")

    return {
        "episode_id": f"{benchmark_config['benchmark_id']}__{policy_config['policy_id']}__{episode_index:03d}",
        "task_family": task_family,
        "task_id": f"{benchmark_config['benchmark_id']}_task_{episode_index:03d}",
        "policy_id": policy_config["policy_id"],
        "policy_class": policy_config["policy_class"],
        "model_id": policy_config["model_strategy"]["primary_model"],
        "prompt_version": "v1",
        "started_at": start_time.isoformat(),
        "ended_at": (start_time + timedelta(seconds=total_latency)).isoformat(),
        "duration_seconds": total_latency,
        "final_status": final_status,
        "failure_category": failure_category,
        "quality_score": round(quality, 4),
        "quality_metrics": metrics,
        "quality_threshold_met": threshold_met,
        "attempts": attempts,
        "indirect_cost": {
            "retry_count": retry_count,
            "human_review_count": int(adjustments["human_review_count"]),
            "human_review_minutes": float(adjustments["human_review_minutes"]),
            "human_intervention_count": int(adjustments["human_intervention_count"]),
            "escalation_trigger": adjustments["escalation_trigger"],
            "recovery_step_count": int(adjustments["recovery_step_count"]),
            "routing_decision_count": int(adjustments["routing_decision_count"]),
            "fallback_path_used": bool(adjustments["fallback_path_used"]),
        },
        "derived_metrics": {
            "total_direct_cost_usd": total_direct_cost,
            "total_tool_cost_usd": total_tool_cost,
            "total_token_count": total_tokens,
            "total_latency_seconds": total_latency,
            "total_human_minutes": float(adjustments["human_review_minutes"]),
            "total_retry_count": retry_count,
            "total_verification_count": total_verification,
            "total_recovery_steps": int(adjustments["recovery_step_count"]),
        },
        "notes": "Deterministic stub episode generated from benchmark and policy config.",
    }


def write_episode(output_dir: Path, episode: dict) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{episode['episode_id']}.json"
    with path.open("w", encoding="utf-8") as handle:
        json.dump(episode, handle, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic stub benchmark logs from configs.")
    parser.add_argument("benchmark_config", help="Path to a benchmark YAML config.")
    parser.add_argument("--episodes-per-policy", type=int, default=3, help="Number of sample episodes per policy.")
    args = parser.parse_args()

    benchmark_path = Path(args.benchmark_config)
    benchmark_config = load_yaml(benchmark_path)
    output_dir = REPO_ROOT / benchmark_config["logging"]["output_dir"]

    generated = 0
    for policy_path in recommended_policy_paths(benchmark_config):
        policy_config = load_yaml(policy_path)
        for episode_index in range(args.episodes_per_policy):
            episode = build_episode(benchmark_config, policy_config, episode_index)
            write_episode(output_dir, episode)
            generated += 1

    print(f"Generated {generated} episode logs in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
