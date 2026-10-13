# NLP revision and interview prompts

| Concept | Recall |
|---|---|
| Tokenization | Defines the units; default word analyzer drops one-character tokens |
| Preprocessing | Preserve task meaning, including negation |
| Bag-of-words | Sparse counts; loses general order |
| TF-IDF | Corpus-dependent weighting fitted on training data |
| N-grams | Local sequences; larger feature space |
| Unknown vocabulary | All-zero vectors need an explicit policy |
| Macro-F1 | Equal class weighting; inspect support and confusion counts |
| Embeddings | Dense representations; contextual versus static |
| RNN / LSTM / GRU | Ordered state updates / gated state architectures |
| Attention | softmax(QKᵀ/sqrt(dk))V |
| Causal mask | Prevents attending to future keys |
| Transformer | Attention plus learned projections, positions and other blocks |

Interview prompts: why fit TF-IDF inside CV? What can stop-word removal lose? How do you test unknown intents? Why can twelve perfect predictions still be weak evidence? What happens if every key is masked? How do sequence and attention models differ in their computation?

[Lessons and worked answers](../../subjects/nlp/README.md)
