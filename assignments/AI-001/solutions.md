# AI-001 answer guide

1. A deterministic schedule is sufficient: read deadline, subtract two days, enqueue a reminder, record delivery and avoid duplicates. Award one mark for recognizing no learned model is required and one for explaining the rule.
2. Training examples pair message content with spam/non-spam labels. The new message is input; its category is the prediction target. Award one mark for examples/labels and one for input/target.
3. Verify the date against a trustworthy source and check that the source actually supports the statement. Fluency is not factual verification. Award one mark for a verification step and one for the distinction.
4. A follows a fixed workflow; B has dynamic tool-selection/control decisions and is agent-like under this curriculum's working definition. A may still use an LLM. Award one mark for fixed/dynamic control and one for recognizing model use alone does not decide the label.
5. The score measures training fit; it does not establish performance on unseen cases. Use an appropriate held-out evaluation, inspect leakage and compare a baseline. Award one mark for limiting the conclusion and one for a valid next check.

## Mini-project example

Use approved syllabus and course policy documents. Answer prerequisites, assignment format and published office hours. Decline to invent an unpublished exam date or reveal another student's marks. Evaluate using a small teacher-checked question set including missing-answer cases. Any message sent to a student or change to a grade needs separate approval. A good design explains both success and failure behavior.

[Questions](questions.md) · [Home](../../README.md)
