#!/usr/bin/env python3
"""Exact free-word identities for the relative potential bimodule resolution.

Only Python's standard library is required.  We test the complete word basis
of active potentials of degree <= 3, with central coefficients left arbitrary.
The tensor convention is D = B tensor B^op, so (a,b)(c,d) = (ac,db), and
flip(a,b) = (b,a) is an anti-involution.  The manuscript uses
H[j,i] = partial_j^nc(partial_i^cyc Phi).

These checks certify polynomial identities and the stated cochain signs.
They do not certify exactness, PBW, projectivity, or a Calabi--Yau theorem.
"""

import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path


LETTERS = "xyz"
EMPTY = ()


def add(*polys):
    result = defaultdict(Fraction)
    for poly in polys:
        for key, coefficient in poly.items():
            result[key] += coefficient
    return {key: value for key, value in result.items() if value}


def scale(poly, coefficient):
    return {key: coefficient * value for key, value in poly.items()
            if coefficient * value}


def word(letters, coefficient=1):
    return {tuple(letters): Fraction(coefficient)}


def multiply(left, right):
    result = defaultdict(Fraction)
    for a, ca in left.items():
        for b, cb in right.items():
            result[a + b] += ca * cb
    return {key: value for key, value in result.items() if value}


def tensor_multiply(left, right):
    result = defaultdict(Fraction)
    for (a, b), ca in left.items():
        for (c, d), cb in right.items():
            result[(a + c, d + b)] += ca * cb
    return {key: value for key, value in result.items() if value}


def flip(poly):
    return {(b, a): coefficient for (a, b), coefficient in poly.items()}


def delta(poly):
    return add({(w, EMPTY): c for w, c in poly.items()},
               {(EMPTY, w): -c for w, c in poly.items()})


def cyclic_derivative(poly, letter):
    result = defaultdict(Fraction)
    for w, coefficient in poly.items():
        for i, value in enumerate(w):
            if value == letter:
                result[w[i + 1:] + w[:i]] += coefficient
    return {key: value for key, value in result.items() if value}


def double_derivative(poly, letter):
    result = defaultdict(Fraction)
    for w, coefficient in poly.items():
        for i, value in enumerate(w):
            if value == letter:
                result[(w[:i], w[i + 1:])] += coefficient
    return {key: value for key, value in result.items() if value}


def verify_potential(phi):
    variables = [word(x) for x in LETTERS]
    differences = [delta(x) for x in variables]
    relations = [cyclic_derivative(phi, x) for x in LETTERS]
    hessian = [[double_derivative(relations[i], x)
                for i in range(3)] for x in LETTERS]

    commutators = [add(multiply(x, r), scale(multiply(r, x), -1))
                   for x, r in zip(variables, relations)]
    assert not add(*commutators), "cyclic commutator identity"

    for j in range(3):
        for i in range(3):
            assert hessian[j][i] == flip(hessian[i][j]), "flip Hessian"
    # Maps are specified on bases of LEFT D-modules.  Thus d1(d2(f_i))
    # has coefficients H[j,i] delta_j, while d2(d3(e)) has delta_i H[j,i].
    for i in range(3):
        composed = add(*(tensor_multiply(hessian[j][i], differences[j])
                         for j in range(3)))
        assert composed == delta(relations[i]), "d1 d2 relation identity"
    for j in range(3):
        composed = add(*(tensor_multiply(differences[i], hessian[j][i])
                         for i in range(3)))
        assert composed == delta(relations[j]), "d2 d3 relation identity"

    # K occupies cochain degrees -3,...,0.  On Hom_D(K,D),
    # d^j(f)=(-1)^(j+1) f d_K; right modules are returned to left via flip.
    # K(3)[-3] has differential -d_K.  Psi has signs (+,-,+,-).
    signs = (1, -1, 1, -1)
    for i in range(3):
        dual_d0 = scale(flip(differences[i]), -1)
        dual_d2 = scale(flip(differences[i]), -1)
        assert scale(dual_d0, signs[1]) == scale(differences[i], -signs[0])
        assert scale(dual_d2, signs[3]) == scale(differences[i], -signs[2])
        for j in range(3):
            dual_d1 = flip(hessian[j][i])
            assert scale(dual_d1, signs[2]) == scale(hessian[i][j], -signs[1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    count = 0
    for degree in range(4):
        for w in product(LETTERS, repeat=degree):
            verify_potential(word(w))
            count += 1

    commutator_potential = add(word("xyz"), word("yxz", -1))
    expected = (add(word("yz"), word("zy", -1)),
                add(word("zx"), word("xz", -1)),
                add(word("xy"), word("yx", -1)))
    assert tuple(cyclic_derivative(commutator_potential, x)
                 for x in LETTERS) == expected
    symmetric_xyz = add(*(word(w, Fraction(1, 6))
                          for w in permutations(LETTERS)))
    for i, x in enumerate(LETTERS):
        y, z = LETTERS[(i + 1) % 3], LETTERS[(i + 2) % 3]
        assert cyclic_derivative(symmetric_xyz, x) == add(
            word(y + z, Fraction(1, 2)), word(z + y, Fraction(1, 2)))
        assert cyclic_derivative(word(x * 3), x) == word(x * 2, 3)
        assert cyclic_derivative(word(x * 2), x) == word(x, 2)
        assert cyclic_derivative(word(x), x) == word(EMPTY)

    result = {
        "status": "pass",
        "active_potential_word_basis_size": count,
        "active_degrees": [0, 1, 2, 3],
        "checks": {
            "cyclic_commutator_identity": True,
            "flip_hessian_identity": True,
            "d1_d2_equals_relation_difference": True,
            "d2_d3_equals_relation_difference": True,
            "cochain_self_duality_signs": True,
            "commutator_and_symmetrization_normalizations": True,
        },
        "conventions": {
            "tensor_product": "(a,b)(c,d)=(ac,db) in B tensor B^op",
            "hessian": "H[j,i]=partial_j^nc(partial_i^cyc Phi)",
            "dual_differential": "d^j(f)=(-1)^(j+1) f d_K",
            "self_duality_signs": [1, -1, 1, -1],
        },
        "scope": "free-word identities and cochain signs only; no exactness or PBW assertion",
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
