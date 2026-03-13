# Industry Scenarios

## Purpose

This document grounds the repository's framework in a small set of realistic deployment scenarios.

## Scenario 1: Code Generation and Repair

Typical workflow:

- developer asks for implementation or patch help
- AI proposes code
- tests or review determine acceptance
- failures create debugging and rework cost

Why this scenario fits:

- quality can be measured with tests
- verification is natural
- human oversight is common but expensive

Most relevant policy questions:

- Is a strong model cheaper than repeated cheap-model retries?
- How much value does executable verification provide?
- When should unresolved failures be escalated to a developer?

Dominant cost risks:

- debugging overhead
- latency in developer workflow
- hidden defects that pass shallow review

## Scenario 2: Document Extraction and Back-Office Processing

Typical workflow:

- AI extracts fields from forms, invoices, or internal documents
- validation and cleanup happen downstream
- uncertain cases are corrected by operations staff

Why this scenario fits:

- structured outputs support precision and recall targets
- human cleanup burden is easy to model
- tools and validators are plausible

Most relevant policy questions:

- When does validator-assisted extraction beat stronger direct generation?
- Is selective review cheaper than blanket human QA?
- How costly are partial errors compared with outright failures?

Dominant cost risks:

- silent field errors
- rework queues
- compliance-sensitive mistakes

## Scenario 3: Classification and Routing Operations

Typical workflow:

- AI classifies or routes tickets, emails, claims, or requests
- hard or high-risk cases are escalated
- bad routing creates downstream handling cost

Why this scenario fits:

- episodes are short and repeatable
- confidence-based deferral is realistic
- queue economics matter

Most relevant policy questions:

- What confidence threshold minimizes total cost?
- When is a stronger default model worth it?
- How much human load does selective escalation create?

Dominant cost risks:

- misrouting
- backlog from over-escalation
- delayed handling on high-priority cases

## Cross-Scenario Insight

These three scenarios create distinct stress tests for the framework:

- code generation stresses verification and recovery
- extraction stresses structured quality and cleanup
- classification stresses routing and deferral

That makes them a strong foundation for a first research cycle before moving into more open-ended agent workflows.

## Recommended Research Use

When presenting results, each benchmark family should be tied back to one of these scenarios so that the cost assumptions feel operational rather than abstract.
