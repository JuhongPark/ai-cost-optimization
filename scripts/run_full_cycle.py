#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def benchmark_configs() -> list[Path]:
    return sorted((REPO_ROOT / "configs" / "benchmarks").glob("*.yaml"))


def raw_dir_from_config(config_path: Path) -> Path:
    stem_map = {
        "coding-human-eval.yaml": "coding_humaneval_v1",
        "classification-mmlu-subset.yaml": "classification_mmlu_subset_v1",
        "extraction-structured-fields.yaml": "extraction_structured_fields_v1",
    }
    return REPO_ROOT / "results" / "raw" / stem_map[config_path.name]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the full local experiment cycle.")
    parser.add_argument("--episodes-per-policy", type=int, default=3)
    args = parser.parse_args()

    for config_path in benchmark_configs():
        run(["python3", "scripts/run_stub_benchmark.py", str(config_path), "--episodes-per-policy", str(args.episodes_per_policy)])
        run(["python3", "scripts/validate_episode.py", str(raw_dir_from_config(config_path))])
        run(["python3", "scripts/aggregate_results.py", str(raw_dir_from_config(config_path))])

    run(["python3", "scripts/synthesize_findings.py"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
