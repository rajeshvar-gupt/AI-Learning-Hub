# NLP-001 · Text tasks, tokenization and preprocessing

Prerequisite: ML-007.

Outcome: define a text task and preserve meaning when turning documents into tokens.

Classification assigns labels to texts; extraction identifies structured fields or spans; retrieval ranks documents; generation produces new text. The support-message project is classification, not a chatbot. Define what the label means and what information exists at prediction time before choosing a representation.

Tokenization divides text into units. A word tokenizer, character tokenizer and subword tokenizer produce different vocabularies and sequence lengths. Case folding merges case variants but may remove distinctions. Removing punctuation can lose sentiment or code structure. Removing stop words can remove negation: “working” and “not working” should not automatically become equivalent.

Stemming applies heuristic reductions; lemmatization uses linguistic analysis to map words to dictionary forms. Neither is universally beneficial. Choose transformations using the training/validation task and document language coverage. A simple English exercise does not establish Hindi or mixed-language capability.

The lab uses the default scikit-learn word analyzer: lowercase processing and tokens of at least two word characters, without stop-word removal. Single-letter words are excluded under that default. Check empty or tokenless texts explicitly; accepting a string does not mean it contains known features.

The dataset contains 48 original invented examples with fixed instructional partitions. No private messages, customer records or student identities are included. For real documents, separate duplicate threads, authors or time periods when those define deployment generalization.

[Questions](../../assignments/NLP-001/questions.md) · [Solutions](../../assignments/NLP-001/solutions.md) · [Module index](README.md)
