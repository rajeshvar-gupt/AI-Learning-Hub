# DATA-002 · Worked solutions

1. One customer may place many valid orders. The row key is an order ID in this dataset, not a customer ID.
2. A one-to-many or many-to-many key match duplicated orders. Enforce a unique product dimension and `validate='many_to_one'`; verify row counts and total revenue before/after the join.
3. Deletion removes the order from the analysis; imputation invents a quantity estimate and changes totals. Log affected row IDs/counts, reasons, the policy and its possible bias. Neither is automatically appropriate for accounting totals.

[Questions](questions.md) · [Lesson](../../subjects/data-analysis/02-pandas.md)
