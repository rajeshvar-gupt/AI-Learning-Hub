# AGIC-002 · Human approval and auditable traces

Prerequisites: AGIC-001. Status: published.

Outcome: locate approval boundaries and avoid confusing a draft with delivery.

The propose_message tool returns awaiting_human_approval and sent false. There is no send tool in the runner, even when retrieved content demands delivery. This separation makes the teaching example's side-effect boundary explicit.

In a real system, approval must bind to concrete reviewed content, recipient, action and expiry. If any material detail changes, the approval may no longer apply. An audit log should record identifiers, policy versions and outcomes while minimizing sensitive payloads.

Trace retention needs access control and deletion rules. Hashing a payload can reduce exposed text but does not anonymize low-entropy personal information by itself. The queue's hash is a local diagnostic, not a privacy certification.

Task: inspect the capstone trace and mark every point where a real recipient-facing action would require additional authorization and reconciliation.

[Questions](../../assignments/AGIC-002/questions.md) · [Solutions](../../assignments/AGIC-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
