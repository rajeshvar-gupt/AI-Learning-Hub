# ML-003 · Classification and decision metrics

Prerequisites: ML-002.


Outcome: read a confusion matrix and select metrics for imbalanced targets.

Logistic regression maps a linear score to probabilities (sigmoid for binary classification). Despite its name, it is a classifier. A threshold converts a score into a decision; changing it trades false positives against false negatives. Select thresholds using training/validation data and the application cost.

For a chosen positive class: precision=`TP/(TP+FP)`, recall=`TP/(TP+FN)`, F1=`2*precision*recall/(precision+recall)`. State your zero-denominator policy. Accuracy can mislead: predicting the majority class gives 99% accuracy when 99% of examples are negative while finding no positives.

Macro-F1 treats each class equally by averaging class F1 values. Weighted-F1 weights by support and may hide poor minority performance. ROC-AUC evaluates ranking across thresholds; precision-recall analysis is often especially useful when positives are rare. Probability calibration asks whether events predicted at 0.7 occur roughly 70% of the time; ranking alone does not guarantee it.

In the Iris lab, a stratified split protects representation, and macro-F1 selects models. The confusion matrix lists actual labels in rows and predicted labels in columns. Each row sum should equal its class support. This is a small botanical demonstration, not a consequential decision system.


## Practice

[Questions](../../assignments/ML-003/questions.md) · [Solutions](../../assignments/ML-003/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
