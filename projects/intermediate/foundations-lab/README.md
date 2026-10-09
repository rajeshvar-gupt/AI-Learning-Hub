# Numerical foundations

Prerequisites: MATH-002, STAT-002. Status: prepared for review in this curriculum release.

Minimize `(w-3)^2`; summarize eight invented measurements and calculate a t interval/test.

## Run

From the repository root, after installing [the shared environment](../../../THROUGH-ML.md):

```bash
python projects/intermediate/foundations-lab/foundations.py
```

All inputs are generated locally, bundled by scikit-learn or written originally for this course. No API keys, network requests or external dataset downloads are needed at runtime. Dependencies require installation first. Scripts with outputs create `outputs/` beside their source; rerunning replaces their own output files. The other scripts print results only.

## Interpret

The optimizer approaches 3 and loss decreases. Inference is a mechanics exercise on invented measurements, not evidence of a real effect.

Compare your output to [the validation record](../../../VALIDATION-ML.md). Preserve your own results and explain differences instead of copying a claimed score. Read the module lessons before changing parameters.

## Practice and review

1. Explain every input, output and assumption.
2. Change one input in a separate experiment and predict what should happen.
3. Exercise one invalid-input or misleading-interpretation case.
4. Write a [model or analysis card](../../templates/model-card.md), separating observed results from proposed improvements.

Run all new lab checks with `python -m unittest discover -s tests -p 'test_through_ml.py' -v` from the repository root.

[Complete path](../../../THROUGH-ML.md)
