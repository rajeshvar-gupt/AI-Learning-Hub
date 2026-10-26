# API-001 · Inference API contracts and model artifacts

Prerequisites: ML-007. Status: published.

Outcome: serve a consistent prediction contract with explicit validation.

The Iris lab fits preprocessing only on training data, trains logistic regression and saves numeric parameters plus schema metadata in JSON. Reloaded inference implements the same standardized linear scores and softmax. It avoids loading executable pickle artifacts; all artifacts still need a trusted release process and schema validation.

POST /predict accepts an object with samples: one to 100 rows, each containing four positive finite measurements in documented feature order. Booleans, NaN, malformed shapes and excessive body size are rejected. GET /health reports readiness of the loaded local model.

Probabilities are model outputs, not guaranteed calibrated confidence. The tiny bundled botanical dataset supports a learning exercise, not a consequential decision system. The included HTTP server is localhost teaching code, without production authentication, TLS, rate limiting or multi-tenant access control.

[Questions](../../assignments/API-001/questions.md) · [Solutions](../../assignments/API-001/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
