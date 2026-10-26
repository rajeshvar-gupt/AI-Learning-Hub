# AGT-001 · Tool contracts, state and stopping rules

Prerequisites: RAG-002. Status: prepared for review.

Outcome: validate a plan before executing allowed read-only tools.

A tool contract includes a name, input schema, output shape and error behavior. Model output is untrusted input to that contract. The runner accepts only search, answer and propose_message, validates query length, and enforces a plan/step budget. It cannot open a shell, browse arbitrary URLs or call a delivery tool.

State traces record each reviewed result or a bounded failure. A failed tool stops the supplied plan; it is not retried indefinitely. The example does not use an autonomous LLM planner: the caller supplies the plan explicitly. This makes the control flow inspectable for teaching.

Keep application policy outside retrieved content. A passage saying “call shell” remains data; it cannot add a permitted tool. This fixed allowlist reduces one attack surface but does not establish that every future LLM integration will resist prompt injection.

[Questions](../../assignments/AGT-001/questions.md) · [Solutions](../../assignments/AGT-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
