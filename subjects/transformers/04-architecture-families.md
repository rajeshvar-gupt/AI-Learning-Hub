# TR-004 · Encoder, decoder and encoder-decoder transformers

Prerequisite: TR-003.

Outcome: select an architecture family based on information flow and training objective.

An encoder commonly builds representations using both left and right input context and supports tasks such as classification or extraction. A causal decoder represents a prefix while blocking future target tokens. An encoder-decoder model first represents a source and then produces target tokens, with decoder cross-attention to source representations. These are broad patterns, not rules that every model must follow.

In self-attention, queries, keys and values derive from the same sequence representation. In cross-attention, queries can derive from a target stream while keys/values derive from encoded source information. Mask design must reflect the task: source padding, target padding and target causality are distinct concerns.

Masked-token learning hides selected input content and predicts it from context. Causal next-token learning predicts the following token from a prefix. Teacher forcing during training supplies the known preceding target tokens; input/target alignment must not expose the token being predicted. Bidirectional context is useful for understanding tasks but cannot simply be substituted into a causal-generation evaluation.

The original BERT work is an example of bidirectional pretraining; the original transformer paper used an encoder-decoder architecture. The current lab implements one self-attention forward block with an optional causal mask, not BERT, a full decoder language model or cross-attention.

Task deliverable: write a comparison table for a support-intent classifier, translation and next-token continuation. Identify objective, allowed context and missing implementation pieces for each.

[Questions](../../assignments/TR-004/questions.md) · [Solutions](../../assignments/TR-004/solutions.md) · [Mechanics lab](../../projects/intermediate/transformer-mechanics/README.md) · [Module index](README.md)
