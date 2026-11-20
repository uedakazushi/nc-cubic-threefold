#!/usr/bin/env python3
"""Validate two independent point-scheme papers; optionally run finite checks/builds.

Checks TeX source graph, labels, references and bibliography; not proofs.
Run at repository root or elsewhere. Requires Python >=3.10.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import argparse
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PAPERS = (
    "papers/mixed-cubic-point-schemes.tex",
    "papers/diagonal-cubic-point-geometry.tex",
)
CALCULATIONS = (
    "verify_mixed_test_family.py",
    "verify_point_scheme_thickening.py",
    "verify_lambda_point_scheme.py",
    "verify_lambda_discriminant.py",
)
def check_paper(root: str) -> set[Path]:
    seen: set[Path] = set()
    parts: list[str] = []
    def visit(relative: str) -> None:
        p = (ROOT / relative).resolve()
        if not p.is_relative_to(ROOT) or not p.is_file():
            raise AssertionError(f"{root}: missing or external TeX input {relative}")
        if p in seen:
            raise AssertionError(f"{root}: repeated/circular TeX input {relative}")
        seen.add(p)
        text = re.sub(r"(?<!\\)%[^\n]*", "", p.read_text(encoding="utf-8"))
        parts.append(text)
        for x in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            visit(x if x.endswith(".tex") else x + ".tex")
    visit(root)
    text = "\n".join(parts)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    refs = re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", text)
    citations = [v.strip() for x in
        re.findall(r"\\cite(?:\[[^]]*\])*\{([^}]+)\}", text)
        for v in x.split(",")]
    bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text)
    dup = [k for k,n in Counter(labels).items() if n>1]
    duplicate_bib = [k for k,n in Counter(bib).items() if n>1]
    assert not dup, f"{root}: duplicated labels {dup}"
    assert not duplicate_bib, f"{root}: duplicated bibliography keys {duplicate_bib}"
    assert set(refs).issubset(labels), f"{root}: missing labels {set(refs)-set(labels)}"
    assert set(citations).issubset(bib), f"{root}: missing citations {set(citations)-set(bib)}"
    assert "\\author{}" in (ROOT / root).read_text(encoding="utf-8"), f"{root}: author must be blank"
    print(f"PASS {root}: {len(seen)} TeX files, {len(labels)} labels, {len(refs)} refs, {len(bib)} bib keys")
    return seen

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calculations", action="store_true")
    parser.add_argument("--build", action="store_true")
    a = parser.parse_args()
    seen = set()
    for entry in PAPERS:
        graph = check_paper(entry)
        assert not graph.intersection(seen), f"Point-scheme papers share source files: {graph & seen}"
        seen.update(graph)
    existing = {p.resolve() for p in (ROOT/"papers"/"point").rglob("*.tex")}
    assert existing.issubset(seen), f"Unused point source: {existing-seen}"
    if a.calculations:
        with tempfile.TemporaryDirectory(prefix="cubic-threefold-point-") as temp:
            for name in CALCULATIONS:
                target = Path(temp) / (Path(name).stem + ".json")
                subprocess.run([sys.executable, str(ROOT/"computations"/"point"/name),
                                "--output", str(target)], check=True, cwd=ROOT)
            subprocess.run([sys.executable, str(ROOT/"computations"/"point"/"verify_diagonal_point_geometry.py")], check=True, cwd=ROOT)
    if a.build:
        for entry in PAPERS:
            subprocess.run(["latexmk", "-g", "-r", ".latexmkrc", entry], check=True, cwd=ROOT)
    print("LIMIT: source/finite calculation checks only; not a mathematical proof audit.")

if __name__ == "__main__":
    main()
