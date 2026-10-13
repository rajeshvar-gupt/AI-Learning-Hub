# NLP-005 · A worked attention example and transformer bridge

Prerequisite: NLP-004.

Outcome: calculate one-head scaled dot-product attention and interpret its mask.

Queries Q compare with keys K using scores QKᵀ/sqrt(dk). A row-wise softmax produces weights over keys; multiplying those weights by V forms weighted combinations of values. The lab uses supplied tiny arrays, not learned language representations. Shape checks require matching query/key feature width and key/value row count.

For Q=K=I₂, each row has one score 1/sqrt(2) and one zero. Softmax gives approximately .66976 on its matching key and .33024 on the other. With values [[2,0],[0,4]], the first output is approximately [1.33952,1.32095]. Each weight row sums to one.

A causal mask forbids attending to future positions. In the two-token demonstration, the first query has only its first key allowed, giving weights [1,0]. The second query can see both. A fully masked row has no defined normalized distribution; the implementation rejects it instead of returning NaNs. Masks can also exclude padding.

A complete transformer adds learned projections, multiple attention heads, positional information, feed-forward blocks, residual connections and normalization. The toy calculation contains none of that training. Attention weights alone are not a guaranteed explanation of why a language model answers a question.

Run the attention script and inspect both unmasked and causal outputs. Next: a dedicated transformer module after this reviewed NLP release. No external model credentials are required for this calculation.

[Questions](../../assignments/NLP-005/questions.md) · [Solutions](../../assignments/NLP-005/solutions.md) · [Module index](README.md)
