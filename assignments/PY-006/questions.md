# PY-006 · Practice

Read [the collections lesson](../../subjects/python/01-fundamentals/06-collections-in-depth.md). Predict results before running code.

1. For values = [10, 20, 30, 40], predict values[-1] and values[1:3]. What happens with values[9]?
2. Explain append([30, 40]) versus extend([30, 40]) on [10, 20].
3. Create a list, an alias and a shallow copy. Change the alias, then the copy. Explain why nested lists require more care.
4. Create a one-item tuple containing Python. Why is ("Python") different? Can a list inside a tuple change?
5. For marks = {"L01": 70}, assign marks["L01"] = 90. How many keys remain? Read a missing L02 with default 0 without adding it.
6. Find the intersection, union and difference of {"L01", "L02"} and {"L02", "L03"}. Explain what information converting enrollment events to a set would lose.
7. Filter [30, 40, 90] into a new list of values at least 40 using a comprehension.
8. Use group_enrollments with [], then [("L01", "Python"), ("L01", "Python"), ("L02", "ML")]. Predict the grouped dictionary and distinct Python learner count.

[Solutions](solutions.md) · [Example](../../subjects/python/examples/course_collections.py)
