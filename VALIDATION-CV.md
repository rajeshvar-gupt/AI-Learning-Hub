# Computer vision validation

Executed 2026-10-11 on Linux, Python 3.12.14, NumPy 2.3.5, scikit-learn 1.8.0 and matplotlib 3.10.8. Used the existing requirements-ml.txt environment; no clean installation, GPU, PyTorch or Windows/macOS execution was tested.

## Executed commands

From the repository root:

```bash
OPENBLAS_NUM_THREADS=1 python projects/intermediate/digits-cnn/train.py
OPENBLAS_NUM_THREADS=1 python -m unittest discover -s tests -p 'test_computer_vision.py' -v
```

The environment prefix limited OpenBLAS to one thread for these runs. Training completed and six new tests passed: known cross-correlation values/shapes, finite differences for all 1,490 parameters on a tiny batch, training improvement/checkpoint restoration, disjoint exhaustive splits, invalid inputs and repeatable initialization. Inspected the generated learning-curve/kernel chart for legibility. Internal Markdown targets and registry prerequisite IDs were validated against new files plus the main tree.

## Observed results

| Item | Actual result |
|---|---|
| Split | 1,077 train / 360 validation / 360 test |
| Trainable parameters | 1,490 |
| Epoch budget / selected epoch | 25 / 25 |
| Majority baseline accuracy / macro-F1 | .10000 / .01818 |
| CNN test accuracy / macro-F1 | .95833 / .95803 |

[Full example report](projects/intermediate/digits-cnn/example-report.json) includes the confusion matrix and loss history. The test set reports the restored validation checkpoint. No hyperparameters were changed after viewing test metrics. The numerical gradient test covers parameters, not input derivatives; input derivatives are not implemented.

This is one seeded toy-data experiment. Validation selected the last epoch here, so the run does not establish an optimal training budget. Dataset identity groups are not used; new-writer or camera generalization is unverified. The earlier dense-network project uses the same split, so comparing its already-visible test score with this score is exploratory rather than independent architecture selection. Obtain fresh evaluation for further test-guided decisions.

Existing ML and dense-network source files were not changed or retested in this extension; their prior validation records remain available. No detection, segmentation, pooling or pretrained architecture training was executed.
