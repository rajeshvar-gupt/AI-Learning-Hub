# MATH-003 · Probability and conditional reasoning

Prerequisites: MATH-001.


Outcome: distinguish joint, conditional and marginal probabilities, and apply Bayes' rule.

Probabilities are between 0 and 1, and exhaustive disjoint outcomes sum to 1. `P(A or B)=P(A)+P(B)-P(A and B)`. Conditional probability is `P(A|B)=P(A and B)/P(B)` for positive P(B). Independence means `P(A and B)=P(A)P(B)`, not that events are mutually exclusive.

Suppose 10% of manufactured items have a defect, a detector flags 80% of defects and flags 20% of good items. Among 1,000 items, expect 80 flagged defects and 180 flagged good items. Of 260 flags, about 30.77% represent defects. Bayes' rule gives the same result: `.8*.1 / (.8*.1 + .2*.9)`. A detector's sensitivity is not the probability that a flagged item is defective.

A Bernoulli variable has outcomes 0/1 and expectation p, variance `p(1-p)`. The count in n independent, constant-probability trials follows a binomial distribution with mean np. Normal distributions describe continuous bell-shaped variation; not every dataset is normal. The sample mean can become approximately normal under suitable conditions without making the original observations normal.

Use a seeded NumPy generator for repeatable simulations. A seed makes a run reproducible; it does not remove sampling uncertainty or prove a probability claim.


## Practice

[Questions](../../assignments/MATH-003/questions.md) · [Solutions](../../assignments/MATH-003/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
