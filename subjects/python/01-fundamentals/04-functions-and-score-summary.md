# PY-004 · Functions and a student-score summary

Prerequisite: [PY-003: Loops and repeated input](03-loops-and-repeated-input.md).
Audience: beginners comfortable with input, conditions, exceptions and loops.
Outcome: define and call functions, distinguish printing from returning, and combine reusable calculations with an interactive program.

## Why functions?

The study log put its input and calculations together. A function gives a task a name and lets us call it with different inputs. Separating calculation from interaction makes the calculation easier to reuse and check.

```python
def add_bonus(score, bonus=5):
    adjusted = score + bonus
    return adjusted

result = add_bonus(70)
print(result)
print(add_bonus(70, 10))
```

Output: 75 then 80, on separate lines. This small example only demonstrates arguments; it does not impose a maximum mark.

| Syntax | Meaning |
|---|---|
| def | Define a function; its body does not run until called |
| score and bonus | Parameters: names that receive values |
| 70 and 10 in the call | Arguments: values supplied by the caller |
| bonus=5 in the definition | Default used when that argument is omitted |
| adjusted | A local name created in this call |
| return adjusted | End the function and send a value back |
| result = add_bonus(70) | Store the returned value |

Keep four-space indentation. The caller cannot access adjusted as a global variable. Each call has its own local names. Defining a function is different from calling it: parentheses with arguments perform the call.

## Return versus print

```python
def show_double(value):
    print(value * 2)

answer = show_double(4)
print(answer)
```

Output: 8, then None. print displays a value; it does not make that value the function's result. A function that reaches the end without returning a value returns None. Use return for a calculation and print when the caller wants to display its result.

## Just enough lists for this project

```python
scores = []
scores.append(70)
scores.append(90)
print(len(scores))
print(sum(scores) / len(scores))
```

Output: 2 then 80.0. A list stores several values in order. [] creates an empty list; append adds a value to the existing list. Do not write scores = scores.append(70): append changes the list and returns None.

len counts items, sum adds them, and min/max find the smallest/largest. In this project every score has the same weight. An empty list is false in a condition, so `if not scores:` handles it before division or min/max.

## Build the project

Open the [student-score project](../../../projects/beginner/student-score-summary/README.md). From the repository root:

```bash
python3 projects/beginner/student-score-summary/score_summary.py
```

Use py instead of python3 on Windows when appropriate. There are no external dependencies.

The [full script](../../../projects/beginner/student-score-summary/score_summary.py) has three functions:

1. parse_score converts text and rejects values outside 0–100. It returns an integer on success. `raise ValueError(...)` reports a failure to the caller; it does not return a score. `from None` suppresses the earlier conversion error's context so direct callers see the simpler message.
2. summarize_scores receives validated values and returns a report string. It checks the empty case first. It never asks for input or prints; the caller chooses how to use the report.
3. main creates a fresh list, repeatedly reads input, handles conversion/range errors and appends accepted scores. Finally it prints the returned report.

`except ValueError as error` gives the caught error a name so its message can be printed. EOFError means the input stream ended; this program then reports any scores already accepted.

The line `if __name__ == "__main__":` calls main when the file is run directly. Importing the file to test its functions does not start the input loop. The triple-quoted strings below function definitions are docstrings explaining purpose and expectations.

## Trace one run

For inputs 70, invalid text, 90 and q:

| Step | Result |
|---|---|
| parse_score("70") | Returns 70; list becomes [70] |
| parse_score("abc") | Raises ValueError; main prints its message; list stays [70] |
| parse_score("90") | Returns 90; list becomes [70, 90] |
| q | Stops input before attempting conversion |
| summarize_scores(scores) | Returns count 2, total 160, average 80.00, lowest 70, highest 90 |

A score of 0 counts as data. No scores is a different case. The program accepts whole numbers only: 82.5 is rejected. It stores no names or files.

## Check your understanding

Why does the summary return text rather than print it? Why is the empty-list check before calculating the average? Why should invalid input never reach append? Explain how the import guard makes testing easier.

Complete [six exercises](../../../assignments/PY-004/questions.md), then read the [solutions](../../../assignments/PY-004/solutions.md). Use the [revision sheet](../../../notes/cheat-sheets/python-functions.md).

Next planned unit: file handling and saving/reloading scores. [Python home](../README.md)
