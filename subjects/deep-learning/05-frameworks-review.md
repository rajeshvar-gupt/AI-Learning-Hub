# DL-005 · Framework transition and deep-learning assessment

Prerequisite: DL-004.

The NumPy project exposes the operations that frameworks automate. In PyTorch, nn.Linear stores dense weights and biases, autograd computes gradients, and an optimizer updates parameters. A typical training step clears gradients, computes logits and loss, calls backward(), then steps the optimizer. CrossEntropyLoss expects logits for integer class targets; do not apply a separate softmax first in that setup.

During validation, model.eval() changes behavior of modules such as dropout and batch normalization. A no-gradient context avoids recording backward graphs; it is a separate concern from evaluation mode. This release contains a mapping guide, not an executed PyTorch program. PyTorch is unavailable in the validation environment, and no GPU result is claimed.

Convolutions share local kernels across spatial positions; sequence models reuse or attend over positions; transformers use attention to combine representations. These architecture families introduce different assumptions and compute costs. They remain subsequent specialized modules rather than being implied by this dense-network project.

Assessment: run the digits project, explain the gradient check, write a model card, inspect the saved curves and propose one validation-only change. Distinguish the executed two-hidden-layer model from the framework and architecture topics described here. Outcome: explain every step from input batch to frozen test report and identify the next specialization.

[Project](../../projects/intermediate/digits-neural-network/README.md) · [Questions](../../assignments/DL-005/questions.md) · [Solutions](../../assignments/DL-005/solutions.md) · [Module index](README.md)
