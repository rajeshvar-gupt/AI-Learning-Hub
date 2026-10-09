# MATH-001 · Vectors, matrices and shapes

Prerequisites: PY-011.


Outcome: calculate predictions with a dot product and reason about array shapes.

A vector is an ordered list of coordinates. For one learner, `x = [2, 3]` could mean two hours of theory and three exercises. With weights `w = [4, 5]`, the dot product is `2*4 + 3*5 = 23`. Adding intercept 7 predicts 30. Units matter: changing hours to minutes changes the weight needed for the same prediction.

Stack samples as rows in matrix X. For n samples and p features, X has shape `(n, p)`, weights `(p,)`, and `X @ w + b` has shape `(n,)`. Matrix multiplication requires matching inner dimensions. Elementwise multiplication `*` does not perform this operation.

```python
import numpy as np
X = np.array([[2., 3.], [1., 4.]])
w = np.array([4., 5.])
assert np.allclose(X @ w + 7, [30, 31])
assert X.T.shape == (2, 2)
```

The Euclidean norm of `[3,4]` is 5. Distance is the norm of a difference. Cosine similarity compares directions: `a @ b / (norm(a)*norm(b))`; it is undefined for zero vectors. Normalize only when the task benefits from removing magnitude. A row of all zeros needs an explicit policy.

A square matrix may be singular: duplicated columns contain redundant information. For fitting linear systems, use least-squares solvers instead of explicitly calculating an inverse. Rank describes independent directions. Covariance eigenvectors later give PCA directions, but core ML here requires understanding projections and shapes rather than a full eigenvalue derivation.


## Practice

[Questions](../../assignments/MATH-001/questions.md) · [Solutions](../../assignments/MATH-001/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
