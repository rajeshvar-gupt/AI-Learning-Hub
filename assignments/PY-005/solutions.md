# PY-005 · Solutions

Try the [questions](questions.md) first.

1. r reads; x creates only if the path is absent; w truncates an existing file; a appends. The project uses x to prevent replacement.
2. Count 3, total 150, average 50.00, lowest 0, highest 100. Zero is a valid score and is included.
3. The save command exits with status 1 and asks for a new filename. The original file contents remain unchanged.
4. Loading fails with a line-2 conversion error and exits with status 1. It prints no partial summary. Otherwise silently dropping abc could misrepresent the dataset.
5. An empty file is a valid empty dataset: “No scores recorded.” A blank line is one invalid record, so loading fails on line 1. A single newline after a valid score is merely its line terminator.
6. Validation before opening avoids creating an output file for invalid scores. with guarantees closing, not rollback or atomicity; a disk error may leave a partial file. A missing parent produces a filesystem error, while an invalid score produces ValueError. Both become useful command messages.

Reproduce answer 2 from repository root with a new filename:

```bash
python3 projects/beginner/student-score-summary/score_files.py save exercise-scores.txt 0 50 100
python3 projects/beginner/student-score-summary/score_files.py load exercise-scores.txt
```

Use py instead of python3 on Windows when appropriate. Choose a different name if the file already exists.

[Lesson](../../subjects/python/01-fundamentals/05-files-and-score-storage.md) · [Project](../../projects/beginner/student-score-summary/README.md)
