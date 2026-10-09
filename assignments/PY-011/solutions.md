# PY-011 · Worked solutions

1. The result is `70.0`, a float because conversion and division use floating-point values.
2. Before conversion, use `values = list(values)` and `if any(isinstance(x, bool) for x in values): raise ValueError("boolean score")`. Materializing once also avoids consuming an iterator twice.
3. Test a valid mapping, missing file, invalid JSON, non-mapping root, empty list, nonnumeric value, NaN and values outside 0–100. Raise clear exceptions; do not overwrite the original file after a failed load. Use a temporary directory in tests. Decide whether an empty learner is invalid (the function above rejects it) and document that policy.
4. A list holds all results; a generator produces results on demand and is consumed by iteration. A main guard permits safe import without running the command-line entry point.

[Questions](questions.md) · [Lesson](../../subjects/python/03-review.md)
