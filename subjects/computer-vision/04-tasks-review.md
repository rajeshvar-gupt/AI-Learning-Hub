# CV-004 · Vision tasks, architecture choices and evaluation

Prerequisite: CV-003.

Outcome: distinguish image classification from detection and segmentation, and write a defensible CNN report.

Classification assigns a label to an image. Object detection predicts labeled boxes and scores, potentially for several objects. Semantic segmentation assigns categories to pixels; instance segmentation also separates individual objects. The digits lab implements classification only. It contains no localization, bounding-box annotations or pixel-mask training.

Classification uses a confusion matrix and per-class metrics. Detection commonly matches predicted boxes to labeled objects using intersection-over-union, with precision/recall and average precision depending on matching rules and thresholds. Segmentation often measures overlap, such as IoU or Dice, along with class support. Do not compare accuracy, detection AP and segmentation IoU as interchangeable scores.

Larger CNN families offer different design choices: repeated convolutions, residual connections, multi-scale paths or efficient channel/spatial operations. Transfer learning reuses pretrained representations, optionally fine-tuning them on the new task. Check input conventions, model license, data suitability and the evaluation split before adopting a checkpoint. No pretrained weights or architecture benchmark is part of this release.

Assessment: run the CNN, explain all tensor shapes, pass the gradient checks, inspect the learning curves and write a model card. Report that this is one seeded small-image experiment. The earlier dense digits project used the same split; comparing already-visible test scores cannot serve as a fresh architecture-selection protocol. For further comparisons, select using validation data and reserve new independent evaluation.

Next specialization: detection/segmentation or sequence/NLP models when requested. This introductory module does not claim to complete the whole computer-vision field.

[Questions](../../assignments/CV-004/questions.md) · [Solutions](../../assignments/CV-004/solutions.md) · [CNN project](../../projects/intermediate/digits-cnn/README.md) · [Module index](README.md)
