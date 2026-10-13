# TR-004 · Worked solutions

1. Encoder-decoder, with source representations and target-side causal decoding/cross-attention. Other designs can also perform translation.
2. It may access future tokens that the intended prefix-only predictor would not have at inference time. Align masks, inputs and labels with the task.
3. No. It changes information flow. Training, tokenizer conventions, vocabulary output head and generation loop are still missing.

[Questions](questions.md)
