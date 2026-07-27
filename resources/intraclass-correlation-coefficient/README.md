# Intraclass Correlation Coefficient Worked Resource

The intraclass correlation coefficient, or **ICC**, measures reliability or agreement among repeated ratings, raters, measurements, devices, or time points. Unlike an ordinary correlation, the ICC is model-dependent. A numerical ICC is not interpretable unless the model, unit of analysis, and definition of agreement are stated.

For a full explanation of ICC models, formulas, confidence intervals, interpretation, and SPSS, Python, R, and Excel workflows, use the [complete intraclass correlation coefficient guide](https://onlineinternetcafe.com/intraclass-correlation-coefficient-icc-formula-interpretation-spss-python-r-and-excel-guide/).

## Quick answer

Before calculating an ICC, answer four questions:

1. Is the model **one-way** or **two-way**?
2. Are rater effects **random** or **fixed/mixed**?
3. Is reliability needed for a **single measurement** or an **average of measurements**?
4. Is the target **consistency** or **absolute agreement**?

These decisions determine which ICC is appropriate. Reporting only “ICC = 0.82” is incomplete.

## Reliability versus agreement

### Consistency

Consistency asks whether raters preserve the relative ordering of subjects. A rater who scores everyone five points higher may still show high consistency.

### Absolute agreement

Absolute agreement asks whether raters assign the same numerical values. Systematic rater differences reduce absolute-agreement ICC.

Choose the definition based on the intended use of the measurement.

## One-way and two-way models

### One-way random-effects model

Use when each subject may be rated by a different random subset of raters and rater identity is not modeled separately.

### Two-way random-effects model

Use when the same raters assess all subjects and the raters are considered a random sample from a broader population. Results may be generalized beyond the observed raters.

### Two-way mixed-effects model

Use when the same specific raters assess all subjects and inference is restricted to those raters. Subjects are commonly random, while raters are fixed.

## Single-measure and average-measure ICC

### Single-measure ICC

Estimates reliability for one rating, one occasion, or one device measurement.

### Average-measure ICC

Estimates reliability of the mean of `k` ratings. Averaging usually reduces random error, so the average-measure ICC is often larger.

Report the version that matches how scores will actually be used.

## Variance-components logic

ICC is based on partitioning total variation into meaningful components such as:

- Between-subject variance
- Between-rater variance
- Subject-by-rater interaction
- Residual measurement error

A simplified reliability concept is:

`ICC = between-subject variance / total relevant variance`

The exact denominator changes with the selected model and agreement definition.

## Data structure

A common wide-format dataset has one row per subject and one column per rater. Long format has one row per subject-rater measurement and includes columns for subject, rater, and score.

Before analysis, verify:

- Every subject has the intended measurements.
- Rater identifiers are correct.
- Missing ratings are handled consistently.
- Scores use the same scale and direction.
- No accidental duplicate rows exist.

## Recommended workflow

1. Define the reliability target.
2. Identify whether raters are fixed or sampled.
3. Decide between consistency and absolute agreement.
4. Decide between single and average measurements.
5. Inspect rater means, distributions, and subject profiles.
6. Check for systematic rater bias and extreme disagreements.
7. Calculate the ICC with a confidence interval.
8. Report the exact model and interpretation.
9. Consider complementary agreement plots when absolute agreement matters.

## Interpreting the magnitude

Rules such as poor, moderate, good, and excellent are context-dependent. Reliability requirements differ for exploratory research, group-level comparison, individual diagnosis, and high-stakes decisions.

Interpretation should consider:

- Confidence-interval width
- Number of subjects
- Number of raters
- Range of true subject differences
- Measurement purpose
- Consequences of error

A high ICC can arise partly because subjects are very heterogeneous. A low ICC can occur in a restricted sample even when absolute measurement error is modest.

## Confidence intervals

The confidence interval indicates uncertainty around the ICC estimate. A wide interval may include both unacceptable and acceptable reliability levels. Report the interval rather than only the point estimate.

Small subject samples often produce unstable intervals. Increasing the number of subjects usually improves precision more directly than increasing the number of raters, although the optimal design depends on the application.

## ICC versus Pearson correlation

Pearson correlation measures linear association. Two raters can have `r = 1.00` even when one consistently scores ten points higher. Absolute-agreement ICC would detect that disagreement.

Use Pearson correlation for association questions, not as a replacement for reliability or agreement analysis.

## ICC versus Cohen’s kappa

ICC is typically used for continuous or approximately continuous scores. Cohen’s kappa is used for categorical ratings. Weighted kappa may be used for ordinal categories.

## Reporting checklist

A complete ICC report should include:

- Number of subjects
- Number and type of raters or measurements
- One-way or two-way model
- Random or mixed effects
- Consistency or absolute agreement
- Single or average measurement
- ICC estimate
- Confidence interval
- F test when relevant
- Software and model specification
- Practical interpretation

## Example reporting language

> Inter-rater reliability was estimated using a two-way random-effects, absolute-agreement, single-measure ICC because the same raters evaluated every subject and the raters were treated as a sample from a broader population. The ICC was 0.84 with a 95% confidence interval from 0.72 to 0.92, indicating good reliability for a single rating in this sample.

For an average-measure result:

> Reliability of the mean of three raters was estimated using the corresponding average-measure ICC. The result was higher than the single-measure coefficient, reflecting the reduction in random error obtained by averaging ratings.

## Common mistakes

- Reporting ICC without the model
- Confusing consistency with agreement
- Reporting average-measure ICC when decisions use one rater
- Treating raters as random when inference is restricted to specific raters
- Ignoring confidence intervals
- Comparing ICC values calculated from different models
- Using correlation as proof of agreement
- Interpreting a high ICC without checking systematic bias

## Complementary diagnostics

Depending on the application, add:

- Bland–Altman plots
- Rater mean comparisons
- Subject profile plots
- Measurement-error estimates
- Standard error of measurement
- Minimal detectable change
- Variance-component tables

These reveal aspects of agreement not summarized by one coefficient.

## Software consistency notes

Different packages may label the same model using notation such as ICC(1,1), ICC(2,1), ICC(3,1), single random raters, average random raters, consistency, or absolute agreement. Confirm the underlying model rather than relying only on labels.

Also verify:

- Missing-data handling
- Whether raters are rows or columns
- Single versus average measures
- Confidence-level method
- Degrees-of-freedom calculation
- Whether negative estimates are retained or truncated

## Practice dataset

The synthetic CSV contains 30 subjects measured by three raters. Suggested exercises:

1. Plot rater scores by subject.
2. Compare rater means.
3. Calculate single-measure consistency ICC.
4. Calculate single-measure absolute-agreement ICC.
5. Calculate average-measure ICC.
6. Explain why the values differ.
7. Create an agreement plot for two selected raters.

## Frequently asked questions

### Which ICC should I use for the same fixed judges rating every subject?

A two-way mixed-effects model is commonly appropriate, with consistency or absolute agreement selected according to the purpose.

### Why is the average-measure ICC higher?

Averaging several measurements reduces random measurement error.

### Can ICC be negative?

Yes. Sampling variation or very poor reliability can produce a negative estimate. It should be interpreted as no evidence of positive reliability rather than as meaningful negative reliability.

### Is 0.75 always good reliability?

No universal threshold applies. The acceptable level depends on the decision and consequences of measurement error.

## Complete learning guide

The full Salar Cafe resource explains model selection, variance components, confidence intervals, interpretation, reporting, and software workflows:

[Open the complete ICC formula and interpretation guide](https://onlineinternetcafe.com/intraclass-correlation-coefficient-icc-formula-interpretation-spss-python-r-and-excel-guide/)

## Suggested citation

Saqib, M. Y. (2026). *Intraclass Correlation Coefficient: ICC Formula, Interpretation, SPSS, Python, R and Excel Guide*. Salar Cafe. https://onlineinternetcafe.com/intraclass-correlation-coefficient-icc-formula-interpretation-spss-python-r-and-excel-guide/