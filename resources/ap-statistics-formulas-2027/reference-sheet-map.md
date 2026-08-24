# AP Statistics 2027 Reference-Sheet Map

This page turns the current AP Statistics reference relationships into a **purpose map**. The goal is to help students recognize when a relationship belongs to the problem rather than treating the sheet as a list to memorize.

Full interactive companion: **[AP Statistics Formula Sheet 2027 — Salar Cafe](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**

## Descriptive statistics and regression

| Relationship | Main use | Critical reminder |
|---|---|---|
| `x̄ = Σxᵢ/n` | Sample mean | Sensitive to skew and outliers |
| `s = √[Σ(xᵢ−x̄)²/(n−1)]` | Sample standard deviation | Sample spread; same units as the variable |
| `ŷ = a + bx` | Least-squares prediction | Prediction does not imply causation |

Additional must-know relationships include `z=(x−μ)/σ`, `IQR=Q3−Q1`, residual `e=y−ŷ`, `b=r(sy/sx)`, `a=ȳ−bx̄`, and `r²`.

## Probability

| Relationship | Main use | Critical reminder |
|---|---|---|
| `P(A∪B)=P(A)+P(B)−P(A∩B)` | Probability of A or B | Subtract overlap once |
| `P(A|B)=P(A∩B)/P(B)` | Conditional probability | Reference set is restricted to B |

## Discrete random variables

| Relationship | Main use | Critical reminder |
|---|---|---|
| `μX=ΣxᵢP(xᵢ)` | Expected value | Long-run average; need not be attainable |
| `σX=√[Σ(xᵢ−μX)²P(xᵢ)]` | Random-variable spread | Probabilities should form a valid distribution |

## Binomial distribution

| Relationship | Main use | Critical reminder |
|---|---|---|
| `P(X=x)=C(n,x)pˣ(1−p)ⁿ⁻ˣ` | Exactly x successes | Fixed n, two outcomes, independence, constant p |
| `μ=np` | Expected successes | Same binomial conditions |
| `σ=√[np(1−p)]` | Spread in success count | Same binomial conditions |

## General inferential structure

| Relationship | Main use | Critical reminder |
|---|---|---|
| `(statistic−null parameter)/(SE under H0)` | Standardized hypothesis-test statistic | Standard error reflects the null model |
| `statistic ± (critical value)(SE)` | Confidence interval | Interpret for the population parameter |
| `χ²=Σ(O−E)²/E` | Categorical association | Current course emphasizes independence/homogeneity |

## Sampling distribution of one proportion

| Relationship | Main use | Critical reminder |
|---|---|---|
| `μp̂=p` | Center of sampling distribution | p is the population proportion |
| `σp̂=√[p(1−p)/n]` | True sampling SD | Theoretical relationship uses p |
| `SE(p̂)=√[p̂(1−p̂)/n]` | Estimated SE for interval | Uses observed p̂ |

## Difference between two proportions

| Relationship | Main use | Critical reminder |
|---|---|---|
| `μ(p̂1−p̂2)=p1−p2` | Center of sampling distribution | Preserve group order |
| `√[p1(1−p1)/n1+p2(1−p2)/n2]` | True sampling SD | Uses population proportions |
| `√[p̂1(1−p̂1)/n1+p̂2(1−p̂2)/n2]` | CI standard error | **Unpooled** |
| `p̂c=(x1+x2)/(n1+n2)` | Common null proportion | Used when H0 assumes p1=p2 |
| `√[p̂c(1−p̂c)(1/n1+1/n2)]` | Two-proportion test SE | **Pooled** under equality null |

### High-value distinction

A two-proportion **confidence interval** estimates the difference between two potentially different population proportions, so it uses separate sample estimates. The usual two-proportion **z test of equality** assumes a common population proportion under the null, so it pools the success information.

## Sampling distribution of one mean

| Relationship | Main use | Critical reminder |
|---|---|---|
| `μx̄=μ` | Center of sample-mean distribution | x̄ is unbiased for μ |
| `σx̄=σ/√n` | True sampling SD | Larger n lowers variability as 1/√n |
| `SE(x̄)=s/√n` | Estimated SE | Leads to t procedures when σ is unknown |

## Difference between two means

| Relationship | Main use | Critical reminder |
|---|---|---|
| `μ(x̄1−x̄2)=μ1−μ2` | Center of difference | Independent-group framework |
| `√(σ1²/n1+σ2²/n2)` | True sampling SD | Population SDs are theoretical parameters |
| `√(s1²/n1+s2²/n2)` | Estimated two-sample SE | Not for matched pairs |

## Paired-data exception

When observations are naturally matched — before/after measurements, twins, matched subjects, repeated measures on the same person — first compute one difference per pair. Then analyze that single list of differences with a one-sample t procedure.

This is one of the most important method-selection rules because the usual independent two-sample standard error is not the correct model for paired observations.

## Regression relationships students should connect

The reference information includes the least-squares prediction relationship `ŷ=a+bx`. Students should also understand these nearby relationships:

- `e=y−ŷ` — residual.
- `b=r(sy/sx)` — regression slope from summary statistics.
- `a=ȳ−bx̄` — regression intercept.
- `r²` — proportion of variation in the response explained by the linear model.

A positive residual means the observed response is above the predicted response. A negative residual means the model overpredicted that observation.

## Quick selection questions

Before using any relationship, answer these:

1. What is the population parameter or descriptive target?
2. Is the response categorical or quantitative?
3. How many samples, groups, or variables are involved?
4. Are observations independent or paired?
5. Is the task estimation, testing, description, association, or prediction?
6. What conditions must hold for the procedure?
7. Does the design support generalization, causation, both, or neither?

## Companion resource

For deeper formula explanations, worked examples, conditions, interpretation guidance, and interactive tools, see **[AP Statistics Formula Sheet 2027](https://onlineinternetcafe.com/ap-statistics-formula-sheet/)**.