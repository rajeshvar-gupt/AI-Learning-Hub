# PY-001 · Your first Python program

Level: beginner · Estimated study time: 45–60 minutes · Prerequisites: basic file/folder use. After this lesson you can run a script, distinguish text from numbers, explain assignment and print a calculated result.

## What is Python, and why use it?

Python is a programming language. A script is a text file containing instructions that the Python interpreter executes. In AI work, programs prepare data, run experiments and connect applications to models. Today we use only basic language features: a profile program is a programming exercise, not an AI model.

## Setup and first run

Use an installed Python 3 interpreter. These examples were executed on Python 3.12.14; no third-party dependencies, account or API key are required. If Python is missing, use your institution's approved installation process. This lesson does not claim to install Python for you.

Download/clone the repository and open a terminal in its root directory (the folder containing this README and subjects/). Check your interpreter:

| Environment | Version check | Run command from repository root |
|---|---|---|
| macOS/Linux | `python3 --version` | `python3 subjects/python/examples/learner_profile.py` |
| Windows with Python launcher | `py --version` | `py subjects/python/examples/learner_profile.py` |

If your installation provides `python` instead, use `python --version` and replace the command name accordingly. A terminal runs the commands above; a `.py` file contains Python code, not terminal commands. Do not include `>>>` prompts in a script.

Optional isolation for future lessons: run `python3 -m venv .venv` (Windows: `py -m venv .venv`). You can run `.venv/bin/python` on macOS/Linux or `.venv\Scripts\python.exe` on Windows without changing your shell's activation settings. No packages need installing for this example.

## How the program works

We choose a fictional learner name and study schedule, calculate weekly hours, then print a summary. Think of the names as labels for values; assignment binds a name to a value. Execution follows the statements from top to bottom.

```python
learner_name = "Asha"
minutes_per_day = 30
study_days = 5
has_python = True
weekly_minutes = minutes_per_day * study_days
weekly_hours = weekly_minutes / 60

print(f"Learner: {learner_name}")
print(f"Weekly study: {weekly_minutes} minutes ({weekly_hours:.1f} hours)")
print(f"Python ready: {has_python}")
```

## Explain each important line

| Expression | Meaning |
|---|---|
| `learner_name = "Asha"` | Bind text to a meaningful name; quotation marks delimit text |
| `minutes_per_day = 30` | Store a whole-number study duration |
| `study_days = 5` | Store the number of study days in the example |
| `has_python = True` | Store a Boolean value; capitalization matters |
| `minutes_per_day * study_days` | Multiply two numbers; here the result is 150 |
| `weekly_minutes / 60` | Convert minutes to hours; `/` produces a floating-point result |
| `print(...)` | Display a value in the terminal |
| `f"...{weekly_hours:.1f}..."` | Insert a value into text and display one decimal place |

Actual output from the supplied example:

```text
Learner: Asha
Weekly study: 150 minutes (2.5 hours)
Python ready: True
```

The formatting changes how a number is displayed; it does not change the stored value. This first exercise deliberately uses fixed valid values. It does not ask for or validate user input yet.

## Key concepts and a prediction exercise

`str` represents text, `int` whole numbers, `float` floating-point numbers and `bool` true/false values. You can inspect a value with `type(value)`. Python associates types with objects; a variable name is not permanently declared as one type. Prefer consistent, clear usage so programs remain easy to understand.

Before running, predict the result after setting `minutes_per_day = 45`. Five study days give 225 minutes, or 3.75 hours; the one-decimal display is 3.8. Set `study_days = 0`: the result should be zero minutes and 0.0 hours.

## Where this becomes useful in AI work

A label may become a dataset column name, a count may become a batch size, and a Boolean may become an option controlling a processing step. Correct types matter: text containing digits is still text. Clear variable names make an experiment easier to review.

## Common mistakes and troubleshooting

| Symptom | Cause / correction |
|---|---|
| Command not found | Interpreter command is unavailable; check the approved installation and command name |
| Cannot open file | Wrong working directory or path; run from repository root |
| `NameError` for `true` | Use `True`, not `true` |
| `NameError` for a variable | Check spelling and that assignment ran first |
| Text repeats unexpectedly | `"30" * 5` repeats a string; use numeric `30` for multiplication |
| Type error when adding text and number | Use an f-string or deliberate conversion |
| Invalid syntax around quotes | Use straight quotation marks, not word-processor curly quotes |

`=` assigns; `==` compares equality (covered further in the next unit). Python names are case-sensitive. Avoid naming a file `python.py` and avoid using built-in names like `print` for your own values.

## Practice, interview questions and mini project

Complete the [assignment](../../../assignments/PY-001/questions.md). Explain why `"30"` differs from `30`, why `print()` is needed in a script, and whether this program learns from data. For a mini project, adapt it into a weekly study card with a topic, daily minutes and days. Predict the output before execution.

## Sources and next step

Official references checked 2 October 2026: [Python introduction](https://docs.python.org/3/tutorial/introduction.html) and [virtual environments](https://docs.python.org/3/tutorial/venv.html). The exercise and learning sequence are original.

Next: [input conversion and conditions](../01-fundamentals/02-input-and-conditions.md). Use the [revision sheet](../../../notes/cheat-sheets/python-first-steps.md) and [solutions](../../../assignments/PY-001/solutions.md) to check this unit. [Python home](../README.md)
