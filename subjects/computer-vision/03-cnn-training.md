# CV-003 · Training a CNN and checking kernel gradients

Prerequisite: CV-002.

Outcome: trace gradients from cross-entropy back into the image kernels and run the offline experiment.

The lab computes logits, stable mean cross-entropy, then the output gradient (probabilities minus one-hot labels)/batch size. Backpropagation through the dense head gives a gradient for every flattened feature. Reshape it to (batch,6,6,4), apply the ReLU derivative, and sum each input patch times its corresponding feature gradient to obtain the kernel gradient. Bias gradients sum across batch and spatial positions.

These are gradients of learned kernels, not merely a classifier fitted on frozen image features. The first convolution sees raw fixed images, so input gradients are not needed to optimize this network's parameters. Stacking another learned layer would require propagating gradients into that earlier layer.

The tests perturb all 1,490 parameters of a tiny batch and compare central finite differences with analytical derivatives. This verifies the chain rule numerically away from ReLU kinks. It does not prove dataset quality or deployment readiness.

Training uses mini-batch SGD for a preset 25 epochs. Copies of the best validation-loss parameters are restored before the held-out test report. Training-label class counts supply a majority-class baseline. No test result selects epochs or hyperparameters. Read the actual validation report rather than treating an illustrative score as a promise.

[Questions](../../assignments/CV-003/questions.md) · [Solutions](../../assignments/CV-003/solutions.md) · [CNN project](../../projects/intermediate/digits-cnn/README.md) · [Module index](README.md)
