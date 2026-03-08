#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def benchmark_configs() -> list[Path]:
    return sorted((REPO_ROOT / "configs" / "benchmarks").glob("*.yaml"))


def raw_real_dir(config_path: Path) -> Path:
    stem_map = {
        "coding-human-eval.yaml": "coding_humaneval_v1",
        "classification-mmlu-subset.yaml": "classification_mmlu_subset_v1",
        "extraction-structured-fields.yaml": "extraction_structured_fields_v1",
    }
    return REPO_ROOT / "results" / "raw_real" / stem_map[config_path.name]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the real execution layer end to end.")
    parser.add_argument("--provider-config", default="configs/providers/offline-heuristic.yaml")
    args = parser.parse_args()

    for config_path in benchmark_configs():
        run(["python3", "scripts/run_real_benchmark.py", str(config_path), "--provider-config", args.provider_config])
        run(["python3", "scripts/validate_episode.py", str(raw_real_dir(config_path))])
        run([
            "python3",
            "scripts/aggregate_results.py",
            str(raw_real_dir(config_path)),
            "--tables-dir",
            "results/tables_real",
            "--reports-dir",
            "results/reports_real",
        ])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
