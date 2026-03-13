# Execution Checklist

## Purpose

This checklist turns the first empirical cycle into an execution-ready workflow.

## Before Running

- confirm the benchmark, policy, and scenario ids in `configs/studies/first-empirical-cycle.yaml`
- confirm that each benchmark has the intended in-scope policies
- confirm the linked reporting template for benchmark-level output
- confirm the weighted profile used for scenario-specific comparison

## During Running

- validate episode logs against the schema
- record threshold-satisfying success separately from raw quality
- keep direct and indirect cost fields separate
- note any evaluator limitations that affect interpretation

## After Running

- fill the benchmark report template
- run cross-benchmark synthesis using the shared template
- record sensitivity findings
- capture ranking instability explicitly

## Exit Criteria

The first empirical cycle is complete when:

- all three benchmark families have benchmark-level reports
- weighted and threshold-constrained winners are documented
- selective HITL has been compared against both full automation and human-first
- second-cycle priorities are written down
