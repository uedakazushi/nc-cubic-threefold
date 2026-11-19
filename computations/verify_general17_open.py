#!/usr/bin/env python3
"""Exact small certificate for the explicit general-17-family open.

Requires Python 3 and SymPy. No input files, network, or numerical approximations.
Checks only displayed polynomial identities and a nonvanishing witness;
it does not certify categorical statements or AS/CY theorems.
"""
import json

import sympy as s


def main():
    p, q, r, X, Y, Z, a, b = s.symbols("p q r X Y Z a b")

    def matrix(x, y, z):
        return s.Matrix([[r*x, q*z, p*y], [p*z, r*y, q*x], [q*y, p*x, r*z]])

    def cubic(x, y, z):
        return p*q*r*(x**3+y**3+z**3)-(p**3+q**3+r**3)*x*y*z

    O = s.Matrix([1, -1, 0])
    P = s.Matrix([p, q, r])
    Q = s.Matrix([q*(r**3-p**3), p*(q**3-r**3), r*(p**3-q**3)])
    D_E = (p**3+q**3+r**3)**3-27*p**3*q**3*r**3
    L6 = p**6+q**6+r**6-p**3*q**3-q**3*r**3-r**3*p**3
    checks = {
        "determinant": s.expand(matrix(X, Y, Z).det()+cubic(X, Y, Z)) == 0,
        "sigma_O": all(s.expand(t) == 0 for t in matrix(*O)*P),
        "sigma_squared_O": all(s.expand(t) == 0 for t in matrix(*P)*Q),
        "second_iterate_on_curve": s.expand(cubic(*Q)) == 0,
        "third_iterate_minor": s.expand(
            matrix(*Q)[0, :].cross(matrix(*Q)[1, :])[2]+p*q*r**2*L6
        ) == 0,
    }
    witness = {a: s.Rational(1, 6), b: 0, p: 2, q: -2, r: -1}
    factors = {
        "smooth_top": a*(27*a**3+b**3),
        "pqr": p*q*r,
        "smooth_point_curve": D_E,
        "p3_minus_q3": p**3-q**3,
        "q3_minus_r3": q**3-r**3,
        "r3_minus_p3": r**3-p**3,
        "third_iterate_factor": L6,
    }
    values = {name: s.factor(value.subs(witness)) for name, value in factors.items()}
    checks["nonempty_open"] = all(value != 0 for value in values.values())
    t = -r/p
    q_R = -q/p
    checks["rains_cubic_denominator"] = s.factor(q_R**3-t**3-(r**3-q**3)/p**3) == 0
    checks["rains_last_denominator"] = s.factor(1+t**3-(p**3-r**3)/p**3) == 0
    checks["rains_sum_denominator"] = s.factor((q_R+1).subs({p: 2-b, q: -(2+b)})-4/(2-b)) == 0
    assert all(checks.values()), checks
    print(json.dumps({
        "status": "pass",
        "checks": checks,
        "witness": {"a": "1/6", "b": "0", "p": "2", "q": "-2", "r": "-1"},
        "factor_values": {name: str(value) for name, value in values.items()},
        "scope": "exact polynomial identities and nonempty-open witness only",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
