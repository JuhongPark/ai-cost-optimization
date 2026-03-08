#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def load_episode(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def aggregate(directory: Path) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for path in sorted(directory.glob("*.json")):
        episode = load_episode(path)
        grouped[episode["policy_id"]].append(episode)

    rows: list[dict] = []
    for policy_id, episodes in sorted(grouped.items()):
        successes = [episode for episode in episodes if episode["quality_threshold_met"]]
        rows.append(
            {
                "policy_id": policy_id,
                "policy_class": episodes[0]["policy_class"],
                "episodes": len(episodes),
                "success_rate": round(len(successes) / len(episodes), 4),
                "avg_quality_score": round(mean([float(episode.get("quality_score") or 0.0) for episode in episodes]), 4),
                "avg_direct_cost_usd": round(mean([float(episode["derived_metrics"]["total_direct_cost_usd"]) for episode in episodes]), 6),
                "avg_latency_seconds": round(mean([float(episode["derived_metrics"]["total_latency_seconds"]) for episode in episodes]), 4),
                "avg_human_minutes": round(mean([float(episode["derived_metrics"]["total_human_minutes"]) for episode in episodes]), 4),
                "avg_retry_count": round(mean([float(episode["derived_metrics"]["total_retry_count"]) for episode in episodes]), 4),
                "avg_verification_count": round(mean([float(episode["derived_metrics"]["total_verification_count"]) for episode in episodes]), 4),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, benchmark_id: str, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"# {benchmark_id} Summary\n\n")
        if not rows:
            handle.write("No rows available.\n")
            return
        headers = list(rows[0].keys())
        handle.write("| " + " | ".join(headers) + " |\n")
        handle.write("| " + " | ".join(["---"] * len(headers)) + " |\n")
        for row in rows:
            handle.write("| " + " | ".join(str(row[key]) for key in headers) + " |\n")
        handle.write("\n")
        best = max(rows, key=lambda row: (row["success_rate"], -row["avg_direct_cost_usd"]))
        handle.write(
            "Leading stub policy by threshold-satisfying success rate: "
            f"`{best['policy_id']}` ({best['policy_class']}) with success rate {best['success_rate']}.\n"
        )


def benchmark_id_from_directory(path: Path) -> str:
    return path.name


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate raw episode logs into CSV and Markdown summaries.")
    parser.add_argument("raw_dir", help="Directory containing raw episode JSON logs.")
    parser.add_argument("--tables-dir", default="results/tables", help="Directory for aggregate CSV output.")
    parser.add_argument("--reports-dir", default="results/reports", help="Directory for Markdown summaries.")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    rows = aggregate(raw_dir)
    benchmark_id = benchmark_id_from_directory(raw_dir)

    csv_path = Path(args.tables_dir) / f"{benchmark_id}.csv"
    md_path = Path(args.reports_dir) / f"{benchmark_id}.md"
    write_csv(csv_path, rows)
    write_markdown(md_path, benchmark_id, rows)

    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
