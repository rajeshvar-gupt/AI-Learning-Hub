# DL-004 · Regularization and diagnosing training failures

Prerequisite: DL-003.

Compare learning curves before adding capacity. High training and validation loss may indicate underfitting, poor optimization or broken labels. Low training loss with rising validation loss suggests overfitting. First try a tiny training subset: a sufficiently flexible network should be able to fit it. If it cannot, check shapes, label indexing, gradient signs and input scale.

L2 regularization penalizes squared weights, while early stopping limits training based on validation performance. Dropout randomly suppresses activations during training and changes behavior during evaluation. Data augmentation adds plausible transformations without changing the label; an inappropriate transformation can change what a sample means. Fit learned normalization only on training data. This lab divides pixels by the known fixed scale 16, which does not estimate statistics from held-out examples.

The lab uses checkpoint selection but does not implement dropout, batch normalization or augmentation. These are conceptual extensions for a later framework exercise. Never label a feature implemented merely because it is discussed.

A reproducible seed does not prove reliability. Report dataset size, split policy, baseline and environment. Random digit-image splits do not establish generalization to unseen writers because the bundled dataset does not provide writer-group IDs for this experiment. Outcome: diagnose a curve and propose one validation-only experiment before viewing test results.

[Project](../../projects/intermediate/digits-neural-network/README.md) · [Questions](../../assignments/DL-004/questions.md) · [Solutions](../../assignments/DL-004/solutions.md) · [Module index](README.md)
