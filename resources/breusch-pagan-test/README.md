# Breusch–Pagan Test Worked Resource

The Breusch–Pagan test is a regression diagnostic used to evaluate whether the variance of the residuals changes systematically with one or more predictors or with the fitted values. Constant residual variance is called **homoscedasticity**. A systematic increase, decrease, or other structured change in residual spread is called **heteroscedasticity**.

This page provides a practical framework for deciding when to use the test, understanding the calculation, interpreting the result, and reporting it responsibly.

## Quick answer

Use the Breusch–Pagan test when you have fitted a linear regression model and want a formal check of whether residual variance appears related to the explanatory variables. A small p-value provides evidence against constant variance. It does **not** automatically prove that the regression is useless, that the coefficients are biased, or that observations should be deleted.

For a full long-form explanation with formulas, diagnostics, charts, and SPSS, Python, R, and Excel workflows, use the [complete Breusch–Pagan test guide](https://onlineinternetcafe.com/breusch-pagan-test/).

## When the test is appropriate

The test is commonly used after ordinary least squares regression when:

- The outcome is continuous.
- The model includes one or more predictors.
- Residual plots suggest changing spread.
- Standard errors and hypothesis tests may be sensitive to nonconstant variance.
- The analyst wants a formal supplement to graphical diagnostics.

The test is not a substitute for checking model form. Curvature, omitted interactions, an inappropriate outcome scale, or influential observations can create residual patterns that resemble heteroscedasticity.

## Data structure

The original regression generally has the form:

`Yᵢ = β₀ + β₁X₁ᵢ + β₂X₂ᵢ + … + βₖXₖᵢ + εᵢ`

After estimating the model, obtain residuals `eᵢ`. The auxiliary regression typically relates squared residuals to the selected predictors:

`eᵢ² = α₀ + α₁Z₁ᵢ + α₂Z₂ᵢ + … + αₘZₘᵢ + uᵢ`

The variables `Z` may be the original predictors, fitted values, or another justified set of variables expected to explain the variance pattern.

## Core calculation

A common Lagrange multiplier form is:

`LM = n × R²auxiliary`

where:

- `n` is the number of observations used in the regression.
- `R²auxiliary` is the coefficient of determination from the auxiliary regression of squared residuals.
- The test statistic is compared with a chi-square distribution.
- Degrees of freedom usually equal the number of tested slope terms in the auxiliary regression.

Some software also reports an F version. The chi-square and F versions may differ slightly in finite samples, but they address the same general question.

## Hypotheses

The null hypothesis is that the tested variance-related slopes are zero:

`H₀: α₁ = α₂ = … = αₘ = 0`

This corresponds to no systematic association between the chosen explanatory variables and residual variance.

The alternative is that at least one variance-related slope is nonzero, indicating structured heteroscedasticity.

## Practical workflow

1. Fit the intended regression model.
2. Inspect the residual-versus-fitted plot.
3. Look for a funnel shape, increasing spread, decreasing spread, clusters, or curved structure.
4. Run the Breusch–Pagan test using a justified set of predictors.
5. Compare the formal result with the plot.
6. Check whether model misspecification could explain the pattern.
7. Decide whether conventional standard errors remain acceptable.
8. Consider robust standard errors, transformation, weighted least squares, generalized least squares, or model revision when appropriate.

## How to interpret the p-value

### Nonsignificant result

A large p-value means the data do not provide strong evidence that residual variance is related to the variables included in the auxiliary regression. This does not prove perfect homoscedasticity. The test may have limited power in small samples or may miss variance patterns not represented by the chosen predictors.

### Significant result

A small p-value indicates evidence that residual variance is not constant with respect to the tested variables. The next step is diagnostic investigation, not automatic rejection of the model.

Questions to ask include:

- Does the residual plot show a clear funnel?
- Is the pattern caused by a few high-leverage observations?
- Is the outcome naturally positive and right-skewed?
- Is a predictor missing a nonlinear term?
- Should an interaction be included?
- Would a log or square-root transformation be meaningful?
- Are robust standard errors sufficient for the inferential goal?

## Why heteroscedasticity matters

Under standard ordinary least squares assumptions, the coefficient estimates may remain unbiased when heteroscedasticity is present and the mean model is otherwise correct. However, conventional standard errors can be incorrect. This affects:

- t tests for regression coefficients
- F tests
- confidence intervals
- prediction uncertainty
- judgments about statistical significance

The practical seriousness depends on the strength of the variance pattern, sample size, leverage structure, and purpose of the analysis.

## Common responses to a significant result

### Heteroscedasticity-robust standard errors

Robust standard errors adjust inference while leaving the estimated coefficients unchanged. They are often useful when the mean model is credible and the primary concern is valid standard errors.

### Transforming the outcome

A transformation may stabilize variance when the scale of measurement naturally produces larger variability at larger means. The transformation must remain substantively interpretable.

### Weighted least squares

Weighted least squares may improve efficiency when the variance structure can be estimated or justified. The weights should reflect the inverse of the conditional variance rather than an arbitrary choice.

### Revising the model

Add missing nonlinear terms, interactions, group indicators, or relevant predictors when diagnostic evidence suggests that the mean structure is incomplete.

### Generalized least squares or another model family

For known correlation and variance structures, generalized least squares may be appropriate. For counts, proportions, durations, or other non-Gaussian outcomes, a generalized linear model may fit the data-generating process better than ordinary least squares.

## Assumptions and limitations

The Breusch–Pagan test relies on the fitted mean model and the chosen auxiliary specification. Important limitations include:

- Sensitivity to non-normal residuals in some implementations
- Limited power with small samples
- Possible over-sensitivity in very large samples
- Dependence on which predictors enter the auxiliary regression
- Inability to identify the best corrective action by itself
- Potential confusion between heteroscedasticity and mean-model misspecification

A formal test should always be interpreted with residual plots and substantive knowledge.

## Reporting checklist

A complete report should state:

- The regression model being evaluated
- The variables used in the variance test
- The test version used
- The LM or F statistic
- Degrees of freedom
- p-value
- Whether graphical diagnostics agreed
- Any corrective action taken
- Whether reported standard errors are conventional or robust

## Example reporting language

> A Breusch–Pagan test was conducted to assess whether residual variance changed systematically across the predictors. The result was statistically significant, indicating evidence of heteroscedasticity. Residual plots showed increasing spread at larger fitted values. Coefficient estimates were retained, but heteroscedasticity-robust standard errors were used for inference.

For a nonsignificant result:

> The Breusch–Pagan test did not provide statistically significant evidence that residual variance was related to the included predictors. Residual plots were also inspected and did not show a strong systematic variance pattern.

## Common mistakes

- Treating a significant result as proof that coefficients are biased
- Deleting observations solely to make the test nonsignificant
- Running the test without inspecting residual plots
- Ignoring model curvature or omitted interactions
- Reporting robust standard errors without naming the robust method
- Claiming homoscedasticity has been proven after a nonsignificant test
- Using the test on a model that is inappropriate for the outcome type

## Software notes

Different software packages may report slightly different versions of the test. Before comparing output, verify:

- Which variables entered the auxiliary regression
- Whether studentized or nonstudentized versions were used
- Whether an LM chi-square or F statistic was reported
- How missing values were handled
- Whether an intercept was included

The numerical conclusion should be compared only after these settings match.

## Practice dataset

The accompanying CSV contains a simple predictor and outcome with residual spread that changes as the predictor increases. Use it to:

1. Fit an ordinary least squares model.
2. Plot residuals against fitted values.
3. Run the Breusch–Pagan test.
4. Compare conventional and robust standard errors.
5. Experiment with a transformation or weighted model.

## Frequently asked questions

### Is the Breusch–Pagan test the same as the White test?

No. Both test for heteroscedasticity, but the White test commonly includes squares and cross-products and can detect a broader class of variance patterns. It also uses more degrees of freedom.

### Should I always transform the outcome after a significant test?

No. Transformation is one possible response. Robust standard errors, weighted models, model revision, or a different distributional model may be more appropriate.

### Can heteroscedasticity affect prediction intervals?

Yes. If uncertainty changes across the predictor range, a single constant-variance prediction interval may misrepresent uncertainty in some regions.

### Can the test be significant with a weak visual pattern?

Yes, especially in large samples. Statistical detectability and practical importance are not identical.

## Complete learning guide

The complete Salar Cafe resource includes detailed formulas, residual diagnostics, interpretation, examples, reporting language, and workflows for SPSS, Python, R, and Excel:

[Open the Breusch–Pagan test guide](https://onlineinternetcafe.com/breusch-pagan-test/)

## Suggested citation

Saqib, M. Y. (2026). *Breusch–Pagan Test: Assumptions, Interpretation, SPSS, Python, R and Excel Guide*. Salar Cafe. https://onlineinternetcafe.com/breusch-pagan-test/