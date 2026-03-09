# MIT SDM Related Work

## Purpose

This note narrows the broader MIT research landscape to work specifically connected to the MIT System Design and Management (SDM) program.

The main conclusion is that, as of March 9, 2026, MIT SDM does not appear to host a large, centralized research stream explicitly framed as "AI cost optimization." Instead, SDM-relevant work is distributed across a small number of theses and research outputs that overlap with this repository in three ways:

- commercialization and deployment strategy for AI systems
- architectural design of AI-enabled or AI-adjacent systems
- efficiency-oriented machine learning work in domain applications

That makes SDM more relevant to this repository's deployment, systems, and governance questions than to its core direct-inference-cost measurement questions.

## High-Level Takeaway

The strongest MIT SDM overlap with this repository is not on token pricing, routing, or serving efficiency. It is on the systems-design question around when AI creates value, how architectural choices change risk and resilience, and how organizations should structure adoption decisions.

In other words:

- MIT-wide research is stronger on direct AI cost economics.
- MIT SDM research is stronger on systems architecture, commercialization, and deployment design.

This is useful for the repository because the project is not only about cheaper inference. It is also about designing end-to-end workflows where technical cost, organizational cost, and governance cost interact.

## Most Relevant SDM Research

### 1. AI commercialization strategy

**Source:** `Thesis: A strategic perspective on the commercialization of artificial intelligence`  
SDM page: https://sdm.mit.edu/research-practice/thesis-a-strategic-perspective-on-the-commercialization-of-artificial-intelligence/

Submitted by Siddhartha Ray Barua, this thesis is the clearest SDM item directly aligned with the repository's research question.

Based on the SDM summary, the thesis examines:

- how firms identify valuable AI use cases
- how AI technologies evolve across industries
- how organizations can prepare to commercialize AI while reducing risk

Why it matters here:

- It supports treating AI deployment as a system-level design and portfolio-allocation problem, not just a model-selection problem.
- It is especially relevant to fixed-cost questions such as integration, organizational readiness, and strategic fit.
- It strengthens the repository's distinction between "can the model solve it?" and "is this AI workflow worth deploying at all?"

### 2. Generative multi-agent system resilience

**Source:** `SDM Student Wins Best Student Paper Award at CAS 2025`  
SDM page: https://sdm.mit.edu/research-practice/dao-best-paper-cas-2025/

On March 18, 2025, MIT SDM reported that Nguyen-Luc Dao, SDM '22, received the Best Student Paper Award at Complex Adaptive Systems 2025 for `Designing Generative Multi-Agent Systems for Resilience`, coauthored with Dr. Bryan Moser.

The SDM summary says the study investigated how architectural choices such as:

- group size
- prompting
- topology

change resilience against malicious agents.

Why it matters here:

- It is directly relevant to AI workflow architecture, especially when this repository evaluates multi-step or agentic policies.
- It provides an SDM-specific bridge between cost optimization and system resilience, since low-cost automation can become expensive if adversarial fragility or recovery overhead is ignored.
- It suggests that architecture choices should be evaluated not only by performance and cost, but also by failure containment and recovery burden.

### 3. Neural-network efficiency in business applications

**Source:** `Thesis: Evaluation of the smoothing activation function in neural networks for business applications`  
SDM page: https://sdm.mit.edu/research-practice/thesis-evaluation-of-the-smoothing-activation-function-in-neural-networks-for-business-applications/

Submitted by Jun Siong Ang, this thesis compares a modified Softplus-family activation function against ReLU, explicitly discussing gradient propagation, model sparsity, and computational efficiency.

Why it matters here:

- It is not a workflow-cost study, but it is still relevant as SDM work on technical efficiency.
- It shows that SDM-related AI research sometimes addresses cost indirectly through model efficiency rather than directly through deployment economics.
- It is best treated as adjacent background rather than a central prior work item for this repository.

### 4. Machine learning plus technoeconomics in geothermal exploration

**Source:** `Research: Machine learning in geothermal exploration`  
SDM page: https://sdm.mit.edu/research-practice/research-machine-learning-in-geothermal-exploration/

MIT SDM reported on April 28 that Chad Holmes SDM '20 authored work on:

- machine learning modeling and uncertainty characterization for geothermal exploration
- geothermal technoeconomic modeling with design flexibility

Both papers were described by SDM as extensions of thesis work completed in the SDM program in summer 2020.

