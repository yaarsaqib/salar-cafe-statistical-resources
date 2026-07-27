# Three-Way ANOVA Worked Resource

Three-way ANOVA, also called three-factor ANOVA, evaluates the effects of three categorical factors on one continuous outcome. The model tests three main effects, three two-way interactions, and one three-way interaction.

For detailed formulas, interaction plots, simple-effects analysis, reporting examples, and SPSS, Python, R, and Excel workflows, use the [complete three-way ANOVA guide](https://onlineinternetcafe.com/three-way-anova/).

## Model structure

A full factorial model can be summarized as:

`Y = μ + A + B + C + AB + AC + BC + ABC + ε`

where:

- `A`, `B`, and `C` are the three factors.
- `AB`, `AC`, and `BC` are two-way interactions.
- `ABC` is the three-way interaction.
- `ε` is within-cell error.

## Quick answer

The most important interpretive rule is: **examine the highest-order interaction first**.

A significant `A × B × C` interaction means the way factors A and B interact changes across levels of factor C. Under that condition, isolated main effects can be misleading because averaging across the other factors may hide or reverse the actual pattern.

## Data requirements

- One continuous dependent variable
- Three categorical independent variables
- Independent observations for a between-subjects design
- Observations in the relevant factor combinations or cells

A balanced `2 × 2 × 2` design has eight cells. Larger numbers of factor levels rapidly increase the required sample size and number of follow-up comparisons.

## Main effects

A main effect tests whether marginal means differ across levels of one factor after averaging over the other two factors.

For example, the main effect of A compares levels of A after collapsing across B and C. This average may be meaningful when interactions are weak. When interactions are strong, the marginal average may conceal important conditional differences.

## Two-way interactions

A two-way interaction, such as `A × B`, asks whether the effect of A depends on B after averaging across C. If the three-way interaction is significant, the averaged two-way interaction should be decomposed separately at each level of C.

## Three-way interaction

A three-way interaction asks whether a two-way interaction differs across the third factor. Practical interpretation usually requires:

1. Plotting cell or estimated marginal means.
2. Examining `A × B` separately within each level of C.
3. Testing simple two-way interactions or simple-simple effects.
4. Applying multiplicity control to follow-up comparisons.

## Recommended workflow

1. Confirm factor coding and cell sizes.
2. Produce a table of cell means, standard deviations, and counts.
3. Inspect distributions and outliers within cells.
4. Check variance homogeneity and independence.
5. Fit the full factorial model.
6. Interpret the three-way interaction first.
7. If needed, examine two-way interactions at specific levels of the third factor.
8. Analyze simple effects and pairwise comparisons.
9. Plot the interactions with uncertainty intervals.
10. Report effect sizes and practical meaning.

## Interaction plots

A useful plot places one factor on the horizontal axis, uses separate lines for the second factor, and creates separate panels for the third factor.

Interpret cautiously:

- Parallel lines suggest little interaction.
- Diverging or converging lines suggest interaction.
- Crossing lines may indicate a reversal.
- Different line patterns across panels suggest a three-way interaction.

Plots should include clear labels and preferably confidence intervals or standard-error bars.

## Assumptions

### Independence

Observations should be independent unless the model explicitly handles repeated or clustered measurements.

### Approximately normal residuals

The model assumes approximately normal errors within cells. Inspect residuals and cell-level outliers rather than relying only on a single normality test.

### Homogeneity of variances

Within-cell variances should be reasonably comparable. Strong inequality combined with unbalanced cells can affect Type I error and interpretation.

### Correct model specification

The factor structure and interaction terms should match the study design. Omitting interactions merely because they are nonsignificant after viewing results can alter the meaning of main effects.

## Balanced and unbalanced designs

Balanced designs provide clearer orthogonality among effects. In unbalanced data, sums-of-squares choices matter.

- Type I sums of squares are sequential and depend on term order.
- Type II tests main effects after other main effects but generally not after interactions containing the tested factor.
- Type III tests each effect after all other terms and depends on coding and estimability.

Report the selected approach and use coding appropriate for the hypotheses.

## Simple effects

A simple effect examines one factor at fixed levels of other factors. With a significant three-way interaction, examples include:

- Effect of A within `B1` and `C1`
- Effect of A within `B2` and `C1`
- Effect of A within `B1` and `C2`
- Effect of A within `B2` and `C2`

These analyses can create many tests, so the comparison family and adjustment method should be planned.

## Effect sizes

Common measures include partial eta squared and omega squared. In factorial designs, partial eta squared describes the proportion of variance associated with an effect relative to that effect plus error, not the proportion of total outcome variance uniquely explained.

Provide confidence intervals or raw mean differences where practical.

## Reporting checklist

Include:

- Factor names and levels
- Cell counts and descriptive statistics
- Full model specification
- Sums-of-squares type for unbalanced data
- F statistic, degrees of freedom, p-value, and effect size for each relevant effect
- Three-way interaction interpretation
- Follow-up simple effects and adjusted comparisons
- Estimated marginal means and confidence intervals
- Interaction plots

## Example reporting language

> The three-way interaction among instructional method, study schedule, and grade level was statistically significant. The method-by-schedule interaction was pronounced in the higher grade level but weak in the lower grade level. Follow-up simple-effects analyses showed that the largest method difference occurred under the intensive schedule in the higher grade group.

## Common mistakes

- Interpreting main effects before a significant three-way interaction
- Reporting seven p-values without explaining the pattern
- Ignoring empty or very small cells
- Using a line plot that hides uncertainty
- Running many unadjusted simple comparisons
- Treating Type I, II, and III sums of squares as interchangeable
- Failing to describe factor coding
- Claiming causation from a nonexperimental design

## Software consistency notes

Before comparing software, match:

- Contrast coding
- Reference levels
- Sums-of-squares type
- Missing-value handling
- Estimated marginal means
- Multiplicity adjustment
- Model term hierarchy
- Confidence level

Different defaults can produce different-looking tests in unbalanced designs.

## Practice dataset

The synthetic CSV contains a balanced `2 × 2 × 2` design with twelve observations per cell. Suggested exercises:

1. Calculate all eight cell means.
2. Create a faceted interaction plot.
3. Fit the full factorial model.
4. Examine the three-way interaction.
5. Test simple two-way interactions by level of factor C.
6. Compare cell means with adjusted intervals.
7. Remove observations to create imbalance and compare sums-of-squares choices.

## Frequently asked questions

### What does a nonsignificant three-way interaction mean?

It means the analysis did not detect evidence that the two-way interaction changes across the third factor. Two-way interactions and main effects may still be meaningful.

### Should nonsignificant interactions be removed?

Not automatically. Preserve model hierarchy and consider whether the terms were part of the planned design.

### How large should each cell be?

There is no universal number. Power depends on effect size, error variance, number of cells, balance, and the interaction being tested.

### Can a three-way ANOVA include covariates?

Yes, but the model becomes factorial ANCOVA and requires covariate-related assumptions and careful interpretation.

## Complete learning guide

The full Salar Cafe resource covers main effects, two-way and three-way interactions, simple effects, assumptions, reporting, and software workflows:

[Open the complete three-way ANOVA guide](https://onlineinternetcafe.com/three-way-anova/)

## Suggested citation

Saqib, M. Y. (2026). *Three Way ANOVA: Formula, Interpretation, SPSS, Python, R and Excel Guide*. Salar Cafe. https://onlineinternetcafe.com/three-way-anova/