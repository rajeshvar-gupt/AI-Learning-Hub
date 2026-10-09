# Handwritten digits · neural network from scratch

Status: prepared for review. Prerequisites: DL-001–DL-004.

Train a 64→32→16→10 dense ReLU network with NumPy and manual backpropagation. The scikit-learn bundled digits dataset contains 1,797 images, each 8×8 pixels, with classes 0–9. No dataset download, API key or GPU is needed. Dataset provenance is available in `load_digits().DESCR`.

From the repository root, activate your environment and install the existing `requirements-ml.txt`. Then run:

```bash
python projects/intermediate/digits-neural-network/train.py
python -m unittest discover -s tests -p 'test_deep_learning.py' -v
```

The fixed split is approximately 60% training, 20% validation and 20% test, stratified by class. Inputs use the known fixed pixel scale 16. Forty epochs of mini-batch SGD use batch size 64 and learning rate .08. The best validation-loss weights are copied and restored, then evaluated on the final test set. A majority-class predictor fitted from training labels supplies a baseline. The test set does not select epochs or parameters.

`outputs/report.json` contains split sizes, metrics, confusion counts and learning history. `outputs/learning-curves.png` shows training and validation loss. Rerunning replaces these generated files. [Observed validation](../../../VALIDATION-DL.md) records actual results; minor platform differences are possible.

The implementation is intentionally small and fixed to ten output classes in fit(). It is a teaching program, not a general estimator API. It does not implement GPU training, dropout, data augmentation or a production inference service. Performance on random splits of small grayscale digits does not establish performance on new writers or phone photographs.

Practice: explain every array shape, derive the output gradient, inspect the numerical gradient test, and write a model card. For a new experiment, change one setting using validation data; do not repeatedly use the existing test scores to tune it.

[Lessons](../../../subjects/deep-learning/README.md)
