# Conclusion Plan

## Purpose

This document defines the minimum scope required to reach a first conclusion in this repository.

## Definition of Done

A first conclusion is considered valid when all of the following are complete:

1. **Measurement freeze**
   - episode schema is fixed
   - policy ids are fixed
   - benchmark configs are fixed
   - aggregation rules are fixed

2. **Benchmark freeze**
   - at least three task families are included
   - each task family has an explicit quality threshold
   - each task family has a fixed comparison set of policies

3. **Policy comparison run**
   - all selected policies are executed on all selected benchmarks
   - raw episode logs are generated
   - all raw logs pass schema validation
   - aggregate tables are generated for every benchmark

4. **Cross-benchmark analysis**
   - each benchmark has a per-policy comparison summary
   - direct cost and indirect cost are both analyzed
   - automation, selective HITL, and human-first policies are compared where relevant

5. **Final synthesis**
   - a repository-level summary is written
   - the boundary of the conclusion is stated clearly
   - remaining limitations and next steps are documented

## Minimum Benchmark Set

The minimum benchmark set for a first conclusion is:

- coding
- classification
- extraction

Agent workflows remain an important extension, but are not required for the first conclusion.

## Minimum Policy Set

The minimum policy comparison set is:

- strong-model single pass
- cheap-model single pass
- routing
- cheap model with retry
- verifier-gated HITL
- confidence-gated HITL
- human-first

Not every benchmark needs every policy, but each benchmark must compare at least:

- one strong automated baseline
- one cheap automated baseline
- one selective HITL policy

## Required Questions for the First Conclusion

The first conclusion must answer:

1. Which policy reaches the quality threshold at the lowest total cost for each task family?
2. When is selective human oversight cheaper than full automation?
3. When does direct-cost reduction fail to reduce total cost?
4. Which task families are most sensitive to indirect-cost burden?

## Current Execution Target

Within the current local environment, the achievable target is a full **stub-backed research cycle**:

- benchmark configs drive execution
- synthetic episode logs are generated deterministically
- logs are validated against the schema
- tables and reports are generated automatically
- repository-level synthesis is produced from those outputs

This is sufficient for a structured first-cycle prototype, but not for a real empirical conclusion about live model behavior.

## Completion Boundary

The first cycle is complete when:

- the full local pipeline runs end to end
- every benchmark produces raw logs, tables, and a report
- a cross-benchmark synthesis report is generated
- the repository documents what is concluded and what remains to be tested with real model execution
