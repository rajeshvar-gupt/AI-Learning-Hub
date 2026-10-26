# RAG-002 · Citations, abstention and RAG evaluation

Prerequisites: RAG-001, LLM-002. Status: published.

Outcome: distinguish retrieval success from answer support and measure each honestly.

The extractive baseline copies retrieved passages with real chunk IDs. With no overlapping vocabulary, it abstains. This lexical rule catches a narrow case; a superficially related passage can still be irrelevant. The optional generation hook validates citation IDs and labels its result generated-unverified-support.

The fixture evaluation asks four controlled questions with known relevant document IDs and reports recall@2. This is a small diagnostic set, not an independent held-out benchmark. Source passages are tiny and related; irrelevant secondary hits are visible. A broader benchmark needs frozen retrieval settings and untouched representative questions.

For generated answers, inspect whether each claim is supported by cited text, whether a supported question was answered, and whether an unsupported one was refused. Compare the extractive baseline before adding a provider. No live provider result is used to claim RAG quality in this release.

[Questions](../../assignments/RAG-002/questions.md) · [Solutions](../../assignments/RAG-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
