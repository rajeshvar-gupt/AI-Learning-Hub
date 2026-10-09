"""Numerical foundations using fixed invented observations; no external data."""
import json
import math
import numpy as np
from scipy import stats


def gradient_descent(start=0.0, rate=0.1, steps=100):
    if not math.isfinite(start) or not math.isfinite(rate) or not 0 < rate < 1:
        raise ValueError("finite start and rate between 0 and 1 required")
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 1:
        raise ValueError("steps must be a positive integer")
    w = float(start)
    losses = [(w - 3) ** 2]
    for _ in range(steps):
        w -= rate * 2 * (w - 3)
        losses.append((w - 3) ** 2)
    return w, losses


def summarize(values, null_mean=10.0):
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or len(x) < 2 or not np.isfinite(x).all():
        raise ValueError("at least two finite one-dimensional observations required")
    if not math.isfinite(null_mean):
        raise ValueError("finite null mean required")
    sd = float(x.std(ddof=1))
    if sd == 0:
        raise ValueError("t inference requires nonzero sample variance")
    se = sd / np.sqrt(len(x))
    margin = stats.t.ppf(.975, df=len(x)-1) * se
    test = stats.ttest_1samp(x, popmean=null_mean)
    return dict(n=len(x), mean=float(x.mean()), median=float(np.median(x)),
                sample_sd=sd, standard_error=float(se),
                mean_ci95=[float(x.mean()-margin), float(x.mean()+margin)],
                null_mean=null_mean, t=float(test.statistic), p=float(test.pvalue))


def main():
    w, losses = gradient_descent()
    report = dict(optimized_w=w, initial_loss=losses[0], final_loss=losses[-1],
                  statistics=summarize([9, 11, 12, 10, 13, 11, 8, 12]))
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
