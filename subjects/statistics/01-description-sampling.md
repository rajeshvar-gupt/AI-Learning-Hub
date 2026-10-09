# STAT-001 · Descriptive statistics and sampling

Prerequisites: MATH-003.


Outcome: summarize data without hiding outliers or confusing spread and uncertainty.

For `[2,4,4,6]`, the mean and median are both 4. Deviations squared sum to 8. Population variance for these four values is `8/4=2`; sample variance estimates population variance using `8/(4-1)=8/3`. Standard deviation is the square root of variance and has the original units. Median and interquartile range are often more informative for strongly skewed values.

Standard deviation describes variation among observations. Standard error of a sample mean is approximately `sample_SD / sqrt(n)` for independent identically distributed observations with finite variance. Four times as many observations roughly halves SE, not SD. Repeated measurements of the same person are not four independent people.

Sampling bias cannot be repaired by a large sample: a survey of only successful course graduates misses dropouts. Separate population, sampling frame, sample and measurement process. Missing values may carry information; record why they are missing before imputing them.

Correlation measures association, not causation. A high correlation can result from a shared cause, selection, a time trend or reverse causality. Plot distributions and relationships before trusting a single statistic. Use the foundations lab for numerical summaries.


## Practice

[Questions](../../assignments/STAT-001/questions.md) · [Solutions](../../assignments/STAT-001/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
