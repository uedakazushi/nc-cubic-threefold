#!/usr/bin/env python3
"""Exact dominance certificate for the classical cubic in the 17-parameter family.

The 35 by 42 matrix consists of 25 infinitesimal GL5 directions and
17 coefficient directions. A nonzero 35-minor modulo a prime proves
surjectivity over Q. Smoothness of the generic cubic is proved separately
by the explicit polynomial in the manuscript; it is not inferred from rank.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("build/commutative_dominance.json"))
    args = parser.parse_args()
    helper_path = HERE / "verify_rat113_tangent.py"
    spec = importlib.util.spec_from_file_location("rat113_polynomials", helper_path)
    poly = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(poly)
    variables = [{e: 1} for e in poly.MON1]
    x, y, z, u, v = variables

    def power(f, n):
        out = {poly.ZERO: 1}
        for _ in range(n):
            out = poly.mul(out, f)
        return out

    derivatives = [
        poly.add(power(x, 3), power(y, 3), power(z, 3)),
        poly.mul(poly.mul(x, y), z),
        poly.mul(v, power(y, 2)),
        poly.mul(poly.add(u, v), power(z, 2)),
    ]
    binary_quadrics = [power(u, 2), poly.mul(u, v), power(v, 2)]
    derivatives += [poly.mul(active, quadratic)
                    for active in (x, y, z) for quadratic in binary_quadrics]
    derivatives += [poly.mul(power(u, 3-j), power(v, j)) for j in range(4)]
    parameters = [3, 5, 2, 3, 1, 1, 2, 2, 3, 1, 1, 4, 5, 1, 2, 3, 4]
    assert len(derivatives) == len(parameters) == 17
    f = poly.add(poly.mul(u, power(x, 2)),
                 *(poly.scale(d, c) for d, c in zip(derivatives, parameters)))
    orbit = [poly.mul(variables[a], poly.der(f, b))
             for a in range(5) for b in range(5)]
    columns = orbit + derivatives
    matrix = [[column.get(e, 0) for column in columns] for e in poly.MON3]
    assert (len(matrix), len(matrix[0])) == (35, 42)
    witness = poly.minor_witness(matrix, 1000003)
    assert witness["size"] == 35
    assert witness["determinant_mod_prime"] == 752849
    # Euler's homogeneous identity is checked over Z, not modulo the prime.
    assert poly.add(*(orbit[6*i] for i in range(5))) == poly.scale(f, 3)

    certificate = {
        "date": "2026-11-19", "version": 1,
        "parameters": {"a": 3, "b": 5, "alpha": 2, "beta": 3,
                       "m": [[1, 1, 2], [2, 3, 1], [1, 4, 5]],
                       "g": [1, 2, 3, 4]},
        "matrix_shape": [35, 42],
        "row_monomials": [list(e) for e in poly.MON3],
        "columns": "x_a*dF/dx_b, a,b=0..4 row-major; a,b,alpha,beta; m10,m11,m12,m20,m21,m22,m30,m31,m32; g0,g1,g2,g3",
        "minor": witness,
        "rank_over_Q": 35,
        "euler_identity_over_Z": True,
        "consequence": "GL5 times the 17-parameter family dominates the affine space of all cubic forms. On the nonempty smooth locus its map to classical cubic moduli is dominant.",
        "scope": "Finite exact rank certificate only; categorical recognition, Serre-stable generation, spreading and descent are separate proofs.",
        "helper_sha256": hashlib.sha256(helper_path.read_bytes()).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"status": "pass", "rank_over_Q": 35,
                      "minor_mod_1000003": 752849,
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
