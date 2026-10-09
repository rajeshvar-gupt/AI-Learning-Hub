# Deep learning validation

Executed on 2026-10-09 in Linux with Python 3.12.14, NumPy 2.3.5, scikit-learn 1.8.0 and matplotlib 3.10.8, using the existing requirements-ml.txt environment. OpenBLAS was limited to one thread for these runs with `OPENBLAS_NUM_THREADS=1`. No clean package installation, GPU, PyTorch, Windows or macOS execution was tested.

## Executed commands

From the repository root (the environment variable prefix is optional on other systems):

```bash
OPENBLAS_NUM_THREADS=1 python projects/intermediate/digits-neural-network/train.py
OPENBLAS_NUM_THREADS=1 python -m unittest discover -s tests -p 'test_deep_learning.py' -v
```

Training exited successfully and all seven new tests passed: parameter shapes/count, central-difference gradients for every parameter of a tiny network, stable extreme-logit loss, disjoint/exhaustive splits, learning and best-checkpoint restoration, invalid inputs, and repeatable initialization. The learning-curve chart was visually inspected for legible labels. Internal Markdown targets and curriculum prerequisite IDs were checked against the release and base tree. Existing ML code was not changed or retested in this extension; its earlier 50-test result remains recorded in VALIDATION-ML.md.

## Actual results

| Item | Result |
|---|---|
| Split | 1,077 train / 360 validation / 360 test |
| Architecture | 64 → 32 → 16 → 10, 2,778 parameters |
| Training | 40 epochs; validation selected epoch 40 |
| Majority baseline test accuracy / macro-F1 | .1000 / .01818 |
| Network test accuracy / macro-F1 | .9500 / .94796 |

See the [full example report](projects/intermediate/digits-neural-network/example-report.json) for loss history and the 10×10 confusion matrix (rows actual, columns predicted, classes 0–9). No hyperparameters were changed after viewing test metrics. This is one seeded split, not a confidence interval or a generalization guarantee for new writers. Validation improved through the final epoch in this run; the checkpoint code supports an earlier best epoch but this result does not demonstrate an optimal stopping budget.
