# ASST-001 · Assistant boundaries and conversation state

Prerequisites: LLM-002, RAG-002. Status: published.

Outcome: define what a course assistant can answer and what should remain with a person.

An assistant responds to a request; a workflow executes predefined stages; an agentic design may choose actions from feedback. These labels overlap, so describe actual control flow. The mock/extractive assistant here does not autonomously select arbitrary tools.

Define allowed knowledge sources, unavailable policies and retention limits. Keep conversation state scoped to the correct user and purpose. Never infer an entitlement, payment or admission decision from invented fixture text. Memory can be incorrect or stale; review the current source before acting on it.

The offline demonstration has no persistent chat history. It answers one request and writes a local report. It sends no messages to learners. A live application would need authentication, consent, redaction and deletion controls appropriate to its context.

[Questions](../../assignments/ASST-001/questions.md) · [Solutions](../../assignments/ASST-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
