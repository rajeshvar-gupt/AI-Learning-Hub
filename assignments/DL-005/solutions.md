# DL-005 · Worked solutions

1. Tensor/module operations implement forward; automatic differentiation computes gradients; optimizer.step updates parameters after backward.
2. Eval mode controls selected module behavior; no-gradient mode controls graph recording. One does not generally imply the other.
3. Record data origin, dimensions, splits, seed, training budget, checkpoint criterion, baseline, actual metrics and distribution limits. Obtain writer IDs or a separate writer dataset, split by writer, select using training/validation writers and evaluate on untouched test writers.

[Questions](questions.md)
