# LLM-001 · Prompts, context and model selection

Prerequisites: GEN-001. Status: prepared for review.

Outcome: write a testable request and document model choice without invented limits or prices.

A useful prompt specifies the task, relevant context, constraints and output contract. Separate source data from instructions. Delimiters improve structure but are not a security boundary. For extraction, provide field meanings and a policy for unavailable information rather than encouraging guessing.

Compare models on representative inputs and the same success rubric. Include language coverage, privacy terms, context needs, schema adherence, latency and measured cost. Consult current provider documentation for account-specific availability and pricing; this release deliberately does not pin a “free” model or promise a quota.

The Gemini adapter reads GEMINI_API_KEY and GEMINI_MODEL from environment configuration. A model ID is chosen by the operator from their available account models. No secrets are committed. The mock mode remains the default, and live requests are opt-in.

[Questions](../../assignments/LLM-001/questions.md) · [Solutions](../../assignments/LLM-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
