# Regression and classification benchmark

Prerequisites: ML-004. Status: prepared for review in this curriculum release.

Compare baseline and candidate pipelines with five-fold training CV, then evaluate the chosen model on a 25% holdout.

## Run

From the repository root, after installing [the shared environment](../../../THROUGH-ML.md):

```bash
python projects/intermediate/supervised-ml/train.py
```

All inputs are generated locally, bundled by scikit-learn or written originally for this course. No API keys, network requests or external dataset downloads are needed at runtime. Dependencies require installation first. Scripts with outputs create `outputs/` beside their source; rerunning replaces their own output files. The other scripts print results only.

## Interpret

Generated regression data and bundled Iris need no downloads. CV uses negative MAE (larger is better) for regression and macro-F1 for classification. A report records all candidates; only the selected model and baseline receive holdout scores. Small toy-data performance is not deployment validation.

Compare your output to [the validation record](../../../VALIDATION-ML.md). Preserve your own results and explain differences instead of copying a claimed score. Read the module lessons before changing parameters.

## Practice and review

1. Explain every input, output and assumption.
2. Change one input in a separate experiment and predict what should happen.
3. Exercise one invalid-input or misleading-interpretation case.
4. Write a [model or analysis card](../../templates/model-card.md), separating observed results from proposed improvements.

Run all new lab checks with `python -m unittest discover -s tests -p 'test_through_ml.py' -v` from the repository root.

[Complete path](../../../THROUGH-ML.md)
