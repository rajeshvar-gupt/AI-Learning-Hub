# ML-002 · Linear regression and regularization

Prerequisites: ML-001, MATH-002.


Outcome: compare a regression model to a baseline and explain residuals and regularization.

Linear regression predicts `Xw+b`. Ordinary least squares minimizes squared residuals. Squared loss heavily penalizes large errors, so inspect outliers and residual plots. A residual is observed minus predicted; patterns against predictions or features suggest a misspecified relationship, changing variance or missing structure.

Ridge adds an L2 penalty on coefficients; larger alpha favors smaller weights and can stabilize correlated predictors. Lasso uses an L1 penalty and can set some coefficients to zero. Scale features when comparing penalties across differently measured columns. Elastic net mixes the penalties. These mechanisms control complexity but cannot fix leaked targets or unrepresentative data.

MAE is average absolute error; RMSE is the square root of average squared error and emphasizes large misses. R² compares squared error to a test-set mean reference and can be negative. A high score on synthetic linear data is expected when the generator matches the model; it does not show skill on real property prices.

The regression lab compares a dummy mean predictor, scaled Ridge and a random forest using training cross-validation. It emits the winning hyperparameters, CV error and held-out MAE/RMSE/R². Explain why the winner fits the data-generating assumptions before adding more models.


## Practice

[Questions](../../assignments/ML-002/questions.md) · [Solutions](../../assignments/ML-002/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
