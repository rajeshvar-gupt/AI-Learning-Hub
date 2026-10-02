# 90-day development roadmap

Planning window: 5 October 2026–2 January 2027, Asia/Kolkata. The first batch was authorized on 1 October and is being prepared early. Dates are targets; move blocked tasks without erasing their IDs. This file is a plan, not a completion record. See PROGRESS.md for actual status.

The intended outcome is a coherent first curriculum release, not exhaustive mastery of every AI field. Each task includes an acceptance check. Preserve existing work; add folders only with real content.

## Actual session tracking

Session Day 2 (2 October 2026) follows PROGRESS.md: original D002 roadmaps/AI distinctions already shipped in the foundation release. This session published PY-001 and PY-002 (D008 scope, introductory D009 types, and input/conditions) through [PR #1](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/1). Planned calendar dates are retained; pending legacy repairs and other tasks are not marked complete.

## Single-repository rule

All 90 tasks now target folders in AI-Learning-Hub. Earlier repository names in the original audit are historical references only. Do not create subject repositories. Existing-project repair/migration requires review; all new educational content belongs in this hub.

## Calendar


Target shorthand: Hub = repository root; Roads = roadmaps/; Notes = notes/; Projects = projects/; Python/Maths/Stats/ML/DL/CV/NLP/GenAI/RAG/Agents/Auto/MLOps = matching folders under subjects/. Named legacy applications mean reviewed reuse or a new hub project under projects/, with the old repository preserved. All days inherit the quality checks; acceptance checks are task-specific.


### Week 1: Foundation and architecture

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D001 · 05 Oct 2026 (Mon) | Hub | Approve account mapping and publish start-here, architecture and topic registry | Every curriculum area has a folder/status entry |
| D002 · 06 Oct 2026 (Tue) | Roads, Notes | Write AI engineer learning sequence and AI concept distinctions | Prerequisites and stage outcomes are explicit |
| D003 · 07 Oct 2026 (Wed) | Projects | Build existing-project catalog with runnable/restricted/repair-needed labels | Catalog makes no unverified execution claims |
| D004 · 08 Oct 2026 (Thu) | Weather-Forecasting-App | Prepare environment-key and honest-output repair PR; owner rotates key | No literal key in changed code; mock API success/failure checks |
| D005 · 09 Oct 2026 (Fri) | Hub, Notes | Create beginner diagnostic, answer guide and Git navigation quick reference | Answers explain misconceptions; links resolve |
| D006 · 10 Oct 2026 (Sat) | Hub, Image-Processing | Add contribution/templates and prepare missing-image fixture repair | One Pillow example runs using distributable fixtures |
| D007 · 11 Oct 2026 (Sun) | Hub | Review initial hub PRs, check links and set next-week priorities | Actual merged and open work are recorded separately |

### Week 2: Python for AI

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D008 · 12 Oct 2026 (Mon) | Roads, Python | Add Python path and setup lesson with first executable example | Clean setup reaches documented output |
| D009 · 13 Oct 2026 (Tue) | Python, Notes | Teach variables, types, strings and collections | Examples demonstrate mutability and conversion errors |
| D010 · 14 Oct 2026 (Wed) | Python, Projects | Build student-score summary CLI using loops and functions | Handles empty input and invalid scores |
| D011 · 15 Oct 2026 (Thu) | Python | Extend CLI with files, exceptions, modules and basic classes | File failures produce useful messages |
| D012 · 16 Oct 2026 (Fri) | Notes, Hub | Add Python cheat sheet, interview set and three-level assignment | Solutions separate; exercises cover errors and reasoning |
| D013 · 17 Oct 2026 (Sat) | Python, Hub | Document venv, dependencies, Git and basic HTTP/JSON API concepts | Student follows installation and navigation from README |
| D014 · 18 Oct 2026 (Sun) | Hub, Python | Run examples and review beginner progress | One end-to-end CLI check plus task ledger update |

### Week 3: Mathematics and statistics

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D015 · 19 Oct 2026 (Mon) | Roads, Maths | Create maths path: vectors, matrices, probability and differentiation | Prerequisites mapped to downstream ML topics |
| D016 · 20 Oct 2026 (Tue) | Maths, Notes | Write vector operations, matrix multiplication and gradient lessons | Shapes and small hand calculations match examples |
| D017 · 21 Oct 2026 (Wed) | Maths, Projects | Build gradient-descent visualization notebook on a quadratic | Objective decreases under documented step size |
| D018 · 22 Oct 2026 (Thu) | Stats | Repair confidence-interval lesson; distinguish SD, SE and uncertainty | Worked numeric case and assumptions verified |
| D019 · 23 Oct 2026 (Fri) | Stats, Notes, Hub | Add hypothesis-testing revision and statistics assignment | Interpretation avoids treating p-value as hypothesis probability |
| D020 · 24 Oct 2026 (Sat) | Maths, Stats | Add READMEs and data provenance notes; link private status honestly | Setup and input file locations documented |
| D021 · 25 Oct 2026 (Sun) | Hub, Stats | Execute selected notebooks and review statistical explanations | Failures recorded; interval correction reviewed |

### Week 4: Data analysis and SQL

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D022 · 26 Oct 2026 (Mon) | Roads, Python | Add data-analysis path with NumPy, pandas, SQL and visualization | Learner entry/exit criteria and dataset selected |
| D023 · 27 Oct 2026 (Tue) | Python, Notes | Teach arrays, data frames, missingness, types and grouping | Small examples include missing and duplicate records |
| D024 · 28 Oct 2026 (Wed) | Projects | Build sales-analysis notebook with small synthetic dataset | Totals and grouped metrics reconcile |
| D025 · 29 Oct 2026 (Thu) | Projects, Python | Extend analysis with SQLite joins and chart interpretation | Join cardinality checked; charts label units |
| D026 · 30 Oct 2026 (Fri) | Notes, Hub | Create NumPy/pandas/SQL cheat sheets and debugging assignment | Questions address leakage, joins and missing values |
| D027 · 31 Oct 2026 (Sat) | Projects, Hub | Write reproducible analysis README and link report interpretation | Student reruns analysis without external account |
| D028 · 01 Nov 2026 (Sun) | Hub, Projects | Validate data-analysis project and review pathway | Queries and chart values checked against known fixture |

### Week 5: Machine learning

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D029 · 02 Nov 2026 (Mon) | Roads, ML | Add hub ML sequence and plan reviewed regression reuse | Existing notebooks preserved; new hub lessons indexed |
| D030 · 03 Nov 2026 (Tue) | ML, Notes | Explain splits, preprocessing pipelines, loss and regression | Fit/transform and data leakage distinctions clear |
| D031 · 04 Nov 2026 (Wed) | ML, Projects | Upgrade regression notebook with held-out baseline evaluation | Train/test separation and actual metrics recorded |
| D032 · 05 Nov 2026 (Thu) | ML, Projects | Add classification comparison and implement book recommender inside projects/ | Small tested baselines; dataset rights/access documented |
| D033 · 06 Nov 2026 (Fri) | Notes, Hub | Add ML metrics cheat sheet and scenario interview assignment | Precision/recall and regression metrics use worked examples |
| D034 · 07 Nov 2026 (Sat) | ML, Projects | Document clustering/tree/ensemble next steps and model limitations | Implemented vs planned algorithms clearly separated |
| D035 · 08 Nov 2026 (Sun) | Hub, ML | Run small ML examples and review leakage/reproducibility | Seeded checks pass or blockers documented |

### Week 6: Deep learning

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D036 · 09 Nov 2026 (Mon) | Roads, DL | Add DL path and tensor/autograd starting unit | Tested environment and entry lesson available |
| D037 · 10 Nov 2026 (Tue) | DL, Notes | Teach neural layers, activations, loss and backpropagation | Gradient example matches numerical intuition |
| D038 · 11 Nov 2026 (Wed) | DL, Projects | Implement small MLP training example | Training smoke test runs on CPU and saves metrics |
| D039 · 12 Nov 2026 (Thu) | DL, Projects | Add validation, regularization and checkpoint reload | Reloaded model produces consistent inference |
| D040 · 13 Nov 2026 (Fri) | Notes, Hub | Add optimization/overfitting cheat sheet and DL assignment | Includes debugging exploding/vanishing gradients |
| D041 · 14 Nov 2026 (Sat) | DL, Hub | Document RNN/LSTM/GRU overview and sequence-learning pathway | Architecture distinctions and prerequisites correct |
| D042 · 15 Nov 2026 (Sun) | Hub, DL | Review training code, outputs and resource requirements | No hardware or benchmark claims without observed evidence |

### Week 7: Computer vision

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D043 · 16 Nov 2026 (Mon) | Roads, CV | Create CV task roadmap and link existing image-processing labs | Classification/detection/segmentation paths distinguished |
| D044 · 17 Nov 2026 (Tue) | CV, Notes | Teach convolutions, pooling, channels and CNN architecture families | Tensor shapes and architecture comparisons checked |
| D045 · 18 Nov 2026 (Wed) | Image-Processing, Projects | Repair and validate image transform/edge-detection lab | All referenced input images available with provenance |
| D046 · 19 Nov 2026 (Thu) | CV, Face-Recognition-Dashboard | Build transfer-learning lab; assess face-project modernization | Runnable small lab; face compatibility findings separately recorded |
| D047 · 20 Nov 2026 (Fri) | Notes, Hub | Add OpenCV cheat sheet and CV evaluation assignment | IoU calculation and dataset-split question verified |
| D048 · 21 Nov 2026 (Sat) | CV, Hub | Document detection/segmentation extension and dataset permissions | No unverified models or datasets redistributed |
| D049 · 22 Nov 2026 (Sun) | Hub, CV | Review CV examples and publish concrete modernization backlog | Image outputs inspected and failed environments disclosed |

### Week 8: NLP and transformers

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D050 · 23 Nov 2026 (Mon) | Roads, NLP | Create NLP route from text preprocessing to attention | Vocabulary, sequence and evaluation prerequisites mapped |
| D051 · 24 Nov 2026 (Tue) | NLP, Notes | Teach tokenization, bag-of-words, TF-IDF and embeddings | Vocabulary learned on training data only |
| D052 · 25 Nov 2026 (Wed) | NLP, Projects | Build text classification baseline with small permissible dataset | Held-out baseline and class metrics reported |
| D053 · 26 Nov 2026 (Thu) | Resume_screening_system, NLP | Repair extraction/setup; teach attention with a tiny worked example | Multipage and empty-text checks; attention weights sum correctly |
| D054 · 27 Nov 2026 (Fri) | Notes, Hub | Add NLP/transformer comparison sheet and interview assignment | RNN vs transformer tradeoffs accurately explained |
| D055 · 28 Nov 2026 (Sat) | NLP, Hub | Document transformer module, positional information and next steps | Terminology and diagram checked; model access requirements explicit |
| D056 · 29 Nov 2026 (Sun) | Hub, NLP | Review NLP notebooks and resume-demo readiness | Sensitive sample provenance and runtime blockers recorded |

### Week 9: Generative AI and LLMs

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D057 · 30 Nov 2026 (Mon) | Roads, GenAI | Create GenAI/LLM path and verified documentation shortlist | GAN/VAE/diffusion/transformer scope distinguished |
| D058 · 01 Dec 2026 (Tue) | GenAI, Notes | Teach generation, context, prompting, decoding and hallucinations | Examples separate likelihood from factual correctness |
| D059 · 02 Dec 2026 (Wed) | GenAI, Projects | Build Gemini-based simple assistant with environment configuration | Mocked tests run without key; live test only with configured access |
| D060 · 03 Dec 2026 (Thu) | GenAI, Projects | Add structured outputs, retry limits and a small evaluation set | Malformed output and rate-limit behavior handled |
| D061 · 04 Dec 2026 (Fri) | Notes, Hub | Add prompt/LLM cheat sheets and model-selection assignment | No invented model prices, limits or scores |
| D062 · 05 Dec 2026 (Sat) | GenAI, Hub | Document model/data limitations and reproducible evaluation protocol | Provider/model versions and actual test status recorded |
| D063 · 06 Dec 2026 (Sun) | Hub, GenAI | Review assistant, examples and provider assumptions | Mock vs live validation clearly distinguished |

### Week 10: RAG and retrieval

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D064 · 07 Dec 2026 (Mon) | Roads, RAG | Create retrieval-to-RAG roadmap with baseline design | Document source and evaluation questions defined |
| D065 · 08 Dec 2026 (Tue) | RAG, Notes | Teach chunking, embeddings, similarity and vector indexing | Small hand-worked retrieval example is consistent |
| D066 · 09 Dec 2026 (Wed) | RAG, Projects | Build local document retrieval baseline | Known relevant passages retrieved from controlled fixture |
| D067 · 10 Dec 2026 (Thu) | RAG, Projects | Add generation with citations, abstention and retrieval comparison | Answers cite real chunks; unsupported question tested |
| D068 · 11 Dec 2026 (Fri) | Notes, Hub | Add RAG cheat sheet and retrieval debugging assignment | Distinguishes retrieval quality from answer quality |
| D069 · 12 Dec 2026 (Sat) | RAG, Hub | Document ingestion, updates and access boundaries | Source IDs stable; no private documents in fixtures |
| D070 · 13 Dec 2026 (Sun) | Hub, RAG | Evaluate retrieval and answer behavior on held-out questions | Actual results and failures recorded; no cherry-picked benchmark |

### Week 11: Agents and agentic systems

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D071 · 14 Dec 2026 (Mon) | Roads, Agents | Create agent path: tools, state, planning and orchestration | Assistant/workflow/agent distinctions use bounded examples |
| D072 · 15 Dec 2026 (Tue) | Agents, Notes | Teach tool schemas, validation, memory and stopping rules | State transitions and failure handling explained |
| D073 · 16 Dec 2026 (Wed) | Agents, Projects | Build one-agent course assistant with read-only tools | Tool inputs validated and maximum steps enforced |
| D074 · 17 Dec 2026 (Thu) | Agents, Projects | Extend to plan-execute-review workflow using Gemini/LangGraph where suitable | Retry/loop limits and failed-tool recovery tested |
| D075 · 18 Dec 2026 (Fri) | Notes, Hub | Add agent evaluation sheet and architecture interview assignment | Task success, tool correctness and cost/latency measured separately |
| D076 · 19 Dec 2026 (Sat) | Agents, Hub | Document agentic-systems module, traces and human approval points | Side effects require explicit approval in the example |
| D077 · 20 Dec 2026 (Sun) | Hub, Agents | Run bounded adversarial-input and tool-failure evaluations | External text cannot override permitted tool scope |

### Week 12: Automation, MLOps and deployment

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D078 · 21 Dec 2026 (Mon) | Roads, Auto, MLOps | Create automation/MLOps path and release lifecycle overview | Deterministic workflow vs AI step clearly identified |
| D079 · 22 Dec 2026 (Tue) | Auto, Notes | Teach n8n/Python workflow concepts, webhooks and idempotency | Example prevents duplicate processing on retries |
| D080 · 23 Dec 2026 (Wed) | iris_classfier_cicd | Build small Iris training and inference API under projects/ | Train/save/load and valid/invalid API input tests |
| D081 · 24 Dec 2026 (Thu) | iris_classfier_cicd, MLOps | Add CI, container recipe and deployment instructions | Build/start smoke test and health endpoint verified |
| D082 · 25 Dec 2026 (Fri) | Notes, Hub | Add Docker/CI cheat sheets and operations interview assignment | Examples match tested configuration |
| D083 · 26 Dec 2026 (Sat) | Auto, MLOps, Hub | Document scheduled workflow demo, monitoring and rollback exercise | Use dry-run fixtures; deployment/access costs explicit |
| D084 · 27 Dec 2026 (Sun) | Hub, MLOps | Review lifecycle project and deployment readiness | Report actual deployed status; do not invent live URL |

### Week 13: Capstones, interviews and release

| Day / date | Target | Deliverable | Acceptance check |
|---|---|---|---|
| D085 · 28 Dec 2026 (Mon) | Roads, Hub | Create role variants and portfolio checklists across requested careers | Each role has skills, project evidence and interview goals |
| D086 · 29 Dec 2026 (Tue) | Projects | Integrate course-mentor RAG/agent capstone from prior modules | End-to-end bounded scenario works with documented setup |
| D087 · 30 Dec 2026 (Wed) | Projects | Integrate data/ML API capstone with evaluation and CI | Held-out metric and API/CI validation reproducible |
| D088 · 31 Dec 2026 (Thu) | Hub, Notes | Consolidate interview packs and three-level assignments | Questions cover concept, code, scenario and project defense |
| D089 · 01 Jan 2027 (Fri) | Hub, Roads | Run ecosystem link, duplicate, source and curriculum review | Broken links and orphan content fixed or visibly blocked |
| D090 · 02 Jan 2027 (Sat) | Hub, Projects | Publish reviewed first-release report and next-quarter backlog | Only merged/validated content counted; remaining scope explicit |


[Home](README.md)
