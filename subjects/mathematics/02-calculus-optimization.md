# MATH-002 · Derivatives and gradient descent

Prerequisites: MATH-001.


Outcome: minimize a quadratic and connect derivatives to a model's loss.

A derivative measures local rate of change. For `f(w)=(w-3)^2`, `f'(w)=2(w-3)`. A gradient collects partial derivatives when parameters form a vector. Gradient descent updates `w <- w - learning_rate * gradient`. The minus sign moves downhill locally, not necessarily to a global minimum for arbitrary functions.

Start at w=0 with learning rate 0.1: gradient -6, new w=0.6, loss falls from 9 to 5.76. The next update gives 1.08. For this quadratic a constant rate strictly between 0 and 1 converges; a rate of 1 oscillates unless already at the optimum. This bound is specific to this curvature.

For mean squared error `L = mean((Xw+b-y)^2)`, `gradient_w = 2 X.T @ (Xw+b-y) / n`. The intercept gradient is twice the mean residual. The chain rule accounts for how changing a weight changes a prediction, then how the prediction changes loss.

Run `python projects/intermediate/foundations-lab/foundations.py` from the repository root. Inspect convergence before using a library optimizer. Stop by a documented iteration budget or small gradient; monitor loss and reject nonfinite inputs. Feature scaling often improves the conditioning of optimization. An excessively large rate may diverge, while a tiny rate may look stuck.


## Practice

[Questions](../../assignments/MATH-002/questions.md) · [Solutions](../../assignments/MATH-002/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
