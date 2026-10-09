# Revision sheet · Python through core ML

| Topic | Recall | Common mistake |
|---|---|---|
| Python | Pure functions, explicit validation, context managers, main guard | Swallowing every exception |
| Shapes | `(n,p) @ (p,) -> (n,)` | Confusing `*` and `@` |
| Gradient | `w -= rate * gradient` | Assuming any rate converges |
| Bayes | `P(A|B)=P(B|A)P(A)/P(B)` | Reversing conditional probability |
| Sample variance | Squared deviations divided by n-1 | Mixing population and sample conventions |
| SD / SE | Observation spread / mean uncertainty | Claiming a larger sample shrinks population SD |
| Confidence interval | Repeated-sampling coverage | Treating it as the range containing 95% of observations |
| p-value | Tail probability under null and assumptions | Probability that the null is true |
| pandas joins | Check key uniqueness and row counts | Multiplying revenue with duplicate dimension keys |
| SQL | WHERE rows, HAVING groups; `IS NULL` | Comparing NULL with `= NULL` |
| Regression | MAE in target units, RMSE sensitive to large errors | Comparing errors across different target units |
| Classification | Precision, recall, macro-F1, confusion matrix | Accuracy alone on imbalanced data |
| CV | Fit learned transforms inside every training fold | Scaling the complete data before CV |
| Regularization | Restrict model flexibility; tune on training folds | Selecting alpha with the final test set |
| Trees / forests | Nonlinear splits / averaging randomized trees | Reading feature importance as causality |
| PCA / clusters | Variance projection / exploratory groups | Calling a silhouette score accuracy |
| Retrieval | Similarity ranking with self-exclusion | Claiming personalization without user data |

## Interview prompts

1. What information is available at prediction time?
2. Why must imputation occur inside cross-validation?
3. How do you distinguish high bias from high variance?
4. When would you choose grouped or chronological splits?
5. Why can R² be negative?
6. Why does a probability threshold affect recall?
7. What changes when features are rescaled for kNN versus trees?
8. What does PCA optimize, and what does it ignore?
9. What evidence would establish a recommender's usefulness?
10. What can a seed guarantee, and what can it not guarantee?

Use the corresponding lessons' worked answers and model card to explain these aloud with an example. [Complete learning path](../../THROUGH-ML.md).
