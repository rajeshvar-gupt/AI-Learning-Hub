# TR-002 · Multi-head attention and masks

Prerequisite: TR-001.

Outcome: trace head dimensions and verify forbidden-key weights.

The prior NLP lab supplied Q, K and V directly. This lab projects each token vector through Wq, Wk and Wv, splits their width into heads, calculates attention independently per head, concatenates the head outputs and applies Wo. All projection matrices are random supplied parameters, not trained language features.

For four tokens, width eight and two heads, each Q/K/V head is (4,4). Scores and weights are (2,4,4), and concatenated output returns to (4,8). Width must divide evenly by the head count in this implementation. Head count does not multiply model width here.

A boolean allowed mask uses true for keys a query may see. The causal lower triangle blocks future keys. Masked scores become negative infinity before softmax; their weights become zero. Every query needs at least one allowed key, so a fully masked row raises an error. Other APIs may use different mask conventions—check the function contract.

Softmax normalizes over keys, not over query rows or heads. Subtracting each score-row maximum stabilizes exponentiation. Attention weights describe the calculation but are not guaranteed explanations of a model's answer.

Task deliverable: inspect attention_shape and row_sums, then perturb the final token and verify earlier causal-block outputs stay unchanged. A padding-mask design exercise follows; the executable example contains four real supplied tokens.

[Questions](../../assignments/TR-002/questions.md) · [Solutions](../../assignments/TR-002/solutions.md) · [Mechanics lab](../../projects/intermediate/transformer-mechanics/README.md) · [Module index](README.md)
