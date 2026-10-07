# Python files · Revision

| Pattern | Meaning |
|---|---|
| with open(path, "r", encoding="utf-8") as handle: | Read text and close automatically |
| open(path, "x", encoding="utf-8") | Create only; refuse an existing target |
| handle.write("70\n") | Write text plus a newline |
| for line in handle: | Read one line per iteration |
| enumerate(handle, start=1) | Include a human-readable line number |
| line.strip() | Remove surrounding whitespace |
| FileNotFoundError | File or parent folder is missing |
| FileExistsError | Exclusive creation found an existing path |
| UnicodeError | Text encoding/decoding failed |
| OSError | General filesystem error family |

Validate before saving. Convert and validate after reading. Relative paths use the current working directory. with closes resources but does not roll back partial writes.

[Lesson](../../subjects/python/01-fundamentals/05-files-and-score-storage.md) · [Practice](../../assignments/PY-005/questions.md)
