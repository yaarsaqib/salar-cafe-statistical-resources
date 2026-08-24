# Statistical Method Selection Guide

This guide is a compact decision aid for the companion [Statistical Calculators Online](https://onlineinternetcafe.com/statistical-calculators/) workspace. It is intentionally question-first: the correct procedure depends on the response type, number of groups or variables, dependence structure, and inferential goal.

## Step 1 — classify the response

| Response/data structure | Typical questions |
|---|---|
| One quantitative variable | center, spread, percentiles, distribution shape, one population mean |
| One binary/categorical variable | one population proportion, category frequencies |
| Two independent quantitative groups | difference in means/distributions |
| Paired quantitative observations | mean/median change within matched pairs |
| Three or more independent quantitative groups | omnibus group comparison, post-hoc contrasts |
| Repeated quantitative measurements | within-subject change across multiple occasions |
| Two categorical variables | association/independence in a contingency table |
| Two quantitative variables | association, prediction, line fitting |
| Multiple predictors | adjusted association or prediction |
| Binary outcome with predictors | probability/odds modeling |
| Time-to-event outcome | survival probability, hazard comparison/modeling |
| Multiple studies/effect estimates | evidence synthesis/meta-analysis |
| Ratings/repeated measurements | reliability or agreement |

## Step 2 — match the question to a method family

| Research goal | Data/design | Common starting method | Important checks |
|---|---|---|---|
| Describe one quantitative sample | one numeric vector | mean/median, SD/IQR, percentiles | missingness, outliers, skew |
| Estimate one population mean | one independent sample | one-sample t interval | sampling/design, independence, shape/sample size |
| Test one population mean | one independent sample | one-sample t test | same as above; null value and direction |
| Compare two means | two independent groups | Welch or independent-samples t test | independence, shape, variance treatment |
| Compare matched means | paired observations | paired t test | correct pairing, distribution of differences |
| Compare 3+ means | independent groups | one-way ANOVA / Welch ANOVA | independence, residual shape, variance pattern |
| Follow significant ANOVA | multiple groups | Tukey HSD or another planned post-hoc method | multiplicity, family of comparisons |
| Estimate one proportion | binary outcome | one-proportion interval | independence, count condition |
| Test one proportion | binary outcome | one-proportion z/binomial test | null proportion, count/exact requirements |
| Compare two proportions | independent groups | two-proportion z procedure | group independence, count condition, pooling rule |
| Test categorical association | contingency table | chi-square independence/homogeneity | expected counts, independent observations |
| Linear association | two quantitative variables | Pearson correlation | linearity, influential points, scale |
| Monotonic/ordinal association | ordinal or non-normal paired ranks | Spearman/Kendall | ties, monotonicity, independence |
| Predict quantitative y | one/multiple predictors | linear regression | linearity, residuals, influence, collinearity |
| Model binary y | predictors + binary outcome | logistic regression | separation, sample size/events, functional form |
| Compare distributions nonparametrically | independent groups | Mann–Whitney / Kruskal–Wallis | independence, interpretation of rank test |
| Compare paired ranks | paired observations | Wilcoxon signed-rank | symmetry assumptions for some interpretations |
| Assess normality | numeric sample/residuals | Q–Q plot + normality test | do not use test mechanically; sample size matters |
| Assess equal variances | groups | Levene/Brown–Forsythe | diagnostic purpose, robustness of main method |
| Diagnose heteroscedasticity | regression residuals | Breusch–Pagan / residual plots | model specification, robust SE alternative |
| Diagnose influential cases | regression | Cook's distance / leverage / DFBETAs | investigate, do not auto-delete |
| Assess rater/measurement reliability | repeated ratings | ICC / kappa / alpha depending design | model type, units, raters, agreement vs consistency |
| Compare diagnostic test performance | binary truth/test | sensitivity, specificity, predictive values, ROC | prevalence and sampling design |
| Analyze event times | censored time-to-event data | Kaplan–Meier / log-rank / Cox model | censoring, proportional hazards when applicable |
| Combine study effects | study-level estimates | fixed/random-effects meta-analysis | effect metric, heterogeneity, dependence, bias |
| Plan a study | proposed design | sample-size/power calculator | effect size, alpha, power, allocation, attrition |

## Step 3 — distinguish procedures that are often confused

### Independent t versus paired t

Use an independent-samples procedure when observations in one group have no natural one-to-one match with observations in the other group. Use a paired procedure when the same unit is measured twice or when units are explicitly matched. Pairing changes the sampling model and standard error.

### Student's t versus Welch's t

The conventional pooled-variance independent-samples t test assumes a common population variance. Welch's t test does not pool the two sample variances and is often a safer default when group variances and sample sizes differ. The question is not whether the sample SDs are exactly equal; it is whether the pooled model is appropriate for the design and data.

### One-way ANOVA versus Welch's ANOVA

Both address an omnibus comparison among independent group means. Welch's ANOVA is designed to be more robust to unequal variances, particularly when sample sizes are unequal.

### ANOVA versus post-hoc tests

An omnibus ANOVA asks whether all population means can be treated as equal under the model. A post-hoc procedure addresses which group differences are supported while controlling an appropriate error rate. A significant omnibus result does not name the differing groups.

### Pearson versus Spearman versus Kendall

Pearson correlation measures linear association on quantitative scales. Spearman correlation is based on ranks and measures monotonic association. Kendall's tau is based on concordant and discordant pairs and has useful variants for ties. The coefficients have different interpretations and should not be swapped merely because one yields a smaller p-value.

### Chi-square test versus proportion test

A 2×2 table can sometimes be expressed either as a two-proportion comparison or a chi-square association test. These may be mathematically related, but the framing, effect measures, and extensions differ. Choose the procedure from the research question and design.

### Confidence interval versus hypothesis test

A confidence interval estimates a plausible range for a parameter under a repeated-sampling procedure. A hypothesis test evaluates evidence against a specified null model. The calculations can be closely related, but the interpretation is not interchangeable.

### Statistical significance versus practical importance

A small p-value can arise from a very small effect in a large sample. A complete result should include a meaningful effect measure and uncertainty whenever possible.

## Assumption checklist by family

### Descriptive statistics

- Confirm the unit of observation.
- Identify missing and impossible values.
- Inspect shape and outliers before choosing center/spread summaries.
- Do not report excessive precision relative to the measurements.

### t procedures and ANOVA

- Observations should be independent within the sampling/model structure unless a paired/repeated method explicitly models dependence.
- Quantitative outcome should be meaningful on the chosen scale.
- Severe skew/outliers deserve attention, especially in small samples.
- Variance assumptions depend on the exact procedure; Welch methods treat them differently from pooled methods.

### Proportion procedures

- The numerator must be a count of target outcomes within a defined denominator.
- Observations should be independent or the dependence should be modeled.
- Normal-approximation procedures require suitable expected counts; exact alternatives may be preferable with sparse data.

### Chi-square procedures

- Work with counts, not a table of percentages entered as if they were observations.
- Observations should contribute to the table according to the design without inappropriate duplication.
- Inspect expected counts; sparse tables may require an exact or alternative method.

### Correlation and regression

- Plot the data before interpreting coefficients.
- Check whether the relationship is approximately linear when using linear methods.
- Inspect residuals for nonlinearity, unequal variance, and unusual observations.
- Distinguish influential observations from merely extreme observations.
- For multiple regression, inspect collinearity and model specification.

### Reliability and agreement

- Specify the unit of analysis and number/type of raters or measurements.
- Decide whether the target is consistency or absolute agreement.
- Match the ICC/kappa/alpha formulation to the design.
- Do not interpret one reliability coefficient without stating its model.

### Survival analysis

- Define time origin, event, and censoring clearly.
- Verify that censoring assumptions are plausible.
- For Cox models, evaluate proportional-hazards assumptions when relevant.

### Meta-analysis

- Use a consistent effect-size definition.
- Confirm that sampling variances correspond to that effect measure.
- Examine heterogeneity rather than reporting only a pooled point estimate.
- Consider dependence among effects from the same study.
- Publication-bias diagnostics are not definitive tests of bias.

## Reporting template

A concise statistical report can usually be built from the following structure:

1. **Question:** what population/process and parameter were studied?
2. **Data/design:** sample size, groups, pairing, repeated structure, or model variables.
3. **Method:** exact procedure and important options.
4. **Diagnostics/conditions:** what was checked and what was found?
5. **Estimate/effect:** mean difference, correlation, odds ratio, effect size, etc.
6. **Uncertainty:** standard error or confidence interval where relevant.
7. **Test result:** statistic, degrees of freedom, and p-value where relevant.
8. **Conclusion:** plain-language interpretation in context.
9. **Limits:** what the design cannot establish.

## Interactive implementation

After choosing the method, open the matching calculator in **[Statistical Calculators Online](https://onlineinternetcafe.com/statistical-calculators/)**. The workspace is designed to keep method choice, assumptions, calculation, diagnostics, and interpretation connected rather than treating the calculator as an isolated number generator.