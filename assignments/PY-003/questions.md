# PY-003 · Practice

Prerequisite: [Loops and repeated input](../../subjects/python/01-fundamentals/03-loops-and-repeated-input.md). Work before opening the separate solutions.

1. Predict every printed value:
   ```python
   total = 0
   for number in range(1, 5):
       total += number
       print(total)
   ```
2. Write a countdown from 3 to 1 with `while`, then print `Done`. Explain why it terminates.
3. Explain the difference between `break` and `continue`. Why is q checked before numeric conversion in the study log?
4. Run the study log with `abc`, `-2`, `0`, `15`, `q`. Predict the accepted session count, total and average. Also test quitting immediately.
5. Modify the log so zero minutes is rejected with “Minutes must be positive.” Verify that `0, 15, q` records exactly one session.
6. Use a `for` loop to add the numbers 1 through 10. Print the total once after the loop. What changes if you initialize the total inside the loop?

Completion: explain your results, show both valid and invalid input, and identify where the loop exits.

[Solutions](solutions.md) · [Python home](../../subjects/python/README.md)
