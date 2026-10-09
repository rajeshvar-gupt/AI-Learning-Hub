# PY-007 · Classes and objects

Prerequisites: [functions](04-functions-and-score-summary.md) and [collections](06-collections-in-depth.md).
Audience: beginners who can write functions and use lists and dictionaries.
Outcome: define a class, create independent instances, use attributes and methods, and explain why state belongs to each object.

## Design before implementation

A learner record needs an ID, a list of scores, and operations to add a valid score and calculate a mean. A dictionary plus functions could do this. Here a class groups the related state and behavior under one interface.

Use simple functions for independent calculations. Use a class when several operations naturally act on the same state. Classes are not automatically better, faster or more secure than dictionaries.

Our design:

| Part | Choice | Reason |
|---|---|---|
| Learner ID | Nonempty text | Identifies the example record |
| Scores | Separate list per instance | Learners must not share marks |
| add_score | Validate, then append | A rejected mark must not alter state |
| average | Number or None | Distinguish missing scores from zero |
| scores | Return a copy | Avoid accidental mutation through the returned list |
| summary | Return formatted text | Let the caller decide when to print |

No inheritance is needed for this first class.

## A small class first

```python
class Learner:
    def __init__(self, learner_id):
        self.learner_id = learner_id

    def greeting(self):
        return f"Hello, {self.learner_id}"

learner = Learner("L01")
print(learner.learner_id)
print(learner.greeting())
```

Output:

```text
L01
Hello, L01
```

class defines a new type. Learner("L01") creates an instance and initializes it through __init__. Strictly, __init__ initializes an already created instance; object creation itself involves __new__, which is outside this unit.

self is the conventional name for the instance received by an instance method. It is written explicitly in the definition; Python supplies it when calling learner.greeting(). You do not pass learner again.

learner_id alone is the parameter local to __init__. self.learner_id is an attribute stored on the instance, accessible after initialization. Dot notation accesses attributes and methods. A method is a function defined on the class that can work with the instance.

## Build the learner record

Open [learner_record.py](../examples/learner_record.py). Read these parts before running:

1. __init__ rejects an invalid ID, trims surrounding whitespace and creates self._scores = []. That statement executes separately for each new object.
2. add_score requires an actual int from 0 to 100. The exact type check also rejects True/False, because bool is a subclass of int. Validation occurs before append.
3. scores returns a shallow copy. The elements here are immutable integers, so a new outer list is enough to prevent list edits from changing the stored list.
4. average returns None for no scores. Otherwise it returns sum divided by count.
5. summary checks `mean is None`. A test such as `if not mean` would wrongly treat a valid average of zero as missing.
6. main creates two records, changes each independently and demonstrates that editing a returned list does not change stored scores.

The leading underscore in _scores signals an internal detail by convention. It is not enforced privacy or a security boundary: callers can still access it. Likewise, the public learner_id can be reassigned directly; initialization validation does not prevent later direct assignments. Use the documented methods for this teaching example.

## Run and inspect

From repository root:

```bash
python3 subjects/python/examples/learner_record.py
```

Use py instead of python3 on Windows if that is your launcher. No packages or keys are needed.

Expected output:

```text
L01: 2 scores, average 80.00
L02: no scores
L02: 1 scores, average 0.00
Stored scores: [70, 90]
```

The two objects do not share scores. The first object's returned list is edited, yet its stored scores remain unchanged. All learner IDs are fictional. The example holds records in memory; it does not connect to the existing file-storage project or save them automatically.

## Instance attributes versus class attributes

A class attribute is defined directly in the class body and is found through the class. It can be useful for a shared constant. Mutable per-learner state should be initialized on self instead.

```python
class WrongRecord:
    scores = []

a = WrongRecord()
b = WrongRecord()
a.scores.append(70)
print(b.scores)
```

Output: [70]. Both attribute lookups reach the same class-level list. This is deliberately incorrect for per-learner marks. Move initialization into __init__ with self.scores = [] to give each instance its own list.

Also avoid a mutable default such as scores=[] in a method signature: that default object is created once and reused between calls. Our constructor creates a fresh list every time.

Assigning alias = first creates another reference to the same object, not a new record. Calling LearnerRecord("L01") again creates a separate object even if the ID text is the same; this example does not enforce unique IDs across instances.

## Errors and checks

Invalid IDs or scores raise ValueError. The fixed demo uses valid values; callers accepting external input should catch the expected error, as in earlier lessons. Empty records return None from average and a useful message from summary.

Run:

```bash
python3 -m unittest discover -s subjects/python/examples -p 'test_learner_record.py' -v
```

[Tests](../examples/test_learner_record.py) cover invalid input, zero, empty records, independent state, copied lists, rounding, import behavior and the demo's exact output.

## Practice and next step

Complete [eight exercises](../../../assignments/PY-007/questions.md) before reading [solutions](../../../assignments/PY-007/solutions.md). [Revision sheet](../../../notes/cheat-sheets/python-classes.md).

Next planned unit: Python environments, dependencies and reproducible project setup. [Python home](../README.md)
