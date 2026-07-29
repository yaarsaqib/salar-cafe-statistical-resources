# Reliability Analysis Validation Benchmark

This resource provides two original synthetic datasets and a set of verified reference results for validating reliability calculators, teaching reproducible measurement analysis, and comparing output from SPSS, Python, R, Excel, and browser-based statistical calculators.

The benchmark is deliberately small enough to inspect manually but rich enough to test several related methods:

- Cronbach’s alpha
- Standardized Cronbach’s alpha
- Corrected item–total correlations
- Alpha if an item is deleted
- Odd–even split-half correlation
- Spearman–Brown corrected reliability
- Guttman split-half coefficient
- Pearson test–retest reliability
- Spearman test–retest reliability
- Paired mean-change analysis
- Mean absolute error and root mean square error
- Spearman–Brown prophecy scenarios

## Files

| File | Purpose |
|---|---|
| `item-responses.csv` | Thirty participants answering eight 1–7 scale items |
| `test-retest-scores.csv` | Thirty participants measured on two occasions |
| `expected-results.csv` | Reference outputs rounded to six decimal places |
| `DATA-DICTIONARY.md` | Variable definitions, coding, formulas, and reproducibility rules |

## Verified headline results

### Internal consistency dataset

Using the eight item columns in `item-responses.csv`:

- Participants: **30**
- Items: **8**
- Raw Cronbach’s alpha: **0.920981**
- Standardized Cronbach’s alpha: **0.920517**
- Mean inter-item correlation: **0.591448**
- Odd–even half-score correlation: **0.848444**
- Spearman–Brown corrected coefficient: **0.918009**
- Guttman split-half coefficient: **0.917476**

The split is fixed for reproducibility:

- Odd half: `item_1`, `item_3`, `item_5`, `item_7`
- Even half: `item_2`, `item_4`, `item_6`, `item_8`

### Test–retest dataset

Using `test_score` and `retest_score` in `test-retest-scores.csv`:

- Participants: **30**
- Pearson correlation: **0.901650**
- Spearman correlation: **0.896483**
- Mean retest minus test change: **1.050000**
- Standard deviation of change: **4.431295**
- Paired t statistic: **1.297834**
- Degrees of freedom: **29**
- Two-sided p-value: **0.204573**
- Mean absolute error: **3.450000**
- Root mean square error: **4.481555**

## Why multiple coefficients are included

No single coefficient answers every reliability question. Cronbach’s alpha summarizes internal consistency under a specific variance-based model. Split-half reliability depends on the selected split and normally requires a correction because each half is shorter than the full scale. Test–retest correlation measures stability of rank ordering across occasions but does not, by itself, prove absolute agreement. Mean change and error measures expose systematic or practical disagreement that a correlation may conceal.

A calculator passes this benchmark only when it reproduces the coefficient that matches the stated method, denominator, data orientation, missing-value rule, and correction convention.

## Reproducibility conventions

1. Use sample variances with denominator `n - 1` when computing raw Cronbach’s alpha.
2. Use complete rows; these benchmark files contain no missing values.
3. Treat item columns as numeric and participant rows as independent cases.
4. Use Pearson correlation for the primary split-half coefficient.
5. Apply the two-half Spearman–Brown correction `2r / (1 + r)`.
6. Calculate Guttman split-half as `2 × [1 − (variance_half_1 + variance_half_2) / variance_total]`.
7. Calculate the paired t test on `retest_score − test_score`.
8. Report at least six decimal places before applying any pass/fail tolerance.
9. A reasonable cross-software tolerance for these datasets is `1e-6` for deterministic descriptive coefficients and `1e-5` for p-values.

## Recommended validation workflow

1. Import the CSV without changing column types.
2. Confirm participant and item counts.
3. Reproduce the raw and standardized alpha values.
4. Compare every corrected item–total correlation and alpha-if-deleted result.
5. Build the odd and even half totals exactly as defined.
6. Reproduce the half correlation, Spearman–Brown coefficient, and Guttman coefficient.
7. Analyze the test–retest file using Pearson, Spearman, paired t, MAE, and RMSE.
8. Compare output with `expected-results.csv` using the stated tolerance.
9. Document software version, options, and any discrepancy.

## Complete Salar Cafe guides and calculators

- [Cronbach’s Alpha guide](https://onlineinternetcafe.com/cronbachs-alpha/)
- [Split-Half Reliability guide](https://onlineinternetcafe.com/split-half-reliability/)
- [Spearman–Brown Formula guide](https://onlineinternetcafe.com/spearman-brown-formula/)
- [Test–Retest Reliability guide](https://onlineinternetcafe.com/test-retest-reliability/)
- [Reliability Analysis in Python](https://onlineinternetcafe.com/reliability-analysis-in-python/)
- [Reliability Analysis in R](https://onlineinternetcafe.com/reliability-analysis-in-r/)
- [Reliability Analysis in SPSS](https://onlineinternetcafe.com/reliability-analysis-in-spss/)
- [Reliability Analysis in Excel](https://onlineinternetcafe.com/reliability-analysis-in-excel/)
- [Split-Half Reliability Calculator](https://onlineinternetcafe.com/statistical-calculators/split-half-reliability-calculator/)
- [Salar Statistical Calculators Library](https://onlineinternetcafe.com/statistical-calculators/)

## Interpretation cautions

- High alpha does not prove unidimensionality.
- Alpha can increase merely because more similar items are added.
- Alpha if deleted should not be used as an automatic item-removal rule.
- A strong test–retest correlation can coexist with systematic score shifts.
- Split-half results can change when a different split is chosen.
- Reliability thresholds must reflect the intended decision and consequences of measurement error.

## License and attribution

The datasets are synthetic and contain no personal or observed research data. Original text and data are released under the Creative Commons Attribution 4.0 International License. Reuse is permitted with attribution to Salar Cafe and a link to the relevant complete guide.

## Suggested citation

Saqib, M. Y. (2026). *Reliability Analysis Validation Benchmark: Synthetic Data and Verified Results*. Salar Cafe Statistical Learning Resources. https://github.com/yaarsaqib/salar-cafe-statistical-resources/tree/main/resources/reliability-benchmark-suite
