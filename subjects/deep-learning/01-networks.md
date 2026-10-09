# DL-001 · Neurons, layers and tensor shapes

Prerequisite: ML-007.

A dense layer maps a batch X of shape (n,d) to XW+b, with W shaped (d,h) and b shaped (h,). A nonlinear activation lets stacked layers represent more than a single affine transformation. Without nonlinearities, two dense layers collapse into one affine map. Width counts units; depth counts successive learned transformations.

The project uses 64 input pixels, hidden widths 32 and 16, and 10 output logits. Its parameter count is 64*32+32 + 32*16+16 + 16*10+10 = 2,778. The batch dimension does not change this count. A logit is an unrestricted score, not a probability.

ReLU keeps positive values and maps negative values to zero. Its derivative is zero on the negative side and one on the positive side; our implementation chooses zero at the nondifferentiable origin. Tanh is smooth but can saturate, producing small derivatives. The lab uses ReLU and variance-aware random initialization. Identical initialization for every hidden unit would preserve symmetry and waste capacity.

Outcome: trace the shapes through the network and explain why its nonlinearities matter. Read initialize() and forward() in the project before training.

[Project](../../projects/intermediate/digits-neural-network/README.md) · [Questions](../../assignments/DL-001/questions.md) · [Solutions](../../assignments/DL-001/solutions.md) · [Module index](README.md)
