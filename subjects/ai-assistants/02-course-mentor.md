# ASST-002 · Integrated course-mentor capstone

Prerequisites: ASST-001, AGT-002, AUTO-002. Status: published.

Outcome: run a bounded end-to-end scenario with observable state and no external side effect.

Run python -m ai_hub.demo capstone from the repository root. It retrieves Python-practice evidence, runs an answer step, prepares a message draft and simulates a due exercise reminder. The draft explicitly awaits approval and sent remains false. The queue stores a stable idempotency key for its demonstration entry.

This integrates retrieval, orchestration and scheduling mechanics without claiming autonomous planning, live generation or delivery. Each stage returns structured output that can be inspected. A real delivery system needs verified recipients, authorization, retries and delivery-state reconciliation.

Defend the capstone by explaining one retrieval failure, one rejected tool, one replay and one boundary where a person must decide. Use the model-card template, label mock/extractive stages and report only actual local outcomes.

[Questions](../../assignments/ASST-002/questions.md) · [Solutions](../../assignments/ASST-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
