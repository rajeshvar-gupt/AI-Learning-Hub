# DL-004 · Worked solutions

1. Try a smaller network or stronger regularization using validation data, or stop earlier. Inspect data quality before assuming capacity is the only issue.
2. No. A fixed domain-defined conversion estimates no dataset statistics. A mean or standard deviation learned from all rows would leak holdout information.
3. Backgrounds, scale, handwriting, lighting and preprocessing may differ. This distribution shift requires representative new evaluation, not confidence from the toy benchmark.

[Questions](questions.md)
