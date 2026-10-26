# OPS-001 · CI, containers and reproducible releases

Prerequisites: API-002. Status: prepared for review.

Outcome: package repeatable checks and distinguish local evidence from hosted CI.

scripts/run_checks.py executes the behavioral suites and link/registry validator. The GitHub Actions workflow runs that command on Python 3.12 after installing requirements-labs.txt. Its definition is provided; hosted execution must be inspected after the branch exists.

The Dockerfile installs dependencies, copies the application, trains a small local Iris model and runs inference as a non-root user. A health check calls /health. The base image tag and dependency artifacts can change, so a stricter release can pin an image digest and verify supply-chain inputs.

Local tests do not imply a successful Docker build. Docker is absent in this environment, and a clean online installation was not performed. The release report states these limits. CI and container status should be updated only from observed run/build evidence.

[Questions](../../assignments/OPS-001/questions.md) · [Solutions](../../assignments/OPS-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
