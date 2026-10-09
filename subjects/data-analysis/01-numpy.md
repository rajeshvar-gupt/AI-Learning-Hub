# DATA-001 · NumPy arrays and vectorization

Prerequisites: MATH-001, STAT-001.


Outcome: select, transform and summarize numerical arrays with deliberate axes and dtypes.

```python
import numpy as np
X = np.array([[1., 2.], [3., 4.], [5., 6.]])
assert X.shape == (3, 2)
assert np.allclose(X.mean(axis=0), [3, 4])
centered = X - X.mean(axis=0)
selected = X[X[:, 0] >= 3]
assert selected.shape == (2, 2)
```

Axis 0 aggregates down rows, producing one value per column here; axis 1 produces one per row. Broadcasting aligns trailing dimensions: a `(2,)` mean broadcasts across `(3,2)`. A `(3,)` vector cannot broadcast in the same way; reshape it to `(3,1)` to apply one value per row.

Array dtypes affect behavior: integer arrays cannot represent missing floating-point values as NaN without conversion. `np.nanmean` skips NaNs, but an all-missing slice has no defined mean. Validate that scenario instead of silently assuming zero. Vectorization moves repeated operations into array kernels, but huge intermediate arrays still cost memory.

Basic slicing often returns a view sharing memory, while advanced indexing usually returns a copy. Use `.copy()` when independent mutation is intended. Know whether an operation changes the input before reusing a dataset.


## Practice

[Questions](../../assignments/DATA-001/questions.md) · [Solutions](../../assignments/DATA-001/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
