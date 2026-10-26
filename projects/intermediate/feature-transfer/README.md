# Frozen convolution feature transfer

Status: published. Prerequisite: CV-003.

Train source kernels only on digits 0–4, freeze them and fit a new head on digits 5–9. Compare raw pixels on the same target split. This is same-domain label transfer, not a pretrained ImageNet benchmark.

## Setup and run

From the repository root, create/activate a Python 3.12 environment and install requirements-labs.txt. Then:

```bash
OPENBLAS_NUM_THREADS=1 python -m ai_hub.transfer
python -m unittest discover -s tests -p 'test_remaining_labs.py' -v
```

Implementation: [ai_hub/transfer.py](../../../ai_hub/transfer.py). Module invocation from the root ensures imports work. Standard demos write JSON under the ignored root outputs/ directory; rerunning overwrites that demo's own output. The repair test suite uses temporary synthetic PDF/image fixtures. The transfer lab also writes an NPZ checkpoint loaded with allow_pickle=False. Generated data and credentials are excluded from git.

## Review

1. Explain inputs, states, outputs and one failure case.
2. Run a supplied invalid-input or repeated-event case.
3. Write a [model/analysis card](../../templates/model-card.md) using actual outputs; distinguish mock, simulation and live behavior.
4. Propose one next experiment and the independent evidence it would require.

[Run guide](../../../FINAL-PATH.md) · [Validation](../../../VALIDATION-REMAINING.md) · [Deployment guide](../../../DEPLOYMENT.md).
