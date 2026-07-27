# Tukey HSD Test Worked Resource

Tukey’s honestly significant difference test is a post-hoc procedure used to compare all pairs of group means while controlling the familywise Type I error rate. It is most commonly applied after a one-way ANOVA when the omnibus test indicates that at least one population mean differs.

For formulas, simultaneous confidence intervals, software output, and detailed interpretation, use the [complete Tukey HSD test guide](https://onlineinternetcafe.com/tukey-hsd-test/).

## Quick answer

Tukey HSD answers the question: **Which specific pairs of means differ after the overall ANOVA?**

It is designed for all pairwise comparisons and provides adjusted p-values or simultaneous confidence intervals. A pair is statistically significant when its adjusted p-value is below the selected alpha level or when its confidence interval for the mean difference excludes zero.

## Why a post-hoc adjustment is needed

With `k` groups, the number of pairwise comparisons is:

`k(k − 1) / 2`

As the number of comparisons increases, the probability of at least one false positive increases. Tukey’s procedure controls the error rate across the complete family of pairwise comparisons.

## Core formula

For equal sample sizes, the honestly significant difference is commonly written as:

`HSD = qcritical × √(MSE / n)`

where:

- `qcritical` is a critical value from the studentized range distribution.
- `MSE` is the within-group mean square from the ANOVA.
- `n` is the common group sample size.

For unequal sample sizes, software usually applies the Tukey–Kramer extension. The standard error then depends on the two group sizes being compared.

## What the result contains

A typical Tukey table reports:

- The two groups being compared
- Estimated mean difference
- Standard error
- Adjusted p-value
- Lower simultaneous confidence limit
- Upper simultaneous confidence limit

The sign of the mean difference depends on the subtraction order. Always identify whether the software reports `Group A − Group B` or the reverse.

## Assumptions

Tukey HSD inherits the major assumptions of the underlying ANOVA:

### Independent observations

Scores from different participants or experimental units should be independent.

### Continuous outcome

The outcome should be measured on a scale for which group means are meaningful.

### Approximate normality within groups

Moderate deviations may be tolerable, especially with reasonably balanced samples, but severe skewness or extreme outliers can affect conclusions.

### Homogeneity of variances

Classic Tukey HSD assumes comparable within-group variances. When variances and sample sizes differ substantially, Games–Howell is often a better follow-up procedure.

## Recommended workflow

1. Inspect group counts, means, standard deviations, and plots.
2. Check outliers and variance equality.
3. Run the omnibus ANOVA.
4. If the ANOVA is significant and all-pairs comparisons are appropriate, run Tukey HSD.
5. Interpret adjusted confidence intervals and p-values.
6. Report the size and direction of important pairwise differences.
7. Connect the pairwise results to the original research question.

## Interpreting confidence intervals

A Tukey simultaneous confidence interval represents a plausible range for a pairwise mean difference while preserving the selected familywise confidence level.

- If the interval excludes zero, the pair differs significantly.
- If the interval includes zero, the comparison is not significant at the familywise alpha level.
- The width shows uncertainty and depends on within-group variability and sample size.
- Statistical significance does not indicate whether the difference is practically important.

## Relationship with the omnibus ANOVA

The omnibus ANOVA tests whether all group means can be treated as equal. It does not identify the differing groups. Tukey HSD decomposes that overall evidence into pairwise comparisons.

It is possible in unusual situations for the omnibus test and a multiple-comparison procedure to appear inconsistent because they test different hypotheses and use different critical values. The analysis plan should specify how follow-up tests are handled rather than using whichever result is most favorable.

## When Games–Howell may be preferable

Games–Howell is commonly selected when:

- Group variances are unequal.
- Sample sizes are unequal.
- Welch’s ANOVA is used as the omnibus test.

It does not pool one common within-group variance in the same way as Tukey HSD. The choice should be based on the design and diagnostics, not on which method produces smaller p-values.

## Reporting checklist

Include:

- The omnibus ANOVA result
- Reason for selecting Tukey HSD
- Familywise alpha level
- Group means and sample sizes
- Pairwise mean differences
- Simultaneous confidence intervals
- Adjusted p-values
- Direction of each important difference
- Effect-size or practical interpretation when available

## Example reporting language

> The omnibus one-way ANOVA indicated that mean scores differed among the four groups. Tukey HSD comparisons showed that Group C had a higher mean than Group A, with the simultaneous confidence interval excluding zero. The comparisons between Groups B and D and between Groups C and D were not statistically significant after familywise adjustment.

## Common mistakes

- Running many ordinary t tests without adjustment
- Reporting only significance stars
- Ignoring the direction of subtraction
- Treating non-significant pairs as exactly equal
- Using classic Tukey HSD despite severe variance inequality
- Performing every possible pairwise comparison when only planned contrasts are relevant
- Reporting adjusted p-values as if they were unadjusted
- Omitting group means and confidence intervals

## Planned contrasts versus Tukey HSD

Tukey HSD is designed for all pairwise comparisons. If the research question specifies a small number of theoretically motivated contrasts before examining the data, planned contrasts may be more direct and powerful. The choice should follow the scientific question.

## Software consistency notes

Before comparing outputs, verify:

- Whether equal-size Tukey or Tukey–Kramer calculations were used
- The familywise confidence level
- The ANOVA error term
- Missing-value handling
- Group ordering
- Whether p-values are multiplicity-adjusted
- Whether the reported difference is first minus second or second minus first

## Practice dataset

The CSV contains four groups with different mean levels. Suggested exercises:

1. Calculate group summaries.
2. Run a one-way ANOVA.
3. Apply Tukey HSD.
4. Recreate the simultaneous confidence intervals.
5. Compare the result with unadjusted pairwise t tests.
6. Increase one group variance and compare Tukey HSD with Games–Howell.

## Frequently asked questions

### Can Tukey HSD be used with only two groups?

It can, but with two groups it reduces to a single comparison, so a standard two-group method is usually simpler.

### Does Tukey HSD require equal group sizes?

The original simple formula assumes equal sizes, but the Tukey–Kramer form handles unequal group sizes. Severe imbalance combined with unequal variances still requires caution.

### Should Tukey HSD be used after Welch’s ANOVA?

Games–Howell is generally the more natural unequal-variance follow-up after Welch’s ANOVA.

### What does “honestly significant difference” mean?

It refers to the minimum pairwise difference required for significance under the studentized-range familywise adjustment.

## Complete learning guide

The full Salar Cafe resource explains formulas, assumptions, simultaneous intervals, adjusted p-values, reporting, and workflows for SPSS, Python, R, and Excel:

[Open the complete Tukey HSD test guide](https://onlineinternetcafe.com/tukey-hsd-test/)

## Suggested citation

Saqib, M. Y. (2026). *Tukey HSD Test: Formula, Interpretation, SPSS, Python, R and Excel Guide*. Salar Cafe. https://onlineinternetcafe.com/tukey-hsd-test/