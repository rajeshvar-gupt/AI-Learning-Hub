# AGT-002 · Agent evaluation and failure cases

Prerequisites: AGT-001. Status: published.

Outcome: test task completion, tool correctness and scope boundaries independently.

A plausible final answer can hide wrong tool use. Evaluate whether the right source was retrieved, arguments matched the schema, the plan stopped, and side-effect proposals remained proposals. Record trace length and failure state. Cost and latency require their own measured run; this offline runner has no token-cost benchmark.

Tests include a forbidden shell tool, an over-budget plan, a failed retriever and a retrieved instruction attempting to change scope. These are bounded adversarial fixtures rather than a universal security claim. The deterministic runner is a baseline for understanding policy enforcement.

Frameworks can organize graph/state transitions, but adopting one does not supply correct permissions or a stopping rule. The current implementation uses plain Python so it runs without external model credentials; LangGraph integration is optional later work, not a dependency falsely claimed as installed.

[Questions](../../assignments/AGT-002/questions.md) · [Solutions](../../assignments/AGT-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
