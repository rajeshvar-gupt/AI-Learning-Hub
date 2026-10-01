# AI engineer roadmap

## Prerequisites and starting point

Begin with basic computer/file skills and school-level algebra. If programming is new, spend enough time on Python to solve small problems independently. If you already build models, demonstrate the earlier exit criteria and start at the first gap.

## Beginner stage

| Step | Learn | Practice | Exit criterion |
|---|---|---|---|
| 1 | AI vocabulary; rules versus learned behavior | Classify five applications and justify the simplest approach | Explain model, dataset, prediction and evaluation |
| 2 | Python types, conditions, loops, functions, exceptions, files | Build a CSV summary program | Handle malformed/empty input and explain each function |
| 3 | Git, environments and debugging | Track a small project and recreate its environment | Another learner follows your README |
| 4 | Vectors, matrices, probability, descriptive statistics and derivatives | Calculate a small matrix product and a gradient | Explain dimensions, uncertainty and rate of change |
| 5 | Data cleaning, joins, SQL, aggregation and visualization | Analyze a small table with missing/duplicate values | Reconcile totals and describe limitations |

## Intermediate stage

| Step | Learn | Practice | Exit criterion |
|---|---|---|---|
| 6 | Supervised/unsupervised ML, baselines and splits | Regression and classification pipelines | Report held-out metrics without fitting transforms on test data |
| 7 | Trees, ensembles, clustering and feature engineering | Compare a few sensible baselines | Explain model choice and errors, not just the best score |
| 8 | Tensors, gradients, neural networks and training loops | Small MLP with validation and saved weights | Reload and reproduce inference; diagnose overfitting |
| 9 | One specialization: CV, NLP or data science | A focused image/text/tabular project | Use an appropriate dataset split and task metric |

## Advanced stage

| Step | Learn | Practice | Exit criterion |
|---|---|---|---|
| 10 | Transformers, LLM behavior and structured outputs | Bounded assistant with a checked evaluation set | Handle unsupported requests and invalid output |
| 11 | Retrieval, chunking, embeddings and RAG evaluation | Document QA with real source citations | Separate retrieval failures from generation failures |
| 12 | Tools, state, stopping rules and agent orchestration | Read-only tool agent, then a controlled workflow | Test tool errors, loop limits and approval boundaries |
| 13 | APIs, containers, CI, deployment, monitoring and rollback | Package a model service | Recreate service, run tests and recover from a failed update |
| 14 | Capstone and communication | Connect selected stages around a real user need | Present tradeoffs, actual results, failures and next improvements |

## Tools and frameworks

Start with Python and Git. Add NumPy/pandas/SQL for data, scikit-learn for classical ML, and one DL framework after learning tensors. Learn HTTP/JSON before provider SDKs. For LLM examples this learning hub plans to use Gemini where suitable; keep provider-specific code isolated. Add vector search, workflow or agent frameworks only when a project needs them. Framework names are not learning outcomes.

## Research reading

After fundamentals, read papers that answer a concrete design question: a CNN paper for a vision task, the transformer paper for attention, and a retrieval paper for a RAG experiment. The verified bibliography is planned; this release does not invent or link unverified paper references. For each paper record its question, method, assumptions, data, evaluation and one limitation. Reproduce a small component before claiming replication.

## Portfolio and interviews

Prepare three strong case studies: a reproducible data/ML baseline, one specialization project, and one deployed or deployment-ready AI application. See the [portfolio checklist](careers/portfolio-checklist.md). Practice explaining leakage, metric choice, failure recovery, model limitations and how a simpler approach compares. Use actual artifacts rather than unsupported “industry-level” labels.

## Start today

Read [AI foundations](../notes/foundations/ai-landscape.md), take the [diagnostic](../assignments/AI-001/questions.md), and select one next milestone. The [project catalog](../projects/catalog.md) identifies which existing work needs repair before reuse.

[Roadmaps home](README.md)
