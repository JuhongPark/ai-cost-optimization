# Future Roadmap

## Next Research Steps

### 1. Freeze the first empirical cycle

- adopt the three core empirical questions defined in `docs/experiments/first-empirical-cycle-plan.md`
- declare which policy comparisons are in scope for coding, classification, and extraction
- define which scenario-cost profile will be used for weighted comparisons

### 2. Build benchmark-ready task sets

- select exact task subsets for coding, classification, extraction, and agent workflows
- document data access and evaluation scripts

### 3. Implement logging-compatible experiment templates

- define machine-readable policy ids
- define JSON episode records
- define analysis scripts for frontier reporting

### 4. Run the first comparison set

- strong-model single pass
- cheap-model single pass
- routing
- retry-enabled policy
- verification-enabled policy
- full automation vs selective HITL vs human-first

### 5. Extend indirect-cost measurement

- estimate human review time more realistically
- define recovery-step accounting
- define confidence and escalation triggers

### 6. Separate research tracks

- workflow-level policy optimization
- systems-level serving optimization

This separation prevents infrastructure gains from obscuring higher-level task-policy questions.
