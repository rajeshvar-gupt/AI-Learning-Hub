# AI foundations — quick revision

| Ask this question | What it clarifies |
|---|---|
| Is the behavior a fixed rule or learned from examples? | Deterministic automation versus ML |
| Does the system classify/predict or generate content? | Task/output type |
| Does it retrieve external evidence? | Retrieval/RAG architecture |
| Who chooses the next step? | Fixed workflow versus dynamic agent control |
| Which tools and actions are permitted? | Scope of autonomy |
| How does it stop or escalate? | Bounded execution and failure handling |
| What evidence measures success? | Evaluation rather than a convincing demo |

Remember: assistant is a product role, RAG is an architecture pattern, and ML/DL describe learning/model approaches. A single application can fit several labels.

Worked classification: a scheduled script that asks an LLM to summarize a report and saves the output is an AI-assisted workflow. A model call alone does not make its control flow an agent loop.

Self-check: give one example of an assistant without dynamic actions, an agent with only read tools, and automation without AI. Explain the simplest adequate design in each case.

[Full note](../foundations/ai-landscape.md) · [Notes home](../README.md)
