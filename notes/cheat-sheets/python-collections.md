# Python collections · Revision

| Need | Choice | Common mistake |
|---|---|---|
| Ordered events, duplicates allowed | list | Treating assignment as copying |
| Fixed positional record | tuple | Forgetting comma in a one-item tuple |
| Lookup by ID or label | dict | Assuming in checks values |
| Unique membership and overlap | set | Depending on iteration order or counts |

- Indexes begin at 0; slices exclude their stop.
- sorted(values) returns a new list; values.sort() changes a list and returns None.
- copy() is shallow; nested objects can remain shared.
- A tuple can reference a mutable list.
- dict.get(key, default) does not insert the key.
- Dictionary keys and set elements must be hashable.
- {} is an empty dict; set() is an empty set.
- Set operators: intersection &, union |, difference -, symmetric difference ^.
- Use a comprehension to build a filtered list instead of deleting during iteration.

[Lesson](../../subjects/python/01-fundamentals/06-collections-in-depth.md) · [Practice](../../assignments/PY-006/questions.md)
