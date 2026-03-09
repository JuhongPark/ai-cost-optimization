# Prior Work

## Scope

This note reviews prior work most relevant to AI cost optimization research. The focus is not general capability improvement, but methods that change the cost of obtaining useful problem-solving performance.

## Key Themes

### 1. Cost-aware model selection and cascades

**FrugalGPT (Chen et al., 2023)**  
Source: https://arxiv.org/abs/2305.05176

FrugalGPT is one of the clearest starting points for this repository. It frames LLM usage as an inference cost problem and proposes three families of cost-reduction strategies: prompt adaptation, model approximation, and LLM cascades. Its central result is that routing across models can drastically reduce cost while maintaining or even improving quality on some tasks.

Relevance to this project:

- establishes cost-aware model routing as a primary optimization axis
- treats the best model as a reference point rather than the default answer
- supports the idea that AI usage should be evaluated at the workflow level, not just at the single-model level

### 2. Cascaded problem solving as a general framework

**Language Model Cascades (Dohan et al., 2022)**  
Source: https://arxiv.org/abs/2207.10342

Language Model Cascades provides a broader conceptual frame for chaining models, verifiers, and tools. It does not focus narrowly on cost, but it is important because it formalizes multi-step LM systems as structured programs with control flow. That matters for cost optimization because most meaningful savings will likely come from system design choices rather than from a single model call.

Relevance to this project:

- gives a language for thinking about tool use, verification, and staged reasoning
- supports evaluating the cost of a full problem-solving process
- suggests that optimization should target policies over sequences of actions, not isolated prompts

### 3. Test-time compute as a substitute for larger models

**Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (Snell et al., 2024)**  
Source: https://arxiv.org/abs/2408.03314

This paper studies how extra inference-time compute can improve performance, and argues that the best strategy depends on prompt difficulty. The key result is that adaptive allocation of test-time compute can outperform simpler baselines and, in some FLOPs-matched settings, outperform a much larger model.

Relevance to this project:

- directly supports the idea that cost optimization is partly a budget-allocation problem
- shows that prompt difficulty should influence how much compute is spent
- suggests that fixed policies are likely suboptimal relative to adaptive ones

### 4. Simple mechanisms for test-time budget control

**s1: Simple test-time scaling (Muennighoff et al., 2025)**  
Source: https://arxiv.org/abs/2501.19393

s1 is important because it shows that test-time scaling does not necessarily require a complicated reinforcement learning pipeline. The paper introduces budget forcing as a way to explicitly control how long a model reasons at inference time, and reports gains on reasoning-heavy tasks.

Relevance to this project:

- provides a concrete mechanism for controlling inference budget
- supports explicit test-time budget policies as an experimental variable
- is especially relevant for reasoning tasks where "think longer" may trade cost for quality

### 5. Decoding acceleration without changing outputs

**Fast Inference from Transformers via Speculative Decoding (Leviathan et al., 2022; ICML 2023)**  
Source: https://arxiv.org/abs/2211.17192

Speculative decoding addresses a different layer of the cost stack: system-side decoding efficiency. It speeds up generation by using a smaller approximation model to propose tokens and a larger model to verify them, while preserving the output distribution.

Relevance to this project:

- shows that cost optimization can happen below the workflow level
- separates quality-preserving acceleration from quality-cost tradeoff strategies
- is useful when latency and serving efficiency are part of the objective

### 6. Online multi-model routing under demand constraints

**Efficient Training-Free Online Routing for High-Volume Multi-LLM Serving (Wu and Silwal, 2025)**  
Source: https://arxiv.org/abs/2509.02718

This work extends the routing idea into an online setting with token budgets and throughput constraints. It is especially relevant for production scenarios where decisions must be made under sustained traffic rather than offline evaluation only.

Relevance to this project:

- highlights the difference between offline cost optimization and online serving optimization
- suggests that routing policies should be evaluated under throughput constraints
- motivates separating research tracks for offline experimental quality-cost tradeoffs and online deployment efficiency

## MIT Research Section

MIT does not appear to treat AI cost optimization as one single centralized lab topic. Instead, the work is distributed across several groups that together cover a broad slice of the problem.

