"""Transparent Wald-Wolfowitz two-sample runs test example.

Companion guide:
https://onlineinternetcafe.com/wald-wolfowitz-runs-test-7-essential-steps-formula-and-worked-example/

The exact distribution implemented here assumes two independent samples and a
unique pooled order. Cross-group ties require a separately documented rule.
"""

from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path
from typing import Iterable


DATA_FILE = Path(__file__).with_name("wald_wolfowitz_example.csv")


def load_data(path: Path) -> list[tuple[float, str]]:
    """Read numeric values and binary group labels from a CSV file."""
    rows: list[tuple[float, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"value", "group"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain 'value' and 'group' columns.")

        for line_number, row in enumerate(reader, start=2):
            try:
                value = float(row["value"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid numeric value on line {line_number}.") from exc

            group = str(row["group"]).strip()
            if not group:
                raise ValueError(f"Missing group label on line {line_number}.")
            rows.append((value, group))

    if not rows:
        raise ValueError("The input file contains no observations.")
    return rows


def validate_two_groups(rows: Iterable[tuple[float, str]]) -> tuple[str, str]:
    """Return the two group labels or raise a clear validation error."""
    labels = sorted({group for _, group in rows})
    if len(labels) != 2:
        raise ValueError(f"Exactly two groups are required; found {len(labels)}.")
    return labels[0], labels[1]


def detect_cross_group_ties(rows: Iterable[tuple[float, str]]) -> list[float]:
    """Identify outcome values shared by both groups."""
    groups_by_value: dict[float, set[str]] = {}
    for value, group in rows:
        groups_by_value.setdefault(value, set()).add(group)
    return sorted(value for value, groups in groups_by_value.items() if len(groups) > 1)


def count_runs(labels: list[str]) -> int:
    """Count maximal consecutive blocks in an ordered label sequence."""
    if not labels:
        raise ValueError("At least one ordered label is required.")
    return 1 + sum(current != previous for previous, current in zip(labels, labels[1:]))


def expected_runs(n1: int, n2: int) -> float:
    total = n1 + n2
    return 1.0 + (2.0 * n1 * n2) / total


def run_variance(n1: int, n2: int) -> float:
    total = n1 + n2
    numerator = 2.0 * n1 * n2 * (2.0 * n1 * n2 - total)
    denominator = total**2 * (total - 1)
    return numerator / denominator


def normal_two_sided_p(z_stat: float) -> float:
    """Return 2*Phi(-abs(z)) using only Python's standard library."""
    return math.erfc(abs(z_stat) / math.sqrt(2.0))


def combinations(n: int, k: int) -> int:
    """Safe combination count that returns zero outside the valid range."""
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def exact_run_probability(run_count: int, n1: int, n2: int) -> float:
    """Probability mass P(R=r) under the tie-free conditional null model."""
    total_sequences = combinations(n1 + n2, n1)
    if run_count % 2 == 0:
        k = run_count // 2
        favorable = (
            2
            * combinations(n1 - 1, k - 1)
            * combinations(n2 - 1, k - 1)
        )
    else:
        k = (run_count - 1) // 2
        favorable = (
            combinations(n1 - 1, k) * combinations(n2 - 1, k - 1)
            + combinations(n1 - 1, k - 1) * combinations(n2 - 1, k)
        )
    return favorable / total_sequences


def exact_doubled_tail_p(observed_runs: int, n1: int, n2: int) -> float:
    """Return twice the smaller exact tail, capped at 1.

    Exact two-sided conventions can differ across software. This function uses
    the common doubled-smaller-tail convention and reports that choice.
    """
    maximum_runs = 2 * min(n1, n2) + (1 if n1 != n2 else 0)
    distribution = {
        run_count: exact_run_probability(run_count, n1, n2)
        for run_count in range(2, maximum_runs + 1)
    }
    lower_tail = sum(
        probability
        for run_count, probability in distribution.items()
        if run_count <= observed_runs
    )
    upper_tail = sum(
        probability
        for run_count, probability in distribution.items()
        if run_count >= observed_runs
    )
    return min(1.0, 2.0 * min(lower_tail, upper_tail))


def main() -> None:
    rows = load_data(DATA_FILE)
    group_1, group_2 = validate_two_groups(rows)

    shared_ties = detect_cross_group_ties(rows)
    if shared_ties:
        preview = ", ".join(str(value) for value in shared_ties[:8])
        raise ValueError(
            "Cross-group ties make the pooled order non-unique. "
            f"Shared values include: {preview}. Apply a documented tie rule "
            "or a minimum/maximum-run sensitivity analysis."
        )

    ordered = sorted(rows, key=lambda item: item[0])
    labels = [group for _, group in ordered]
    counts = Counter(labels)
    n1, n2 = counts[group_1], counts[group_2]

    observed = count_runs(labels)
    expected = expected_runs(n1, n2)
    variance = run_variance(n1, n2)
    z_stat = (observed - expected) / math.sqrt(variance)
    asymptotic_p = normal_two_sided_p(z_stat)
    exact_p = exact_doubled_tail_p(observed, n1, n2)

    print("Wald-Wolfowitz two-sample runs test")
    print(f"Group labels: {group_1}, {group_2}")
    print(f"Sample sizes: {n1}, {n2}")
    print(f"Ordered labels: {' '.join(labels)}")
    print(f"Observed runs: {observed}")
    print(f"Expected runs: {expected:.6f}")
    print(f"Variance: {variance:.6f}")
    print(f"z statistic: {z_stat:.6f}")
    print(f"Two-sided normal p-value: {asymptotic_p:.6f}")
    print(f"Doubled-tail exact p-value: {exact_p:.6f}")


if __name__ == "__main__":
    main()
