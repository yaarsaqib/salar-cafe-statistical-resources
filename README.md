# Salar Cafe Statistical Learning Resources

A public collection of original learning notes, worked examples, synthetic practice datasets, interpretation checklists, and software-oriented guidance for statistics and data analysis.

The repository is maintained as a companion resource to **Salar Cafe**, where each method is explained in a complete long-form guide with formulas, assumptions, practical interpretation, charts, reporting examples, and workflows for SPSS, Python, R, and Excel.

## Why this repository exists

Statistical methods are often taught as isolated commands: select a menu item, run a function, and copy the p-value. That approach is not enough for reliable analysis. A defensible result requires a clear research question, the correct data structure, appropriate assumptions, meaningful diagnostics, and an interpretation that explains what the result does and does not establish.

This repository provides a compact, reusable layer between a textbook definition and a full analysis. Each topic folder is designed to help a learner answer five questions:

1. **What problem does the method solve?**
2. **What type of variables and study design does it require?**
3. **What assumptions or diagnostics matter most?**
4. **How should the numerical output be interpreted?**
5. **What information belongs in a complete report?**

The materials are suitable for students, instructors, analysts, researchers, and software learners. The included datasets are synthetic and intended for teaching, practice, and reproducibility demonstrations rather than substantive scientific conclusions.

## Resource collection

