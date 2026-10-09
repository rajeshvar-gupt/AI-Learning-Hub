# Complete learning path through core machine learning

Status: published on main through [PR #8](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/8), merged 2026-10-09. This release supplies the remaining instructional path through introductory core ML. Learner completion is demonstrated by solving the exercises and explaining results; creating these materials does not mark your personal mastery complete.

## Study sequence

| Stage | Units | Demonstrate readiness |
|---|---|---|
| Existing Python | [PY-001–010](subjects/python/README.md) | Run and explain the existing examples and score project |
| Python consolidation | [PY-011](subjects/python/03-review.md) | Validate inputs, separate I/O, debug and test |
| Mathematics | [MATH-001–003](subjects/mathematics/README.md) | Shapes, dot products, derivatives, Bayes |
| Statistics | [STAT-001–002](subjects/statistics/README.md) | SD/SE, sampling, intervals and test interpretation |
| Data analysis | [DATA-001–003](subjects/data-analysis/README.md) | NumPy, cleaning, joins, SQLite, charts |
| Core ML | [ML-001–007](subjects/machine-learning/README.md) | Splits, baselines, regression, classification, model families, clustering, PCA, retrieval and review |

Each new lesson has questions and separate worked solutions. Work through them before checking answers. Use the [revision and interview sheet](notes/cheat-sheets/through-ml.md) after each stage.

## Environment

Tested with Python 3.12.14 on Linux. From the repository root:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell alternative: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-ml.txt
```

The pinned packages describe the environment used for execution. A clean internet-based installation and Windows/macOS execution were not verified here. Installation may need internet access and suitable wheels; the labs themselves are offline and use no secrets. Jupyter is optional and is not part of the required environment; the sales script is the primary runnable entry point.

## Run the five labs

```bash
python projects/intermediate/foundations-lab/foundations.py
python projects/intermediate/sales-analysis/sales.py
python projects/intermediate/supervised-ml/train.py
python projects/intermediate/unsupervised-ml/explore.py
python projects/intermediate/book-recommender/recommend.py
python -m unittest discover -s tests -p 'test_through_ml.py' -v
```

[Foundations lab](projects/intermediate/foundations-lab/README.md) · [Sales lab](projects/intermediate/sales-analysis/README.md) · [Supervised lab](projects/intermediate/supervised-ml/README.md) · [Unsupervised lab](projects/intermediate/unsupervised-ml/README.md) · [Book retrieval](projects/intermediate/book-recommender/README.md).

The sales and clustering labs write charts; the sales and supervised labs also write tables/reports. Generated files stay in each project's ignored `outputs/` folder. The [sales notebook](projects/intermediate/sales-analysis/sales.ipynb) wraps the same script without stored outputs.

## Completion assessment

1. Explain one worked example from every lesson without reading the solution.
2. Run each lab, retain its actual outputs and explain their limits.
3. Pass the code checks and describe what they do not prove.
4. Complete the ML-007 three-level assignment and [model card](projects/templates/model-card.md).
5. Review [validation evidence](VALIDATION-ML.md) and [primary sources](resources/through-ml-sources.md).

This release ends at core ML. Deep learning, specialized NLP/computer vision, deployment and MLOps remain planned. Original roadmap dates and legacy repository repair statuses are unchanged. All material stays inside this one AI-Learning-Hub repository.
