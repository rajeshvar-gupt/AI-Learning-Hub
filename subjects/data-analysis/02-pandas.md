# DATA-002 · pandas cleaning, grouping and joins

Prerequisites: DATA-001.


Outcome: create an auditable table-cleaning pipeline and check aggregate totals.

Start with a data dictionary: what does one row represent, what identifies it, which columns are numeric, what units do they use and which values may be absent? A duplicate ID may be a repeated export or a legitimate repeated observation. Never drop duplicates without defining that distinction.

The sales lab defines one row per order, removes an exact duplicate and rejects orders with a missing/nonpositive quantity or negative/missing price. This is an explicit demonstration policy, not a universal missing-data strategy. It preserves a cleaning summary. Revenue is quantity times unit price. A groupby sum is checked against the overall sum.

Use `pd.to_numeric(..., errors='coerce')` to expose malformed numbers as missing, then handle them explicitly. `isna()` finds missing values. Use `.loc` for deliberate assignment and `.copy()` for independent filtered tables. Grouping can omit missing keys unless configured otherwise; investigate them before reporting totals.

Join orders to a unique product table with `merge(..., validate='many_to_one')`. Duplicate keys in the dimension table would otherwise multiply rows and inflate revenue. A left join preserves orders but may reveal unmatched product names. Check for unmatched rows instead of turning them into silent omissions.

Run the sales lab and explain both the chart and its limitations: invented data, tiny sample, no costs, and no grounds for forecasting or causal conclusions.


## Practice

[Questions](../../assignments/DATA-002/questions.md) · [Solutions](../../assignments/DATA-002/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
