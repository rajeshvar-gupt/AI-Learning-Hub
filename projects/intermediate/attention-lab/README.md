# Scaled dot-product attention lab

Status: published. Prerequisite: NLP-005.

A tiny NumPy calculation shows how query-key scores turn into normalized weights and weighted values. It includes a causal mask and explicit rejection of fully masked query rows. It is not a trained transformer or a language model.

From the repository root in the existing requirements-ml.txt environment:

```bash
python projects/intermediate/attention-lab/attention.py
python -m unittest discover -s tests -p 'test_nlp.py' -v
```

The script prints its arrays and writes no files. Each weight row should sum to one; forbidden keys have zero mass. Shape, finiteness and mask validation are included. Input matrices are supplied directly, so there are no datasets, model weights, keys or network calls.

Practice: manually calculate the first unmasked output, explain the first causal row and change the value vectors while keeping weights fixed. Then explain which learned components a full transformer would still need.

[Lesson](../../../subjects/nlp/05-attention.md) · [Validation](../../../VALIDATION-NLP.md)
