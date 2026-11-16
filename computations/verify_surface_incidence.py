#!/usr/bin/env python3
"""Exact rational witness for cubic surface / P3 incidence. Python 3 + SymPy.
Does not prove global comparison with the AOU compactification or smooth tails.
"""
import itertools as it
import json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

x,y,z,t=s.symbols('x y z t'); X=(x,y,z,t)
F=3*(x**3+y**3+z**3)+5*x*y*z+t*(x*x+2*y*y+3*z*z)+t*t*(x+2*y+4*z)+7*t**3
pairs=list(it.combinations(range(4),2))
mons=[X[i]*X[j] for i in range(4) for j in range(i,4)]
def parity(a): return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def jac(f,h):
    P=s.zeros(4)
    for i,j in pairs:
        k,l=[r for r in range(4) if r not in (i,j)]
        P[i,j]=s.expand(parity((i,j,k,l))*(s.diff(f,X[k])*s.diff(h,X[l])-s.diff(f,X[l])*s.diff(h,X[k])))
        P[j,i]=-P[i,j]
    return P
P=jac(F,t)
def vec(P):
    return s.Matrix([s.Poly(P[i,j],*X).coeff_monomial(m) for i,j in pairs for m in mons])
def rank(M): return len(DomainMatrix.from_Matrix(M).to_field().rref()[1])
def certificate(M):
    D=DomainMatrix.from_Matrix(M).to_field(); cols=list(D.rref()[1]);
    rows=list(D.extract(list(range(M.rows)),cols).transpose().rref()[1])
    Q=M.extract(rows,cols)
    det=DomainMatrix.from_Matrix(Q).to_field().det()
    return {'shape':list(M.shape),'rank':len(cols),'rows_zero_based':rows,'columns_zero_based':cols,'determinant':str(det)}
def jacobi(P):
    return [s.expand(sum(P[i,a]*s.diff(P[j,k],X[a])+P[j,a]*s.diff(P[k,i],X[a])+P[k,a]*s.diff(P[i,j],X[a]) for a in range(4))) for i,j,k in it.combinations(range(4),3)]
assert all(v==0 for v in jacobi(P))
assert all(s.expand(sum(s.diff(P[i,j],X[i]) for i in range(4)))==0 for j in range(4))
assert P*s.Matrix([s.diff(F,q) for q in X])==s.zeros(4,1) or all(s.expand(v)==0 for v in P*s.Matrix([s.diff(F,q) for q in X]))
G=s.groebner([s.diff(F,q) for q in X],*X)
assert G.is_zero_dimensional
cub=[x**i*y**j*z**k*t**(3-i-j-k) for i in range(4) for j in range(4-i) for k in range(4-i-j)]
M=s.Matrix.hstack(*[vec(jac(f,t)) for f in cub],*[vec(jac(F,h)) for h in X]); assert rank(M)==22
orb=[]
for a,b in it.product(range(4),repeat=2):
    O=s.zeros(4)
    for i,j in pairs:
        O[i,j]=X[b]*s.diff(P[i,j],X[a])-(P[b,j] if i==a else 0)-(P[i,b] if j==a else 0)
    orb.append(vec(O))
O=s.Matrix.hstack(*orb); assert rank(O)==15
# Full linearized Jacobi + divergence conditions at P, not merely restricted family.
eps=s.symbols('eps'); cols=[]
cubmons=cub
for i,j in pairs:
    for m in mons:
        Q=s.zeros(4);Q[i,j]=m;Q[j,i]=-m
        linear=[s.expand(v).coeff(eps,1) for v in jacobi(P+eps*Q)]
        row=[s.Poly(v,*X).coeff_monomial(n) for v in linear for n in cubmons]
        div=[s.expand(sum(s.diff(Q[a,b],X[a]) for a in range(4))) for b in range(4)]
        row += [s.Poly(v,*X).coeff_monomial(n) for v in div for n in X]
        cols.append(row)
J=s.Matrix.hstack(*(s.Matrix(c) for c in cols)); assert rank(J)==38
assert J*M==s.zeros(96,24)
# Independent left/right action on quadratic graph relations.
products=[X[i]*X[j]+P[i,j]/2 for i,j in it.product(range(4),repeat=2)]
def relation(i,j):
    R=s.zeros(4);R[i,j]=1;R[j,i]=-1
    pol=s.Poly(P[i,j],*X)
    for a in range(4):
        for b in range(a,4):
            c=pol.coeff_monomial(X[a]*X[b])
            R[a,b]-=c if a==b else c/2
            if a!=b:R[b,a]-=c/2
    return R
rels=[relation(i,j) for i,j in pairs]
bi=[]
for side,a,b in it.product(range(2),range(4),range(4)):
    E=s.zeros(4);E[a,b]=1;col=[]
    for R in rels:
        S=E*R if side==0 else R*E.T
        pol=s.Poly(s.expand(sum(S[i,j]*products[4*i+j] for i,j in it.product(range(4),repeat=2))),*X)
        col.extend(pol.coeff_monomial(m) for m in mons)
    bi.append(col)
H=s.Matrix.hstack(*(s.Matrix(c) for c in bi)); assert rank(H)==30
out={'date':'2026-11-14','version':'surface-v1','field':'QQ','F':str(F),'variables':[str(q) for q in X],
     'smooth_cubic_witness':'homogeneous gradient ideal is zero-dimensional',
     'poisson_jacobi_divergence_casimirs':'exact zero',
     'jacobian_incidence_differential':certificate(M),
     'projective_orbit_differential':certificate(O),
     'full_unimodular_poisson_linearization':certificate(J),
     'two_factor_graph_stabilizer':certificate(H),
     'linearization_times_family_derivative':'exact zero',
     'scope':'Nonzero rational minors prove generic ranks; no global AOU/ambient stack equivalence, no smooth-tails assertion.'}
p=Path(__file__).resolve().parent/'surface_incidence_certificate.json';p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
for k in ('jacobian_incidence_differential','projective_orbit_differential','full_unimodular_poisson_linearization','two_factor_graph_stabilizer'):
    print(k,out[k]['shape'],out[k]['rank'],out[k]['determinant'])
print('PASS smooth witness, Jacobi, divergence, Casimirs and exact tangent containment')
