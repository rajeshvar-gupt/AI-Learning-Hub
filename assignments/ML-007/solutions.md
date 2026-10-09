# ML-007 · Worked solutions

1. Use the run instructions in THROUGH-ML.md; compare report structure and approximate scores with VALIDATION.md. Minor version/platform differences can change numerical results. Explain MAE/RMSE/R², macro-F1/confusion counts and silhouette in their respective contexts.
2. A common policy is `OneHotEncoder(handle_unknown="ignore")` inside a ColumnTransformer and pipeline fitted on training folds. An unseen value becomes zeros for that feature's learned categories; document that information loss and monitor unknown frequency. Do not fit an encoder on test values just to avoid an error.
3. Group all rows from one subject together, or reserve the most recent period and use time-respecting validation. Define the metric from error costs, fit all learned transforms inside each fold, tune only with training folds, freeze decisions and evaluate once on the final partition. Report uncertainty and dataset limitations.
4. A pipeline prevents some preprocessing leakage but cannot remove a future-information feature, overlapping subjects, mislabeled split boundaries or repeated test-driven decisions. Correct task design remains essential.

[Questions](questions.md) · [Lesson](../../subjects/machine-learning/07-review.md)
