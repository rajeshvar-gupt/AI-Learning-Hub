# NLP-004 · Worked solutions

1. They share subword fragments across related spellings. They may also increase noise and features, so compare on training/validation data.
2. Bag-of-words loses general sequence order; an RNN updates a state in token order. This adds sequential computation and optimization challenges.
3. Define a cutoff, keep complete conversations together, tune only on earlier training/validation conversations, freeze the pipeline and evaluate on later untouched conversations. Check duplicate templates and policy changes across the boundary.

[Questions](questions.md)
