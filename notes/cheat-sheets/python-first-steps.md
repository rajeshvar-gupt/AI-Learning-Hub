# Python first steps · PY-001

| Need | Example | Check |
|---|---|---|
| Store text | `topic = "Python"` | Quotes denote a string |
| Store a whole number | `days = 5` | Numeric value, no quotes |
| Store true/false | `ready = True` | Capital T/F |
| Calculate total | `total = 30 * days` | Units remain minutes |
| Convert to hours | `hours = total / 60` | Division returns a float |
| Inspect type | `type(hours)` | Use `print(type(hours))` in a script to display it |
| Display labeled value | `print(f"Hours: {hours:.1f}")` | One decimal place in output |

A name refers to a value. Assignment is `=`; equality comparison is `==`. A script executes in order. Values do not update retroactively: changing `days` after calculating `total` does not recalculate `total` unless that assignment runs again.

Try: calculate total, then change days and print total. Explain why the old calculated value remains. This is a useful debugging habit before working with data pipelines.

[Full lesson](../../subjects/python/00-introduction/01-first-program.md) · [Practice](../../assignments/PY-001/questions.md) · [Hub](../../README.md)
