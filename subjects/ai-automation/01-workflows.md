# AUTO-001 · Webhooks, schedules and idempotency

Prerequisites: PY-010. Status: published.

Outcome: reason about repeated events and choose an idempotency key.

A deterministic workflow transforms an event through predefined stages. An AI step may be one stage; adding a model does not remove retry and state-management needs. Webhooks can be duplicated or arrive out of order. Verify authentication/signatures in a live receiver and validate its payload before accepting work.

The local queue uses a unique key for one logical job, a timezone-aware due time and a JSON payload. Reusing the same key with identical content returns false instead of adding another job. Reusing it with different content raises an error rather than silently overwriting.

SQLite is adequate for this single-process demonstration. Concurrent production workers need a deliberate claim/lease and transaction design. The example does not expose a public webhook and does not claim exactly-once external delivery.

[Questions](../../assignments/AUTO-001/questions.md) · [Solutions](../../assignments/AUTO-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
