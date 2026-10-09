# ML-007 · Reproducibility, error analysis and capstone review

Prerequisites: ML-006.


Outcome: produce a model report someone else can inspect and reproduce.

Record the question, prediction time, data source/license, row count, feature definitions, target, split policy, seed, preprocessing, candidate grid, metric and environment. Preserve the selected parameters and both baseline and final scores. A fixed seed controls some randomness; package versions and platform details may still affect exact floating-point results.

Review errors by relevant slices with enough samples to support interpretation. A good overall score can hide weak performance in an important subgroup. Do not keep revisiting the final test set during development. Use training out-of-fold predictions for iterative analysis; collect a fresh evaluation set if decisions have been guided by the old test results.

Distribution shift means future data differ from training conditions. Plan checks for schema changes, missingness, ranges, target drift and subgroup performance when labels arrive. A model artifact also needs its preprocessing and feature schema. Only load pickle/joblib artifacts from trusted sources because loading can execute code; this course emits JSON reports rather than distributing serialized estimators.

Capstone: run all labs, write a one-page model card using the template, explain a baseline comparison, inspect three failure cases and propose one next experiment without executing test-driven tuning. Completion means you can justify your choices and rerun the project, not merely that files exist.

Scope boundary: this completes an introductory core-ML learning path. Deep learning, NLP specialization, deployment/MLOps and advanced mathematical theory remain later modules. Legacy external projects retain their separate repair status.


## Practice

[Questions](../../assignments/ML-007/questions.md) · [Solutions](../../assignments/ML-007/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
