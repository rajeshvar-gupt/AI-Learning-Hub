# PY-002 answer guide

1. input() reads a textual response; explicit conversion makes the intended numeric type clear.
2. Replace 30 with 45 in both comparison and remaining-time calculation. Input 44 needs one more minute; 45 and 46 reach the goal. Better extension: store `goal = 45` once and refer to it in both expressions.
3. Use `minutes >= 45`; test 44, 45 and 46 to cover both sides and the boundary.
4. Blank and `2.5` fail integer conversion. `-2` converts successfully but violates the nonnegative-duration rule.
5. After conversion, check `score < 0 or score > 100` first; otherwise use `elif score >= 40`, then `else`. Test -1, 0, 39, 40, 100, 101 and nonnumeric text. This is a practice rule, not an assessment of an actual student.

[Questions](questions.md) · [Lesson](../../subjects/python/01-fundamentals/02-input-and-conditions.md)
