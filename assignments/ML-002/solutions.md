# ML-002 · Worked solutions

1. Errors have magnitudes 1 and 3: MAE=2, RMSE=`sqrt((1+9)/2)=sqrt(5)`, about 2.236.
2. Coefficients shrink strongly, increasing bias and potentially underfitting. The intercept is typically not penalized in this setup. Scaling changes the meaning of coefficient penalties.
3. This uses test labels for model selection and makes the reported estimate optimistic. Tune using training CV and reserve test labels for the final evaluation.

[Questions](questions.md) · [Lesson](../../subjects/machine-learning/02-regression.md)