### 1. MIT FutureTech: cost-adjusted AI progress and automation economics

**The Price of Progress: Algorithmic Efficiency and the Falling Cost of AI Inference (FutureTech, November 28, 2025)**  
Source: https://futuretech.mit.edu/publication/the-price-of-progress-algorithmic-efficiency-and-the-falling-cost-of-ai-inference

This work is one of the most directly relevant MIT contributions to this repository. It argues that benchmark progress should be evaluated together with the falling cost required to reach a fixed level of performance.

Relevance to this project:

- supports reporting cost at fixed quality rather than quality alone
- strengthens the case for cost-adjusted benchmark analysis
- helps motivate model substitution and routing based on price-performance rather than raw capability

Likely lead group and researchers:

- MIT FutureTech
- Neil Thompson as the central lead figure
- Hans Gundlach, Jayson Lynch, and Matthias Mertens as coauthors

**AI and Scale: A Quantitative Task-Based Theory of Automation (FutureTech, January 1, 2026)**  
Source: https://futuretech.mit.edu/publication/ai-and-scale-a-quantitative-task-based-theory-of-automation

This paper studies when AI automation is economically worthwhile once fixed deployment cost and task scale are considered explicitly.

Relevance to this project:

- sharpens the distinction between fixed deployment cost and marginal inference cost
- extends the cost lens from single episodes to deployment decisions
- is directly relevant for deciding when automation beats human-first or human-in-the-loop policies

Likely lead group and researchers:

- MIT FutureTech
- Danial Lashkari, Wensu Li, Christina Qiu, and Neil Thompson

### 2. LIDS / IDSS / MechE: adaptive compute and efficient policy learning

**A smarter way for large language models to think about hard problems (MIT Schwarzman College of Computing, December 4, 2025)**  
Source: https://computing.mit.edu/news/a-smarter-way-for-large-language-models-to-think-about-hard-problems/

This research describes an adaptive inference approach in which an LLM spends more or less compute depending on question difficulty.

Relevance to this project:

- aligns closely with test-time budget allocation
- supports difficulty-aware inference policies
- suggests fixed reasoning budgets are often inefficient

Likely lead group and researchers:

- LIDS, IDSS, and MechE, with MIT-IBM Watson AI Lab collaboration
- Navid Azizan as the principal MIT lead
- Young-Jin Park, Kristjan Greenewald, Kaveh Alim, and Hao Wang as key collaborators

**MIT researchers develop an efficient way to train more reliable AI agents (MIT News, November 22, 2024)**  
Source: https://news.mit.edu/2024/mit-researchers-develop-efficiency-training-more-reliable-ai-agents-1122

This work shows that reliable agents can be trained with much less data than standard methods in simulated environments.

Relevance to this project:

- broadens cost optimization beyond inference into data efficiency and policy training
- supports the idea that better control policies can reduce end-to-end cost

Likely lead group and researchers:

- LIDS, IDSS, and CEE
- Cathy Wu as the main lead
- Jung-Hoon Cho, Vindula Jayawardana, and Sirui Li as key collaborators

### 3. CSAIL / EECS: training efficiency and smaller-model reasoning

**Synthetic imagery sets new bar in AI training efficiency (MIT News, November 20, 2023)**  
Source: https://news.mit.edu/2023/synthetic-imagery-sets-new-bar-ai-training-efficiency-1120

This work shows that synthetic image training can outperform some real-image alternatives at scale, reducing reliance on expensive real-world data pipelines.

Relevance to this project:

- expands the cost lens to data creation and training pipelines
- shows that lower-cost inputs can sometimes improve downstream performance

Likely lead group and researchers:

- CSAIL and EECS
- Lijie Fan as lead researcher
- Phillip Isola as principal investigator

MIT also has adjacent efficiency work worth tracking:

- `CodeSteer` from Chuchu Fan's LIDS group: https://news.mit.edu/2025/smart-coach-helps-llms-switch-between-text-and-code-0717
- `DisCIPL` from CSAIL with Gabriel Grand, Jacob Andreas, and Joshua Tenenbaum: https://news.mit.edu/2025/new-method-enables-small-language-models-solve-complex-reasoning-tasks-1212
- scalable self-learners from CSAIL with Hongyin Luo, James Glass, and Yoon Kim: https://news.mit.edu/2023/language-models-scalable-self-learners-0608

