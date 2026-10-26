# TR-001 · Token embeddings and positional information

Prerequisite: NLP-005.

Outcome: turn token IDs into vectors and explain how order reaches an attention block.

A tokenizer maps text to discrete IDs according to its vocabulary and segmentation rules. An embedding table has shape (vocabulary_size, model_width); an ID selects one row. The vector is a parameter representation, not a word definition or a probability. Different tokenizers and models can assign different IDs to the same visible string.

Attention without a position mechanism cannot generally distinguish sequence order in the way a sequential model does. Position signals provide additional information. The lab adds fixed sine/cosine coordinates to supplied embedding rows; learned position vectors are another choice. Other position methods are outside this introductory implementation.

The lab vocabulary has six rows and width eight. IDs [1,3,2,5] select a (4,8) matrix; adding positions preserves that shape. At position zero, the sine coordinates are zero and cosine coordinates are one. These fixed coordinates are deterministic, but the embedding rows are randomly initialized and not trained.

Keep the tokenizer, special-token conventions and model checkpoint paired. Padding needs a mask; token ID zero is not universally a padding token. Context length counts model tokens rather than words, and a permitted input length does not guarantee reliable use of every fact.

Task deliverable: run positions(), verify its origin row and explain the complete ID-to-vector shape trace. This lab starts from supplied IDs and does not implement text tokenization or learn embeddings.

[Questions](../../assignments/TR-001/questions.md) · [Solutions](../../assignments/TR-001/solutions.md) · [Mechanics lab](../../projects/intermediate/transformer-mechanics/README.md) · [Module index](README.md)
