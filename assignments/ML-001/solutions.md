# ML-001 · Worked solutions

1. Certificate date is only known after completion, so it leaks the target. Define the prediction time and remove future information.
2. Group by learner so no learner appears in both partitions; use grouped cross-validation within training as well. If deployment predicts future periods, time ordering may also be necessary.
3. Predict the training mean (or median for an absolute-error-oriented baseline). MAE is in currency units. Fit the baseline using training targets, never the full dataset.

[Questions](questions.md) · [Lesson](../../subjects/machine-learning/01-problem-framing.md)
