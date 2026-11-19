#!/usr/bin/env python3
"""Exact polynomial certificates for point schemes and Poisson zero loci.

Requires Python 3 and SymPy. Run, for example:
    python computations/verify_point_poisson.py --output point_poisson_certificate.json

All nine checks use exact arithmetic; no numerical sampling is used. The JSON
records the script's SHA256 and the SymPy version. These identities support the
proofs, but do not on their own prove point-functor representability, global
scheme decompositions, or categorical reconstruction.

The last check uses the Weierstrass coefficients in Artebani--Dolgachev,
The Hesse pencil of plane cubic curves, arXiv:math/0611590, Section 2,
equations (6)--(8), with j = 1728*4*A^3/(4*A^3+27*B^2) for
the Weierstrass equation Y^2*Z = X^3+A*X*Z^2+B*Z^3.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


def require(condition, label):
    if not condition:
        raise RuntimeError("Exact verification failed: " + label)


def require_zero(expression, label):
    require(sp.expand(expression) == 0, label)


def run_checks():
    x, y, z, u, v, h, lam = sp.symbols("x y z u v h lambda")
    checks = []

    def record(name, **details):
        checks.append({"name": name, "passed": True, **details})

    # 1. Fermat boundary equation and a polynomial representative of its shift.
    e_fermat = x**3 + y**3 + z**3 + h**2 * x * y * z
    matrix = sp.Matrix([
        [-h * x, -z, y],
        [z, -h * y, -x],
        [-y, x, -h * z],
    ])
    q = sp.Matrix([x * z + h * y**2,
                   y * z - h * x**2,
                   z**2 + h**2 * x * y])
    require_zero(matrix.det() + h * e_fermat, "Fermat determinant")
    expected_product = sp.Matrix([0, 0, -h * e_fermat])
    for i, entry in enumerate(matrix * q - expected_product):
        require_zero(entry, "Fermat shift representative, row " + str(i))
    record("fermat_boundary_determinant",
           identity="det(M) = -h*(x^3+y^3+z^3+h^2*x*y*z)",
           shift_representative_verified=True)

    # 2. Evaluation of the central cubic on three consecutive point coordinates.
    p = sp.Matrix([x, y, z])

    def polynomial_shift(point):
        a, b, c = point
        return sp.Matrix([a * c + h * b**2,
                          b * c - h * a**2,
                          c**2 + h**2 * a * b])

    r = polynomial_shift(q)
    nine_w_multilinear = (
        3 * sum(p[i] * q[i] * r[i] for i in range(3))
        - h**2 * sum(p[i] * q[j] * r[k]
                     for i, j, k in itertools.permutations(range(3)))
    )
    quotient = (2 * h**4 * x**2 * y**2 + h**3 * x**3 * z
                - h**3 * y**3 * z + h**2 * x * y * z**2 + z**4)
    require_zero(nine_w_multilinear - 3 * e_fermat * quotient,
                 "Fermat central cubic multilinearization")
    record("fermat_central_multilinearization",
           identity="9*w_ml(p,q,q(q)) = 3*e_h*quotient",
           quotient="2*h^4*x^2*y^2+h^3*x^3*z-h^3*y^3*z+h^2*x*y*z^2+z^4")

    # 3. General Hesse parameters and boundary determinant.
    f3 = (x**3 + y**3 + z**3) / 3 + lam * x * y * z
    a = 1 - lam * h / 2
    b = -1 - lam * h / 2
    c = -h
    hesse_matrix = sp.Matrix([
        [c * x, b * z, a * y],
        [a * z, c * y, b * x],
        [b * y, a * x, c * z],
    ])
    coeff_a = 1 - lam**2 * h**2 / 4
    coeff_b = 3 * lam + (1 + lam**3 / 4) * h**2
    e_hesse = coeff_a * (x**3 + y**3 + z**3) + coeff_b * x * y * z
    require_zero(hesse_matrix.det() + h * e_hesse,
                 "general Hesse boundary determinant")
    record("hesse_boundary_determinant",
           identity="det(M_Hesse) = -h*(A*(x^3+y^3+z^3)+B*x*y*z)",
           A="1-lambda^2*h^2/4",
           B="3*lambda+(1+lambda^3/4)*h^2")

    # 4. Finite Hessian correction, including its coefficient.
    hessian = sp.hessian(f3, (x, y, z))
    hessian_det = hessian.det()
    expected_hessian_det = ((8 + 2 * lam**3) * x * y * z
                            - 2 * lam**2 * (x**3 + y**3 + z**3))
    require_zero(hessian_det - expected_hessian_det, "Hesse Hessian determinant")
    require_zero(e_hesse - 3 * (f3 + h**2 * hessian_det / 24),
                 "finite Hessian correction")
    record("hesse_hessian_correction",
           identity="e_h = 3*(f3+h^2*det(Hess(f3))/24)",
           hessian_determinant="(8+2*lambda^3)*x*y*z-2*lambda^2*(x^3+y^3+z^3)")

    # 5. The two Hesse cubics are not proportional in the fixed plane when
    #    h != 0 and the classical cubic is smooth (lambda^3 != -1).
    require_zero(coeff_b - 3 * lam * coeff_a - h**2 * (1 + lam**3),
                 "Hesse coefficient separation")
    record("hesse_coefficient_separation",
           identity="B-3*lambda*A = h^2*(1+lambda^3)")

    # 6. Integrability of M*grad(f3). Rows: coefficients x,y,z in entries
    #    (1,2), (1,3), (2,3) of M*Hess(f3)-(M*Hess(f3))^T.
    #    Columns: m11,m12,m13,m21,m22,m23,m31,m32,m33.
    m = sp.symbols("m11 m12 m13 m21 m22 m23 m31 m32 m33")
    unknown_matrix = sp.Matrix(3, 3, m)
    product = unknown_matrix * hessian
    equations = [
        sp.Poly(sp.expand(product[i, j] - product[j, i]), x, y, z)
          .coeff_monomial(variable)
        for i, j in ((0, 1), (0, 2), (1, 2))
        for variable in (x, y, z)
    ]
    integrability, rhs = sp.linear_eq_to_matrix(equations, m)
    require(integrability.shape == (9, 9), "integrability matrix shape")
    require(rhs == sp.zeros(9, 1), "homogeneous integrability equations")
    identity_vector = sp.Matrix([1, 0, 0, 0, 1, 0, 0, 0, 1])
    require(integrability * identity_vector == sp.zeros(9, 1),
            "scalar integrability kernel")
    minor_rows = [0, 1, 2, 3, 4, 5, 7, 8]
    minor_cols = list(range(8))
    minor = integrability.extract(minor_rows, minor_cols).det()
    require_zero(minor - lam**2 * (lam**3 - 8)**2,
                 "integrability 8 by 8 minor")
    record("gradient_integrability_minor",
           matrix_shape=[9, 9], zero_based_minor_rows=minor_rows,
           zero_based_minor_columns=minor_cols,
           determinant="lambda^2*(lambda^3-8)^2",
           scalar_kernel_verified=True,
           rank_on_open=8,
           open_condition="lambda*(lambda^3-8) != 0")

    # 7. First derivative of the shift, and tangency to the classical cubic.
    shift_x = (x + h * y**2) / (1 + h**2 * x * y)
    shift_y = (y - h * x**2) / (1 + h**2 * x * y)
    velocity_x = sp.diff(shift_x, h).subs(h, 0)
    velocity_y = sp.diff(shift_y, h).subs(h, 0)
    require_zero(velocity_x - y**2, "shift x velocity")
    require_zero(velocity_y + x**2, "shift y velocity")
    plane_equation = x**3 + y**3 + 1
    require_zero(velocity_x * sp.diff(plane_equation, x)
                 + velocity_y * sp.diff(plane_equation, y),
                 "shift velocity tangency")
    record("shift_velocity_and_tangency",
           chart="z=1", velocity=["y^2", "-x^2"],
           tangent_to="x^3+y^3+1=0")

    # 8. Explicit 24-point witness; no cubic roots need to be approximated.
    witness = ((x**3 + y**3 + z**3) / 3
               - u**2 * (x + 4 * y + 16 * z) + u**3 + v**3)
    critical_equations = [sp.diff(witness, t) for t in (x, y, z)]
    expected_critical = [x**2 - u**2, y**2 - 4 * u**2, z**2 - 16 * u**2]
    for i, difference in enumerate(
            a - b for a, b in zip(critical_equations, expected_critical)):
        require_zero(difference, "Lefschetz critical equation " + str(i))
    sign_sums = []
    cubic_rhs = []
    for eps1, eps2, eps3 in itertools.product((-1, 1), repeat=3):
        sign_sum = eps1 + 8 * eps2 + 64 * eps3
        value = sp.Rational(2, 3) * sign_sum - 1
        substitution = {x: eps1, y: 2 * eps2, z: 4 * eps3, u: 1}
        for equation in critical_equations:
            require_zero(equation.subs(substitution), "Lefschetz critical branch")
        require_zero(witness.subs(substitution) - (v**3 - value),
                     "Lefschetz branch cubic value")
        require(value != 0, "nonzero Lefschetz cubic value")
        require(sp.diff(witness, u).subs(substitution) != 0,
                "Lefschetz witness smoothness obstruction")
        sign_sums.append(sign_sum)
        cubic_rhs.append(value)
    require(len(set(sign_sums)) == 8, "eight distinct sign sums")
    require(len(set(cubic_rhs)) == 8, "eight distinct nonzero cubic values")
    require(sorted(sign_sums) == [-73, -71, -57, -55, 55, 57, 71, 73],
            "explicit sign sums")
    chart_equations = sp.Matrix(critical_equations + [witness]).subs(u, 1)
    jacobian_det = chart_equations.jacobian((x, y, z, v)).det()
    require_zero(jacobian_det - 24 * x * y * z * v**2,
                 "Lefschetz point Jacobian determinant")
    record("lefschetz_twenty_four_point_witness",
           sign_sums=sorted(sign_sums),
           distinct_nonzero_cubic_rhs=[str(value) for value in sorted(cubic_rhs)],
           number_of_branches=8, number_of_points=24,
           jacobian_determinant="24*x*y*z*v^2")

    # 9. The usual j invariant from primary-source Weierstrass coefficients.
    # Artebani--Dolgachev: (t0,t1)=(s0,6*s1), here s0=1 and s1=h^2/6.
    s1 = h**2 / 6
    weierstrass_a = 12 * s1 * (1 - s1**3)
    weierstrass_b = 2 * (1 - 20 * s1**3 - 8 * s1**6)
    j_from_weierstrass = (
        1728 * 4 * weierstrass_a**3
        / (4 * weierstrass_a**3 + 27 * weierstrass_b**2)
    )
    j_expected = h**6 * (216 - h**6)**3 / (27 + h**6)**3
    require(sp.cancel(j_from_weierstrass - j_expected) == 0,
            "Fermat Hesse j invariant")
    record("fermat_hesse_j_invariant",
           j="h^6*(216-h^6)^3/(27+h^6)^3",
           reference="Artebani--Dolgachev, arXiv:math/0611590, Section 2, equations (6)-(8)")

    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("point_poisson_certificate.json"),
                        help="destination for the small JSON certificate")
    args = parser.parse_args()
    checks = run_checks()
    source = Path(__file__).resolve()
    certificate = {
        "certificate_format_version": 1,
        "arithmetic": "exact polynomial and rational arithmetic over Q",
        "source_file": source.name,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "sympy_version": sp.__version__,
        "check_count": len(checks),
        "all_checks_passed": all(check["passed"] for check in checks),
        "checks": checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps({"all_checks_passed": certificate["all_checks_passed"],
                      "check_count": len(checks), "certificate": str(args.output)},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
