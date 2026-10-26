# Remaining-release validation · 27 October 2026

Executed on Linux/Python 3.12.14 using already-installed packages: NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0, scikit-learn 1.8.0, matplotlib 3.10.8, Pillow 12.3.0, pypdf 6.10.0 and reportlab 4.4.9. Requirements files record this environment. A clean installation, Docker build, Windows/macOS runtime and live provider access were not tested.

## Combined check

```bash
OPENBLAS_NUM_THREADS=1 python scripts/run_checks.py
```

| Check | Observed result |
|---|---|
| Central tests (new and prior ML/DL/CV/NLP/TR) | 78 passed |
| Existing score-summary/files suites | 19 passed |
| Existing learner-record/HTTP-JSON suites | 14 passed |
| Total | 111 passed |
| Ecosystem Markdown targets | 1,049 checked; no missing file targets |
| Registry | 85 entries; unique IDs and resolved prerequisites/paths |

The 27 new checks comprise 26 application/repair tests plus one scalar autodiff test. Coverage includes transient-provider retry limits, authentication failure, missing config, malformed/blocked output, citation validation, mocked generation hook, chunking, lexical abstention, forbidden/over-budget tools, failed-tool stopping, external-text scope, approval-awaiting drafts, persistent queue replay, conflicting keys/timezones, synthetic multipage/empty PDF extraction, mocked weather errors, synthetic images, Iris reload and real localhost HTTP routes/invalid inputs/body limits.

No new code was changed after the combined test pass; this finalization adds reports and links only. The link/registry validator is rerun after final documentation changes. [Machine-readable examples](validation/remaining-examples.json).

## Executed examples

All commands in FINAL-PATH.md ran successfully, including the six offline demo cases, scalar autodiff, Iris training and source-feature transfer. The two new notebook code cells also ran successfully as Python subprocesses; no Jupyter frontend was tested. The modified dense-digit script ran and verified NPZ checkpoint reload equality. The synthetic edge image and quadratic-loss chart were visually inspected.

| Example | Actual outcome |
|---|---|
| Mock assistant | Schema-valid fixture response; no live model-quality score |
| Retrieval | TF-IDF recall@2=1 and keyword-overlap recall@2=1 on four diagnostic questions; no improvement claimed |
| Unsupported query | Abstained with no citation |
| Tool runner | Two read-only planned steps completed; explicit failure/adversarial fixtures passed |
| Mentor capstone | Cited Python passage, reviewed draft awaiting approval, one simulated reminder; sent=false |
| Queue replay | One first simulation, empty repeat |
| Iris | 38 held-out examples; accuracy .92105, macro-F1 .92296; majority baseline accuracy .31579 |
| Feature transfer | 540 source training rows, 537 target training rows, 180 target test rows; frozen-feature and raw-pixel accuracies both .98333 |
| Dense checkpoint | Reloaded logits matched; previous held-out accuracy .95 reproduced |
| Scalar autodiff | (x-3)^2 at x=2: loss 1, derivative -2 |
| Images/PDF | Original synthetic rectangle transforms and generated two-page/empty PDF cases passed |

The tiny document diagnostic is not an independent held-out RAG benchmark. Generated citation IDs do not prove semantic support. Iris/digit splits were already used by earlier teaching projects; these reruns are reproducibility evidence, not new independent evaluations. Transfer was not tuned after viewing test results and did not outperform its baseline. Models are not deployment-certified.

## Outstanding validation

Docker is absent. Container build/start/health checks remain outstanding. Live Gemini/weather calls, account-specific access/costs, owner weather-key rotation, independent representative RAG quality and legacy face inference remain unverified. CI configuration is included; a file is not a hosted workflow pass. No public endpoint or actual recurring automation was deployed. [Exact release boundaries](RELEASE-REPORT.md).
