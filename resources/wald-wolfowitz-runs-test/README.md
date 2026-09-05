# Wald–Wolfowitz Two-Sample Runs Test

This resource explains the **two-sample Wald–Wolfowitz runs test**, a nonparametric procedure for evaluating whether two independent samples could have come from the same continuous population distribution.

The method should not be confused with the one-sample runs test for randomness. In the two-sample procedure, observations from both groups are pooled and sorted by the measured outcome. Each ordered observation is then replaced by its group label. The test statistic is the number of uninterrupted blocks, or **runs**, in that ordered label sequence.

For a complete worked analysis with formulas, tie-order sensitivity, SPSS, Python, R and Excel workflows, see the [Wald Wolfowitz runs test guide at Salar Cafe](https://onlineinternetcafe.com/wald-wolfowitz-runs-test/).

## Files

- `wald_wolfowitz_example.csv` — synthetic, tie-free two-group practice data.
- `wald_wolfowitz_runs_test.py` — transparent Python implementation of the observed run count, large-sample statistic and a doubled-tail exact probability for tie-free samples.

## Research question

> Do the complete population distributions represented by Group A and Group B differ?

The null and alternative hypotheses are:

- **H₀:** `F_A(x) = F_B(x)` for every value of `x`.
- **H₁:** The two cumulative distribution functions differ for at least one value of `x`.

A rejection is broader than a claim about means or medians. It may reflect a difference in location, spread, shape, tails, or a combination of distributional features.

## Data dictionary

| Variable | Type | Meaning |
|---|---|---|
| `value` | Numeric outcome | Measurement used to order the pooled observations |
| `group` | Binary categorical | Independent sample membership: `A` or `B` |

The example contains 10 observations in each group and no tied outcome values. Tie-free data are used because the standard exact distribution assumes a unique pooled order.

## Algorithm

1. Combine the observations from both independent samples.
2. Sort the pooled observations from smallest to largest.
3. Retain the group label attached to every observation.
4. Count one run for the first label.
5. Add one run whenever the current label differs from the preceding label.
6. Compare the observed run count with its null distribution.

For example, the ordered labels

```text
A A A B B A B B
```

contain four runs:

```text
AAA | BB | A | BB
```

## Large-sample formulas

Let `n1` and `n2` be the two sample sizes, `N = n1 + n2`, and `R` the observed number of runs.

The expected run count under the null hypothesis is

```text
E(R) = 1 + 2 n1 n2 / N
```

The usual tie-free variance is

```text
Var(R) = 2 n1 n2 (2 n1 n2 - N) / [N²(N - 1)]
```

The standardized statistic is

```text
z = [R - E(R)] / sqrt[Var(R)]
```

The script reports a two-sided normal-approximation probability using the standard normal distribution.

## Exact tie-free distribution

For an even number of runs, `R = 2k`,

```text
P(R = 2k) = 2 C(n1 - 1, k - 1) C(n2 - 1, k - 1) / C(N, n1)
```

For an odd number of runs, `R = 2k + 1`,

```text
P(R = 2k + 1) =
[C(n1 - 1, k) C(n2 - 1, k - 1)
 + C(n1 - 1, k - 1) C(n2 - 1, k)] / C(N, n1)
```

The included Python file constructs this finite-sample distribution and reports a doubled-tail exact probability. Exact two-sided conventions can differ across software, so the reporting method should always be named.

## Verified example result

Running the script on `wald_wolfowitz_example.csv` gives approximately:

| Quantity | Result |
|---|---:|
| Group A size | 10 |
| Group B size | 10 |
| Observed runs | 10 |
| Expected runs | 11.000000 |
| Run-count variance | 4.736842 |
| z statistic | -0.459468 |
| Two-sided normal p-value | 0.645898 |
| Doubled-tail exact p-value | 0.828141 |

At `α = 0.05`, the example does not provide evidence that the two complete distributions differ. The difference between the exact and normal probabilities also demonstrates why the exact distribution is preferable for small tie-free samples.

## Tie handling

Ties shared by both groups make the pooled label order non-unique. A secondary sort by group can manufacture an artificially small or large run count, so it should never be treated as if it were determined by the outcome.

Defensible options include:

- reporting the tie rule used by the selected software;
- obtaining minimum and maximum possible run counts within tied blocks;
- conducting a documented permutation procedure;
- using another two-sample method better suited to discrete outcomes.

IBM SPSS can report minimum and maximum possible runs when cross-group ties occur. The `statsmodels` two-sample implementation uses its own documented tie treatment and should not be assumed to reproduce SPSS exactly.

## Interpretation checklist

A complete report should identify:

- the two independent groups;
- the outcome used to order observations;
- both sample sizes;
- the observed and expected numbers of runs;
- the exact or asymptotic inference method;
- any continuity correction;
- the tie-handling rule;
- the test statistic and p-value;
- descriptive statistics or plots showing how the distributions differ.

A significant result establishes evidence against equality of the complete distributions. It does not identify causation and does not by itself prove that only the means, medians or variances differ.

## Suggested reporting template

> A two-sample Wald–Wolfowitz runs test was used to compare the complete outcome distributions for Group A (`n = ...`) and Group B (`n = ...`). After pooling and ordering the observations, the label sequence contained `R = ...` runs compared with `E(R) = ...` under the null model, `z = ...`, `p = ...`. The analysis used [exact/asymptotic] inference with [tie rule or no ties].

## Current Salar Cafe resources

- [Complete Wald–Wolfowitz runs test guide](https://onlineinternetcafe.com/wald-wolfowitz-runs-test/)
- [Wald–Wolfowitz runs test calculator](https://onlineinternetcafe.com/statistical-calculators/wald-wolfowitz-calculator/)
- [Runs test for randomness — one-sample procedure](https://onlineinternetcafe.com/runs-test/)
- [Mann–Whitney U test guide](https://onlineinternetcafe.com/mann-whitney-u-test/)
- [Two-sample Kolmogorov–Smirnov test guide](https://onlineinternetcafe.com/kolmogorov-smirnov/)
- [Moses test of extreme reactions](https://onlineinternetcafe.com/moses-test/)
- [Ansari–Bradley scale test guide](https://onlineinternetcafe.com/ansari-bradley-test/)
- [Parametric vs nonparametric tests](https://onlineinternetcafe.com/parametric-vs-nonparametric-tests/)
- [Nonparametric tests in Python](https://onlineinternetcafe.com/nonparametric-tests-in-python/)
- [Salar Statistics Analysis Studio](https://onlineinternetcafe.com/statistical-calculators/)

## Citation

Saqib, Muhammad Yar. (2026). *Wald–Wolfowitz Two-Sample Runs Test Learning Resource*. Salar Cafe Statistical Learning Resources. GitHub.

Complete companion guide: [Wald Wolfowitz Runs Test: Formula, Worked Example and Software Workflows](https://onlineinternetcafe.com/wald-wolfowitz-runs-test/).
