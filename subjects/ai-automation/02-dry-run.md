# AUTO-002 · Timezone-aware scheduling and monitoring

Prerequisites: AUTO-001. Status: prepared for review.

Outcome: simulate due jobs safely and explain monitoring/rollback behavior.

The queue rejects timezone-naive timestamps and normalizes supplied offsets to UTC. The demo uses a fixed clock to make results repeatable. A first dry run marks due jobs simulated; a second run returns no repeat jobs. It never sends notifications or starts a hosted recurring task.

Monitor pending age, failed/simulated counts, duplicate submissions and time conversion errors. A real scheduler also needs a defined policy for daylight-saving changes and missed occurrences. Local civil-time recurrence is more complex than storing one absolute timestamp.

Rollback should preserve event IDs and clarify which side effects already occurred. Restoring a database snapshot alone can make completed deliveries appear pending again. Keep an external effect ledger and verify recovery before replaying work.

[Questions](../../assignments/AUTO-002/questions.md) · [Solutions](../../assignments/AUTO-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
