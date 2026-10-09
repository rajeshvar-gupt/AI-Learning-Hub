# DATA-003 · Worked solutions

1. Add `HAVING SUM(o.quantity * o.unit_price) > 50` after GROUP BY and before ORDER BY.
2. Rows with NULL quantity contribute to `COUNT(*)` but not `COUNT(quantity)`.
3. You can compare observed revenue under the stated cleaning policy and period. You cannot infer profitability without costs or future demand from this small invented sample. An intervention causing sales growth requires a causal design, not this chart.

[Questions](questions.md) · [Lesson](../../subjects/data-analysis/03-sql-visualization.md)
