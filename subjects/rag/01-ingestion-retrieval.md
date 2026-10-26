# RAG-001 · Chunking, retrieval and index lifecycle

Prerequisites: NLP-003. Status: prepared for review.

Outcome: build and inspect a reproducible document-to-chunk index.

Chunking trades local coherence against retrieval granularity. Overlap can preserve boundary context but increases duplicate evidence. Stable IDs should include source/version identity and location. In this immutable teaching fixture, IDs use document ID and word offset; if source text changes, explicitly version or rebuild the index rather than claiming offsets remain stable forever.

The baseline fits TF-IDF on four original public invented documents and ranks chunks by normalized dot product. Dense embeddings and vector databases offer other representations/indexing choices but are not required for a small baseline. Do not use test questions to fit the index's vocabulary.

For private sources, filter by access rights before retrieval and propagate deletion/update rules into cached content. This lab contains no private documents or multi-user authorization service. Its index is rebuilt in memory on each run, so no stale persisted index is silently reused.

[Questions](../../assignments/RAG-001/questions.md) · [Solutions](../../assignments/RAG-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