### 4. MIT Economics / MIT Sloan / IDE: labor, organization, and model-market economics

**Experimental evidence on the productivity effects of generative artificial intelligence (MIT News coverage, July 14, 2023)**  
Source: https://news.mit.edu/2023/study-finds-chatgpt-boosts-worker-productivity-writing-0714

This study reports that generative AI improved speed and quality for selected writing tasks.

Relevance to this project:

- widens the notion of cost from API price to labor time
- provides evidence that indirect cost and human productivity should be part of evaluation

Likely lead group and researchers:

- MIT Department of Economics
- Shakked Noy and Whitney Zhang

**Generative AI and the Nature of Work / Beyond Productivity (MIT IDE, August 11, 2025)**  
Source: https://ide.mit.edu/insights/beyond-productivity-genai-and-the-changing-nature-of-work/

This line of work studies how generative AI changes the composition of work, including coordination burden and task allocation.

Relevance to this project:

- supports adding organizational and coordination cost to indirect-cost accounting
- helps connect benchmark optimization to real deployment environments

Likely lead group and researchers:

- MIT Initiative on the Digital Economy
- Frank Nagle and collaborators from GitHub, Microsoft, the Linux Foundation, and UC Irvine

**MIT Sloan coverage of open-model economics (January 20, 2026)**  
Source: https://mitsloan.mit.edu/ideas-made-to-matter/ai-open-models-have-benefits-so-why-arent-they-more-widely-used

This work highlights the economic importance of open-model substitution and the gap between technical availability and enterprise adoption.

Relevance to this project:

- directly supports model-selection and routing questions
- suggests that switching and adoption costs matter alongside token price

Likely lead group and researchers:

- MIT Initiative on the Digital Economy and MIT Sloan
- Frank Nagle and Daniel Yue

### 5. MIT Industrial Performance Center: field evidence on deployment

**Generative AI and the Work of the Future working group (MIT News, March 28, 2024)**  
Source: https://news.mit.edu/2024/mit-launches-working-group-generative-ai-and-work-of-the-future-0328

This initiative aims to collect organizational evidence on how firms adopt generative AI and how jobs, skills, and training change in practice.

Relevance to this project:

- offers a path from benchmark evidence to real organizational cost accounting
- is especially relevant for hidden deployment, governance, and reskilling costs

Likely lead group and researchers:

- MIT Industrial Performance Center
- Ben Armstrong, Julie Shah, and Kate Kellogg

For a broader MIT-specific research landscape with labs, lead researchers, and adjacent work, see `mit-research-landscape.md`. For the narrower MIT System Design and Management subset, see `mit-sdm-related-work.md`.

## Synthesis

These papers suggest that prior work on AI cost optimization can be grouped into four main directions:

- **routing and cascades**: choose different models or stages for different queries
- **test-time budget allocation**: spend more or less reasoning compute depending on difficulty
- **verification-based acceleration**: use cheap models to propose and expensive models to verify
- **systems-level serving optimization**: reduce latency and serving cost without changing task policies

## Gaps Relative to This Repository

The existing literature is strong on inference cost reduction, routing, and test-time compute, but weaker on a unified definition of problem-solving cost at the workflow level. In particular, the papers above do not fully cover:

- human intervention cost
- retry and recovery cost across full workflows
- task-level acceptance thresholds as explicit optimization constraints
- cross-task evaluation under a shared cost-quality framework
- integration of tool use, routing, retries, and verification into one total-cost metric

This gap supports the direction of this repository: define AI problem solving itself as a cost-sensitive process, then evaluate and optimize that process under explicit quality constraints.

## Immediate Implications for Our Research Plan

The first experimental track should focus on the strongest and most mature prior-work directions:

1. model selection and routing
2. test-time budget control
3. verification and retry policy

System-level serving optimizations should be treated as a separate layer that can later be integrated into total-cost accounting.
