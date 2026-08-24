# Validation Examples for Core Statistical Calculations

These examples provide small, hand-checkable reference calculations for several common statistical quantities. They are intended for teaching and for verifying that software or calculator settings match the intended formula.

The interactive companion is [Statistical Calculators Online](https://onlineinternetcafe.com/statistical-calculators/).

## Example 1 — sample mean and sample standard deviation

Data:

`2, 4, 5, 7, 8, 10`

### Mean

\[
\bar{x}=\frac{2+4+5+7+8+10}{6}=\frac{36}{6}=6.
\]

### Sample standard deviation

Squared deviations from 6 are:

`16, 4, 1, 1, 4, 16`

Their sum is 42. Therefore

\[
s^2=\frac{42}{6-1}=8.4
\]

and

\[
s=\sqrt{8.4}=2.898275349\ldots
\]

Reference values:

- n = 6
- mean = 6
- sample variance = 8.4
- sample SD ≈ 2.898275349

## Example 2 — Pearson correlation

Paired data:

| x | y |
|---:|---:|
| 2 | 5 |
| 4 | 8 |
| 5 | 7 |
| 7 | 11 |
| 8 | 13 |
| 10 | 14 |

Means:

- x̄ = 6
- ȳ = 9.666666667

Using

\[
r=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2\sum(y_i-\bar{y})^2}},
\]

the reference correlation is

\[
r\approx0.969458418.
\]

This indicates a strong positive linear relationship in this small synthetic example. It is not evidence of causation.

## Example 3 — simple linear regression

Using the same x and y values, the least-squares slope is

\[
b=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}
\approx1.190476190.
\]

The intercept is

\[
a=\bar{y}-b\bar{x}\approx2.523809524.
\]

Reference fitted line:

\[
\hat{y}=2.523809524+1.190476190x.
\]

For x=6, the fitted value equals the sample mean of y, approximately 9.666666667, because the least-squares line with an intercept passes through (x̄,ȳ).

## Example 4 — Welch two-sample t statistic

Group A:

`12, 15, 14, 10, 13, 16`

Group B:

`9, 11, 8, 12, 10, 9`

Reference summaries:

| Quantity | Group A | Group B |
|---|---:|---:|
| n | 6 | 6 |
| mean | 13.333333333 | 9.833333333 |
| sample SD | 2.160246899 | 1.471960144 |

Difference in sample means:

\[
\bar{x}_A-\bar{x}_B=3.5.
\]

Welch standard error:

\[
SE=\sqrt{\frac{s_A^2}{n_A}+\frac{s_B^2}{n_B}}
\approx1.067187373.
\]

Welch t statistic:

\[
t=\frac{3.5}{1.067187373}\approx3.279649000.
\]

Welch–Satterthwaite degrees of freedom:

\[
\nu=\frac{(s_A^2/n_A+s_B^2/n_B)^2}{(s_A^2/n_A)^2/(n_A-1)+(s_B^2/n_B)^2/(n_B-1)}
\approx8.819517314.
\]

These values verify the statistic and degrees-of-freedom calculation. A complete inferential conclusion still requires an alternative hypothesis, significance level, and appropriate design/assumption checks.

## Example 5 — chi-square statistic for a 2×2 table

Observed table:

| | Outcome 1 | Outcome 2 | Row total |
|---|---:|---:|---:|
| Group A | 30 | 20 | 50 |
| Group B | 15 | 35 | 50 |
| Column total | 45 | 55 | 100 |

Expected counts under independence are

\[
E_{ij}=\frac{(\text{row total})(\text{column total})}{\text{grand total}}.
\]

Therefore the expected table is:

| | Outcome 1 | Outcome 2 |
|---|---:|---:|
| Group A | 22.5 | 27.5 |
| Group B | 22.5 | 27.5 |

The Pearson chi-square statistic is

\[
\chi^2=\sum\frac{(O-E)^2}{E}\approx9.090909091.
\]

For a 2×2 table, df=(2−1)(2−1)=1.

The statistic quantifies departure from the expected table under independence. The p-value and substantive importance should be considered separately, and an effect-size measure can complement the test.

## Example 6 — two-proportion pooled standard error under an equality null

Suppose:

- Group A: 84 successes out of 120, so p̂₁=0.700000000
- Group B: 70 successes out of 110, so p̂₂≈0.636363636

For a test of H₀:p₁=p₂, the pooled estimate is

\[
\hat{p}_c=\frac{84+70}{120+110}=\frac{154}{230}\approx0.669565217.
\]

The pooled standard error is

\[
SE_0=\sqrt{\hat{p}_c(1-\hat{p}_c)\left(\frac{1}{120}+\frac{1}{110}\right)}
\approx0.062089230.
\]

The z statistic is

\[
z=\frac{0.700000000-0.636363636}{0.062089230}
\approx1.024917909.
\]

Important distinction: pooling is appropriate for this usual equality test because the null model assumes a common population proportion. A confidence interval for p₁−p₂ ordinarily uses an unpooled standard error.

## Validation philosophy

A calculator should be checked at more than one level:

1. **Input validation** — reject impossible or malformed values.
2. **Formula validation** — match published definitions and parameterization.
3. **Reference-case validation** — reproduce hand-checkable examples such as those above.
4. **Cross-software validation** — compare with another reliable implementation using identical options.
5. **Edge-case validation** — test zeros, ties, empty cells, small samples, boundary probabilities, singular models, or non-finite values where relevant.
6. **Interpretation validation** — confirm that explanatory text matches the actual statistic, alternative hypothesis, confidence level, and design.

The accompanying `validate_reference_examples.py` script verifies several of the numerical values in this document using only Python's standard library.