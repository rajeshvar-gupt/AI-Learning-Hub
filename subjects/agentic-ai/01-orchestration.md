# AGIC-001 · Plan–execute–review orchestration

Prerequisites: AGT-002. Status: prepared for review.

Outcome: explain state transitions and distinguish a supplied workflow from autonomous agency.

The local runner follows a supplied list: validate, execute an allowed tool, review the result and stop or continue within budget. This is a bounded orchestration example. An autonomous planner would add model-generated action selection and replanning; neither is claimed by this release.

Break a complex goal into observable steps with explicit inputs and termination criteria. Keep the review stage able to reject unsupported answers or request a person. Do not treat a second model's approval as a guarantee of correctness.

The course-mentor capstone illustrates composition with retrieval and a dry-run schedule. Multiple named roles can be useful for teaching responsibilities, but separate “agents” are not automatically more capable or safer than a single well-scoped workflow. Measure any added complexity against a simpler baseline.

[Questions](../../assignments/AGIC-001/questions.md) · [Solutions](../../assignments/AGIC-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
