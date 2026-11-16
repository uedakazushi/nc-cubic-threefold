#!/usr/bin/env python3
"""Exact QQ check: four-node directed Beilinson syzygy for commutative P3.
Requires Python3 with sympy. This checks a single model, not global AS-regularity.
"""
import itertools
import sympy as s

R=[]
for i,j in itertools.combinations(range(4),2):
    v=s.zeros(16,1)
    v[4*i+j]=1
    v[4*j+i]=-1
    R.append(v)
A=s.zeros(64,24)
B=s.zeros(64,24)
for r,v in enumerate(R):
    for c in range(4):
        for ab in range(16):
            A[4*ab+c,4*r+c]=v[ab]
    for a in range(4):
        for bc in range(16):
            B[16*a+bc,4*r+a]=v[bc]
X=A.row_join(-B)
kernel=X.nullspace()
K=s.Matrix.hstack(*[A*v[:24,:] for v in kernel])
C0=s.Matrix.hstack(*[
    s.Matrix([K[16*a+4*b+c,d] for a in range(4) for b in range(4)])
    for d in range(4) for c in range(4)])
C1=s.Matrix.hstack(*[
    s.Matrix([K[16*a+4*b+c,d] for b in range(4) for c in range(4)])
    for d in range(4) for a in range(4)])
C2=s.Matrix.hstack(*[
    s.Matrix([K[16*a+4*b+c,d] for c in range(4) for d in range(4)])
    for a in range(4) for b in range(4)])
C3=s.Matrix.hstack(*[
    s.Matrix([K[16*a+4*b+c,d] for d in range(4) for a in range(4)])
    for b in range(4) for c in range(4)])
ranks=[M.rank() for M in (C0,C1,C2,C3)]
assert X.rank()==44 and K.rank()==4 and ranks==[6]*4
print("PASS: dim K=4, four quadratic relation ranks="+str(ranks))
