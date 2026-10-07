# PY-003 · Loops and repeated input

Prerequisite: [PY-002: Input and conditions](02-input-and-conditions.md).
Audience: beginners who can convert input and use conditions. Allow 45–60 minutes.
Outcome: repeat work with `for` and `while`, use `break` and `continue`, and accumulate a study-session summary.

## Why repeat?

The previous goal checker reads once. A study log needs to accept several sessions and let the learner choose when to finish. A loop runs a block repeatedly. Conditions still decide what happens within each repetition.

## A fixed number of repetitions: for and range

```python
total = 0
for day in range(1, 4):
    total += 20
    print(f"Day {day}: {total} minutes so far")
```

Actual output:

```text
Day 1: 20 minutes so far
Day 2: 40 minutes so far
Day 3: 60 minutes so far
```

`range(1, 4)` supplies 1, 2 and 3: the stop value is excluded. `total += 20` means `total = total + 20`. Initialize an accumulator before the loop so it keeps its value across repetitions. Indented statements run once per supplied value.

## Repeating while a condition is true

```python
remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1
print("Start!")
```

Actual output is 3, 2, 1 and Start!, each on its own line. Python checks the condition before every iteration. If the condition starts false, the body runs zero times. Removing the decrement here would leave the condition true forever.

Use `for` to visit values in an iterable such as a range. Use `while` when repetition depends on a condition. For user-controlled input, `while True` can be useful when the body has an explicit exit.

## Build a study log

From the repository root, run:

```bash
python3 subjects/python/examples/study_log.py
```

On Windows, use `py` instead of `python3` if that is your installed launcher. No packages or API keys are required. Open [the full script](../examples/study_log.py).

| Part | Purpose |
|---|---|
| Initialize total and count to zero | Set summary values once before reading |
| `while True:` | Keep asking until the exit branch runs |
| `.strip()` and `.lower()` | Accept surrounding spaces and either q or Q |
| Check q before `int()` | Treat the exit command as text, not a number |
| `break` | Exit the nearest loop and continue after it |
| `except ValueError` then `continue` | Explain invalid text and start the next iteration |
| Negative check then `continue` | Reject invalid durations without counting them |
| Update total and count | Record only accepted sessions |
| Check count before division | Avoid division by zero when quitting immediately |

`continue` skips the remaining statements in the current iteration; it does not end the loop. `break` ends the loop. Zero minutes is accepted and counts as one session: it represents an explicitly recorded session with no study time.

Example terminal interaction (numbers and q are typed by the learner):

```text
Session minutes (q to finish): 20
Recorded 20 minutes.
Session minutes (q to finish): 40
Recorded 40 minutes.
Session minutes (q to finish): q
Sessions: 2
Total: 60 minutes
Average: 30.0 minutes
```

The average uses `:.1f` to display one decimal place. The script keeps only a count and total in memory; it does not save sessions to a file.

## Try the boundaries

| Inputs in order | Expected result |
|---|---|
| q | Count 0, total 0, “No sessions recorded.” |
| 0, q | Count 1, total 0, average 0.0 |
| 20, 40, q | Count 2, total 60, average 30.0 |
| abc, blank, 2.5, -1, 30, q | Four rejection messages, count 1, total 30 |
| Space-padded Q | Exit immediately |

These sequences are checked with scripted input during validation. For normal interactive use, enter q to finish. Closing standard input or interrupting the process is outside this introductory example's handling.

## Common mistakes

Resetting the total inside the loop loses earlier sessions. Incrementing the count before validation counts rejected input. Dividing by count without checking zero fails when the learner quits immediately. Putting `continue` before a necessary update in a countdown can prevent it from ending.

## Practice and next step

Complete the [questions](../../../assignments/PY-003/questions.md) before reading the [solutions](../../../assignments/PY-003/solutions.md). Keep the [loop revision sheet](../../../notes/cheat-sheets/python-loops.md) nearby.

Next: [PY-004: functions and a student-score summary](04-functions-and-score-summary.md). [Python home](../README.md)
