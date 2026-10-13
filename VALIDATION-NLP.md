# NLP validation

Executed 2026-10-13 on Linux with Python 3.12.14, NumPy 2.3.5 and scikit-learn 1.8.0, using the existing requirements-ml.txt environment. No clean dependency installation, Windows/macOS execution, GPU or external language-model access was tested.

## Commands

From the repository root:

```bash
python projects/intermediate/support-text-classifier/train.py
python projects/intermediate/attention-lab/attention.py
python -m unittest discover -s tests -p 'test_nlp.py' -v
```

Both scripts completed successfully. All eleven new tests passed: fixture partition uniqueness, test-only vocabulary exclusion, no refitting during prediction, unknown-feature review routing, invalid text/label checks, prediction contract, uniform attention, causal masking, shift invariance and invalid matrix/mask handling. Internal Markdown targets and curriculum prerequisites were validated against new files plus the base tree.

## Measured results

| Item | Actual result |
|---|---|
| Text fixture | 36 training / 12 test messages, three classes |
| Training CV | Three folds, four configurations |
| Selected parameters | Word unigrams, logistic-regression C=2 |
| Training vocabulary | 113 features |
| Majority baseline test accuracy / macro-F1 | .33333 / .16667 |
| Selected test accuracy / macro-F1 | .91667 / .91534 |
| Test errors | One: “Has my refund been issued” classified as access instead of billing |
| Unknown-word route | needs_review, zero known features |
| Attention matching-key weight | .66976155, other-key weight .33023845 |
| First causal weights / output | [1,0] / [2,0] |

The [full classifier report](projects/intermediate/support-text-classifier/example-report.json) records fold scores/variation, class support, confusion counts and all test predictions. No parameters or fixture examples were changed after observing test outcomes. The error is reported for transparency, not followed by test-guided tuning.

The test set is twelve invented messages with four per class. Its score is not a population estimate or evidence of real support-service readiness. Unknown-feature routing only catches all-zero vectors; a message with familiar words can still have an unseen intent. The attention lab uses supplied arrays and no trained projections or model weights.

Existing ML, deep-learning and computer-vision source was unchanged and not retested in this extension. Previously recorded results remain in their separate validation files. Historical resume extraction/setup and advanced architecture work were not repaired or validated here.
