# PY-001 · Solutions

1. `str`, `int`, `float`, `bool`, respectively (0.5 mark each). Quotation marks make digits text.
2. 20 × 6 = 120 minutes; 120 / 60 = 2.0 hours (one mark for each calculation).
3. One solution:

```python
topic = "Python"
minutes_per_day = 40
study_days = 3
weekly_minutes = minutes_per_day * study_days
weekly_hours = weekly_minutes / 60
print(f"Topic: {topic}")
print(f"Study: {weekly_minutes} minutes ({weekly_hours:.1f} hours)")
```

Observed output:

```text
Topic: Python
Study: 120 minutes (2.0 hours)
```

Award one mark each for suitable variables, correct calculation and labeled output. Equivalent runnable solutions are acceptable.

4. The value is a string, so multiplication repeats it. Use `minutes = 30` and `print(minutes * 2)` to obtain `60`. Alternatively, convert valid numeric text deliberately with `int(minutes)`. Award one mark for explanation and one for a correct fix.
5. No: it applies fixed arithmetic to supplied values, without fitting parameters from examples. Award one mark for that distinction.

Challenge: `completed_today = False` can be displayed with `print(f"Completed today: {completed_today}")`. Zero study days give zero minutes and 0.0 hours. Negative days are nonsensical for this scenario; input validation is future work, not implemented by these examples.

[Questions](questions.md) · [Lesson](../../subjects/python/00-introduction/01-first-program.md)
