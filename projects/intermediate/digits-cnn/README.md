# Handwritten digits · CNN from scratch

Status: published. Prerequisites: CV-001–CV-003.

An actual trainable CNN: four 3×3 convolution kernels, ReLU, flatten and a dense ten-class head. Both kernels and the head learn by backpropagation. The network has 1,490 parameters. It uses scikit-learn's bundled grayscale digits, so no dataset download, API key or GPU is needed.

From the repository root, activate the existing environment installed from requirements-ml.txt:

```bash
python projects/intermediate/digits-cnn/train.py
python -m unittest discover -s tests -p 'test_computer_vision.py' -v
```

The fixed stratified split is approximately 60% train, 20% validation and 20% test. Pixels are divided by their known maximum 16. Twenty-five epochs of mini-batch SGD use batch size 64 and learning rate .08. The lowest validation-loss checkpoint is restored before evaluating test labels. A training-label majority baseline supplies context.

The script creates outputs/report.json and outputs/training.png beside train.py. Rerunning replaces its own generated files; outputs/ is already ignored by the parent project rules. The report includes confusion counts (actual rows, predicted columns, digits 0–9), loss history and held-out metrics. The plot shows loss curves and the learned kernels. [Actual results](../../../VALIDATION-CV.md).

This implementation is fixed to 8×8 grayscale inputs and ten labels. It has no pooling, stacked convolution, input-gradient API, pretrained weights or production inference endpoint. The convolution uses cross-correlation, without flipping kernels. It is a teaching model for CPU execution; a framework implementation can be a later exercise.

Practice: calculate every shape and the parameter count; explain the kernel gradient; inspect the finite-difference tests; then write a model card and propose a validation-only experiment. Phone photos and new writers require representative independent evaluation.

[Lessons](../../../subjects/computer-vision/README.md)
