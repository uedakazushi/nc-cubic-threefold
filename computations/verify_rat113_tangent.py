#!/usr/bin/env python3
"""Characteristic-zero certificate for the Rat(1,1,3) Poisson component.

Constructs the full strict-Jacobi-plus-divergence differential (375 x 150)
and the Jacobian-family differential (150 x 37) over Z.  The product is
checked over Z. Nonzero minors modulo a prime certify lower bounds over Q;
the exact product supplies the opposite bounds. No zero modulo p is used
as an identity over Q. No historical file or external repository is read.
"""
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path
import argparse
import hashlib
import json

N = 5
PAIRS = list(combinations(range(N), 2))
TRIPLES = list(combinations(range(N), 3))
ZERO = (0,) * N


def monomials(degree):
    out = []
    for factors in combinations_with_replacement(range(N), degree):
        e = [0] * N
        for i in factors:
            e[i] += 1
        out.append(tuple(e))
    return out


def add(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: c * a for e, a in p.items() if c * a}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            g = tuple(a + b for a, b in zip(e, f))
            out[g] = out.get(g, 0) + c * d
    return {e: c for e, c in out.items() if c}


def der(p, i):
    out = {}
    for e, c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c * e[i]
    return out


def sign(indices):
    return (-1) ** sum(indices[i] > indices[j]
                       for i in range(len(indices))
                       for j in range(i + 1, len(indices)))


def jacobian(f, a, b):
    # i_(J) (dx dy dz du dv) = df wedge da wedge db.
    out = {}
    for i, j in PAIRS:
        rest = [l for l in range(N) if l not in (i, j)]
        p = {}
        for order in permutations(rest):
            p = add(p, scale(mul(mul(der(f, order[0]), der(a, order[1])),
                                 der(b, order[2])), sign((i, j) + order)))
        out[i, j] = p
    return out


def entry(p, i, j):
    if i == j:
        return {}
    return p.get((i, j), {}) if i < j else scale(p.get((j, i), {}), -1)


def differential(p, q):
    out = []
    for i, j, k in TRIPLES:
        poly = {}
        for a, b, c in [(i, j, k), (j, k, i), (k, i, j)]:
            for l in range(N):
                poly = add(poly, mul(entry(q, a, l), der(entry(p, b, c), l)),
                           mul(entry(p, a, l), der(entry(q, b, c), l)))
        out.extend(poly.get(e, 0) for e in MON3)
    for j in range(N):
        poly = add(*(der(entry(q, i, j), i) for i in range(N)))
        out.extend(poly.get(e, 0) for e in MON1)
    return out


MON1, MON2, MON3 = (monomials(i) for i in (1, 2, 3))
COLUMNS = [(ij, e) for ij in PAIRS for e in MON2]


def vector(p):
    return [p.get(ij, {}).get(e, 0) for ij, e in COLUMNS]


def transpose(columns):
    return [list(row) for row in zip(*columns)]


