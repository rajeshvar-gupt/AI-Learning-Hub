# Transformer module validation

Executed 2026-10-13 on Linux with Python 3.12.14 and NumPy 2.3.5 in the existing environment. No clean installation, GPU, PyTorch/Transformers-library execution, downloaded model or Windows/macOS runtime was tested.

## Commands

From the repository root:

```bash
python projects/intermediate/transformer-mechanics/mechanics.py
python -m unittest discover -s tests -p 'test_transformers.py' -v
```

The script completed successfully and all ten new tests passed. Checks cover positional origin values, per-row normalization, head shapes and mask zeros, identity-projection attention against a manual calculation, future-token exclusion through the full causal block, seeded repeatability, temperature/top-k behavior and invalid inputs. Internal Markdown targets and curriculum prerequisites were checked against new files plus the base tree.

## Observed numerical evidence

| Item | Actual result |
|---|---|
| Input / block output | (4,8) / (4,8) |
| Attention weights | (2,4,4), two heads |
| Attention row sums | 1 for every query in both heads |
| First causal query | [1,0,0,0] for each head |
| Temperature .7 / top-k two | Probabilities [.80667863,.19332137,0,0] |
| Seeded sample | Token ID 0 |
| Top-k one check | Selects the highest-logit token |

The [full example report](projects/intermediate/transformer-mechanics/example-report.json) preserves the numerical block output. These are values from randomly initialized, untrained parameters and supplied logits, not accuracy, language generation or evidence of task quality. There is no backward/gradient implementation to validate and no trained-model benchmark.

Existing Python/ML/DL/CV/NLP source was unchanged and not retested in this extension. The five completed content tasks are TR-001 through TR-005; publication completed through PR #12. Earlier legacy repairs and specialized architecture projects remain separate work.
