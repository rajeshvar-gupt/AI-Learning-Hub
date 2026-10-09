# Validation · Python through core ML

Executed 2026-10-09 on Linux, Python 3.12.14. Packages: NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0, scikit-learn 1.8.0, matplotlib 3.10.8. The already-installed environment was used; a clean dependency installation was not tested.

## Commands and outcomes

All five script commands in [THROUGH-ML.md](THROUGH-ML.md) exited successfully. The sales notebook's code cell was executed as Python from the repository root; the Jupyter frontend was not tested. Both generated PNG charts were visually inspected for legible labels and unclipped content.

| Check | Result |
|---|---|
| New offline lab tests | 17 passed |
| Existing score-summary and file tests | 19 passed |
| Existing learner-record and HTTP/JSON tests | 14 passed |
| Total automated tests | 50 passed |
| Documented Python lesson blocks | Executed successfully |
| Internal file links and registry paths | Validated against branch files plus the base repository tree |
| Registry IDs and prerequisites | Unique IDs; prerequisite references resolve |

Test commands, from the repository root:

```bash
python -m unittest discover -s tests -p 'test_through_ml.py' -v
python -m unittest discover -s projects/beginner/student-score-summary -p 'test_*.py' -v
python -m unittest discover -s subjects/python/examples -p 'test_*.py' -v
```

## Observed results

| Lab | Actual result in this environment |
|---|---|
| Gradient descent | w = 2.9999999994; loss fell from 9 to about 3.735e-19 |
| Statistics | Mean 10.75; sample SD 1.6690; SE .5901; 95% mean interval [9.3546, 12.1454]; two-sided p=.2443 against mean 10 |
| Sales | 8 input rows; 1 duplicate and 2 invalid orders removed; 5 retained; revenue 190 (books 100, courses 90); SQL and pandas agree |
| Regression | Ridge alpha=1 selected; CV MAE 9.269; holdout MAE 9.419, RMSE 12.252, R² .98824; baseline holdout MAE 94.540 |
| Classification | Gaussian Naive Bayes selected; CV macro-F1 .97309; holdout macro-F1 .92296, accuracy .92105; baseline macro-F1 .16 |
| Clustering | Three clusters of 80; silhouette .78031; two PCA components retain about .96743 of sample variance |
| Book retrieval | Python query ranks data, ML, SQL; no self-match; garden query has no positive-similarity results |

The [full supervised example report](projects/intermediate/supervised-ml/example-report.json) preserves candidate scores, parameters, environment and confusion matrices. The CV difference between Naive Bayes and kNN is tiny (.97309 versus .97301); deterministic maximum selection does not establish that one is reliably superior. Fold variation is recorded, not presented as a confidence interval.

No candidate or parameter was changed after inspecting the final holdout. Repeating the fixed code for automated verification does not constitute a new independent statistical evaluation. The 38-row Iris holdout is small; toy-data results do not establish production performance. Clustering is descriptive and the recommender has no relevance benchmark. Historical external projects, Windows/macOS execution, a clean install and later deep-learning modules were not validated.
