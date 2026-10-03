# PY-003 · Solutions

Try the [questions](questions.md) first.

## 1. Accumulation

Output: 1, 3, 6, 10 on separate lines. The stop value 5 is excluded, so the loop adds 1, 2, 3 and 4 to the existing total.

## 2. Countdown

```python
remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1
print("Done")
```

Output: 3, 2, 1, Done on separate lines. Subtracting one eventually makes the condition false. Without that update, the loop would repeatedly print 3.

## 3. Control flow

`break` exits the nearest loop. `continue` skips to its next iteration. Check q first because it is a command; converting it to an integer would raise ValueError. Invalid numeric text uses continue so it cannot reach the accumulation statements.

## 4. Study log

abc fails integer conversion; -2 is rejected as negative. Zero and 15 are accepted. The final count is 2, total is 15 minutes, and average is 7.5 minutes. Quitting immediately prints count 0, total 0, and “No sessions recorded.” It never divides by zero.

## 5. Positive durations only

Replace the negative check in the original script with this block, retaining its position before accumulation:

```python
    if minutes <= 0:
        print("Minutes must be positive.")
        continue
```

With 0, 15, q, only 15 is counted: count 1, total 15, average 15.0. Both zero and negative durations are now rejected; the rest of the script is unchanged.

## 6. Sum

```python
total = 0
for number in range(1, 11):
    total += number
print(total)
```

Output: 55. If `total = 0` is moved inside the loop before addition, earlier values are discarded and the final printed total is 10.

[Lesson](../../subjects/python/01-fundamentals/03-loops-and-repeated-input.md) · [Python home](../../subjects/python/README.md)
