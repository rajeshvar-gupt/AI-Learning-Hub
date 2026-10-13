# Transformer primary references

Checked 2026-10-13. The course derivations, worked examples and NumPy implementation are original teaching material; they do not reproduce published benchmarks.

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017: original transformer architecture and attention background.
- PyTorch, [TransformerEncoderLayer reference](https://docs.pytorch.org/docs/2.14/generated/torch.nn.TransformerEncoderLayer.html): attention/feed-forward layer interface and configurable normalization placement. Official stable documentation redirected to version 2.14 when checked; PyTorch is not used by the executable lab.
- Devlin et al., [BERT](https://arxiv.org/abs/1810.04805), 2018/2019: bidirectional pretraining example.
- Hugging Face, [Generation strategies](https://huggingface.co/docs/transformers/main/en/generation_strategies): decoding concepts. The main documentation can differ from stable installations; this release makes no Transformers-library API execution claim.

No pretrained weights, external corpus or third-party figures are redistributed. A future downloaded-model experiment must record checkpoint identity, license, tokenizer, environment and actual measured results.
