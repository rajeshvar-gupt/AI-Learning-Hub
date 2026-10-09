# PY-007 · Solutions

Try the [questions](questions.md) first.

1. LearnerRecord is the class. Each call creates an instance. learner_id and _scores hold that instance's data. add_score and average are methods that operate on the instance.
2. Python supplies the instance as self for record.add_score(70); 70 is bound to score.
3. The first summary is “L01: 2 scores, average 70.00”; the untouched second is “L02: no scores”, assuming IDs L01 and L02.
4. Empty means average() returns None. One zero produces 0.0 and a count of one. Both None and 0.0 are false in a boolean condition, but is None distinguishes them.
5. Each input raises ValueError before append. The first two are outside 0–100; the others are not exact integers. True is rejected explicitly through the type check even though bool inherits from int.
6. Editing the returned copy does not alter the record. Directly editing record._scores would alter it: the underscore is a convention, not enforced access control.
7. A mutable class attribute can be shared across instances. Initialize self._scores = [] inside __init__ so each record gets a new list.
8. Use a function that returns whether the snapshot is nonempty:

```python
def has_scores(record):
    return bool(record.scores())
```

After importing LearnerRecord from the example module:

```python
record = LearnerRecord("L01")
print(has_scores(record))
record.add_score(0)
print(has_scores(record))
```

Output: False, then True. Presence of a score is different from the numeric value of that score. To try this interactively, start Python from subjects/python/examples and run `from learner_record import LearnerRecord` first.

[Lesson](../../subjects/python/01-fundamentals/07-classes-and-objects.md) · [Python home](../../subjects/python/README.md)
