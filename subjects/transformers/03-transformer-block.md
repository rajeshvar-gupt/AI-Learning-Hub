# TR-003 · Residual paths, normalization and feed-forward layers

Prerequisite: TR-002.

Outcome: execute a complete forward block and explain each component.

The lab block uses a pre-normalization layout: normalize token rows, apply attention, add the original X, normalize the resulting residual, apply a two-layer ReLU feed-forward function, then add that result to the residual. Normalization placement varies by architecture; this implementation does not reproduce every detail of the original paper.

Layer normalization computes statistics across the feature coordinates of one token. It does not estimate a dataset-wide mean or use the batch axis. The lab uses unit gains, zero offsets and epsilon 1e-5; learned affine normalization parameters are omitted. A constant row becomes zero rather than causing division by zero.

The feed-forward function maps width eight to 16 and back to eight independently at each position. It uses shared parameters across token rows and supplies nonlinear transformation after attention mixes token information. Residual addition requires matching shapes and lets the input contribute directly.

The block has no dropout, optimizer, backward pass, loss head or stack of layers. Its randomly initialized forward output demonstrates mechanics, not language ability. A later trained model requires a task, objective, representative data and an evaluation protocol.

Task deliverable: trace both residual branches, compare normalization axes with batch normalization conceptually, and verify output shape and finiteness. The causal test covers attention plus token-wise normalization/feed-forward paths.

[Questions](../../assignments/TR-003/questions.md) · [Solutions](../../assignments/TR-003/solutions.md) · [Mechanics lab](../../projects/intermediate/transformer-mechanics/README.md) · [Module index](README.md)
