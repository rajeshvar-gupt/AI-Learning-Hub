# ML-004 · Trees, ensembles and alternative models

Prerequisites: ML-003.


Outcome: choose candidate families based on data and explain bias/variance tradeoffs.

A decision tree repeatedly splits features into regions. Deep trees can fit noise; maximum depth and minimum leaf size control complexity. Random forests average many randomized trees to reduce variance. Boosting adds learners sequentially to correct remaining errors; learning rate and iteration count affect complexity. These methods capture nonlinear interactions without requiring manually specified polynomial terms.

k-nearest neighbors predicts from nearby training points; scaling and the choice of k matter. It stores the training set, so prediction can become expensive. Support-vector machines seek a wide margin; kernels can model nonlinear boundaries but need suitable scaling and tuning. Naive Bayes combines class-conditional likelihoods under conditional-independence assumptions and is often a useful text baseline. No family wins for every dataset.

Underfitting shows poor training and validation performance. Overfitting shows strong training performance with worse validation performance. Learning curves vary training size to diagnose whether more data may help; validation curves vary a hyperparameter. Compare models on the same folds and metric, including variability rather than treating tiny differences as decisive.

Feature importance describes model behavior, not causality. Tree impurity importance can favor features with many possible splits. Permutation importance measures degradation after shuffling a feature, but correlated features can mask each other's contributions. Keep interpretation separate from claims about interventions.

The lab compares a shallow tree, forest, scaled logistic regression, kNN, SVM and Gaussian Naive Bayes against a dummy classifier. Small grids keep the offline exercise manageable.


## Practice

[Questions](../../assignments/ML-004/questions.md) · [Solutions](../../assignments/ML-004/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
