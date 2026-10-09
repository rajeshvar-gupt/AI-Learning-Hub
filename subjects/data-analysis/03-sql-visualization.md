# DATA-003 · SQL analysis and communicating results

Prerequisites: DATA-002.


Outcome: reproduce a pandas aggregation in SQLite and make an interpretable chart.

SQL `SELECT` chooses columns, `WHERE` filters rows, `GROUP BY` defines groups and `HAVING` filters aggregated groups. An inner join keeps matches; a left join also keeps unmatched left rows. `COUNT(*)` counts rows while `COUNT(column)` excludes NULL values. SQL NULL uses `IS NULL`, not `= NULL`.

```sql
SELECT p.category, SUM(o.quantity * o.unit_price) AS revenue
FROM orders AS o
JOIN products AS p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC, p.category;
```

The sales lab loads cleaned tables into an in-memory SQLite database and compares SQL and pandas results. For user-supplied values, use bound parameters (`WHERE category = ?`) rather than string interpolation. Table/column identifiers require separate validation and cannot generally be bound as value parameters.

A bar chart compares categories; a line chart suits ordered time; a histogram shows a numerical distribution; a scatterplot shows paired measurements. Label units and the observed period. Begin ordinary bar axes at zero to preserve magnitude comparisons. Report sample size, cleaning decisions and what the data cannot establish.

The lab writes a CSV summary and PNG into an ignored `outputs/` directory. The notebook version executes the same pipeline so script and notebook stay consistent.


## Practice

[Questions](../../assignments/DATA-003/questions.md) · [Solutions](../../assignments/DATA-003/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
