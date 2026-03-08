#!/usr/bin/env python3

from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TABLES_DIR = REPO_ROOT / "results" / "tables"
REPORTS_DIR = REPO_ROOT / "results" / "reports"
DOC_REPORTS_DIR = REPO_ROOT / "docs" / "reports"


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def to_float(row: dict[str, str], key: str) -> float:
    return float(row[key])


def find_lowest_cost_success(rows: list[dict[str, str]]) -> dict[str, str] | None:
    successful = [row for row in rows if to_float(row, "success_rate") >= 1.0]
    if not successful:
        return None
    return min(successful, key=lambda row: to_float(row, "avg_weighted_total_cost"))


def benchmark_label(stem: str) -> str:
    labels = {
        "coding_humaneval_v1": "coding",
        "classification_mmlu_subset_v1": "classification",
        "extraction_structured_fields_v1": "extraction",
    }
    return labels.get(stem, stem)


def build_summary() -> str:
    sections: list[str] = []
    sections.append("# Final Cycle Summary\n")
    sections.append("## Scope\n")
    sections.append(
        "This report summarizes the completed local first-cycle experiment pipeline. "
        "The results are generated from deterministic stub executions, so they validate the framework and execution flow rather than prove live-model empirical claims.\n"
    )
    sections.append("## Benchmark Findings\n")

    cross_benchmark_claims: list[str] = []
    for csv_path in sorted(TABLES_DIR.glob("*.csv")):
        rows = load_rows(csv_path)
        best = find_lowest_cost_success(rows)
        label = benchmark_label(csv_path.stem)
        sections.append(f"### {label.capitalize()}\n")
        if best is None:
            sections.append("- No policy reached the quality threshold in the current local cycle.\n")
            continue
        sections.append(
            f"- Lowest-cost successful policy: `{best['policy_id']}` "
            f"(`{best['policy_class']}`) with weighted total cost {best['avg_weighted_total_cost']}, "
            f"direct cost {best['avg_direct_cost_usd']}, and human minutes {best['avg_human_minutes']}.\n"
        )
        sections.append(
            f"- Success rate: {best['success_rate']}; latency: {best['avg_latency_seconds']}; "
            f"retries: {best['avg_retry_count']}.\n"
        )
        if best["policy_class"] == "selective_hitl":
            cross_benchmark_claims.append(f"{label}: selective HITL was cost-competitive and threshold-satisfying")
        elif best["policy_class"] == "full_automation":
            cross_benchmark_claims.append(f"{label}: full automation reached the threshold at the lowest weighted total cost")
        else:
            cross_benchmark_claims.append(f"{label}: human-first remained competitive")

    sections.append("\n## Cross-Benchmark Interpretation\n")
    sections.append(
        "- Weighted total-cost formula used in this local cycle: "
        "`direct + 0.0001*latency + 0.002*human_minutes + 0.0005*retries + 0.00025*verification`.\n"
    )
    for claim in cross_benchmark_claims:
        sections.append(f"- {claim}\n")

    sections.append(
        "- Inference from the local cycle: the optimal policy class depends on task family rather than admitting a single universal winner.\n"
    )
    sections.append(
        "- The local cycle shows that winner selection can vary across task families once weighted total cost and quality thresholds are applied.\n"
    )
    sections.append(
        "- This supports the repository thesis that direct cost alone is not sufficient; policy choice must be evaluated under explicit quality thresholds and with indirect-cost visibility.\n"
    )

    sections.append("\n## Conclusion Boundary\n")
    sections.append(
        "- Completed: measurement freeze, benchmark freeze, stub-backed policy comparison run, cross-benchmark summary, and repository-level synthesis.\n"
    )
    sections.append(
        "- Not yet completed: live model execution against real benchmark data. The current conclusion is therefore structural and procedural, not a final empirical claim about production models.\n"
    )

    sections.append("\n## Next Step\n")
    sections.append(
        "- Replace the stub benchmark runner with a real benchmark execution layer while preserving the same schema, configs, and aggregation pipeline.\n"
    )
    return "".join(sections)


def main() -> int:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    DOC_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    summary_text = build_summary()
    result_path = REPORTS_DIR / "final_cycle_summary.md"
    doc_path = DOC_REPORTS_DIR / "final-cycle-summary.md"

    result_path.write_text(summary_text, encoding="utf-8")
    doc_path.write_text(summary_text, encoding="utf-8")
    print(f"Wrote {result_path}")
    print(f"Wrote {doc_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
