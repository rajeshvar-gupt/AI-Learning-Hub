# AI engineering revision

| Topic | Check |
|---|---|
| Prompts | Task, evidence, constraints and output contract |
| Structured output | Schema validation plus semantic/source review |
| Retries | Bounded attempts, classified failures and time budgets |
| RAG | Source/version IDs, access filtering, retrieval and answer rubrics |
| Tool execution | Allowlist, arguments, budget, trace and stopping |
| Approval | Bind to concrete content/target; draft is not delivery |
| Idempotency | Stable logical-event key; conflicting reuse is an error |
| Schedule | Aware timestamps, UTC normalization, recurrence policy |
| API | Feature order/units, schema, strict values and body limits |
| Artifacts | Trusted provenance and matched preprocessing; avoid arbitrary pickle |
| Operations | Health versus quality; monitor drift and rollback a compatible bundle |
| Containers/CI | Configuration is not an observed build or hosted test result |

Gradient debugging: repeated factors .5 across 20 steps give .5^20≈9.54e-7; factors 2 give 2^20=1,048,576. Inspect gradient norms, initialization, learning rate and numerical stability. Clipping can bound exploding gradients but does not supply missing long-range signal. The scalar dual-number demo differentiates automatically by local sum/product rules; it is forward mode, not a tensor autograd framework.

OpenCV transition note: OpenCV is not installed here. Many image loaders use RGB while common OpenCV color operations expect BGR; document dtype/range/channel conventions before translating the tested Pillow lab. No OpenCV runtime is claimed.

[Learning path](../../FINAL-PATH.md)
