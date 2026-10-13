# NLP-003 · A leakage-aware text classification baseline

Prerequisite: NLP-002.

Outcome: train a text classifier and compare it to an explicit baseline.

The project uses a TF-IDF/logistic-regression pipeline. Logistic regression learns decision boundaries over text features; it does not generate replies. A majority-label dummy classifier is fitted using training labels. Both are evaluated on the same twelve instructional test messages after selection is frozen.

Three stratified training folds compare four configurations: unigram versus unigram+bigram features, and C values .5 versus 2. C controls inverse regularization strength. The entire pipeline is fitted within each fold, then the selected configuration is refitted on all 36 training texts. The test messages do not enter this search.

Macro-F1 treats each class equally. Read per-class precision, recall and support, plus confusion counts with actual labels in rows and predictions in columns. A high score on twelve invented, clearly worded examples cannot establish real support-routing quality. Record errors and describe the sample rather than claiming a deployed automation.

The route helper preserves the raw predicted class for explanation but sets route to needs_review when the feature vector is all zeros. It rejects blank texts. This policy does not automatically catch every unknown intent, and known vocabulary is not a confidence guarantee.

Run the project from the repository root using the existing requirements-ml.txt environment. Inspect the actual report, selected parameters and training-fold variation. Fold standard deviation is descriptive, not automatically a confidence interval.

[Questions](../../assignments/NLP-003/questions.md) · [Solutions](../../assignments/NLP-003/solutions.md) · [Module index](README.md)