def minor_witness(matrix, prime):
    m = [[a % prime for a in row] for row in matrix]
    labels = list(range(len(m)))
    rows, cols = [], []
    r = 0
    for j in range(len(m[0])):
        k = next((i for i in range(r, len(m)) if m[i][j]), None)
        if k is None:
            continue
        m[r], m[k] = m[k], m[r]
        labels[r], labels[k] = labels[k], labels[r]
        rows.append(labels[r])
        cols.append(j)
        inv = pow(m[r][j], -1, prime)
        m[r] = [a * inv % prime for a in m[r]]
        for i in range(r + 1, len(m)):
            if m[i][j]:
                c = m[i][j]
                m[i] = [(a - c * b) % prime for a, b in zip(m[i], m[r])]
        r += 1
        if r == min(len(m), len(m[0])):
            break
    # Recompute the determinant of the original indicated square submatrix.
    square = [[matrix[i][j] % prime for j in cols] for i in rows]
    det = 1
    for j in range(r):
        k = next(i for i in range(j, r) if square[i][j])
        if k != j:
            square[j], square[k] = square[k], square[j]
            det = -det
        pivot = square[j][j]
        det = det * pivot % prime
        inv = pow(pivot, -1, prime)
        for i in range(j + 1, r):
            c = square[i][j] * inv % prime
            for l in range(j, r):
                square[i][l] = (square[i][l] - c * square[j][l]) % prime
    assert det != 0
    return {"size": r, "rows_zero_based": rows, "columns_zero_based": cols,
            "prime": prime, "determinant_mod_prime": det}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("build/rat113_tangent.json"))
    args = parser.parse_args()
    x, y, z, u, v = ({e: 1} for e in MON1)
    # Same active polynomial as the existing 31x31 slice certificate;
    # binary cubics have no effect on its Jacobian bracket.
    terms = {
        (3, 0, 0, 0, 0): 3, (0, 3, 0, 0, 0): 3, (0, 0, 3, 0, 0): 3,
        (1, 1, 1, 0, 0): 5,
        (2, 0, 0, 1, 0): 1, (0, 2, 0, 0, 1): 2,
        (0, 0, 2, 1, 0): 3, (0, 0, 2, 0, 1): 3,
        (1, 0, 0, 2, 0): 1, (1, 0, 0, 1, 1): 1, (1, 0, 0, 0, 2): 2,
        (0, 1, 0, 2, 0): 2, (0, 1, 0, 1, 1): 3, (0, 1, 0, 0, 2): 1,
        (0, 0, 1, 2, 0): 1, (0, 0, 1, 1, 1): 4, (0, 0, 1, 0, 2): 5,
    }
    p = jacobian(terms, u, v)
    assert all(c == 0 for c in differential(p, p))
    matrix = transpose([differential(p, {ij: {e: 1}}) for ij, e in COLUMNS])
    family_columns = [vector(jacobian({e: 1}, u, v))
                      for e in MON3 if sum(e[:3]) > 0]
    family_columns += [vector(jacobian(terms, w, v)) for w in (x, y, z)]
    family_columns += [vector(jacobian(terms, u, w)) for w in (x, y, z)]
    family = transpose(family_columns)
    assert (len(matrix), len(matrix[0])) == (375, 150)
    assert (len(family), len(family[0])) == (150, 37)
    # The upper bound is exact integer arithmetic, not a modular zero test.
    assert all(sum(a * b for a, b in zip(row, col)) == 0
               for row in matrix for col in family_columns)
    pm, ps = minor_witness(matrix, 1000003), minor_witness(family, 1000003)
    assert (pm["size"], ps["size"]) == (113, 37), (pm["size"], ps["size"])
    certificate = {
        "date": "2026-11-13", "version": 1,
        "variables": ["x", "y", "z", "u", "v"],
        "active_polynomial_terms": [{"exponents": e, "coefficient": c}
                                    for e, c in terms.items()],
        "monomial_order": "combinations_with_replacement(range(5), degree)",
        "matrix_rows": "10 lex triples x 35 degree3 monomials, then 5 divergence components x 5 degree1 monomials",
        "matrix_columns": "10 lex pairs x 15 degree2 monomials",
        "family_columns": "31 nonbinary degree3 monomials, then variation of u by x,y,z, then v by x,y,z",
        "jacobi_and_divergence_exact_zero": True,
        "matrix_times_family_exact_zero": True,
        "equation_differential": pm, "family_differential": ps,
        "rank_over_Q": 113, "affine_tangent_dimension": 37,
        "projectivized_tangent_dimension": 36,
        "conclusion": "The full unimodular Poisson scheme is smooth of dimension 37 at this point; the Rat113 cone is a generically reduced irreducible component.",
        "scope": "Does not by itself prove algebraicity of the full Z-algebra stack or generic reducedness of an unmarked quantum moduli stack.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"rank_Q": 113, "tangent_dimension": 37,
                      "minor113_mod_1000003": pm["determinant_mod_prime"],
                      "minor37_mod_1000003": ps["determinant_mod_prime"],
                      "integer_product_zero": True, "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
