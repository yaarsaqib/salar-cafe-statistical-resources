# Kendall’s Tau-b Worked Resource

Kendall’s tau-b is a nonparametric measure of monotonic association between two ordinal or ranked variables. It is based on concordant and discordant observation pairs and includes corrections for tied values in both variables.

For a full explanation of the formula, tie correction, worked calculations, reporting, and SPSS, Python, R, and Excel workflows, use the [complete Kendall’s tau-b guide](https://onlineinternetcafe.com/kendalls-tau-b/).

## Quick answer

Use Kendall’s tau-b when:

- Both variables are ordinal or can be meaningfully ranked.
- The relationship of interest is monotonic.
- Ties occur in one or both variables.
- Pearson’s linearity and distributional assumptions are inappropriate.
- A pair-order interpretation is useful.

Tau-b ranges from `−1` to `+1`. Positive values indicate that higher ranks on one variable tend to accompany higher ranks on the other. Negative values indicate an inverse ordering. Values near zero indicate little net concordance, although nonlinear or nonmonotonic relationships may still exist.

## Concordant and discordant pairs

For two observations `i` and `j`:

- The pair is **concordant** when the observation ranked higher on X also ranks higher on Y.
- The pair is **discordant** when the observation ranked higher on X ranks lower on Y.
- The pair is tied on X when the X values are equal.
- The pair is tied on Y when the Y values are equal.

Tau-b compares concordance with discordance while adjusting the denominator for ties.

## Core formula

`τb = (C − D) / √[(C + D + Tₓ)(C + D + Tᵧ)]`

where:

- `C` is the number of concordant pairs.
- `D` is the number of discordant pairs.
- `Tₓ` counts pairs tied only on X.
- `Tᵧ` counts pairs tied only on Y.

Pairs tied on both variables do not contribute to concordance or discordance in the same way and are handled according to the standard counting definitions used by the software.

## Pair-based interpretation

The numerator `C − D` represents the net excess of concordant over discordant pairs. A positive coefficient means concordance is more common. A negative coefficient means discordance is more common.

Tau-b should not be interpreted as a percentage of variance explained. That interpretation belongs to other contexts and is not appropriate for an ordinal pair-order coefficient.

## Tau-a, tau-b, and tau-c

### Tau-a

Tau-a does not correct for ties. It is most natural when ties are absent, such as strict rankings.

### Tau-b

Tau-b corrects for ties in both variables and is widely used for square ordinal tables or ordinary ranked data containing repeated values.

### Tau-c

Tau-c adjusts for table dimensions and is sometimes used for rectangular contingency tables with different numbers of categories.

State the version used. “Kendall correlation” alone can be ambiguous.

## Kendall’s tau-b versus Spearman correlation

Both measure monotonic association, but they are calculated differently.

Kendall’s tau-b:

- Uses concordant and discordant pairs
- Has a direct ordering interpretation
- Corrects explicitly for ties
- Often has a smaller absolute numerical magnitude than Spearman’s rho for the same data

Spearman’s rho:

- Is Pearson correlation applied to ranks
- Often feels more familiar to users of standard correlation
- May be more sensitive to the sizes of rank differences

The two coefficients should not be compared by asking which is “larger” without considering their different scales and interpretations.

## Data requirements

- Paired observations on two variables
- Ordinal or rankable values
- Independent observational units
- A relationship that is reasonably monotonic if one coefficient is to summarize it

Kendall’s tau-b does not require normal distributions. It does not correct for dependent or clustered observations.

## Recommended workflow

1. Confirm that the two variables are paired correctly.
2. Inspect frequency tables and the number of ties.
3. Create a jittered scatterplot, mosaic display, or ordered contingency table.
4. Check whether the pattern is monotonic.
5. Calculate tau-b with its p-value and confidence interval if available.
6. Report sample size and tie structure.
7. Interpret direction, magnitude, uncertainty, and practical meaning.

## Hypothesis test

The usual null hypothesis is that there is no ordinal association in the population, often expressed as `τb = 0`.

Software may use:

- An asymptotic normal approximation
- A tie-adjusted variance
- An exact or permutation method for small samples

Results can differ slightly across packages if one uses an exact calculation and another uses an asymptotic approximation.

## Confidence intervals

A confidence interval communicates uncertainty around tau-b. Bootstrap intervals may be used when software does not provide a suitable analytical interval, but the bootstrap procedure should preserve the observational structure.

A wide interval may include both weak and practically meaningful associations, even when the point estimate appears moderate.

## Interpreting magnitude

There are no universal cutoffs. Interpretation depends on:

- Measurement reliability
- Number of categories
- Tie prevalence
- Sample composition
- Research field
- Consequences of the association

Report the coefficient numerically and explain what the direction means for the variables.

## Example interpretation

Suppose tau-b between study-engagement category and achievement category is `0.42`. A responsible interpretation is:

> Higher engagement categories tended to be associated with higher achievement categories, with more concordant than discordant observation pairs. The association was positive and moderate in this sample.

Avoid saying that engagement “explains 42%” of achievement or causes higher achievement.

## Reporting checklist

Include:

- Variable names and category order
- Valid paired sample size
- Kendall coefficient version
- Tau-b estimate
- Test statistic or standardized value when provided
- p-value
- Confidence interval when available
- Treatment of ties
- Exact or asymptotic method
- Plain-language interpretation

## Example reporting language

> Kendall’s tau-b showed a positive ordinal association between satisfaction level and likelihood of recommendation, τb = 0.38, p < .001. Higher satisfaction categories tended to accompany higher recommendation categories. The analysis included tied observations in both variables and used the tie-corrected tau-b coefficient.

## Common mistakes

- Reporting tau-a when ties are common
- Treating ordinal codes as continuous without justification
- Claiming causation from an association
- Interpreting tau-b as variance explained
- Ignoring category ordering
- Combining repeated measurements as independent pairs
- Comparing tau-b and Spearman values as if they share an identical scale
- Reporting only a p-value
- Failing to state whether an exact or asymptotic test was used

## Ties and category design

A large number of ties may be a natural consequence of an ordinal scale with few categories. Ties do not automatically invalidate tau-b; they are the reason for using the tie-corrected version.

However, very coarse categories can limit the maximum observable association and reduce information. Report the number and meaning of categories.

## Software consistency notes

Before comparing output, verify:

- Tau-a, tau-b, or tau-c
- Missing-value deletion
- Category order
- Exact versus asymptotic p-values
- Continuity correction
- Confidence-interval method
- Handling of pairs tied on both variables

## Practice dataset

The synthetic CSV contains two five-level ordinal variables with many ties and a generally positive monotonic pattern. Suggested exercises:

1. Create a cross-tabulation.
2. Count concordant and discordant pairs for a smaller subset.
3. Calculate tau-b.
4. Compare tau-a, tau-b, and Spearman’s rho.
5. Reverse the order of one variable and observe the sign change.
6. Add more ties and observe the effect on the denominator.
7. Use a permutation or bootstrap procedure for uncertainty.

## Frequently asked questions

### Can Kendall’s tau-b be used for Likert items?

Yes, when the categories have a meaningful order and the pairwise association question is appropriate.

### Why is tau-b smaller than Spearman’s rho?

They use different calculations and scales. A smaller numerical tau-b does not imply a weaker conclusion by itself.

### Does tau-b require a linear relationship?

No. It measures monotonic ordering rather than linearity.

### What happens when every observation is tied on one variable?

The coefficient is undefined because there is no rank variation in that variable.

### Is a nonsignificant tau-b proof of no association?

No. It indicates insufficient evidence under the selected test and sample. Consider the interval, sample size, category resolution, and measurement quality.

## Complete learning guide

The full Salar Cafe resource covers tie correction, concordant and discordant pairs, tau-a, tau-b, tau-c, comparison with Spearman correlation, interpretation, reporting, and software workflows:

[Open the complete Kendall’s tau-b guide](https://onlineinternetcafe.com/kendalls-tau-b/)

## Suggested citation

Saqib, M. Y. (2026). *Kendall’s Tau-b: Formula, Interpretation, Python, R, SPSS and Excel Guide*. Salar Cafe. https://onlineinternetcafe.com/kendalls-tau-b/