#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import requests
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def slug_to_filename(policy_id: str) -> str:
    return policy_id.replace("_", "-") + ".yaml"


@dataclass
class ProviderResponse:
    text: str
    latency_seconds: float
    input_tokens: int
    output_tokens: int


class BaseProvider:
    def complete(self, model_name: str, prompt: str) -> ProviderResponse:
        raise NotImplementedError


class OfflineHeuristicProvider(BaseProvider):
    def __init__(self, benchmark_family: str) -> None:
        self.benchmark_family = benchmark_family

    def complete(self, model_name: str, prompt: str) -> ProviderResponse:
        strong = "strong" in model_name
        if self.benchmark_family == "coding":
            if "add(a, b)" in prompt:
                text = "def add(a, b):\n    return a + b\n" if strong else "def add(a, b):\n    return a-b\n"
            else:
                text = "def is_even(n):\n    return n % 2 == 0\n" if strong else "def is_even(n):\n    return n % 2\n"
        elif self.benchmark_family == "classification":
            if "Red Planet" in prompt:
                text = "B" if strong else "A"
            else:
                text = "C" if strong else "D"
        else:
            if "Alice Kim" in prompt:
                text = json.dumps({
                    "name": "Alice Kim",
                    "role": "Data Scientist",
                    "company": "Acme Labs" if strong else "Acme"
                })
            else:
                text = json.dumps({
                    "name": "Brian Lee",
                    "role": "Product Manager",
                    "company": "Northwind"
                } if strong else {
                    "name": "Brian",
                    "role": "Manager",
                    "company": "Northwind"
                })
        latency = 1.8 if strong else 0.9
        input_tokens = max(1, len(prompt) // 4)
        output_tokens = max(1, len(text) // 4)
        return ProviderResponse(text=text, latency_seconds=latency, input_tokens=input_tokens, output_tokens=output_tokens)


class OpenAICompatibleProvider(BaseProvider):
    def __init__(self, provider_config: dict[str, Any]) -> None:
        base_url_env = provider_config["base_url_env"]
        api_key_env = provider_config["api_key_env"]
        self.base_url = os.environ.get(base_url_env)
        self.api_key = os.environ.get(api_key_env)
        timeout = provider_config.get("request", {}).get("timeout_seconds", 60)
        self.timeout = float(timeout)
        if not self.base_url or not self.api_key:
            raise RuntimeError(
                f"Missing provider environment variables: {base_url_env} and/or {api_key_env}"
            )

    def complete(self, model_name: str, prompt: str) -> ProviderResponse:
        started = datetime.now(tz=UTC)
        response = requests.post(
            f"{self.base_url.rstrip('/')}/chat/completions",
            timeout=self.timeout,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model_name,
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        response.raise_for_status()
        payload = response.json()
        content = payload["choices"][0]["message"]["content"]
        usage = payload.get("usage", {})
        ended = datetime.now(tz=UTC)
        return ProviderResponse(
            text=content,
            latency_seconds=(ended - started).total_seconds(),
            input_tokens=int(usage.get("prompt_tokens", max(1, len(prompt) // 4))),
            output_tokens=int(usage.get("completion_tokens", max(1, len(content) // 4))),
        )


def make_provider(provider_config: dict[str, Any], benchmark_family: str) -> BaseProvider:
    provider_type = provider_config["provider_type"]
    if provider_type == "offline_heuristic":
        return OfflineHeuristicProvider(benchmark_family)
    if provider_type == "openai_compatible":
        return OpenAICompatibleProvider(provider_config)
    raise ValueError(f"Unsupported provider_type: {provider_type}")


def evaluate_task(task_family: str, predicted: str, expected: Any) -> dict[str, Any]:
    if task_family == "coding":
        normalized_pred = predicted.strip()
        normalized_expected = str(expected).strip()
        score = 1.0 if normalized_pred == normalized_expected else 0.0
        return {"pass_rate": score, "quality_score": score}
    if task_family == "classification":
        score = 1.0 if predicted.strip() == str(expected).strip() else 0.0
        return {"accuracy": score, "quality_score": score}
    parsed = {}
    try:
        parsed = json.loads(predicted)
    except json.JSONDecodeError:
        parsed = {}
    expected_fields = dict(expected)
    matched = sum(1 for key, value in expected_fields.items() if parsed.get(key) == value)
    precision = matched / max(1, len(parsed))
    recall = matched / max(1, len(expected_fields))
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "quality_score": round(f1, 4),
    }


def threshold_met(benchmark_config: dict[str, Any], metrics: dict[str, Any]) -> bool:
    primary_metric = benchmark_config["acceptance_criteria"]["metric"]
    primary_threshold = float(benchmark_config["acceptance_criteria"]["threshold_value"])
    primary_value = float(metrics.get(primary_metric, 0.0))
    if primary_value < primary_threshold:
        return False
    for key, threshold in benchmark_config.get("secondary_criteria", {}).items():
        metric_key = key.removesuffix("_min")
        if float(metrics.get(metric_key, 0.0)) < float(threshold):
            return False
    return True


def select_model_name(policy_config: dict[str, Any], provider_config: dict[str, Any], task: dict[str, Any]) -> tuple[str, int]:
    strategy = policy_config["model_strategy"]
    if strategy.get("routing") == "difficulty_based":
        difficulty = task.get("metadata", {}).get("difficulty", "easy")
        key = "strong_model" if difficulty in {"hard", "medium"} else "cheap_model"
        return provider_config["models"][key], 1
    primary = strategy["primary_model"]
    return provider_config["models"].get(primary, primary), 0


def prompt_with_policy(task_prompt: str, policy_config: dict[str, Any]) -> str:
    policy_id = policy_config["policy_id"]
    return f"Policy: {policy_id}\n\n{task_prompt}"


def direct_cost_usd(input_tokens: int, output_tokens: int, model_name: str) -> float:
    rate = 0.000004 if "strong" in model_name or "gpt-4" in model_name else 0.000002
    return round((input_tokens + output_tokens) * rate / 1000, 6)


def build_episode(
    benchmark_config: dict[str, Any],
    policy_config: dict[str, Any],
    provider_config: dict[str, Any],
    task: dict[str, Any],
    episode_index: int,
) -> dict[str, Any]:
    provider = make_provider(provider_config, benchmark_config["task_family"])
    model_name, routing_decisions = select_model_name(policy_config, provider_config, task)
    prompt = prompt_with_policy(task["prompt"], policy_config)
    response = provider.complete(model_name, prompt)
    metrics = evaluate_task(benchmark_config["task_family"], response.text, task["expected_answer"])
    success = threshold_met(benchmark_config, metrics)
    human_mode = policy_config["human_oversight"]["mode"]
    human_review_count = 1 if human_mode in {"immediate", "selective"} and not success else 0
    human_review_minutes = 5.0 if human_mode == "immediate" else (1.5 if human_review_count else 0.0)
    retry_enabled = bool(policy_config.get("retry_policy", {}).get("enabled"))
    retry_count = 1 if retry_enabled and not success else 0
    verification_enabled = bool(policy_config.get("verification_policy", {}).get("enabled"))
    verification_count = 1 if verification_enabled else 0
    tool_enabled = bool(policy_config.get("tool_policy", {}).get("enabled", False))
    tool_call_count = 1 if tool_enabled else 0
    attempt_cost = direct_cost_usd(response.input_tokens, response.output_tokens, model_name)
    started = datetime(2026, 3, 8, 13, 0, 0, tzinfo=UTC) + timedelta(minutes=episode_index)
    ended = started + timedelta(seconds=response.latency_seconds)
    failure_category = None if success else ("human_escalation" if human_review_count else "quality_below_threshold")

    return {
        "episode_id": f"{benchmark_config['benchmark_id']}__{policy_config['policy_id']}__{task['task_id']}",
        "task_family": benchmark_config["task_family"],
        "task_id": task["task_id"],
        "policy_id": policy_config["policy_id"],
        "policy_class": policy_config["policy_class"],
        "model_id": model_name,
        "prompt_version": "real_v1",
        "started_at": started.isoformat(),
        "ended_at": ended.isoformat(),
        "duration_seconds": round(response.latency_seconds, 4),
        "final_status": "success" if success else ("human_escalation" if human_review_count else "failure"),
        "failure_category": failure_category,
        "quality_score": float(metrics["quality_score"]),
        "quality_metrics": {
            "accuracy": metrics.get("accuracy"),
            "pass_rate": metrics.get("pass_rate"),
            "f1": metrics.get("f1"),
            "precision": metrics.get("precision"),
            "recall": metrics.get("recall"),
        },
        "quality_threshold_met": success,
        "attempts": [
            {
                "attempt_index": 0,
                "attempt_model_id": model_name,
                "input_tokens": response.input_tokens,
                "output_tokens": response.output_tokens,
                "attempt_latency_seconds": round(response.latency_seconds, 4),
                "attempt_cost_usd": attempt_cost,
                "verification_count": verification_count,
                "tool_call_count": tool_call_count,
                "tool_cost_usd": round(tool_call_count * 0.001, 6),
                "attempt_outcome": "accepted" if success else ("escalated" if human_review_count else "failed"),
            }
        ],
        "indirect_cost": {
            "retry_count": retry_count,
            "human_review_count": human_review_count,
            "human_review_minutes": human_review_minutes,
            "human_intervention_count": human_review_count,
            "escalation_trigger": policy_config["human_oversight"]["escalation_trigger"] if human_review_count else None,
            "recovery_step_count": retry_count,
            "routing_decision_count": routing_decisions,
            "fallback_path_used": bool(retry_count),
        },
        "derived_metrics": {
            "total_direct_cost_usd": round(attempt_cost + (tool_call_count * 0.001), 6),
            "total_tool_cost_usd": round(tool_call_count * 0.001, 6),
            "total_token_count": response.input_tokens + response.output_tokens,
            "total_latency_seconds": round(response.latency_seconds, 4),
            "total_human_minutes": human_review_minutes,
            "total_retry_count": retry_count,
            "total_verification_count": verification_count,
            "total_recovery_steps": retry_count,
        },
        "notes": "Real execution layer episode using provider adapter.",
    }


def write_episode(path: Path, episode: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(episode, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a benchmark through the real execution layer.")
    parser.add_argument("benchmark_config")
    parser.add_argument("--provider-config", default="configs/providers/offline-heuristic.yaml")
    args = parser.parse_args()

    benchmark_config = load_yaml(Path(args.benchmark_config))
    provider_config = load_yaml(Path(args.provider_config))
    dataset_path = REPO_ROOT / benchmark_config["dataset_path"]
    output_dir = REPO_ROOT / benchmark_config["logging"]["real_run_output_dir"]
    tasks = load_jsonl(dataset_path)

    for policy_id in benchmark_config["recommended_policies"]:
        policy_path = REPO_ROOT / "configs" / "policies" / slug_to_filename(policy_id)
        policy_config = load_yaml(policy_path)
        for episode_index, task in enumerate(tasks):
            episode = build_episode(benchmark_config, policy_config, provider_config, task, episode_index)
            write_episode(output_dir / f"{episode['episode_id']}.json", episode)

    print(f"Wrote real-run episodes to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
