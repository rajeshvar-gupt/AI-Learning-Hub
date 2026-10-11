# CV-001 · Worked solutions

1. (12,8,8) and (12,8,8,3). Some frameworks require an explicit grayscale channel axis.
2. The features are assigned to different channels than the model saw during training. Numeric values alone do not identify their meaning.
3. Keep all frames from a video in one partition and use separate validation videos for selection. Consider capture location and time if those define intended generalization.

[Questions](questions.md)
