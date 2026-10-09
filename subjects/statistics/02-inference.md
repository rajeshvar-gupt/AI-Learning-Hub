# STAT-002 · Confidence intervals and hypothesis tests

Prerequisites: STAT-001, MATH-002.


Outcome: report uncertainty and interpret a one-sample t-test correctly.

For a mean with unknown population variance, a conventional two-sided interval is `sample_mean ± t_critical * sample_SD/sqrt(n)`, with n-1 degrees of freedom. Exact small-sample coverage assumes independent normal observations. Approximation may work for larger samples; heavy tails, dependence or selection bias can undermine it.

A 95% confidence procedure covers the fixed true mean in 95% of repeated samples under its assumptions. It does not mean 95% of observations lie in the interval. After computing this frequentist interval, avoid assigning a 95% probability to the fixed parameter being inside it.

A null hypothesis could specify a population mean of 10. The t statistic is `(sample_mean-10)/SE`. A two-sided p-value measures how surprising a statistic at least this extreme would be under that null and the model assumptions. It is not the probability the null is true. Failure to reject does not establish equivalence.

Before collecting data, specify the question, sampling method, effect worth detecting, test and significance level. Report the effect estimate and interval alongside the p-value. Testing many hypotheses and reporting only the smallest p-value inflates false discoveries. Use a suitable multiplicity correction or a separately collected confirmation sample.

The lab uses fixed invented measurements to demonstrate mechanics, not to infer a real-world effect. Bootstrap resampling can approximate uncertainty for some statistics, but it also depends on a representative sample and a suitable resampling scheme (blocks/groups for dependence).


## Practice

[Questions](../../assignments/STAT-002/questions.md) · [Solutions](../../assignments/STAT-002/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
