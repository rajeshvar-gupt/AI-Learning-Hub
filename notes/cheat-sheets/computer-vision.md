# Computer vision revision

| Topic | Recall |
|---|---|
| Image contract | Shape, dtype, range, channel order and corrupt-input policy |
| Output dimension | floor((H+2p-k)/s)+1 for dilation one |
| Kernel parameters | k*k*Cin*Cout + Cout biases |
| Weight sharing | Same kernel at many spatial locations |
| Kernel gradient | Sum patch × activation-gradient contributions |
| ReLU | Gradient blocked where preactivation is nonpositive |
| Pooling | Reduces spatial resolution; not implemented in this lab |
| Classification | One image label; confusion matrix and class metrics |
| Detection | Labeled boxes; IoU matching and AP/precision/recall |
| Segmentation | Pixel labels; overlap metrics and class support |
| Evaluation | Select with validation; freeze before independent test |

Interview practice: why can near-duplicate frames leak across a split? Does convolution guarantee translation invariance? Why can an inappropriate augmentation change the label? Which project parameters are actually learned?

[Lessons and worked answers](../../subjects/computer-vision/README.md)
