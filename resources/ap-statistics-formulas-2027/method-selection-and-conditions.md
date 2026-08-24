# AP Statistics Method Selection and Conditions Guide

This guide is designed to answer the question students most often get wrong before any calculation begins: **Which statistical method actually matches the problem?**

Interactive companion: **[AP Statistics Formula Sheet 2027 — Salar Cafe](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**

## Step 1 — Identify the response variable

### Categorical response

Typical targets are proportions, differences between proportions, or association between categorical variables.

Common procedures:

- One-proportion confidence interval
- One-proportion z test
- Two-proportion confidence interval
- Two-proportion z test
- Chi-square test of independence/homogeneity

### Quantitative response

Typical targets are means, differences between means, or prediction from another quantitative variable.

Common procedures:

- One-sample t confidence interval/test
- Two-sample t confidence interval/test
- Paired t procedure
- Least-squares regression

## Step 2 — Determine the structure

| Structure | Typical question | Procedure family |
|---|---|---|
| One categorical sample | What proportion has the characteristic? | One-proportion z |
| Two independent categorical groups | Do the proportions differ? | Two-proportion z |
| Two categorical variables | Are the variables associated? | Chi-square |
| One quantitative sample | What is the population mean? | One-sample t |
| Two independent quantitative groups | Do population means differ? | Two-sample t |
| Matched quantitative observations | Is the average pairwise difference nonzero? | Paired t |
| Two quantitative variables | How are x and y linearly related? | Regression |

## Step 3 — Distinguish estimation from testing

### Confidence interval

A confidence interval estimates a parameter. Its structure is:

`statistic ± critical value × standard error`

A strong interpretation identifies the **population parameter** and gives the interval in context.

### Hypothesis test

A hypothesis test evaluates evidence against a null claim. Its standardized structure is:

`(observed statistic − null parameter) / null-model standard error`

A p-value is the probability, **assuming the null model is true**, of obtaining a result at least as extreme as the observed result. It is not the probability that the null hypothesis is true.

## Step 4 — Check design before inference

### Random sampling

Random sampling supports generalization from the sample to the population represented by the sampling process.

### Random assignment

Random assignment supports causal comparisons between treatments, assuming the experiment is otherwise well conducted.

### Observational study

An observational association does not by itself prove causation because confounding variables may explain some or all of the relationship.

## Step 5 — Check procedure-specific conditions

### One-proportion z procedures

Check:

- Appropriate random/representative sampling or experimental design
- Independence of observations
- Sample size small relative to the population when sampling without replacement
- Large-count condition appropriate to the procedure

For a confidence interval, the large-count check is usually based on observed successes and failures. For a test, the null value is used in the null-model count condition.

### Two-proportion z procedures

Check:

- Independent groups/samples
- Appropriate randomization
- Independence within groups
- Large counts in both groups

Important distinction:

- Confidence interval → unpooled standard error
- Equality test → pooled null standard error

### One-sample t procedures

Check:

- Independent observations
- Appropriate sampling/design
- Quantitative response
- Distribution shape/sample size adequate for t inference

As sample size grows, t procedures become more robust to moderate non-Normality, but severe skew or influential outliers still deserve attention.

### Two-sample t procedures

Check:

- Two independent groups
- Independent observations within each group
- Appropriate sampling/design
- Quantitative response
- Shape/sample-size conditions for each group

Do not automatically pool sample variances. The usual AP Statistics two-sample t framework does not require an equal-variance assumption.

### Paired t procedures

Check:

- A defensible pairing or repeated-measures structure
- Independence between pairs
- Quantitative pairwise differences
- Shape/sample-size conditions applied to the distribution of the **differences**

The unit of analysis is the pairwise difference, not the two raw columns separately.

### Chi-square independence/homogeneity

Check:

- Data are counts, not percentages or measurements
- Observations are independent
- Expected counts are sufficiently large for the chi-square approximation

Expected count for a cell:

`(row total × column total) / grand total`

### Regression

Before interpreting a least-squares model, examine whether a linear model is sensible. Relevant checks include:

- Two quantitative variables
- Approximate linear pattern
- No dominant influential observations
- Residual pattern compatible with the fitted model
- Avoidance of unjustified extrapolation

The revised AP Statistics course still includes regression analysis, but inference for a population regression slope is not a current 2027 exam topic.

## Method-selection examples

### Example A — one proportion

A random sample of students is asked whether they support a new schedule. The research question concerns a single population proportion.

Use a one-proportion procedure.

### Example B — two proportions

Two independent schools are sampled and their graduation-plan proportions are compared.

Use a two-proportion procedure.

### Example C — paired means

The same students take a test before and after tutoring.

Compute `after − before` for each student and use a one-sample t procedure on those differences.

### Example D — chi-square

Students are classified by grade level and preferred learning format. The question asks whether the two categorical variables are associated.

Use chi-square independence/homogeneity logic.

### Example E — regression

A sample records weekly study hours and exam score for each student. The goal is to describe or predict the linear relationship.

Use regression analysis, while keeping causal claims separate from association unless random assignment is present.

## Common wrong-method traps

1. **Using two-sample t for paired data.** The matching structure has been lost.
2. **Pooling proportions for a confidence interval.** Pooling belongs to the usual equality test, not the interval.
3. **Using means for a categorical response.** A proportion or categorical method is usually required.
4. **Using chi-square on percentages without counts.** Chi-square calculations are built from observed and expected counts.
5. **Treating a random sample as an experiment.** Random sampling does not create treatment groups.
6. **Treating random assignment as a representative sample.** Random assignment alone does not guarantee population generalization.
7. **Using a regression line far outside the observed x range.** This is extrapolation.
8. **Interpreting p < 0.05 as a large effect.** Statistical and practical significance are different ideas.

## Interpretation templates

### Confidence interval

“We are ___% confident that the population [parameter] lies between ___ and ___.”

### Hypothesis test

“Because the p-value is ___, there is [sufficient/insufficient] evidence that [contextual alternative claim].”

### Regression slope

“For each additional 1 [x-unit], the predicted [response] changes by about ___ [y-units], on average.”

### Coefficient of determination

“About ___% of the variation in [response] is explained by the linear relationship with [explanatory variable].”

### Residual

“The model [underpredicted/overpredicted] this observation by about ___ units.”

## Final decision checklist

Before submitting an answer, verify:

- Parameter identified
- Variable type identified
- Group structure identified
- Design identified
- Correct procedure selected
- Conditions checked
- Formula inputs preserve group order and units
- Calculator output interpreted in context
- Scope of inference matches the design

For formula-by-formula explanations and interactive tools, continue to **[AP Statistics Formula Sheet 2027](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**.