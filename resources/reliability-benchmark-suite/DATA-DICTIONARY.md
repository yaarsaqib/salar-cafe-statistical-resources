# Reliability Benchmark Data Dictionary

## Dataset 1: `item-responses.csv`

This file contains synthetic ordinal-style item responses for internal-consistency and split-half analysis.

| Variable | Type | Coding | Role |
|---|---|---|---|
| `participant_id` | Text | `P01` through `P30` | Unique case identifier; exclude from calculations |
| `item_1` | Integer | 1–7 | Scale item |
| `item_2` | Integer | 1–7 | Scale item |
| `item_3` | Integer | 1–7 | Scale item |
| `item_4` | Integer | 1–7 | Scale item |
| `item_5` | Integer | 1–7 | Scale item |
| `item_6` | Integer | 1–7 | Scale item |
| `item_7` | Integer | 1–7 | Scale item |
| `item_8` | Integer | 1–7 | Scale item |

All items are positively keyed. No reverse scoring is required. There are no missing values, duplicate participant identifiers, text responses, or out-of-range scores.

### Raw Cronbach’s alpha

For `k` items, calculate:

`alpha = [k / (k - 1)] × [1 - sum(item variances) / variance(total score)]`

Use sample variances consistently. The total score is the row sum of all eight item columns.

### Standardized alpha

Let `r_bar` be the mean of the 28 unique off-diagonal Pearson item correlations:

`standardized alpha = [k × r_bar] / [1 + (k - 1) × r_bar]`

### Corrected item–total correlation

For each item, correlate that item with the sum of the other seven items. Do not correlate an item with a total that includes itself.

### Alpha if deleted

Remove one item, recompute the row total and item variances for the remaining seven items, and apply the raw-alpha formula with `k = 7`.

### Fixed split-half definition

To ensure reproducible results, use:

- Odd half total: `item_1 + item_3 + item_5 + item_7`
- Even half total: `item_2 + item_4 + item_6 + item_8`

Calculate the Pearson correlation `r` between the two half totals.

### Spearman–Brown correction

For two equally intended halves:

`corrected reliability = 2r / (1 + r)`

### Guttman split-half coefficient

Let `V1` and `V2` be sample variances of the two half totals, and `VT` be the sample variance of their sum:

`Guttman split-half = 2 × [1 - (V1 + V2) / VT]`

## Dataset 2: `test-retest-scores.csv`

This file contains synthetic continuous scores measured at two occasions.

| Variable | Type | Coding | Role |
|---|---|---|---|
| `participant_id` | Text | `P01` through `P30` | Pairing identifier |
| `test_score` | Decimal | Observed scale score | First occasion |
| `retest_score` | Decimal | Observed scale score | Second occasion |

Rows must remain paired by participant. There are no missing pairs.

### Stability coefficients

Calculate both:

- Pearson correlation between `test_score` and `retest_score`
- Spearman rank correlation between `test_score` and `retest_score`

Pearson correlation measures linear rank-order stability. Spearman correlation measures monotonic rank-order stability. Neither coefficient alone establishes exact agreement.

### Change scores

Define:

`change = retest_score - test_score`

Report the mean change and sample standard deviation of change.

### Paired t test

Test whether the mean change equals zero:

`t = mean(change) / [SD(change) / sqrt(n)]`

Use `df = n - 1` and a two-sided p-value.

### Error summaries

`MAE = mean(abs(retest_score - test_score))`

`RMSE = sqrt(mean((retest_score - test_score)^2))`

These measures remain in the original score units and complement the correlation coefficients.

## Spearman–Brown prophecy benchmark

The expected-results file includes scenarios beginning with reliability `0.72`.

For a length multiplier `m`:

`new reliability = (m × r) / [1 + (m - 1) × r]`

For a target reliability `r_target`:

`required multiplier = [r_target × (1 - r)] / [r × (1 - r_target)]`

A multiplier of `2` means twice the original test length under the parallel-item assumptions of the prophecy formula. It does not mean that any arbitrary additional items will produce the predicted gain.

## Quality-control rules

- Exclude identifier columns from statistical calculations.
- Preserve decimal values in the test–retest file.
- Use two-sided p-values.
- Do not silently apply listwise deletion, because no values are missing.
- Do not standardize items before calculating raw alpha.
- Do not use population variances in only part of a calculation.
- Report software defaults if they differ from these conventions.
- Compare unrounded internal values before deciding that output matches.

## Related complete resources

- [Cronbach’s Alpha](https://onlineinternetcafe.com/cronbachs-alpha/)
- [Split-Half Reliability](https://onlineinternetcafe.com/split-half-reliability/)
- [Spearman–Brown Formula](https://onlineinternetcafe.com/spearman-brown-formula/)
- [Test–Retest Reliability](https://onlineinternetcafe.com/test-retest-reliability/)
- [Salar Statistical Calculators](https://onlineinternetcafe.com/statistical-calculators/)
