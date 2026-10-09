# DL-002 · Softmax, cross-entropy and backpropagation

Prerequisite: DL-001.

Softmax converts a row of logits z into probabilities exp(z)/sum(exp(z)). Subtract the row maximum before exponentiation: adding a constant to every logit leaves probabilities unchanged, while the subtraction prevents overflow. Compute log probabilities as shifted_logits - log(sum(exp(shifted_logits))) instead of taking log of rounded probabilities.

For one correct class y, cross-entropy is -log(p_y). Uniform probabilities over ten classes yield loss log(10), about 2.303. For a batch mean loss, the derivative with respect to logits is (probabilities - one_hot_targets)/n. Each dense layer then has dW=A_previous.T @ dZ and db=sum(dZ, axis=0). Propagate dA=dZ @ W.T backward, multiplying by the activation derivative at each hidden layer.

Backpropagation computes derivatives using the chain rule; an optimizer uses those derivatives to change parameters. These are separate operations. The lab calculates gradients before changing any weights, avoiding a backward pass through already-updated parameters.

A finite-difference check estimates a derivative with (L(w+epsilon)-L(w-epsilon))/(2*epsilon). Compare every parameter of a tiny smooth-region example with analytical gradients. Avoid points at ReLU kinks; tiny epsilon can cause cancellation and large epsilon can bias the approximation. Outcome: derive the output gradient and pass the numerical gradient test.

[Project](../../projects/intermediate/digits-neural-network/README.md) · [Questions](../../assignments/DL-002/questions.md) · [Solutions](../../assignments/DL-002/solutions.md) · [Module index](README.md)
