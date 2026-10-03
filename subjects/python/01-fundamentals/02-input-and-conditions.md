# PY-002 · Input and conditions

Prerequisite: [PY-001](../00-introduction/01-first-program.md). Time: 30–45 minutes. Goal: accept text input, convert a whole number, reject invalid values and select one response.

## What and why?

A fixed profile prints the same result each run. Interactive input lets a learner supply today's study time. Conditions select a response based on that value. This is useful for form validation and application rules, including applications that later call AI models.

## How it works

`input()` returns text, even when someone types digits. `int()` converts valid integer text to an integer; `"abc"`, an empty string and `"2.5"` cannot be converted this way and raise ValueError. The supplied example catches that specific conversion error. `try`/`except` handles an operation failing; `if`/`elif`/`else` selects a branch after conversion succeeds.

Run from repository root:

```bash
python3 subjects/python/examples/study_goal.py
```

On Windows use `py` instead of `python3` if that is your installed launcher. Uses Python built-ins only; tested on 3.12.14. Open [the complete code](../examples/study_goal.py) alongside this explanation.

| Code | Meaning |
|---|---|
| `raw_minutes = input(...)` | Read the learner's text |
| `minutes = int(raw_minutes)` | Convert integer text |
| `except ValueError:` | Handle invalid numeric text with a useful message |
| `else:` after the exception handler | Continue only if conversion succeeded |
| `if minutes < 0:` | Reject a negative duration |
| `elif minutes >= 30:` | Treat exactly 30 and larger values as reaching the goal |
| final `else:` | Calculate the remaining minutes for values from 0 to 29 |

Python uses indentation to group statements. Keep the supplied four-space indentation. Only one of the final three branches executes. `=` assigns a name, `==` tests equality, and `>=` means greater than or equal to.

## Expected behavior

| Input | Message after the prompt |
|---|---|
| `10` | Keep going: 20 more minutes to reach your goal. |
| `30` | Daily goal reached. |
| `45` | Daily goal reached. |
| `0` | Keep going: 30 more minutes to reach your goal. |
| `-1` | Minutes cannot be negative. |
| `abc`, blank, or `2.5` | Please enter a whole number, such as 30. |

These cases were executed during validation. Spaces around an integer are accepted by int(). This version reads once and stops; retry loops are a later lesson. It does not store personal data, measure actual attendance or verify that the entered time is truthful.

## Common mistakes

Comparing input text directly with a number causes a type error. Using `>` instead of `>=` mishandles exactly 30. Using several independent `if` statements can trigger multiple messages when your intention is one exclusive outcome. Catching every exception hides unrelated bugs; catch the expected conversion error here.

## Practice and interview questions

Why should negative input be checked before the success branch? Which test catches a boundary error at 30? What differs between invalid text and an invalid negative duration? Explain the two different uses of `else` in the program.

Mini project: change the goal to 45 minutes and retest zero, 44, 45 and 46. Keep invalid input behavior. [Questions](../../../assignments/PY-002/questions.md) · [Solutions](../../../assignments/PY-002/solutions.md)

Next: [PY-003: loops and repeated input](03-loops-and-repeated-input.md). [Python home](../README.md)
