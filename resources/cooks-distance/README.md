# Cook’s Distance Worked Resource

Cook’s distance is a regression diagnostic that measures how much the fitted model would change if one observation were removed. It combines information about the observation’s residual and leverage, allowing the analyst to identify cases that may have substantial influence on coefficients, fitted values, or overall model conclusions.

For formulas, leverage and residual diagnostics, threshold discussion, plots, and SPSS, Python, R, and Excel workflows, use the [complete Cook’s distance guide](https://onlineinternetcafe.com/cooks-distance/).

## Quick answer

A large Cook’s D value is a signal to investigate an observation. It is **not** an automatic rule for deleting the case. The observation may be:

- A data-entry error
- A valid but unusual case
- Evidence of model misspecification
- A member of an unmodeled subgroup
- Highly influential because the sample is small

The correct response depends on data quality, design, model purpose, and sensitivity analysis.

## Core formula

One common expression is:

`Dᵢ = [eᵢ² / (p × MSE)] × [hᵢᵢ / (1 − hᵢᵢ)²]`

where:

- `eᵢ` is the residual for observation `i`.
- `hᵢᵢ` is the leverage value.
- `p` is the number of estimated model parameters, including the intercept.
- `MSE` is the residual mean square.

The formula shows why an observation can be influential through a large residual, high leverage, or a combination of both.

## Residual, leverage, and influence

### Residual

A residual measures how far the observed outcome lies from the fitted value. A large residual indicates poor fit for that observation.

### Leverage

Leverage measures how unusual the predictor values are relative to the rest of the data. A high-leverage case lies far from the center of the predictor space.

### Influence

Influence concerns how much the fitted model changes because the observation is present. A case can have high leverage but little influence if it follows the fitted pattern. A case with a large residual but ordinary predictor values may also have limited effect on the coefficients.

Cook’s distance combines these components.

## Recommended diagnostic workflow

1. Fit the intended regression model.
2. Check data quality and variable coding.
3. Inspect residual-versus-fitted and normal diagnostic plots.
4. Calculate leverage, studentized residuals, Cook’s D, and preferably DFBETAs or DFFITS.
5. Identify observations with relatively large diagnostic values.
6. Inspect the original records and predictor pattern.
7. Refit the model with and without the case as a sensitivity analysis.
8. Explain whether substantive conclusions change.
9. Retain valid observations unless a defensible reason supports exclusion.

## Threshold rules

Several screening rules are commonly encountered:

- `Dᵢ > 1`
- `Dᵢ > 4/n`
- Comparing each value with an F-distribution reference
- Looking for observations that stand far above the rest of the Cook’s D plot

These rules are not equivalent. The `4/n` rule can flag many observations in large datasets, while `D > 1` may be too conservative in some settings. Relative separation and model sensitivity are often more informative than a single universal cutoff.

## Interpreting a Cook’s distance plot

A useful plot places observation numbers on the horizontal axis and Cook’s D on the vertical axis. Look for:

- One or two observations far above the rest
- Clusters of influential cases
- A general rise at one end of the predictor range
- Cases that are influential only under a particular model specification

Labeling the largest values allows direct investigation of the underlying records.

## Sensitivity analysis

A sensitivity analysis should compare:

- Coefficient signs and magnitudes
- Standard errors
- p-values and confidence intervals
- Predicted values
- Model fit measures
- Substantive conclusions

If removing one valid observation reverses the central conclusion, the report should acknowledge that instability. Hiding the sensitivity is not appropriate.

## Reasons not to delete automatically

Automatic deletion can:

- Bias the sample toward cases that fit the preferred model
- Remove genuine population variation
- Understate uncertainty
- Create a misleadingly clean result
- Turn diagnostic analysis into outcome-driven data selection

Deletion is defensible when there is evidence of measurement error, ineligibility, duplicate records, impossible values, or a clearly prespecified exclusion rule.

## Model revision options

An influential case may reveal that the model needs:

- A nonlinear term
- An interaction
- A group indicator
- A transformation
- A robust regression approach
- A different outcome distribution
- A hierarchical or clustered model

The case can therefore provide useful information rather than merely being an inconvenience.

## Reporting checklist

Report:

- The regression model examined
- Diagnostic measures used
- Largest Cook’s D values
- Threshold or comparison strategy
- Whether records were checked for errors
- Results of sensitivity analysis
- Any exclusions and their justification
- Whether the main conclusion changed

## Example reporting language

> Influence diagnostics identified one observation with a Cook’s distance substantially larger than the remaining cases. The record was verified as valid. Re-estimating the model without the observation changed the magnitude of one coefficient but did not alter its direction or the overall conclusion; the observation was therefore retained and the sensitivity result was reported.

When conclusions change:

> The substantive conclusion was sensitive to one high-leverage observation. Results from the full model and the sensitivity model are both reported, and the instability is considered when interpreting the evidence.

## Common mistakes

- Deleting every case above `4/n`
- Treating Cook’s D as an outlier test for the outcome only
- Examining influence after choosing a preferred result
- Failing to verify the original record
- Reporting only a plot with no case-level interpretation
- Ignoring clusters of moderate influence
- Confusing leverage with influence
- Hiding sensitivity analyses that change conclusions

## Related diagnostics

### Studentized residuals

Useful for identifying observations with unusually large outcome deviations relative to estimated residual variation.

### Hat values

Measure leverage in predictor space.

### DFBETAs

Show how deleting a case changes each individual coefficient.

### DFFITS

Measures how much the fitted value for a case changes when that case is excluded.

### COVRATIO

Assesses the effect of an observation on the covariance matrix of coefficient estimates.

No single diagnostic should carry the entire decision.

## Software consistency notes

Verify:

- Whether the intercept is counted in `p`
- Whether deleted or ordinary residuals are used
- Missing-value handling
- Standardization conventions
- Observation numbering after filtering
- Whether the model contains weights or robust fitting

## Practice dataset

The synthetic CSV includes a generally linear pattern and one deliberately influential observation. Suggested exercises:

1. Fit the full regression.
2. Plot residuals and leverage.
3. Calculate Cook’s D.
4. Identify the largest value.
5. Refit the model without that observation.
6. Compare coefficients and predictions.
7. Decide whether the case is an error, a valid unusual point, or evidence for model revision.

## Frequently asked questions

### Is a Cook’s D value above 1 always unacceptable?

No. It deserves careful investigation, but the correct action depends on context and sensitivity.

### Can an observation have high leverage but low Cook’s D?

Yes. A high-leverage case that lies close to the fitted relationship may have limited influence.

### Can Cook’s D be used in multiple regression?

Yes. It is especially useful because unusual combinations of predictors may not be obvious from separate univariate plots.

### Should influential observations be reported?

Yes, particularly when they affect substantive conclusions or motivate exclusions.

## Complete learning guide

The full Salar Cafe resource covers the formula, leverage, studentized residuals, influence plots, threshold rules, interpretation, sensitivity analysis, and software workflows:

[Open the complete Cook’s distance guide](https://onlineinternetcafe.com/cooks-distance/)

## Suggested citation

Saqib, M. Y. (2026). *Cook’s Distance: Formula, Interpretation, SPSS, Python, R and Excel Guide*. Salar Cafe. https://onlineinternetcafe.com/cooks-distance/