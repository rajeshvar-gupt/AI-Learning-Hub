# CV-003 · Worked solutions

1. One shared kernel parameter contributes at every position, so the chain rule sums its contributions across positions and examples.
2. The backward pass may use weights different from those in the forward computation, producing inconsistent derivatives. Compute all gradients first, then update.
3. Validation loss chooses the saved checkpoint. The untouched test partition reports accuracy, macro-F1 and confusion counts after restoration.

[Questions](questions.md)
