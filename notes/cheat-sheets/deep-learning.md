# Deep learning revision

| Concept | Remember |
|---|---|
| Dense layer | XW+b; parameters shared across batch rows |
| Nonlinearity | Prevents stacked affine layers collapsing into one |
| Stable softmax | Subtract each row maximum before exponentiation |
| Mean cross-entropy gradient | (probabilities − one-hot labels) / batch size |
| Backpropagation | Chain rule computes gradients; optimizer applies updates |
| Epoch / step | One training-data pass / one batch update |
| Validation checkpoint | Copy best weights; restore before frozen test evaluation |
| Gradient check | Central finite differences away from ReLU kinks |
| Overfitting | Training improves while validation deteriorates |
| Framework modes | Evaluation behavior and gradient recording are separate |

Interview practice: derive the parameter count; explain the need for nonlinearities; explain why a random seed is not a reliability guarantee; distinguish loss from accuracy; propose a split for unseen writers. Worked answers are in DL-001–005 assignments.

[Module](../../subjects/deep-learning/README.md)
