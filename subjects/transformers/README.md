# Transformers · five-task module

Status: prepared for review. Start after [NLP-005](../nlp/05-attention.md).

| Task | Lesson | Reviewable deliverable |
|---|---|---|
| 1 | [TR-001 · Token embeddings and positional information](01-embeddings-positions.md) | Worked exercises and the corresponding lab checks |
| 2 | [TR-002 · Multi-head attention and masks](02-multihead-masks.md) | Worked exercises and the corresponding lab checks |
| 3 | [TR-003 · Residual paths, normalization and feed-forward layers](03-transformer-block.md) | Worked exercises and the corresponding lab checks |
| 4 | [TR-004 · Encoder, decoder and encoder-decoder transformers](04-architecture-families.md) | Worked exercises and the corresponding lab checks |
| 5 | [TR-005 · Decoding, evaluation and transformer assessment](05-decoding-evaluation.md) | Worked exercises and the corresponding lab checks |

Work in order, attempt the separate question sets and explain the solutions. Run the [mechanics lab](../../projects/intermediate/transformer-mechanics/README.md), then complete a [model card](../../projects/templates/model-card.md) with the lab's limits.

[Revision/interview sheet](../../notes/cheat-sheets/transformers.md) · [Validation](../../VALIDATION-TRANSFORMERS.md) · [Primary sources](../../resources/transformer-sources.md)

Implemented: fixed positions, randomly initialized projections, two-head self-attention, causal masking, residual/feed-forward forward computation and supplied-logit temperature/top-k sampling. No transformer training, model download, API access or task-quality benchmark is claimed. The next subject is Generative AI/LLM applications when requested.
