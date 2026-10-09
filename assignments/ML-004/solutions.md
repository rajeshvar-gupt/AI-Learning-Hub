# ML-004 · Worked solutions

1. Restricting depth prevents fitting small noisy partitions. Bias may rise while variance falls; validation must determine whether the tradeoff helps.
2. kNN uses distances, so a large numeric scale can dominate neighbors. Axis-aligned tree splits are generally insensitive to monotonic rescaling of an individual feature.
3. No. Importance is a property of fitted associations and the chosen importance method. Confounding, proxies and correlated features can drive it; causal claims need an appropriate design.

[Questions](questions.md) · [Lesson](../../subjects/machine-learning/04-model-families.md)
