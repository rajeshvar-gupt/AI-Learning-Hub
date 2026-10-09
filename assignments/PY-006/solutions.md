# PY-006 · Solutions

Attempt the [questions](questions.md) first.

## 1. Indexing

values[-1] is 40. values[1:3] is [20, 30]. values[9] raises IndexError: there is no element at that position.

## 2. Append and extend

```python
a = [10, 20]
b = [10, 20]
a.append([30, 40])
b.extend([30, 40])
print(a)
print(b)
```

Output: [10, 20, [30, 40]] then [10, 20, 30, 40]. append adds one object; extend adds each supplied item.

## 3. References

```python
a = [1, 2]
alias = a
copy = a.copy()
alias.append(3)
copy.append(4)
print(a)
print(copy)
```

Output: [1, 2, 3] then [1, 2, 4]. A shallow copy has a different outer container, but any inner list objects are still shared.

## 4. Tuple

Use ("Python",). Without the comma, ("Python") is just a parenthesized string. Tuple elements cannot be replaced; mutable objects referenced by its elements can still change.

## 5. Dictionary

```python
marks = {"L01": 70}
marks["L01"] = 90
print(len(marks))
print(marks.get("L02", 0))
print("L02" in marks)
```

Output: 1, 0, False on separate lines. Updating an existing key replaces its value; get does not insert a key.

## 6. Set operations

Intersection: {"L02"}. Union: {"L01", "L02", "L03"}. First minus second: {"L01"}. Set display order is not guaranteed. Conversion loses duplicates and event ordering, so use a list when counts or chronology matter.

## 7. Filtering

```python
scores = [30, 40, 90]
passing = [score for score in scores if score >= 40]
print(passing)
print(scores)
```

Output: [40, 90] then [30, 40, 90]. The original list is unchanged.

## 8. Grouping

Empty input returns {}. The second input returns {"Python": ["L01", "L01"], "ML": ["L02"]}. There are two Python events but one distinct Python learner: len(set(grouped["Python"])) equals 1.

[Lesson](../../subjects/python/01-fundamentals/06-collections-in-depth.md) · [Python home](../../subjects/python/README.md)
