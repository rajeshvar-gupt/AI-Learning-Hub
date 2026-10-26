# Remaining-check follow-up · 27 October 2026

## Completed on hosted CI

[Observed successful run](https://github.com/rajeshvar-gupt/AI-Learning-Hub/actions/runs/40422756171) on source commit `78cec380df3400767e3b472322fae7e8f95e71c1` passed the existing suites plus two new evaluation-contract tests: **113 tests total**. The Docker job also passed. This follow-up is prepared for review; it does not yet claim publication on main.

### Container build and execution (D081)

GitHub's Ubuntu runner built the actual Dockerfile, trained the model in the image, started a non-root learner process with a read-only filesystem, dropped Linux capabilities and enabled no-new-privileges. A valid localhost prediction returned setosa; invalid payloads returned 422. The script executed the image's configured healthcheck successfully. It stopped only the exact container it created; no broad prune was used.

Local Docker remains unavailable, but that no longer blocks the observed hosted container validation. This is container evidence, not a public deployment, production-server certification or cross-platform guarantee.

### External-label retrieval evaluation (D070)

SQuAD 1.1 development labels were authored externally. Before observing scores, the protocol was fixed to the first 20 articles, first two paragraphs per article and first two questions per paragraph, yielding 40 passages, 323 chunks and 80 questions. No parameters or sampling were changed after the first result.

| Metric | Result |
|---|---|
| Labeled-document recall@1 | .8750 |
| Labeled-document recall@2 | .9250 |
| Labeled-document recall@5 | .9875 |
| MRR@5 (first relevant chunk) | .91875 |
| Keyword-overlap document recall@2 | .8125 |
| Gold-answer span available in a top-two chunk | .7250 |

The ranking unit is a chunk; document hit means a retrieved chunk belongs to the labeled passage. The gold-span metric checks availability only, not that the system generated a correct answer. Results are not official SQuAD EM/F1. SQuAD 1.1 answerable questions do not independently test abstention; the existing invented unsupported-query case remains a separate diagnostic.

The immutable upstream commit/blob and downloaded bytes are integrity checked. The raw dataset is cached only in ignored outputs/, not redistributed in git. [Summary and provenance](validation/external-rag-summary.json) · [Protocol and attribution](validation/EXTERNAL-RAG.md).

## Still requiring external authority or representative inputs

- GEMINI_API_KEY, GEMINI_MODEL and OPENWEATHER_API_KEY were not configured in the available runtime (presence checked only; no secret values printed). No live provider call or account-specific quality/cost claim was made.
- Weather-key rotation requires the provider account owner; repository changes cannot prove revocation.
- SQuAD provides an independent general-English retrieval check, not representative private course-policy Q&A, live answer faithfulness or real unsupported questions. Those need approved domain documents/questions and scoring.
- Legacy face inference remains unverified: no permitted model/data fixture was supplied, and untrusted biometric pickle/H5 artifacts were not loaded or copied.
- A public API deployment requires an appropriate serving/security/cost plan. The current standard-library API remains an educational service; no public URL or cloud resources were created.
