# MATH-002 · Worked solutions

1. Gradient is `2*(1.08-3)=-3.84`; w becomes `1.464`.
2. Derivative is `6*w+2`; the minimizer is `-1/3`.
3. `r = X @ w + b - y; dw = 2 * X.T @ r / len(y); db = 2*r.mean()`. Division makes the loss a mean, keeping the gradient scale comparable when sample count changes. Sum loss has the same minimizer but requires different learning-rate scaling.

[Questions](questions.md) · [Lesson](../../subjects/mathematics/02-calculus-optimization.md)
