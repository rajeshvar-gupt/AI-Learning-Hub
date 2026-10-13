# Transformer revision and interview sheet

| Concept | Recall |
|---|---|
| Embeddings | Token IDs select rows from a vocabulary-by-width table |
| Positions | Supply order information; token index is not token meaning |
| Heads | Divide projected width; normalize each query over permitted keys |
| Causal mask | Current and earlier keys allowed; future keys zero |
| Normalization | Across one token's features in this lab |
| Residual | Shape-preserving additive path |
| Feed-forward | Shared token-wise nonlinear transformation |
| Encoder | Commonly bidirectional input representations |
| Decoder | Prefix-conditioned causal processing |
| Encoder-decoder | Source representations plus target generation/cross-attention |
| Temperature / top-k | Rescale scores / restrict candidates |
| Perplexity | exp(mean target NLL), dependent on evaluation/tokenization |

Interview prompts: Why must model width divide by head count here? What if every key is masked? How is cross-attention different from self-attention? Can a causal mask alone create language ability? Why can lower temperature still produce false facts? Which steps in this lab are actually trained?

[Lessons and separate solutions](../../subjects/transformers/README.md)
