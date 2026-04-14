# Policy Configs

This directory stores reusable execution policies for benchmark studies. Each file declares a model strategy, retry policy, verification policy, and human-oversight mode.

## Single-Pass Baselines

- [`cheap-model-single-pass.yaml`](cheap-model-single-pass.yaml): cheap model baseline for first-pass cost comparison.
- [`strong-model-single-pass.yaml`](strong-model-single-pass.yaml): strong model baseline with no planned retries and no proactive human review.
- [`human-first.yaml`](human-first.yaml): human-first baseline for high-risk or high-recovery-cost tasks.

## Automation With Recovery

- [`cheap-model-retry.yaml`](cheap-model-retry.yaml): cheap model with limited retries before terminal failure.
- [`difficulty-routing.yaml`](difficulty-routing.yaml): route easy cases to a cheap model and hard cases to a strong model.
- [`tool-assisted-extraction.yaml`](tool-assisted-extraction.yaml): extraction policy that uses tools or external APIs before resorting to human review.

## Selective Human-In-The-Loop

- [`cheap-model-verifier-hitl.yaml`](cheap-model-verifier-hitl.yaml): cheap model policy with verification and selective human escalation on failure.
- [`confidence-gated-hitl.yaml`](confidence-gated-hitl.yaml): escalate to human review when model confidence falls below threshold.
- [`verifier-gated-hitl.yaml`](verifier-gated-hitl.yaml): escalate when verification fails or repeated retries do not recover quality.
