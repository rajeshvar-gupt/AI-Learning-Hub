# Transformer mechanics · offline NumPy lab

Status: prepared for review. Prerequisites: TR-001–005.

One executable lab accompanies all five tasks. It uses supplied token IDs and random untrained embedding/projection parameters to run a two-head forward block, then decodes an unrelated fixed-logit vector. It does not produce language or claim model quality.

From the repository root, activate the existing environment installed from requirements-ml.txt:

```bash
python projects/intermediate/transformer-mechanics/mechanics.py
python -m unittest discover -s tests -p 'test_transformers.py' -v
```

No credentials, GPU, external dataset or model download is needed. NumPy is the only imported third-party dependency. The script writes outputs/report.json beside its source; rerunning replaces that generated output, covered by the existing parent project ignore rules.

The example uses four token IDs, width eight, two heads and feed-forward width 16. The block uses pre-normalization, unit/zero normalization affine values, ReLU, no dropout and no final normalization. Its lower-triangular mask permits current and earlier keys. All active rows must permit at least one key.

The separate decoding example uses logits [2,1,0,-1], temperature .7, top-k two and seed 42. It samples token IDs, not words. The script does not implement top-p, beam search, autoregressive generation, backward gradients or training.

[Actual validation](../../../VALIDATION-TRANSFORMERS.md) records numerical outcomes. Practice: trace shapes; verify attention rows sum to one; perturb a future token; compare top-k one with two; write an honest model card. Architecture-family selection and evaluation planning are written exercises rather than implemented pretrained-model experiments.

[Five-task module](../../../subjects/transformers/README.md)
