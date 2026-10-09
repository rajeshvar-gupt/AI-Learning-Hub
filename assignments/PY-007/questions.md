# PY-007 · Practice

Prerequisite: [classes and objects](../../subjects/python/01-fundamentals/07-classes-and-objects.md).

1. Explain class, instance, attribute and method using LearnerRecord.
2. Why does add_score define self, score while record.add_score(70) passes only one argument?
3. Create two records. Add 60 and 80 to the first. Predict both summaries.
4. Compare an empty record with one containing 0. Why must summary check is None rather than truthiness?
5. Try -1, 101, 70.5, "70" and True as scores. Explain why the stored list must remain unchanged.
6. Obtain a scores() snapshot and append 100 to it. Does the record change? Would direct access to _scores have the same protection?
7. Explain the bug in placing scores = [] directly in the class body. How do you fix it?
8. Write a separate function has_scores(record) that uses the public scores() method and returns a boolean. Test it before and after adding a score.

[Solutions](solutions.md) · [Example](../../subjects/python/examples/learner_record.py)
