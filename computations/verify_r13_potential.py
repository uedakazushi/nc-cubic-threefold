#!/usr/bin/env python3
"""Exact quartic potential and determinantal tangent certificate for R(1,3).
All ranks are computed over QQ. Finite tangent tests do not prove the intrinsic
surface recognition or the global AOU/W(E6) identification.
"""
from __future__ import annotations
import itertools as it
import json, argparse
from collections import defaultdict
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

V=range(4); X=s.symbols('t x y z'); t,x,y,z=X
words=list(it.product(V,repeat=4)); idx={w:i for i,w in enumerate(words)}
pairs=list(it.product(V,repeat=2)); ip={w:i for i,w in enumerate(pairs)}
cub_mons=[t**a*x**b*y**c*z**(3-a-b-c) for a in range(4) for b in range(4-a) for c in range(4-a-b)]

def parity(w):return (-1)**sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
def add(A,B,scale=1):
    C=dict(A)
    for w,v in B.items():C[w]=C.get(w,0)+scale*v
    return {w:s.cancel(v) for w,v in C.items() if v!=0}
def cyc(A):
    C=defaultdict(lambda:s.S.Zero)
    for w,v in A.items():
        for k in range(4):C[w[k:]+w[:k]]+=(-1)**k*v
    return {w:s.expand(v) for w,v in C.items() if v!=0}
def symmon(m):
    p=s.Poly(m,*X);D={}
    for powers,c in p.terms():
        w=sum(([i]*e for i,e in enumerate(powers)),[])
        ps=set(it.permutations(w))
        for u in ps:D[u]=c/s.Integer(len(ps))
    return D
ALT={tuple(w):s.Integer(parity(w)) for w in it.permutations(V)}
def pot(F):return add(ALT,cyc({(0,)+w:v for w,v in symmon(F).items()}),-3)
def flatten(W,shift=0):
    M=s.zeros(16)
    for w,c in W.items():
        q=w[shift:]+w[:shift]; M[ip[q[:2]],ip[q[2:]]]=c
    return M

def rank(M):return len(DomainMatrix.from_Matrix(M).convert_to(s.QQ).rref()[1])
def cert(M):
    D=DomainMatrix.from_Matrix(M).convert_to(s.QQ)
    cols=list(D.rref()[1]); rows=list(D.extract(list(range(M.rows)),cols).transpose().rref()[1])
    d=D.extract(rows,cols).det()
    return {'shape':list(M.shape),'rank':len(cols),'rows_zero_based':rows,'columns_zero_based':cols,'minor':str(d)}

def graph(F):
    R=[]
    for a in (1,2,3):
        d={(0,a):s.S.One,(a,0):-s.S.One};R.append(d)
    for a,b,c in ((1,2,3),(2,3,1),(3,1,2)):
        d={(a,b):s.S.One,(b,a):-s.S.One}
        for w,v in symmon(s.diff(F,X[c])).items():d[w]=d.get(w,0)-v
        R.append(d)
    return s.Matrix([[d.get(w,0) for w in pairs] for d in R])

def tangent_rank_conditions(W):
    rows=[]
    for shift in (0,1):
        M=flatten(W,shift)
        assert rank(M)==6
        L=M.T.nullspace();R=M.nullspace()
        assert len(L)==len(R)==10
        for l in L:
            for r in R:
                coeff=[s.S.Zero]*256
                for i in range(16):
                    if not l[i]:continue
                    for j in range(16):
                        if not r[j]:continue
                        q=pairs[i]+pairs[j]
                        w=q[-shift:]+q[:-shift] if shift else q
                        coeff[idx[w]]=l[i]*r[j]
                rows.append(coeff)
    return s.Matrix(rows)

def orbit(W):
    cols=[]
    for slot,a,b in it.product(range(4),V,V):
        col=[s.S.Zero]*256
        for w,c in W.items():
            if w[slot]==b:
                u=list(w);u[slot]=a;col[idx[tuple(u)]]+=c
        cols.append(col)
    return s.Matrix.hstack(*(s.Matrix(c) for c in cols))

