# ML-003 · Worked solutions

1. Precision=.8; recall=8/12≈.667; F1=16/22≈.727; accuracy=94/100=.94.
2. More observations are labeled positive, so recall cannot decrease and false positives cannot decrease (ties aside in how thresholds are represented). Precision need not vary monotonically.
3. No. Choose on training/validation data, freeze it, and evaluate on untouched test data. If the test set has already guided decisions, obtain a new evaluation set or label the estimate accordingly.

[Questions](questions.md) · [Lesson](../../subjects/machine-learning/03-classification.md)
