# AP Statistics 2027 Practice Prompts — Formula Choice Before Calculation

These original prompts are designed to train method selection, conditions, and interpretation. They are not reproduced College Board questions.

Interactive companion: **[AP Statistics Formula Sheet 2027 — Salar Cafe](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**

## 1. One proportion

A random sample of 160 students finds that 104 support a new attendance policy.

**Tasks**

1. Identify the parameter.
2. Compute the sample proportion.
3. State the standard-error relationship for a confidence interval.
4. Explain what random sampling allows you to conclude.

**Check**

- Parameter: population proportion of students who support the policy.
- `p̂=104/160=0.65`.
- Interval SE: `√[p̂(1−p̂)/n]`.
- Random sampling supports generalization to the population represented by the sampling frame, assuming the design is implemented appropriately.

## 2. Two proportions — interval or test?

In two independent samples, 72 of 100 students in School A and 63 of 105 students in School B favor a new program.

**Tasks**

1. If the goal is to estimate `pA−pB`, should the standard error be pooled or unpooled?
2. If the goal is to test `H0:pA=pB`, should the standard error be pooled or unpooled?
3. Explain why.

**Check**

- Confidence interval: unpooled.
- Equality test: pooled.
- The null test assumes a common population proportion; the interval does not.

## 3. Paired or independent?

Twenty students take a reading test before and after a four-week intervention.

**Tasks**

1. Identify whether the data are paired or independent.
2. State the correct inferential structure.
3. Explain why a two-sample independent t test is not the best choice.

**Check**

The measurements are paired because each after score belongs to the same student as a before score. Define one difference for each student and use a one-sample t procedure on the differences.

## 4. Chi-square association

A school surveys 300 students and records grade level and preferred study format: individual, small group, or whole class.

**Tasks**

1. Identify the variable types.
2. Name the appropriate procedure family.
3. State the expected-count formula for one cell.
4. Describe what a large chi-square statistic means.

**Check**

Both variables are categorical. Use chi-square independence/homogeneity logic. Expected count is `(row total × column total)/grand total`. A large chi-square statistic means the observed table is farther from the pattern expected under the null model of no association.

## 5. Sampling distribution of p̂

Suppose the true population proportion is `p=0.40` and random samples of `n=100` are repeatedly selected.

**Tasks**

1. Find the mean of the sampling distribution of `p̂`.
2. Find its standard deviation.
3. Explain what the standard deviation represents.

**Check**

- `μp̂=0.40`.
- `σp̂=√[0.40(0.60)/100]≈0.049`.
- Across repeated random samples of size 100, sample proportions typically vary by about 0.049 around the population proportion.

## 6. Sampling distribution of x̄

A population has mean `μ=50` and standard deviation `σ=12`. Random samples of `n=36` are selected.

**Tasks**

1. Find `μx̄`.
2. Find `σx̄`.
3. Explain how increasing sample size affects the sampling variability.

**Check**

- `μx̄=50`.
- `σx̄=12/√36=2`.
- Sampling variability decreases at the rate `1/√n`.

## 7. Regression residual

The fitted model is `ŷ=18+2.4x`. For an observation with `x=10`, the observed response is `y=45`.

**Tasks**

1. Find the predicted response.
2. Find the residual.
3. Interpret the sign of the residual.

**Check**

- `ŷ=18+2.4(10)=42`.
- `e=45−42=3`.
- The observation is 3 response units above the model prediction; the model underpredicted it by 3.

## 8. Correlation and r²

A study reports `r=-0.80` between two quantitative variables.

**Tasks**

1. Find `r²`.
2. Interpret it.
3. Explain why the negative sign disappears after squaring.

**Check**

`r²=0.64`. About 64% of the variation in the response is explained by the fitted linear relationship with the explanatory variable. The sign of `r` describes direction; `r²` describes explained variation and is nonnegative.

## 9. Random sample versus random assignment

A district randomly samples 400 students and finds an association between sleep duration and test score.

**Tasks**

1. What does the random sample support?
2. Can the study establish that increasing sleep causes higher scores?
3. What design feature would strengthen a causal claim?

**Check**

The random sample supports population generalization when the sampling frame and implementation are appropriate. It does not by itself establish causation. Random assignment to a treatment would be the key design feature for a causal comparison.

## 10. P-value interpretation

A hypothesis test gives `p=0.012`.

Which interpretation is correct?

A. There is a 1.2% probability that the null hypothesis is true.

B. Assuming the null model is true, a result at least as extreme as the observed result would occur about 1.2% of the time.

C. The alternative hypothesis has a 98.8% probability of being true.

D. The effect must be important in practice.

**Answer: B.** A p-value is calculated under the null model. It does not directly assign probabilities to hypotheses and does not measure practical importance.

## 11. Confidence-interval interpretation

A 95% confidence interval for a population proportion is `(0.52, 0.66)`.

Which interpretation is strongest?

A. 95% of individuals have values between 0.52 and 0.66.

B. There is a 95% probability that this fixed parameter is in this already-computed interval.

C. The interval-producing method captures the true parameter in about 95% of repeated samples under its assumptions, and this sample produced the interval 0.52 to 0.66.

D. 95% of sample proportions must fall in this interval.

**Answer: C.** Confidence refers to the long-run performance of the procedure.

## 12. Current-course check

Which topic is no longer a current AP Statistics exam topic under the revised 2026–27 course?

A. Two-sample t inference

B. Chi-square independence

C. Inference for a population regression slope

D. One-proportion z inference

**Answer: C.** Regression analysis remains, but inference for a population regression slope was removed in the revised course.

## Final practice rule

For every problem, write this short chain before calculating:

`Target → Variable type → Design → Parameter → Procedure → Conditions → Calculation → Interpretation`

For deeper formula explanations and interactive calculation support, use **[AP Statistics Formula Sheet 2027](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**.