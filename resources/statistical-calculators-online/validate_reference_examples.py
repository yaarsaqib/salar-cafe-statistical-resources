"""Validate core reference examples for the Statistical Calculators Online resource.

This script uses only Python's standard library. It is intended as a small,
transparent cross-check for hand-calculated examples in validation-examples.md.
"""

from __future__ import annotations

import math
import statistics


def close(actual: float, expected: float, tol: float = 1e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"expected {expected}, got {actual}")


def pearson_r(x: list[float], y: list[float]) -> float:
    xbar = statistics.mean(x)
    ybar = statistics.mean(y)
    numerator = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    denominator = math.sqrt(
        sum((xi - xbar) ** 2 for xi in x)
        * sum((yi - ybar) ** 2 for yi in y)
    )
    return numerator / denominator


def regression(x: list[float], y: list[float]) -> tuple[float, float]:
    xbar = statistics.mean(x)
    ybar = statistics.mean(y)
    slope = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y)) / sum(
        (xi - xbar) ** 2 for xi in x
    )
    intercept = ybar - slope * xbar
    return intercept, slope


def welch_t(a: list[float], b: list[float]) -> tuple[float, float, float]:
    na, nb = len(a), len(b)
    ma, mb = statistics.mean(a), statistics.mean(b)
    sa, sb = statistics.stdev(a), statistics.stdev(b)
    va, vb = sa * sa / na, sb * sb / nb
    se = math.sqrt(va + vb)
    t = (ma - mb) / se
    df = (va + vb) ** 2 / (va * va / (na - 1) + vb * vb / (nb - 1))
    return se, t, df


def chi_square(observed: list[list[float]]) -> float:
    row_totals = [sum(row) for row in observed]
    col_totals = [sum(observed[i][j] for i in range(len(observed))) for j in range(len(observed[0]))]
    total = sum(row_totals)
    statistic = 0.0
    for i, row in enumerate(observed):
        for j, value in enumerate(row):
            expected = row_totals[i] * col_totals[j] / total
            statistic += (value - expected) ** 2 / expected
    return statistic


def pooled_two_proportion_z(x1: int, n1: int, x2: int, n2: int) -> tuple[float, float, float]:
    p1 = x1 / n1
    p2 = x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    se = math.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    return pooled, se, z


def main() -> None:
    x = [2, 4, 5, 7, 8, 10]
    y = [5, 8, 7, 11, 13, 14]

    close(statistics.mean(x), 6.0)
    close(statistics.variance(x), 8.4)
    close(statistics.stdev(x), 2.898275349237888)
    close(pearson_r(x, y), 0.9694584179118516)

    intercept, slope = regression(x, y)
    close(intercept, 2.5238095238095237)
    close(slope, 1.1904761904761905)

    group_a = [12, 15, 14, 10, 13, 16]
    group_b = [9, 11, 8, 12, 10, 9]
    se, t_stat, df = welch_t(group_a, group_b)
    close(se, 1.0671873729054748)
    close(t_stat, 3.2796489996607274)
    close(df, 8.819517313746063)

    close(chi_square([[30, 20], [15, 35]]), 9.09090909090909)

    pooled, prop_se, z = pooled_two_proportion_z(84, 120, 70, 110)
    close(pooled, 0.6695652173913044)
    close(prop_se, 0.06208922985323716)
    close(z, 1.0249179090606126)

    print("PASS: all reference calculations match expected values")


if __name__ == "__main__":
    main()
