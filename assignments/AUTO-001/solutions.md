# AUTO-001 · Worked solutions

1. A combination such as course ID, learner ID and reminder occurrence, suitably protected from disclosure.
2. It prevents duplicate detection because each retry appears new.
3. The database can reject duplicate job keys, while an external send may succeed before a local acknowledgment. Delivery needs reconciliation or provider-supported idempotency.

[Questions](questions.md)
