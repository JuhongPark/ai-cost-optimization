# Policy Design Space

## Purpose

This document expands the strategy taxonomy into a more explicit design space for benchmarked AI execution policies.

## Core Idea

A policy is not just a model choice. It is a combination of decisions about model selection, routing, verification, fallback, tool use, and human oversight.

## Main Design Axes

### 1. Model Selection Axis

Possible values:

- single cheap model
- single strong model
- fixed cascade
- adaptive routing

Main effect:

- direct spend
- baseline accuracy
- probability of downstream retry or escalation

### 2. Routing Axis

Possible values:

- none
- difficulty-based
- confidence-based
- metadata-based
- budget-aware adaptive routing

Main effect:

- average cost per episode
- error concentration on hard cases

Primary risk:

- bad routing can create both direct and indirect waste

### 3. Verification Axis

Possible values:

- none
- heuristic checks
- executable tests
- structured validators
- weaker-model judge
- human review gate

Main effect:

- hidden error reduction
- acceptance reliability
- extra latency and review burden

### 4. Retry and Recovery Axis

Possible values:

- no retry
- same-model retry
- stronger-model retry
- retry with critique
- retry followed by escalation

Main effect:

- recovery of borderline failures
- longer tails in latency and spend

### 5. Tool-Use Axis

Possible values:

- no tools
- fixed tool calls
- selective tool calls
- mandatory tool-backed answers

Main effect:

- reduction of reasoning burden
- increase in orchestration complexity

### 6. Human Oversight Axis

Possible values:

- none
- final-failure-only escalation
- selective escalation
- mandatory approval
- human-first handling

Main effect:

- final reliability
- queue load
- operational cost

## Policy Classes Derived From the Design Space

### Full Automation

Typical pattern:

- no human review by default
- optional routing, verification, or retry inside the automated path

Best suited for:

- low-risk, high-volume tasks

### Selective HITL

Typical pattern:

- automated first pass
- explicit escalation trigger for uncertain or failed cases

Best suited for:

- medium-risk tasks with skewed difficulty

### Human-First

Typical pattern:

- human review early in the episode
- AI assists rather than decides autonomously

Best suited for:

- high-risk or high-ambiguity tasks

## Minimal Policy Matrix for Early Experiments

The first benchmark cycle should cover a small but expressive matrix:

- cheap single pass
- strong single pass
- difficulty-based routing
- cheap plus retry
- cheap plus verifier plus selective HITL
- tool-assisted extraction
- human-first baseline

## Interpretation Rule

The goal is not to search an unlimited policy space. The goal is to identify which axis shifts the cost-quality frontier most for each task family.

## Questions This Design Space Supports

- Does routing help more than retry?
- Does verification reduce more cost than it adds?
- When does selective escalation dominate human-first review?
- Which policy axes matter only for certain benchmark families?
