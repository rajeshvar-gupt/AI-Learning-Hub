# Introductory hub release report · 27 October 2026

The remaining local instructional path is published on main: 18 new lessons, separate assignments/solutions, eight project guides, capstones and repair labs. Transformer PR #12 was merged before this batch. New material was published through [PR #13](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/13), merged at commit `200995685bf98360117f8a76eb4226cc657aca1a`. [Task-by-task evidence](ROADMAP-STATUS.md) preserves all 90 IDs.

## What runs locally

Mockable Gemini REST requests with schema/retry/error checks; four-document TF-IDF retrieval with real citations and lexical abstention; a supplied-plan tool runner; an idempotent SQLite dry-run queue; a course-mentor capstone; Iris train/save/reload and real localhost HTTP tests; synthetic image transforms/edges; all-page PDF extraction; a same-domain frozen-feature transfer experiment; checkpoint reload and notebook code cells. [Exact validation](VALIDATION-REMAINING.md).

The runner is deterministic orchestration, not an autonomous LLM planner. RAG defaults to extraction; its generated-answer hook is tested with fixtures, not a live model. Four hand-authored diagnostic questions are not an independent representative benchmark.

## Explicitly outstanding checks

| Check | Why still outstanding | Concrete next action |
|---|---|---|
| Live Gemini/weather access and quality | No live request made; credentials/model/account permission and current terms belong to the operator | Configure authorized environment values, run the opt-in command and record observed outcomes/costs |
| Weather key rotation (D004) | Account-owner security action cannot be demonstrated by a mock | Owner rotates/revokes the historically exposed credential; never paste it into this repo |
| Docker build/start (D081) | Docker executable is absent in the validation environment | Run the documented build/start/health/predict checks on an authorized Docker host |
| Independent RAG evaluation (D070) | Only tiny controlled diagnostics are included | Freeze settings; label representative untouched questions and score retrieval/support/abstention |
| Legacy face runtime | Only public README and requirements were inspected | Choose a permitted model/data fixture, isolate/update dependencies and validate inference separately |
| Public deployment/production operation | No service/paid resources were created | Decide an appropriate serving/security/cost plan before deploying; no live URL is claimed |

## Face-project audit

Read the external project's public README and requirements.txt on 2026-10-27. README describes MTCNN/ArcFace. Pins include TensorFlow 1.14.0, Keras 2.1.3, MXNet 1.5.1.post0, dlib 19.19.0 and NumPy 1.18.1. These differ substantially from the current Python 3.12/NumPy 2.3.5 teaching environment. Installation/inference was not attempted, so compatibility is unverified rather than reported as a tested failure. No faces or weights were redistributed.

Old weather/resume/face code and data were not modified. New hub replacements have bounded, tested contracts; they do not establish quality of old applications. Private content, camera identities and third-party assets remain excluded.

## Review priorities

Check generated-answer faithfulness with real evidence before a live RAG claim; test deployment security beyond the localhost educational HTTP server; verify concurrent queue semantics before multiple workers; retain compatible artifact/preprocessing versions for rollback. An installation recipe, model score or health response alone is not a production-ready badge.

## Hosted CI evidence

[The hosted Linux/Python 3.12 run](https://github.com/rajeshvar-gupt/AI-Learning-Hub/actions/runs/40418645281) installed requirements-labs.txt successfully and passed scripts/run_checks.py (111 tests, 85 registry entries and the file-link validator). This adds fresh-install evidence; Docker, live providers, cross-platform operation and public deployment remain unverified.
