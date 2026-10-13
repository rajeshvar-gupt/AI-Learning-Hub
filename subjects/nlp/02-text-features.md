# NLP-002 · Bag-of-words, TF-IDF and embeddings

Prerequisite: NLP-001.

Outcome: explain a numerical text representation and prevent feature-learning leakage.

Bag-of-words counts vocabulary terms in each document. Its features do not preserve arbitrary word order. Bigrams add adjacent pairs and can distinguish “not working” from “working,” but increase feature count. Sparse matrices store mostly nonzero entries, which is useful for large vocabularies.

TF-IDF combines within-document term frequency with a corpus-frequency weight. In the lab's default smoothed scikit-learn configuration, IDF is log((1+n)/(1+df))+1, followed by row L2 normalization of weighted term counts. The vocabulary and document frequencies must be learned on training data, including separately within cross-validation folds. Transform validation/test text without refitting.

A term absent from the learned vocabulary contributes no word feature. A completely unseen message can therefore yield an all-zero vector. The demo flags this case for human review; it does not treat the classifier's intercept-only decision as useful evidence. Text with some known features can still be ambiguous or out of domain, so zero-feature detection is only one limited check.

Embeddings represent tokens or documents as dense vectors. Static word vectors assign a fixed representation per word; contextual models can represent the same word differently depending on surrounding tokens. Similarity does not prove factual correctness or label relevance. No embedding model is downloaded or trained in this release.

Outcome check: explain vocabulary size, row sparsity and why a pipeline is essential for the project's CV search.

[Questions](../../assignments/NLP-002/questions.md) · [Solutions](../../assignments/NLP-002/solutions.md) · [Module index](README.md)
