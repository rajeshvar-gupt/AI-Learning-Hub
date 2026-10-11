# CV-002 · Convolution, receptive fields and pooling

Prerequisite: CV-001.

Outcome: calculate output sizes and parameter counts, then inspect the project's shared kernels.

A CNN applies a learned local kernel at many image positions. Most library layers perform cross-correlation: multiply a patch by the kernel without reversing it. In the project, four 3×3 kernels traverse each grayscale 8×8 input at stride one with no padding, producing a 6×6×4 feature map. The same nine coefficients are reused at every location for each channel.

For a spatial dimension H, kernel k, padding p, stride s and dilation one, output size is floor((H+2p-k)/s)+1. A conventional dense convolution with input channels Cin and output channels Cout has k*k*Cin*Cout weights plus Cout biases. The project convolution has 36 weights and 4 biases. Its flattened 144 features feed a ten-logit dense head with 1,450 parameters; total 1,490.

ReLU supplies nonlinearity. Max pooling selects a local maximum; average pooling averages a region. Both can reduce resolution and discard spatial information. Pooling is discussed here but is not implemented in this first CNN. Flattening retains positions in the dense head, so this complete classifier is not guaranteed translation-invariant.

A receptive field is the input region affecting one activation. Stacking local layers increases it. Weight sharing reduces parameter count and introduces a useful spatial assumption; it does not guarantee better results than every dense model.

[Questions](../../assignments/CV-002/questions.md) · [Solutions](../../assignments/CV-002/solutions.md) · [CNN project](../../projects/intermediate/digits-cnn/README.md) · [Module index](README.md)
