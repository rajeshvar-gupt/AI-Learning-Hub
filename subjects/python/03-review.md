# PY-011 · Python integration and debugging

Prerequisites: PY-010.


Outcome: turn a small data-processing requirement into a tested function and explain its failure cases.

A function should make its inputs, outputs and errors predictable. Keep calculations separate from console input and file access: that lets the same function work in a script, test or later data pipeline. Catch errors where you can recover; a broad `except Exception: pass` hides corrupted inputs.

```python
import math

def mean_score(values):
    scores = [float(value) for value in values]
    if not scores:
        raise ValueError("at least one score is required")
    if any(not math.isfinite(x) or not 0 <= x <= 100 for x in scores):
        raise ValueError("scores must be finite and between 0 and 100")
    return sum(scores) / len(scores)

assert mean_score(["60", 80]) == 70
```

The list comprehension transforms each value. A generator inside `any` can stop at the first invalid value. Conversion rejects nonnumeric strings; explicit validation rejects NaN, infinity and out-of-range values. Document whether booleans are accepted: this small numeric converter treats them as 0/1. A stricter public API should reject them explicitly.

Modules organize reusable functions. Put executable demonstrations under `if __name__ == "__main__":` so importing a module does not request input or write files. Use `with open(..., encoding="utf-8")` for text files and `pathlib.Path` for portable paths. Test valid input, boundary values, empty input and malformed input separately.

Debugging loop: reproduce the smallest failing input; read the last traceback frame in your code; inspect values/types; fix the cause; add a regression test. Assertions are useful in tests but can be disabled, so validate user input with explicit exceptions.

Three-level integration exercise: read score strings; build summaries by learner using dictionaries; then load/save JSON using a context manager. Keep parsing errors separate from calculations. The existing score-summary project supplies a working reference; this exercise consolidates it before scientific Python.


## Practice

[Questions](../../assignments/PY-011/questions.md) · [Solutions](../../assignments/PY-011/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
