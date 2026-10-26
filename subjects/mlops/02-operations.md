# OPS-002 · Monitoring, drift and rollback assessment

Prerequisites: OPS-001. Status: prepared for review.

Outcome: separate service health from model quality and prepare a bounded rollback.

A healthy endpoint can return poor predictions. Monitor request failures, latency, input schema/range/missingness and prediction distributions. When reliable labels arrive, track model errors and relevant slices. Distribution changes are signals for investigation, not automatic proof that retraining will help.

Record a model/version identifier with deployment events while avoiding unnecessary personal payload logs. A rollback selects a known-good artifact and compatible preprocessing/schema. Test it using fixed valid/invalid requests and verify health before resuming traffic.

The capstone is validated locally with held-out metrics and real localhost HTTP tests. No cloud hosting, paid resources, production traffic or live monitoring integration was created. The guide gives manual commands for later deployment validation; their unexecuted status remains visible.

[Questions](../../assignments/OPS-002/questions.md) · [Solutions](../../assignments/OPS-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
