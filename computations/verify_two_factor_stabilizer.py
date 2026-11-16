#!/usr/bin/env python3
"""Exact certificate for a finite projective two-factor relation stabilizer.

The matrix has 150 rows (10 relations x 15 degree-two quotient coordinates)
and 50 columns (the two 5 x 5 infinitesimal changes of generators).
Its two scalar kernel vectors are checked over Z.  A nonzero 48 x 48
minor modulo 1000003 supplies the opposite rank bound over Q.
No vanishing modulo a prime is used as a characteristic-zero identity.
"""
from pathlib import Path
import argparse
import hashlib
import json

from verify_rat113_tangent import MON1, MON2, PAIRS, entry, jacobian, minor_witness, transpose


def active_polynomial():
    # F_0 from the paper, omitting the binary cubic that does not affect R.
    return {
        (3, 0, 0, 0, 0): 3, (0, 3, 0, 0, 0): 3, (0, 0, 3, 0, 0): 3,
        (1, 1, 1, 0, 0): 5,
        (2, 0, 0, 1, 0): 1, (0, 2, 0, 0, 1): 2,
        (0, 0, 2, 1, 0): 3, (0, 0, 2, 0, 1): 3,
        (1, 0, 0, 2, 0): 1, (1, 0, 0, 1, 1): 1, (1, 0, 0, 0, 2): 2,
        (0, 1, 0, 2, 0): 2, (0, 1, 0, 1, 1): 3, (0, 1, 0, 0, 2): 1,
        (0, 0, 1, 2, 0): 1, (0, 0, 1, 1, 1): 4, (0, 0, 1, 0, 2): 5,
    }


def matrices():
    x, y, z, u, v = ({e: 1} for e in MON1)
    poisson = jacobian(active_polynomial(), u, v)
    # Q is twice the projection V^2 -> Sym^2 V along the relation graph.
    quotient = [[0] * 25 for _ in MON2]
    for i in range(5):
        for j in range(5):
            e = tuple(int(k == i) + int(k == j) for k in range(5))
            quotient[MON2.index(e)][5 * i + j] = 2
            for e, c in entry(poisson, i, j).items():
                quotient[MON2.index(e)][5 * i + j] += c
    # The columns are twice the relations, so all entries are integers.
    relations = []
    for i, j in PAIRS:
        r = [0] * 25
        r[5 * i + j] = 2
        r[5 * j + i] = -2
        for e, c in poisson[i, j].items():
            a, b = [k for k, n in enumerate(e) for _ in range(n)]
            if a == b:
                r[5 * a + b] -= 2 * c
            else:
                r[5 * a + b] -= c
                r[5 * b + a] -= c
        relations.append(r)
    assert all(sum(q * r for q, r in zip(row, rel)) == 0
               for row in quotient for rel in relations)
    columns = []
    for side in range(2):
        for a in range(5):
            for b in range(5):
                column = []
                for rel in relations:
                    moved = [0] * 25
                    for j in range(5):
                        if side == 0:
                            moved[5 * a + j] += rel[5 * b + j]
                        else:
                            moved[5 * j + a] += rel[5 * j + b]
                    column.extend(sum(q * r for q, r in zip(row, moved))
                                  for row in quotient)
                columns.append(column)
    matrix = transpose(columns)
    assert (len(matrix), len(matrix[0])) == (150, 50)
    scalars = [[int(j == offset + 5 * a + a)
                for j in range(50)] for offset in (0, 25) for a in range(5)]
    scalar_left = [sum(scalars[a][j] for a in range(5)) for j in range(50)]
    scalar_right = [sum(scalars[5 + a][j] for a in range(5)) for j in range(50)]
    for vector in (scalar_left, scalar_right):
        assert all(sum(a * b for a, b in zip(row, vector)) == 0 for row in matrix)
    return matrix


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('build/two_factor_stabilizer.json'))
    args = parser.parse_args()
    matrix = matrices()
    witness = minor_witness(matrix, 1000003)
    assert witness['size'] == 48
    assert witness['determinant_mod_prime'] == 815096
    root = Path(__file__).resolve().parent
    certificate = {
        'date': '2026-11-14', 'version': 1,
        'matrix_shape': [150, 50],
        'variables': ['x', 'y', 'z', 'u', 'v'],
        'polynomial': 'F_0 in eq:F0, binary cubic omitted',
        'rows': '10 lexicographic pairs, then 15 combinations_with_replacement degree-two monomials',
        'columns': 'left factor E_ab in row-major order, then right factor E_ab in row-major order',
        'integer_scaling': 'relation columns doubled; quotient projection doubled',
        'equation': 'M(X,Y) = vec(Q (X tensor 1 + 1 tensor Y) R)',
        'quotient_times_relations_zero_over_Z': True,
        'two_scalar_kernel_vectors_zero_over_Z': True,
        'minor': witness,
        'rank_over_Q': 48,
        'projective_two_factor_stabilizer_lie_dimension': 0,
        'conclusion': 'The projective two-factor stabilizer is finite at F_0 and on a nonempty open subset of the family.',
        'limit': 'Does not compute the finite group order, the degree of period-forgetting, or a global Z-algebra moduli component.',
        'source_sha256': {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                          for name in ('verify_two_factor_stabilizer.py', 'verify_rat113_tangent.py')},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps({'rank_Q': 48, 'minor_mod_1000003': 815096,
                      'scalar_kernel_exact': True, 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
