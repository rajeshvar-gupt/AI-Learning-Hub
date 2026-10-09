# Python classes · Revision

| Concept | Example | Meaning |
|---|---|---|
| Class | class LearnerRecord: | Defines a type |
| Instance | record = LearnerRecord("L01") | Creates and initializes an object |
| Initialization | def __init__(self, learner_id): | Sets initial state |
| Attribute | self.learner_id | Data attached to this instance |
| Method | record.add_score(70) | Calls behavior with record supplied as self |
| Per-instance mutable state | self._scores = [] in __init__ | Fresh list for each record |
| Missing result | None | Distinct from numeric zero |
| Internal naming convention | _scores | Not enforced privacy |
| Alias | other = record | Same object, not a copy |

Validate before mutation. Return calculated values; let callers print. A copied list protects its outer structure; nested mutable values may still be shared. Use functions when no object state is needed.

[Lesson](../../subjects/python/01-fundamentals/07-classes-and-objects.md) · [Practice](../../assignments/PY-007/questions.md)
