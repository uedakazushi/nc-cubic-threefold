#!/usr/bin/env python3
"""Exact finite checks for the four-vertex quartic potential model.

This verifies the signed convention, two examples and tangent linear algebra.
It does not certify Koszulity at arbitrary points of the determinantal locus.
Only Python's standard library is used.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, combinations_with_replacement, permutations, product
import json
from pathlib import Path


WORDS = list(product(range(4), repeat=4))
INDEX = {word: i for i, word in enumerate(WORDS)}
PAIRS = list(product(range(4), repeat=2))


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][c]
        a[r] = [x / v for x in a[r]]
        for i in range(r + 1, len(a)):
            v = a[i][c]
            if v:
                a[i] = [x - v * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def signed_potential(tensor):
    out = defaultdict(int)
    for word, coefficient in tensor.items():
        for s in range(4):
            out[s, word[s:] + word[:s]] += (-1) ** s * coefficient
    return {p: c for p, c in out.items() if c}


def rotate(potential):
    out = defaultdict(int)
    for (start, word), coefficient in potential.items():
        out[(start + 1) % 4, word[1:] + word[:1]] += coefficient
    return {p: c for p, c in out.items() if c}


def derivatives(potential, target):
    # Columns are length-two prefixes, rows are the remaining length-two paths.
    start = (target - 2) % 4
    return [[potential.get((start, prefix + tail), 0) for prefix in PAIRS]
            for tail in PAIRS]


def symmetrized_row(word, swaps):
    row = [0] * len(WORDS)
    for choices in product((0, 1), repeat=2):
        w = list(word)
        for choice, (i, j) in zip(choices, swaps):
            if choice:
                w[i], w[j] = w[j], w[i]
        row[INDEX[tuple(w)]] += 1
    return row


def run_checks():
    alt = {w: (-1) ** sum(w[i] > w[j] for i in range(4) for j in range(i + 1, 4))
           for w in permutations(range(4))}
    bad = {(a, b, a, b): 1 for a, b in PAIRS}
    omega = signed_potential(alt)
    omega_bad = signed_potential(bad)
    for p in (omega, omega_bad):
        assert rotate(p) == {word: -c for word, c in p.items()}

    commutators = []
    for tail in PAIRS:
        commutators.append([int(tail == (a, b)) - int(tail == (b, a))
                            for a, b in combinations(range(4), 2)])
    good_ranks, bad_ranks = [], []
    for i in range(4):
        matrix = derivatives(omega, i)
        good_ranks.append(rank(matrix))
        assert rank([r + c for r, c in zip(matrix, commutators)]) == 6
        bad_ranks.append(rank(derivatives(omega_bad, i)))
    assert good_ranks == [6] * 4
    assert bad_ranks == [16] * 4

    unordered = list(combinations_with_replacement(range(4), 2))
    cut01 = [symmetrized_row((a, b, c, d), ((0, 1), (2, 3)))
             for a, b in unordered for c, d in unordered]
    cut12 = [symmetrized_row((d, a, b, c), ((1, 2), (3, 0)))
             for a, b in unordered for c, d in unordered]
    constraints = cut01 + cut12
    assert rank(cut01) == rank(cut12) == 100
    constraint_rank = rank(constraints)
    assert constraint_rank == 165

    columns = []
    for slot in range(4):
        for new, old in PAIRS:
            column = [0] * len(WORDS)
            for word, coefficient in alt.items():
                if word[slot] == old:
                    changed = list(word)
                    changed[slot] = new
                    column[INDEX[tuple(changed)]] += coefficient
            columns.append(column)
    orbit = [list(row) for row in zip(*columns)]
    orbit_rank = rank(orbit)
    assert orbit_rank == 46
    assert all(sum(x * y for x, y in zip(row, col)) == 0
               for row in constraints for col in columns)
    assert any(sum(row[INDEX[word]] * coefficient for word, coefficient in alt.items())
               for row in constraints) is False

    return {
        "date": "2026-11-14",
        "version": 1,
        "field": "Q; exact Fraction elimination",
        "potential_space_dimension": 256,
        "signed_rotation": "rho(omega)=-omega, verified over Z",
        "polynomial_tensor": "sum_{sigma in S4} sign(sigma) x_sigma(0)^(0) ... x_sigma(3)^(3)",
        "polynomial_derivative_ranks": good_ranks,
        "polynomial_relations_equal_commutator_spaces": True,
        "bad_tensor": "sum_{a,b=0}^3 x_a^(0) x_b^(1) x_a^(2) x_b^(3)",
        "bad_derivative_ranks": bad_ranks,
        "bad_quotient_degree_two_is_zero": True,
        "tangent_constraint_matrix_shape": [200, 256],
        "tangent_constraint_rank": constraint_rank,
        "two_constraint_row_space_dimensions": [100, 100],
        "intersection_dimension": 35,
        "affine_tensor_tangent_dimension": 91,
        "projective_tensor_tangent_dimension": 90,
        "orbit_matrix_shape": [256, 64],
        "affine_GL4_fourfold_orbit_rank": orbit_rank,
        "projective_orbit_rank": 45,
        "orbit_directions_satisfy_constraints_over_Z": True,
        "quotient_tangent_dimension": 45,
        "scope": "Finite signed-potential and tangent checks; not a global AS-locus or component classification.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="build/p3_potential_checks.json")
    args = parser.parse_args()
    result = run_checks()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"polynomial_ranks": result["polynomial_derivative_ranks"],
                      "bad_ranks": result["bad_derivative_ranks"],
                      "constraint_rank": result["tangent_constraint_rank"],
                      "orbit_rank": result["affine_GL4_fourfold_orbit_rank"],
                      "quotient_tangent_dimension": result["quotient_tangent_dimension"],
                      "output": str(output)}, indent=2))