| Topic | Repository resource | Complete Salar Cafe guide |
|---|---|---|
| Breusch–Pagan test | [Heteroscedasticity diagnostic resource](resources/breusch-pagan-test/) | [Breusch–Pagan test assumptions and interpretation](https://onlineinternetcafe.com/breusch-pagan-test/) |
| MANCOVA | [Multivariate covariance-adjustment resource](resources/mancova/) | [MANCOVA formula, assumptions, and software guide](https://onlineinternetcafe.com/mancova/) |
| Tukey HSD test | [Post-hoc pairwise-comparison resource](resources/tukey-hsd-test/) | [Tukey HSD formula and interpretation](https://onlineinternetcafe.com/tukey-hsd-test/) |
| Welch’s ANOVA | [Unequal-variance ANOVA resource](resources/welchs-anova/) | [Welch’s ANOVA guide](https://onlineinternetcafe.com/welchs-anova/) |
| Cook’s distance | [Regression-influence diagnostic resource](resources/cooks-distance/) | [Cook’s distance formula and interpretation](https://onlineinternetcafe.com/cooks-distance/) |
| Intraclass correlation coefficient | [ICC model-selection and reliability resource](resources/intraclass-correlation-coefficient/) | [Intraclass correlation coefficient guide](https://onlineinternetcafe.com/intraclass-correlation-coefficient-icc-formula-interpretation-spss-python-r-and-excel-guide/) |
| Three-way ANOVA | [Three-factor interaction resource](resources/three-way-anova/) | [Three-way ANOVA formula and interpretation](https://onlineinternetcafe.com/three-way-anova/) |
| Correlation heatmap | [Correlation-matrix visualization resource](resources/correlation-heatmap/) | [Correlation heatmap interpretation guide](https://onlineinternetcafe.com/correlation-heatmap/) |
| Dice counter | [Probability and roll-frequency resource](resources/dice-counter/) | [Free online dice counter](https://onlineinternetcafe.com/dice-counter/) |
| Kendall’s tau-b | [Tie-corrected ordinal-association resource](resources/kendalls-tau-b/) | [Kendall’s tau-b formula and interpretation](https://onlineinternetcafe.com/kendalls-tau-b/) |

## How to use the materials

A productive workflow is to begin with the topic README, inspect the practice dataset, reproduce the analysis in one software package, and then compare the output with another package. Differences in formatting are normal; the underlying statistical meaning should remain consistent when the same model, coding, missing-value rules, and options are used.

### Recommended learning sequence

1. State the research question in one sentence.
2. Identify the outcome, predictor, grouping, rating, covariate, or ordinal variables.
3. Confirm whether observations are independent, paired, clustered, or repeatedly measured.
4. Read the method overview and verify that the design matches the method.
5. Inspect the synthetic dataset and reproduce the example.
6. Check assumptions and diagnostics before interpreting the main statistic.
7. Report the estimate, test statistic, degrees of freedom, p-value, confidence interval, or effect-size measure required by the method.
8. Write a plain-language conclusion that remains within the evidence provided by the design.

## What makes a statistical report complete

A p-value alone is rarely sufficient. Depending on the method, a complete report may need:

- The purpose of the analysis
- The variables and their coding
- Valid sample size and exclusions
- Descriptive statistics
- Assumption checks and diagnostic plots
- Test statistic and degrees of freedom
- Exact p-value when practical
- Effect size, reliability coefficient, mean difference, or correlation
- Confidence interval
- Follow-up comparisons or simple effects
- Software and important options
- A conclusion stated in the language of the research question

The topic pages in this repository identify which of these elements matter for each method.

## Major themes across the collection

### Regression diagnostics

The Breusch–Pagan and Cook’s distance resources address two different regression questions. The Breusch–Pagan test concerns the **variance pattern of residuals**, while Cook’s distance concerns the **influence of individual observations on the fitted model**. A model may show heteroscedasticity without an unusually influential case, or may contain an influential observation even when residual variance is reasonably stable.

### Mean comparisons

Tukey HSD, Welch’s ANOVA, and three-way ANOVA belong to the broad family of mean-comparison procedures but solve different problems. Tukey HSD is a post-hoc method for pairwise comparisons after an omnibus ANOVA. Welch’s ANOVA is designed for independent groups when equal variances are doubtful. Three-way ANOVA examines three factors and their interactions, requiring careful interpretation of higher-order effects.

### Multivariate and reliability analysis

MANCOVA evaluates several related outcomes while adjusting for covariates. The intraclass correlation coefficient focuses on reliability or agreement among measurements or raters. Both require model choices that cannot be made from a single coefficient or software default.

### Association and visualization

Kendall’s tau-b measures ordinal association and explicitly corrects for ties. A correlation heatmap is a visualization rather than a statistical test; its validity depends on the correlation method used to produce the matrix and on clear, non-misleading design choices.

### Probability learning

The Dice Counter provides a direct way to record outcomes and compare observed relative frequencies with theoretical probabilities. It is useful for classroom experiments, simulations, and game-session tracking.

## Software consistency checklist

When comparing SPSS, Python, R, and Excel results, confirm the following before concluding that software packages disagree:

- The same rows were included.
- Missing values were handled in the same way.
- Categorical reference groups were identical.
- The same sums-of-squares or model options were selected.
- Confidence levels and multiple-comparison adjustments matched.
- One-tailed and two-tailed settings were not mixed.
- Single-measure and average-measure ICC results were not confused.
- Pearson, Spearman, and Kendall correlations were not treated as interchangeable.
- Robust and conventional standard errors were clearly distinguished.

Most apparent disagreements result from different defaults rather than computational errors.

## Responsible interpretation principles

These resources follow several general principles:

- A statistically significant result is not automatically important in practice.
- A nonsignificant result is not proof that no effect or relationship exists.
- Assumption checks should guide analysis, not become mechanical pass-or-fail rituals.
- Diagnostic thresholds are screening rules, not automatic deletion commands.
- Correlation does not by itself establish causation.
- Reliability and agreement are related but not identical concepts.
- Higher-order interactions should be interpreted before isolated main effects.
- Multiple pairwise tests require appropriate error-rate control.
- Visualizations should clarify the data rather than exaggerate patterns.

## Repository structure

Each topic directory contains a detailed README and a small CSV file. Additional teaching files may be added over time, including code examples, reporting templates, data dictionaries, and software comparison notes.

```text
resources/
├── breusch-pagan-test/
├── mancova/
├── tukey-hsd-test/
├── welchs-anova/
├── cooks-distance/
├── intraclass-correlation-coefficient/
├── three-way-anova/
├── correlation-heatmap/
├── dice-counter/
└── kendalls-tau-b/
```

## About the practice data

All practice datasets are synthetic. They are designed to demonstrate expected data layouts and common analytical patterns. They should not be presented as real survey, clinical, educational, commercial, or experimental observations.

Synthetic data are useful because they allow learners to:

- Reproduce an analysis without privacy concerns
- Modify values and observe how output changes
- Deliberately create assumption violations
- Compare software packages using identical input
- Practice interpretation before working with real research data

## Citation

Saqib, Muhammad Yar. (2026). *Salar Cafe Statistical Learning Resources*. GitHub. Companion website: [Salar Cafe](https://onlineinternetcafe.com/).

Individual topic pages contain method-specific citations.

## License

Original educational text and synthetic datasets in this repository are released under the Creative Commons Attribution 4.0 International License unless a file states otherwise. Reuse is permitted with attribution to Salar Cafe and preservation of the relevant complete-guide link.

## Main website

For the full collection of statistical tutorials, calculators, worked examples, and software guides, visit [Salar Cafe](https://onlineinternetcafe.com/).