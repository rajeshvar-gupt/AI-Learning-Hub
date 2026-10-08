# Student-score summary

**Level:** beginner · **Topic:** Python functions, lists, validation and loops.
Prepared with PY-004 for review. Requires [the functions lesson](../../../subjects/python/01-fundamentals/04-functions-and-score-summary.md).

## Problem and behavior

Enter several whole-number marks from 0 to 100 and receive their count, total, mean, minimum and maximum. Invalid entries produce a message and are excluded. Enter q (or Q, with optional surrounding spaces) to finish. Zero is valid. Quitting immediately produces “No scores recorded.” End-of-input also finishes and summarizes accepted marks.

This is an arithmetic teaching project. Each accepted entry represents one equally weighted score out of 100. It does not assign grades, predict performance, identify students or implement an institution's assessment policy.

## Run

Use Python 3; no packages, accounts or keys are needed. From the repository root:

```bash
python3 projects/beginner/student-score-summary/score_summary.py
```

On Windows, replace python3 with py if that is your installed launcher.

Type 70, 80, 90 and q, pressing Enter after each. The final report is:

```text
Count: 3
Total: 240
Average: 80.00
Lowest: 70
Highest: 90
```

## Code map

| Function | Input | Output / responsibility |
|---|---|---|
| parse_score | Text | Valid integer or ValueError |
| summarize_scores | List of valid integer scores | Report string; no printing or mutation |
| main | Terminal input | Collect entries and display the report |

Read [score_summary.py](score_summary.py). Calculation is separate from terminal interaction so it can be checked without manually typing scores. summarize_scores expects already validated integers in the range 0–100; callers using it directly must honor that contract.

## Checks

From repository root:

```bash
python3 -m unittest discover -s projects/beginner/student-score-summary -p 'test_*.py' -v
```

[Test cases](test_score_summary.py) cover boundaries, invalid text, empty input, rounding, repeated entries, EOF, import behavior and keeping calculation free of printing or input-list changes.

Validated on 7 October 2026 with Python 3.12.14: all eight automated tests and the documented sample report passed.

## Limitations and extension

Scores exist only in memory and disappear when the program ends. Fractional marks such as 82.5 are rejected. Every accepted entry counts, including duplicates. The average is displayed to two decimal places; underlying arithmetic is not rounded before formatting. KeyboardInterrupt is not caught.

Next planned extension: save and reload scores using files, with explicit error handling.

[Projects](../../README.md) · [Questions](../../../assignments/PY-004/questions.md)
