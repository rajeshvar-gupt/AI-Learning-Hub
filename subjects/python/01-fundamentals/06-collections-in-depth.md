# PY-006 · Lists, tuples, dictionaries and sets

Prerequisite: [PY-004: Functions](04-functions-and-score-summary.md). You can follow the normal sequence after [PY-005](05-files-and-score-storage.md); this unit needs no file operations.
Audience: beginners comfortable with loops, conditions and functions.
Outcome: choose a suitable collection, access and update values, explain shared references, and group fictional enrollment records.

## Choose the structure before coding

We need to keep enrollment events, group them by course, and find learners attending both courses. One structure does not answer every question equally well.

| Type | Use in this example | Ordering | Changeable? | Duplicates |
|---|---|---|---|---|
| list | Enrollment events | Positional order | Yes | Retained |
| tuple | A pair: learner ID and course | Positional order | Items cannot be reassigned | Retained |
| dict | Course mapped to learner IDs | Insertion order | Yes | Keys unique; values may repeat |
| set | Unique learner IDs | No guaranteed iteration order | Yes | Equal values collapse |

Dictionaries and sets use hashable keys/elements: strings and integers work, lists do not. A tuple is hashable only when all its elements are hashable. “Hashable” means a value supports a stable hash and compatible equality for use in these structures.

## Lists: indexing, slicing and updates

```python
scores = [70, 80, 70]
print(scores[0], scores[-1])
print(scores[1:])
scores[1] = 85
scores.append(90)
print(scores)
print(sorted(scores))
print(scores)
```

Output:

```text
70 70
[80, 70]
[70, 85, 70, 90]
[70, 70, 85, 90]
[70, 85, 70, 90]
```

Indexes start at zero; -1 selects the last item. A slice such as scores[1:3] includes positions 1 and 2 and excludes stop position 3. An out-of-range single index raises IndexError, while a slice can safely stop at the end.

append adds one object; extend adds items from an iterable. remove(value) removes the first matching value and raises ValueError if absent. pop() removes and returns the final item and fails on an empty list. sorted creates a new list; scores.sort() changes the original list and returns None. Do not assign the result of sort back to scores.

## Assignment is not copying

```python
original = [70, 80]
alias = original
copy = original.copy()
alias.append(90)
copy[0] = 0
print(original)
print(copy)
```

Output: [70, 80, 90] then [0, 80]. alias and original refer to the same list. copy is a new outer list.

A shallow copy still shares nested objects:

```python
rows = [[70], [80]]
other = rows.copy()
other[0].append(90)
print(rows)
```

Output: [[70, 90], [80]]. Copying the outer list does not copy the inner lists. When independent nested state is needed, design explicit copies of the necessary levels; copying is not automatically recursive.

## Tuples: fixed positions and unpacking

```python
enrollment = ("L01", "Python")
learner_id, course = enrollment
print(learner_id, course)
single = ("Python",)
print(len(single))
```

Output: L01 Python, then 1. The comma creates a one-item tuple. ("Python") alone is a string. Unpacking requires matching the number of items unless using starred unpacking.

A tuple prevents replacing its elements, but an element may reference a mutable object: a list inside a tuple can still change. Use pairs for a small fixed record; for many named fields, a dictionary or later a class can be clearer.

## Dictionaries: lookup by meaning

```python
profile = {"id": "L01", "course": "Python"}
profile["course"] = "ML"
print(profile["course"])
print(profile.get("level", "beginner"))
print("course" in profile)
for key, value in profile.items():
    print(key, value)
```

Output: ML, beginner, True, id L01, course ML on separate lines. Direct indexing raises KeyError for a missing key. get returns a default and does not insert the missing key. Membership checks keys, not values; use profile.values() when checking values.

Assigning an existing key replaces its value rather than creating a second key. Insertion order is preserved, but dictionary keys are not sorted automatically. Do not add/delete keys while iterating over that dictionary.

## Sets: membership and comparisons

```python
python_ids = {"L01", "L02", "L01"}
ml_ids = {"L01", "L03"}
print(sorted(python_ids & ml_ids))
print(sorted(python_ids | ml_ids))
print(sorted(python_ids - ml_ids))
print(sorted(python_ids ^ ml_ids))
```

Output:

```text
['L01']
['L01', 'L02', 'L03']
['L02']
['L02', 'L03']
```

& is intersection, | union, - difference, and ^ symmetric difference (in exactly one set). These operators create new sets. add inserts an item. discard removes it if present; remove raises KeyError if absent. An empty set is set(); {} creates an empty dictionary. Sets do not support positional indexing.

Use sorted for predictable display of these string IDs. It returns a list and requires mutually comparable values. Converting a list to a set loses counts and sequence information, so do not replace enrollment events with a set when repeated events matter.

## Comprehensions: build a new collection

```python
scores = [30, 40, 90]
passing = [score for score in scores if score >= 40]
print(passing)
```

Output: [40, 90]. Read this as “take each score, keep it if it meets the condition, and put it in a new list.” This avoids removing items from a list while iterating over it. Prefer a normal loop when several steps make a comprehension difficult to read.

## Runnable enrollment example

From repository root:

```bash
python3 subjects/python/examples/course_collections.py
```

Windows users can use py instead of python3. No packages or keys are needed. [Complete code](../examples/course_collections.py).

The list retains four events. Each tuple is unpacked into learner_id and course. The grouping dictionary holds a separate list for each course. Sets are derived afterward to answer unique-membership questions. get(..., []) gives an empty fallback if a course is absent.

Expected output:

```text
Records: 4
Python: ['L01', 'L02', 'L01']
ML: ['L01']
Unique Python learners: ['L01', 'L02']
Both courses: ['L01']
Python only: ['L02']
```

group_enrollments expects pairs of string IDs/course names; it is a fixed-data teaching helper, not an input-validation service. Empty input returns an empty dictionary. Repeated events remain in the grouped lists. Course names are case-sensitive. All records are fictional.

## Practice and next step

Complete [eight exercises](../../../assignments/PY-006/questions.md), then check [solutions](../../../assignments/PY-006/solutions.md). Use the [revision sheet](../../../notes/cheat-sheets/python-collections.md).

Next: [PY-007: classes and objects](07-classes-and-objects.md). [Python home](../README.md)
