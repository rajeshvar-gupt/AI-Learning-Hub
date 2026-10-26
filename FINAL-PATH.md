# Complete introductory AI engineering path

The published Python→ML→DL→CV→NLP material and merged transformer release are extended here through GenAI, retrieval, assistants, agents, automation and MLOps. New content is published. This is a coherent introductory first release, not exhaustive expertise in every specialty. Personal learning completion still requires doing the exercises.

## Learning sequence

| Stage | Entry point | Practical outcome |
|---|---|---|
| Foundations through ML | [Existing path](THROUGH-ML.md) | Python, maths, statistics, data and baseline ML |
| Deep learning | [DL](subjects/deep-learning/README.md) | Manual gradients, checkpoints and inference |
| Computer vision | [CV](subjects/computer-vision/README.md) | CNN, synthetic image lab, feature transfer |
| NLP | [NLP](subjects/nlp/README.md) | Text features, baseline classification and attention |
| Transformers | [TR](subjects/transformers/README.md) | Tested untrained forward mechanics |
| Generative AI | [GEN](subjects/generative-ai/README.md) | Model-family distinctions and evaluation |
| LLMs | [LLM](subjects/llms/README.md) | Prompts, schema validation and bounded provider calls |
| RAG | [RAG](subjects/rag/README.md) | Index, retrieval, cited baseline and abstention |
| Agents | [Tools](subjects/ai-agents/README.md) → [Orchestration](subjects/agentic-ai/README.md) | Bounded plans, traces and approval points |
| Automation | [AUTO](subjects/ai-automation/README.md) | Idempotent, timezone-aware dry runs |
| Assistants | [ASST](subjects/ai-assistants/README.md) | Scoped Q&A and integrated mentor capstone |
| APIs and operations | [API](subjects/ai-apis/README.md) → [OPS](subjects/mlops/README.md) | Train/save/reload, localhost HTTP, CI/container recipes |

## Environment

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-labs.txt
```

On Windows PowerShell activate with .venv\\Scripts\\Activate.ps1. Runtime validation used Linux/Python 3.12.14 and already-installed pinned packages; a fresh online dependency install subsequently passed in hosted Linux CI; Windows/macOS runs remain untested. Notebook wrappers are optional; no Jupyter frontend validation is claimed.

## Offline commands

```bash
python -m ai_hub.demo assistant
python -m ai_hub.demo rag
python -m ai_hub.demo agent
python -m ai_hub.demo automation
python -m ai_hub.demo capstone
python -m ai_hub.demo images
python -m ai_hub.autodiff
python -m ai_hub.iris_api train
OPENBLAS_NUM_THREADS=1 python -m ai_hub.transfer
python scripts/run_checks.py
```

The OpenBLAS prefix bounds CPU threading on Linux/macOS; it is optional for the code's logic. Scripts create only local outputs. No recurring task, external message or paid infrastructure is started. For serving and optional live Gemini access see [DEPLOYMENT.md](DEPLOYMENT.md).

## Review and completion

Each new lesson links separate exercises/solutions. Use [interview and three-level capstones](interview-preparation/final-assessment.md), the [role/portfolio matrix](roadmaps/careers/final-role-matrix.md) and [model card](projects/templates/model-card.md). Check [the 90-task evidence ledger](ROADMAP-STATUS.md), [validation](VALIDATION-REMAINING.md) and [explicit external checks](RELEASE-REPORT.md) before calling a task fully released.

Optional notebook wrappers: [quadratic visualization](notebooks/foundations.ipynb) and [supervised benchmark](notebooks/supervised.ipynb). Their code cells were executed; the Jupyter frontend was not tested.
