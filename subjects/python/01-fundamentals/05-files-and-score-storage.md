# PY-005 · Files and score storage

Prerequisite: [PY-004: Functions](04-functions-and-score-summary.md).
Audience: beginners who can use functions, lists, loops and exceptions.
Outcome: create and read UTF-8 text files, reuse functions from another module, and report file/data errors clearly.

## Why files?

The interactive score list disappears when its process ends. A file lets another run recover the values. We will store one whole-number score per line. For example, a file containing 70, 80 and 90 on separate lines represents three scores, not a single total.

## Open, write and close

```python
with open("practice-scores.txt", "x", encoding="utf-8") as handle:
    handle.write("70\n80\n90\n")
```

The with block closes the file when the block ends, including when an exception occurs. write accepts text; `\n` inserts a newline. A relative filename is resolved from the directory where you run the command, not automatically from the script's folder.

| Mode | Purpose | Existing file |
|---|---|---|
| r | Read text | Reads it; missing file raises an error |
| x | Create a new text file | Refuses to overwrite it |
| w | Write from the beginning | Truncates existing content |
| a | Append text at the end | Retains previous content |

This project uses x for saving. Choose a new filename for another snapshot. A with block closes a file; it does not undo a partial write.

## Read lines and convert values

```python
with open("practice-scores.txt", "r", encoding="utf-8") as handle:
    for line_number, line in enumerate(handle, start=1):
        print(line_number, int(line.strip()))
```

After the creation example, the output is:

```text
1 70
2 80
3 90
```

enumerate supplies both a counter and each line. strip removes surrounding whitespace. Text read from disk still needs conversion and validation. The actual project reuses parse_score so file inputs obey the same 0–100 rule as terminal input.

An ordinary final newline terminates the last score. An extra blank line is an invalid record. An empty file contains zero records and produces “No scores recorded.”

## Reuse a module

In [score_files.py](../../../projects/beginner/student-score-summary/score_files.py), the line
`from score_summary import parse_score, summarize_scores` imports functions from the adjacent score_summary.py file. Its import guard prevents the interactive program from starting. Run the documented script command so Python can locate the adjacent module.

save_scores validates the complete list before opening the output file. It accepts a list of integers from 0 to 100; booleans and floats are rejected even though Python considers bool a subclass of int. load_scores builds a new list and returns it only after every line is valid. It raises a line-numbered error instead of silently discarding a bad mark or returning a partial result.

## Save and reload

Run these commands from the repository root, using a filename that does not yet exist:

```bash
python3 projects/beginner/student-score-summary/score_files.py save practice-scores.txt 70 80 90
python3 projects/beginner/student-score-summary/score_files.py load practice-scores.txt
```

If you ran the earlier writing example, choose a different filename such as practice-scores-2.txt in both commands. Windows users can replace python3 with py.

The save command reports three saved scores. The load command reports count 3, total 240, average 80.00, lowest 70 and highest 90. No third-party packages or keys are needed.

The standard-library argparse module reads the command and path. Extra values belong to save only. `nargs="*"` permits zero or more scores; saving zero scores creates an empty file. The command returns exit status 0 for success, 1 for file/data errors and 2 for invalid command syntax. `raise SystemExit(main())` passes that status to the shell.

## Handle expected failures

| Failure | Behavior |
|---|---|
| Existing save target | Refuse to overwrite; ask for a new filename |
| Missing file or parent directory | Show a path error; do not create directories automatically |
| Invalid score or blank line | Reject load with a line number |
| Invalid UTF-8 bytes | Show an encoding error |
| Directory used as input file, or permission error | Show an operating-system error |
| Empty file | Return an empty list and the empty summary |

Messages go to stderr, the error-output stream. Successful reports go to stdout. File helpers raise exceptions; the command function catches expected failures and turns them into messages. Programming errors are not hidden by a catch-all exception handler.

Permission failure is checked with a simulated PermissionError in the test suite so the check works even in environments with broad filesystem access. Other file cases use temporary files.

## Limits and practice

This is a text snapshot tool, not a database. It does not append sessions, store names or offer concurrent editing. Disk failures during writing may leave a partial new file; inspect it and use a new filename after correcting the problem. Real learner records should not be committed as exercise fixtures.

Run the [project tests](../../../projects/beginner/student-score-summary/README.md), attempt the [questions](../../../assignments/PY-005/questions.md), then read the [solutions](../../../assignments/PY-005/solutions.md). [Revision sheet](../../../notes/cheat-sheets/python-files.md).

Next planned unit: collections in depth—lists, tuples, dictionaries and sets. [Python home](../README.md)
