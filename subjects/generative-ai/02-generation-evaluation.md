# GEN-002 · Generation, hallucinations and evaluation

Prerequisites: GEN-001. Status: published.

Outcome: separate output likelihood, factual support and task success.

A model can assign high probability to a false statement. Temperature and sampling control token selection, not truth. A context window limits tokens a request can include; it does not guarantee reliable recall of every included fact. Retrieval can improve evidence access while still failing at relevance or faithful use.

Build an evaluation set before tuning prompts. Include normal, ambiguous, unsupported and malformed-input cases. Record prompt version, provider/model ID, date, output schema, success criteria and failure examples. Keep development cases separate from any final task-quality evaluation.

The local demos distinguish mock, extractive and generated-unverified-support modes. Citation-ID validation checks that cited passages exist; it does not establish semantic entailment. Never report a mocked response as live model accuracy. Use the model-card template for observed results and unsupported claims.

[Questions](../../assignments/GEN-002/questions.md) · [Solutions](../../assignments/GEN-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
