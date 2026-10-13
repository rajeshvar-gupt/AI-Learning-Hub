# NLP-004 · Error analysis, sequence models and NLP assessment

Prerequisite: NLP-003.

Outcome: distinguish representation limits from model errors and justify the next experiment.

Assess text systems beyond one aggregate score. Check negation, misspellings, short inputs, mixed-language text, repeated templates and unseen intents. Keep a separate representative evaluation set for claims about intended use. A handcrafted challenge set is diagnostic; do not silently turn it into a claimed population benchmark.

Avoid publishing sensitive source text in error reports. The project's examples are invented, so its report can show every test message safely. A real support dataset needs permission, minimization and a retention policy. Label provenance and annotation disagreements belong in the model card.

An RNN updates a hidden state as it reads a sequence. Repeated state transitions can make gradients shrink or grow across long paths. LSTM and GRU architectures introduce gates to regulate state updates; they help some sequence-learning problems but do not guarantee perfect long-context retention. An embedding layer converts token IDs to learned dense vectors. Padding and masks distinguish real tokens from filler.

RNN/LSTM/GRU are introduced conceptually here; none is implemented or trained in this baseline project. Transformers introduce attention-based sequence processing and are the subsequent module. Choose them because the task and validation support the tradeoff, not because a larger architecture sounds more advanced.

Assessment: run the text pipeline, explain its baseline and all-zero policy, pass the tests and write a model card. Propose a validation-only extension using character n-grams, new labels or more representative data. Mark hypothetical improvements separately from measured output.

[Questions](../../assignments/NLP-004/questions.md) · [Solutions](../../assignments/NLP-004/solutions.md) · [Module index](README.md)
