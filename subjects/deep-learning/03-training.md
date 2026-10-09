# DL-003 · Mini-batches, validation and checkpoints

Prerequisite: DL-002.

An epoch passes through the training set once; an optimizer step updates weights from one batch. With 100 examples and batch size 32, an epoch has four steps including an incomplete final batch. Shuffle training indices with a seeded generator. Validation and test examples never appear in optimizer batches.

The lab uses mini-batch stochastic gradient descent with a fixed learning rate and 40-epoch budget. It saves copies of the weights whenever validation cross-entropy improves. After training, it restores the best validation checkpoint before evaluating the test set. Selecting a checkpoint is model selection, so the test set cannot choose the epoch.

A large learning rate can cause unstable loss; a very small one can converge slowly. Momentum accumulates a direction from prior gradients; Adam adapts updates using moving gradient moments. Neither replaces validation or fixes leakage. This first lab deliberately uses plain SGD so the update is inspectable.

Training loss is measured after each complete epoch over the training partition, making its history comparable to validation loss. Accuracy is useful but ignores how confident wrong predictions are. Record both loss and classification metrics. Outcome: explain the loop, identify the checkpoint criterion and distinguish best_epoch from epochs_run.

[Project](../../projects/intermediate/digits-neural-network/README.md) · [Questions](../../assignments/DL-003/questions.md) · [Solutions](../../assignments/DL-003/solutions.md) · [Module index](README.md)
