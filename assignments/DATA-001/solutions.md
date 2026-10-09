# DATA-001 · Worked solutions

1. `X.mean(axis=1)` gives `[1.5,3.5,5.5]`.
2. `scale=X.std(axis=0); scale=np.where(scale==0,1,scale); Z=(X-X.mean(axis=0))/scale`. Constant columns become zero. For ML, learn the means/scales on training data only, preferably in a pipeline.
3. The slice shares storage; X may change too. Use `y=X[:2].copy()` when this is unwanted.

[Questions](questions.md) · [Lesson](../../subjects/data-analysis/01-numpy.md)
