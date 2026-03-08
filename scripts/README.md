# Scripts

This directory stores runnable helpers for the experiment skeleton.

- `validate_episode.py`: validate raw episode logs against the JSON schema
- `run_stub_benchmark.py`: generate deterministic sample episode logs from benchmark and policy configs
- `aggregate_results.py`: aggregate raw episode logs into CSV and Markdown summaries
- `run_full_cycle.py`: run the full local benchmark cycle end to end
- `synthesize_findings.py`: write a cross-benchmark final summary from aggregate outputs
- `run_real_benchmark.py`: run benchmark tasks through a provider-backed execution layer
- `run_real_cycle.py`: run the provider-backed execution layer across all benchmark configs