def verify_universal_presentation():
    # Symbolic remainder test for all 19 coefficients, not random sampling.
    mon=[m for m in cub_mons if m!=t**3]; q=s.symbols('q:'+str(len(mon)))
    F=sum(c*m for c,m in zip(q,mon));W=pot(F)
    # Projection to Sym^2(V) along the 6 graph relations.
    P=s.zeros(4)
    for a,b,c in ((1,2,3),(2,3,1),(3,1,2)):
        P[a,b]=s.diff(F,X[c]);P[b,a]=-P[a,b]
    for prefix in pairs:
        remainder=0
        for suffix in pairs:
            remainder+=W.get(prefix+suffix,0)*(X[suffix[0]]*X[suffix[1]]+P[suffix[0],suffix[1]]/2)
        assert s.expand(remainder)==0,(prefix,s.expand(remainder))
    # Antisymmetrised active two-derivatives give 2*[t,x], and tx
    # derivatives recover the three graph relations after subtracting [t,x].
    R=graph(F)
    for a,b,c in ((1,2,3),(2,3,1),(3,1,2)):
        der=s.Matrix([[s.expand(W.get((a,b)+u,0)-W.get((b,a)+u,0)) for u in pairs]])
        assert der==2*R[c-1,:],(a,b,c,der)
    # t^3 is in the kernel of the potential correction.
    assert pot(t**3)==ALT
    return True

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--output',type=Path,default=Path(__file__).with_name('r13_potential_certificate.json'));pa.add_argument('--quick',action='store_true');args=pa.parse_args()
    verify_universal_presentation(); print('PASS universal 19-coefficient two-derivative containment',flush=True)
    F=3*(x**3+y**3+z**3)+5*x*y*z+t*(x*x+2*y*y+3*z*z)+t*t*(x+2*y+4*z)
    W=pot(F);G=graph(F);D=flatten(W)
    assert rank(D)==rank(G)==rank(D.col_join(G))==6
    assert all(W.get(w,0)==-W.get(w[1:]+w[:1],0) for w in words)
    print('PASS witness cyclicity and relation span',flush=True)
    T=tangent_rank_conditions(W)
    O=orbit(W)
    fam=[]
    for m in cub_mons:
        if m==t**3:continue
        corr=add(pot(m),ALT,-1)
        fam.append(s.Matrix([corr.get(w,0) for w in words]))
    S=O.row_join(s.Matrix.hstack(*fam))
    seven_mons=[x**3+y**3+z**3,x*y*z,t*y*y,t*z*z,t*t*x,t*t*y,t*t*z]
    seven=[s.Matrix([add(pot(m),ALT,-1).get(w,0) for w in words]) for m in seven_mons]
    S7=O.row_join(s.Matrix.hstack(*seven))
    assert rank(S7)==68
    assert T*S7==s.zeros(200,71)
    print('PASS seven-parameter slice plus orbit has rank68',flush=True)
    assert T*S==s.zeros(200,83)
    print('PASS exact tangent containment',flush=True)
    rt,ro,rs=rank(T),rank(O),rank(S)
    print('ranks',rt,ro,rs,flush=True)
    result={'date':'2026-11-15','version':'surface-v2','field':'QQ','variables':[str(v) for v in X], 'F':str(F),'potential':'Alt(txyz)-3*(1-c+c^2-c^3)(t*sym(F))','universal_containment_19_coefficients':True,'witness_flattening_ranks':[rank(flatten(W,i)) for i in range(4)],'tangent_containment':'exact T*S=0','rank_T':rt,'rank_orbit_GL4_four_factors':ro,'rank_family_with_orbit':rs,'rank_seven_slice_with_orbit':rank(S7),'projective_tangent_dimension':255-rt,'projective_orbit_dimension':ro-1,'family_projective_dimension':rs-1,'not_proved':['global intrinsic cubic recognition','AOU/Weyl global equivalence','global finite-type AS locus','generic smooth proper tails']}
    if not args.quick:
        for label,M in [('rank_condition_differential',T),('orbit',O),('family_with_orbit',S),('seven_slice_with_orbit',S7)]:
            result[label]=cert(M);print('certificate',label,result[label]['rank'],flush=True)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('written',args.output)
if __name__=='__main__':main()
