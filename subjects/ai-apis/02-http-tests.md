# API-002 · HTTP failure cases and local smoke testing

Prerequisites: API-001. Status: prepared for review.

Outcome: test actual HTTP behavior as well as pure prediction functions.

The tests start a localhost server on an ephemeral port, call /health and /predict, and verify success and invalid-input status codes. Unknown routes return 404; invalid prediction payloads return 422; oversized bodies return 413. Tests shut the server down and remove temporary artifacts.

Unit checks validate model arrays and reload consistency; endpoint checks validate the transport contract. Neither proves public deployment readiness. Slow clients, connection limits, cancellation and TLS termination are outside this small server's scope.

Run training first, then serve locally. The deployment guide includes a container recipe and rollback exercise. Docker is unavailable in the validation environment, so the recipe is explicitly unbuilt. No public URL or cloud service is invented.

[Questions](../../assignments/API-002/questions.md) · [Solutions](../../assignments/API-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
