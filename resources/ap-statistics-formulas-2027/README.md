# AP Statistics Formulas 2027 — Reference Sheet Guide, Method Selection, and Worked Checks

This open learning resource is a compact companion for students and teachers preparing for the revised AP Statistics course and the May 2027 exam. It focuses on a skill that matters more than memorizing isolated equations: **choosing the correct statistical relationship for the question, checking the conditions, carrying out the calculation, and interpreting the result in context**.

The full interactive companion is available at **[AP Statistics Formula Sheet 2027 — Salar Cafe](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**.

## Why this resource exists

A formula sheet can tell you what mathematical relationships are available, but it does not decide which procedure matches a research question. Students still need to identify the variable type, parameter, design, inferential goal, conditions, and scope of inference before using a calculator or formula.

This repository resource therefore organizes the current AP Statistics reference relationships by **purpose** rather than by symbol alone.

## Current 2026–27 course context

The revised AP Statistics course is effective for the 2026–27 school year. The former eight-unit structure was consolidated into five units, and several older topics were removed, including geometric distributions, combining random variables, chi-square goodness-of-fit, and inference for a population regression slope.

The May 2027 exam is fully digital in Bluebook. Students complete 42 multiple-choice questions and 4 free-response questions. Reference information is available in Bluebook and is also provided in printed form. Approved graphing calculators remain permitted.

This means a useful study resource should not merely reproduce equations. It should train students to decide:

1. What quantity is being estimated, tested, predicted, or described?
2. Is the response variable categorical or quantitative?
3. Is the design one-sample, two-sample, paired, tabular, or regression-based?
4. Is the goal descriptive, inferential, or predictive?
5. Are the relevant conditions satisfied?
6. What formula or procedure matches the design?
7. What conclusion is justified by the sampling or assignment mechanism?

## Five-unit study map

### Unit 1 — Exploring One-Variable Data and Collecting Data

Primary ideas include descriptive statistics, graphical summaries, center, spread, z-scores, percentiles, sampling methods, experiments, bias, random sampling, and random assignment.

Important relationships include the sample mean and sample standard deviation. Students should also know when median and IQR are more informative than mean and standard deviation.

### Unit 2 — Probability, Random Variables, and Probability Distributions

Primary ideas include probability rules, conditional probability, discrete random variables, expected value, standard deviation of a random variable, and the binomial distribution.

Important relationships include the addition rule, conditional probability, discrete random-variable mean and standard deviation, and binomial probability, mean, and standard deviation.

### Unit 3 — Inference for Categorical Data: Proportions

Primary ideas include sampling distributions of sample proportions, confidence intervals, hypothesis tests, two-proportion comparisons, and chi-square methods for categorical association.

A central exam distinction is that a two-proportion confidence interval uses an **unpooled** standard error, while the usual two-proportion z test of equality uses a **pooled** null standard error.

### Unit 4 — Inference for Quantitative Data: Means

Primary ideas include sampling distributions of sample means, one-sample t procedures, two-sample t procedures, and paired t procedures.

Paired data should be converted to a single list of differences and analyzed as a one-sample mean problem. Treating matched observations as independent groups discards the matching structure.

### Unit 5 — Regression Analysis

Primary ideas include least-squares regression, prediction, residuals, correlation, coefficient of determination, and interpretation of linear association.

Regression analysis remains in the revised course, but inference for the population regression slope is no longer a current AP Statistics exam topic.

## Formula families by purpose

### Describing quantitative data

- Sample mean: `x̄ = Σxᵢ / n`
- Sample standard deviation: `s = √[Σ(xᵢ − x̄)² / (n − 1)]`
- z-score, a must-know relationship: `z = (x − μ) / σ`
- Interquartile range: `IQR = Q3 − Q1`

Use these to summarize location and spread. Before choosing mean and standard deviation, inspect the distribution for strong skew or influential outliers.

### Probability

- Addition rule: `P(A ∪ B) = P(A) + P(B) − P(A ∩ B)`
- Conditional probability: `P(A | B) = P(A ∩ B) / P(B)`

The subtraction term in the addition rule prevents the overlap from being counted twice. Conditional probability changes the reference set to outcomes in which the conditioning event has occurred.

### Discrete random variables

- Mean: `μX = Σ xᵢ P(xᵢ)`
- Standard deviation: `σX = √[Σ(xᵢ − μX)² P(xᵢ)]`

The expected value is a long-run average and does not need to be one of the values the random variable can actually take.

### Binomial distribution

- Exact probability: `P(X = x) = C(n,x)pˣ(1−p)ⁿ⁻ˣ`
- Mean: `μ = np`
- Standard deviation: `σ = √[np(1−p)]`

Before using the binomial model, verify a fixed number of trials, two outcomes per trial, independence, and a constant probability of success.

### General inference structure

- Standardized test statistic: `(statistic − null parameter) / null-model standard error`
- Confidence interval: `statistic ± (critical value)(standard error)`

A hypothesis test asks whether the observed statistic would be unusually far from a null value if the null model were true. A confidence interval estimates a population parameter with a range of plausible values.

### Chi-square

- `χ² = Σ (Observed − Expected)² / Expected`

In the current revised course, chi-square work focuses on independence and homogeneity rather than the removed goodness-of-fit topic.

### Sampling distribution of a sample proportion

- `μp̂ = p`
- `σp̂ = √[p(1−p)/n]`
- Estimated interval SE: `SE(p̂) = √[p̂(1−p̂)/n]`

The theoretical sampling-distribution standard deviation uses the population proportion `p`; a confidence interval estimates the unknown standard error using `p̂`.

### Difference between two sample proportions

- Center: `μ(p̂1−p̂2) = p1−p2`
- Theoretical SD: `√[p1(1−p1)/n1 + p2(1−p2)/n2]`
- Unpooled estimated SE for intervals: `√[p̂1(1−p̂1)/n1 + p̂2(1−p̂2)/n2]`
- Pooled proportion under `H0: p1=p2`: `p̂c = (x1+x2)/(n1+n2)`
- Pooled null SE: `√[p̂c(1−p̂c)(1/n1 + 1/n2)]`

This family is a frequent source of errors. **Do not pool for a two-proportion confidence interval. Pool for the usual two-proportion z test of equality because the null model assumes a common proportion.**

### Sampling distribution of a sample mean

- `μx̄ = μ`
- `σx̄ = σ/√n`
- Estimated SE: `SE(x̄) = s/√n`

Larger samples reduce sampling variability by the square root of the sample size, not directly in proportion to `n`.

### Difference between two sample means

- Center: `μ(x̄1−x̄2) = μ1−μ2`
- Theoretical SD: `√(σ1²/n1 + σ2²/n2)`
- Estimated SE: `√(s1²/n1 + s2²/n2)`

For paired observations, do **not** use the independent two-sample standard error. Create one difference per pair and use a one-sample t procedure on the differences.

### Regression

- Least-squares prediction: `ŷ = a + bx`
- Residual: `e = y − ŷ`
- Slope from summaries: `b = r(sy/sx)`
- Intercept: `a = ȳ − bx̄`
- Coefficient of determination: `r²`

A residual is observed minus predicted. A positive residual means the model underpredicted the response. `r²` describes the proportion of variation in the response explained by the linear relationship with the explanatory variable.

## A practical method-selection sequence

Use this order before calculating:

| Question | Decision |
|---|---|
| What kind of response variable? | Categorical → proportions/chi-square; quantitative → means/regression |
| How many groups or variables? | One sample, two independent groups, paired data, two-way table, or two quantitative variables |
| What is the goal? | Describe, estimate, test, compare, or predict |
| What was the design? | Random sample, randomized experiment, observational study, census, convenience sample, etc. |
| Which conditions matter? | Independence, large counts, shape/sample-size conditions, expected counts, or linear-model checks |
| What can the conclusion claim? | Generalization depends on sampling; causation depends on random assignment |

## Worked check 1 — one-proportion confidence interval

Suppose 118 of 200 randomly sampled students favor a new tutoring program.

1. Sample proportion: `p̂ = 118/200 = 0.59`.
2. Estimated standard error: `√[0.59(0.41)/200] ≈ 0.0348`.
3. Approximate 95% margin of error: `1.96(0.0348) ≈ 0.0682`.
4. Interval: approximately `(0.522, 0.658)`.

Interpretation: under the sampling assumptions, we are about 95% confident that the population proportion favoring the program is between 52.2% and 65.8%.

## Worked check 2 — two-proportion test

Suppose Group A has 84 successes in 120 observations and Group B has 70 successes in 110 observations. To test equality of population proportions:

- `p̂1 = 84/120 = 0.700`
- `p̂2 = 70/110 ≈ 0.636`
- Pooled proportion under the null: `p̂c = 154/230 ≈ 0.6696`
- Null standard error: `√[0.6696(1−0.6696)(1/120+1/110)] ≈ 0.0621`
- `z ≈ (0.700−0.636)/0.0621 ≈ 1.03`

The important concept is not the final z value alone. The pooled standard error is appropriate because the null hypothesis assumes the two population proportions are equal.

## Worked check 3 — paired data

Suppose the same 12 students are measured before and after tutoring. Let `d = after − before`, with `d̄ = 4.1` and `sd = 5.2`.

- `SE(d̄) = 5.2/√12 ≈ 1.50`
- A test of `H0: μd = 0` gives `t ≈ 4.1/1.50 ≈ 2.73`

This is a **one-sample t problem on the differences**, not an independent two-sample t problem.

## Common exam errors

- Using a formula before identifying the parameter.
- Pooling two proportions for a confidence interval.
- Failing to pool in the usual two-proportion equality test.
- Treating paired observations as independent samples.
- Confusing random sampling with random assignment.
- Treating statistical significance as practical importance.
- Interpreting a p-value as the probability that the null hypothesis is true.
- Claiming causation from observational association.
- Extrapolating a regression line far beyond the observed explanatory-variable range.
- Reporting calculator output without explaining what the result means in context.

## Files in this resource

- [`reference-sheet-map.md`](reference-sheet-map.md) — relationship-by-relationship purpose map.
- [`method-selection-and-conditions.md`](method-selection-and-conditions.md) — procedure-selection and condition checks.
- [`practice-prompts.md`](practice-prompts.md) — original short practice prompts with answers.

## Interactive companion

For expanded explanations, worked examples, formula-specific guidance, and interactive calculation tools, use:

**[AP Statistics Formula Sheet 2027: Formulas, Tables, and How to Use It — Salar Cafe](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**

## Source alignment

Course and exam structure in this repository was checked against the College Board AP Statistics Course and Exam Description effective Fall 2026 and the AP Statistics revisions information for the May 2027 exam. The explanatory text and practice examples here are original educational material.

AP and College Board are trademarks of College Board. This repository is an independent educational resource and is not affiliated with or endorsed by College Board.