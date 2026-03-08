# Results

This directory stores experiment outputs.

## Layout

- `raw/`: raw episode logs that should conform to `schemas/episode.schema.json`
- `tables/`: aggregated CSV or Markdown tables
- `figures/`: charts such as cost-quality frontiers
- `reports/`: benchmark-specific summaries

## Output Contract

Every benchmark run should produce:

1. raw episode logs
2. one aggregate table with per-policy metrics
3. one short summary note describing dominant cost drivers