Why it matters here:

- This is domain-specific rather than general AI cost optimization research.
- It is still useful because it combines predictive modeling with technoeconomic reasoning, which is conceptually close to this repository's effort to connect technical performance with total cost.
- It suggests a pattern SDM is well suited for: combining analytics with system-level economic design in applied sectors.

### 5. Technology improvement forecasting

**Source:** `Research: Predicting technology performance improvements`  
SDM page: https://sdm.mit.edu/research-practice/research-predicting-technology-performance-improvements/

MIT SDM reported on August 26 that Anuraag Singh SDM '18 coauthored research using patent data to estimate future performance improvement across technology domains.

Why it matters here:

- This is not AI-cost work by itself.
- It is relevant as a method for forecasting future cost-performance shifts in enabling technologies.
- For this repository, it is best interpreted as supporting context for thinking about how quickly AI price-performance frontiers can move.

## Assessment Relative to This Repository

The SDM-specific material is useful, but it does not replace the broader MIT literature already captured in [mit-research-landscape.md](/home/jpark/Project/ai4-cost-optimization/docs/references/mit-research-landscape.md). The best reading is:

- MIT FutureTech and related MIT labs provide the strongest direct evidence on AI cost, inference economics, and automation thresholds.
- MIT SDM provides complementary evidence on systems architecture, commercialization, and deployment design.

That implies the most defensible way to use MIT SDM in this repository is as support for the indirect-cost and system-design side of the thesis.

### Where SDM is especially useful

- fixed versus marginal deployment cost
- commercialization readiness and strategic fit
- system architecture and resilience tradeoffs
- domain-specific technoeconomic integration

### Where SDM is comparatively weak

- token-level inference cost analysis
- routing or cascade optimization
- test-time compute control
- serving-stack efficiency

## Recommended Incorporation Into This Research

MIT SDM-related work suggests three concrete refinements for this repository.

### 1. Separate deployment design from inference optimization

The SDM material reinforces that some of the biggest costs are determined before the first model call:

- integration effort
- operating-model redesign
- risk-management requirements
- architectural resilience decisions

This repository should keep distinguishing episode-level variable cost from deployment-level fixed cost.

### 2. Expand indirect cost to include resilience and governance burden

The CAS 2025 SDM work implies that architecture choices can create downstream recovery cost when systems face malicious or unreliable behavior. A low-cost policy may not be globally efficient if it increases:

- monitoring burden
- escalation frequency
- containment cost
- recovery cost

### 3. Treat commercialization fit as a cost filter

The Barua thesis implies that some use cases should be rejected before workflow optimization begins because their strategic value, organizational readiness, or use-case fit is weak. That is a useful upstream screen for this repository's practical guidance.

## Bottom Line

There is relevant MIT SDM work, but it is complementary rather than central to the repository's main literature base.

The most relevant SDM contribution is the AI commercialization thesis, followed by the CAS 2025 work on generative multi-agent resilience. Together, they strengthen the repository's argument that AI cost optimization is not only about cheaper model calls, but also about better system architecture, safer deployment, and more disciplined adoption decisions.

## Source Pointers

- MIT SDM: `Thesis: A strategic perspective on the commercialization of artificial intelligence`  
  https://sdm.mit.edu/research-practice/thesis-a-strategic-perspective-on-the-commercialization-of-artificial-intelligence/
- MIT SDM: `SDM Student Wins Best Student Paper Award at CAS 2025`  
  https://sdm.mit.edu/research-practice/dao-best-paper-cas-2025/
- MIT SDM: `Thesis: Evaluation of the smoothing activation function in neural networks for business applications`  
  https://sdm.mit.edu/research-practice/thesis-evaluation-of-the-smoothing-activation-function-in-neural-networks-for-business-applications/
- MIT SDM: `Research: Machine learning in geothermal exploration`  
  https://sdm.mit.edu/research-practice/research-machine-learning-in-geothermal-exploration/
- MIT SDM: `Research: Predicting technology performance improvements`  
  https://sdm.mit.edu/research-practice/research-predicting-technology-performance-improvements/

## Caveat

This note is based on publicly accessible MIT SDM summaries and research-output pages that were reachable on March 9, 2026. The assessment that SDM has limited direct work on "AI cost optimization" is an inference from those sources, not an official MIT SDM claim.
