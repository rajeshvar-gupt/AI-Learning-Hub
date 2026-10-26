# Iris training and local HTTP API

Status: prepared for review. Prerequisite: OPS-002.

Training-only scaling, saved JSON numeric parameters, reload equivalence and strict input handling. See the deployment guide for localhost serving, container commands and rollback. No public service exists.

## Setup and run

From the repository root, create/activate a Python 3.12 environment and install requirements-labs.txt. Then:

```bash
python -m ai_hub.iris_api train
python -m unittest discover -s tests -p 'test_remaining_labs.py' -v
```

Implementation: [ai_hub/iris_api.py](../../../ai_hub/iris_api.py). Module invocation from the root ensures imports work. Standard demos write JSON under the ignored root outputs/ directory; rerunning overwrites that demo's own output. The repair test suite uses temporary synthetic PDF/image fixtures. The transfer lab also writes an NPZ checkpoint loaded with allow_pickle=False. Generated data and credentials are excluded from git.

## Review

1. Explain inputs, states, outputs and one failure case.
2. Run a supplied invalid-input or repeated-event case.
3. Write a [model/analysis card](../../templates/model-card.md) using actual outputs; distinguish mock, simulation and live behavior.
4. Propose one next experiment and the independent evidence it would require.

[Run guide](../../../FINAL-PATH.md) · [Validation](../../../VALIDATION-REMAINING.md) · [Deployment guide](../../../DEPLOYMENT.md).
