# PY-004 · Solutions

Try the [questions](questions.md) first.

## 1. Return a value

```python
def double(value):
    return value * 2

print(double(6))
```

Output: 12.

## 2. Printing does not return the printed value

answer receives None. The printed 12 appears on the screen, but no explicit value is returned. To let the caller calculate with 12, return it.

## 3. A default parameter

```python
def is_passing(score, threshold=40):
    return score >= threshold

print(is_passing(39))
print(is_passing(40))
print(is_passing(60, threshold=60))
```

Output: False, True, True on separate lines. This function assumes score and threshold are valid numeric values in the intended assessment scale. The threshold is an exercise rule, not an institutional policy.

## 4. Invalid entries do not count

abc fails conversion. -1 and 101 are outside the range. Only 0 and 100 are accepted:
count 2, total 100, average 50.00, lowest 0, highest 100.

## 5. Empty versus zero

An empty list has length zero, so dividing by its length raises ZeroDivisionError; min/max also need a nonempty input here. Immediate quit displays “No scores recorded.” A single zero is valid data: count 1, total 0, average 0.00, lowest 0, highest 0.

## 6. Count passing scores

```python
def count_passes(scores, threshold=40):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

print(count_passes([]))
print(count_passes([39, 40, 100]))
print(count_passes([0, 100], threshold=100))
```

Output: 0, 2, 1 on separate lines. Like the summary calculation, this function expects already validated scores. It reads the list without appending, removing or replacing entries. Initialize count before the loop and return after the loop.

[Lesson](../../subjects/python/01-fundamentals/04-functions-and-score-summary.md) · [Project](../../projects/beginner/student-score-summary/README.md)
