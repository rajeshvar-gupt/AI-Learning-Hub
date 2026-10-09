# ML-001 · Problem framing, splits and baselines

Prerequisites: DATA-003, STAT-002.


Outcome: turn a question into a prediction task with a defensible evaluation plan.

Supervised learning uses labeled examples: regression predicts a number, classification a category. Unsupervised learning explores structure without a target label. Define the unit of prediction, target, time of prediction and available features before fitting anything. A field recorded after the outcome is leakage even if its column name looks innocent.

Reserve a final test set before learned preprocessing. Use training folds to fit transformations and tune models; put imputation, scaling and estimation in a pipeline. Stratification helps preserve class proportions. For repeated subjects use group-aware splits; for forecasting use chronological splits. Random splitting is not a universal recipe.

A baseline tells you whether complexity helps: mean prediction for regression, majority or prior prediction for classification. Choose the metric using the error cost, not the largest-looking score. Specify a test protocol before seeing test performance. Repeated test-driven changes turn the test set into another validation set.

The supervised lab uses generated regression data and the bundled Iris dataset, holds out 25%, then compares candidates by five training folds. The chosen candidate is fitted on all training data and scored once on the held-out partition. These small educational datasets demonstrate procedure, not production readiness.


## Practice

[Questions](../../assignments/ML-001/questions.md) · [Solutions](../../assignments/ML-001/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
