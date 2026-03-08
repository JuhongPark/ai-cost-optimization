# Practitioner Guidance

## Purpose

This document translates the current research program into practical guidance for teams using AI systems.

## Core Guidance

### 1. Do not optimize API spend alone

A cheaper model path is not automatically cheaper in practice if it increases retries, verification effort, or human review.

### 2. Define acceptable quality before cost optimization

Without a quality floor, cost reduction claims are not decision-ready.

### 3. Measure full episodes, not single calls

If a task usually requires retries, tools, or fallback review, the real unit of cost is the whole episode.

### 4. Separate direct cost from indirect cost

Teams should report both:

- direct monetary spend
- operational overhead such as human time, retries, and recovery

### 5. Start with routing and verification before complex orchestration

The most practical early gains usually come from:

- replacing unnecessary strong-model usage
- routing based on task difficulty
- adding targeted verification where failure is expensive

### 6. Treat human escalation as a priced resource

Human review should be measured explicitly in minutes, rates, or queue load rather than treated as free safety margin.

## Operational Checklist

- define the task-level quality threshold
- log per-episode cost and outcome
- report retries separately from first-pass success
- report human review load separately from API cost
- compare policies on a frontier, not only on a single score
