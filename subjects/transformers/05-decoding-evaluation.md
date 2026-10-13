# TR-005 · Decoding, evaluation and transformer assessment

Prerequisite: TR-004.

Outcome: explain token selection and distinguish numerical mechanics from measured model quality.

Greedy decoding chooses the highest-scoring next token. Sampling draws from a probability distribution. Temperature divides logits before normalization: smaller positive values usually concentrate mass, larger values flatten it. Top-k restricts choices to k highest-scoring tokens before normalization. Top-p instead selects a probability-mass prefix; it is described but not implemented here.

The lab applies temperature .7 and top-k two to supplied logits [2,1,0,-1]. It gives probabilities approximately [.80668,.19332,0,0]. A seeded draw is repeatable for this environment; it is not text generation because these logits do not come from a trained language head. Top-k one is deterministic highest-score selection with the implementation's stable tie handling.

A next-token model is evaluated with aligned targets and masks. Mean negative log-likelihood averages -log probability of the correct target over valid tokens; perplexity is its exponential. Compare perplexity only under compatible tokenization, data and evaluation conditions. A low loss does not establish factual correctness, instruction-following or safe application behavior.

For an application, define representative tasks, references, failure criteria, latency and resource limits. Separate development prompts from final evaluation prompts. Check model license and access requirements before adding a downloaded checkpoint. No checkpoint, API call, GPU experiment or trained transformer benchmark is included in this release.

Task deliverable: run the decoding examples and all checks; explain the causal test; complete a model card that explicitly labels the lab untrained; design a future evaluation without inventing quality scores. Generative-AI/LLM application work can follow when requested.

[Questions](../../assignments/TR-005/questions.md) · [Solutions](../../assignments/TR-005/solutions.md) · [Mechanics lab](../../projects/intermediate/transformer-mechanics/README.md) · [Module index](README.md)
