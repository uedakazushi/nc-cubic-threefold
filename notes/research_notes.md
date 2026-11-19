# 研究ノート：非可換三次三様体と非可換P^4

2026-11-19 / research-plan-v5。現在有効な研究知識。詳細証明は主論文とその `papers/sections` に保持する。H3曲面の分類メモは移管対象外。

## 1. 何をモジュライのデータに含めるか

### 1.1 豊富列を保持する座標模型

二つの座標代数stackは、各成分が局所自由な正の連結Z-algebraのfpqc stackの部分問題として定義する。ambient Bはb_m=binom(m+4,4)、cubic Aはh_m=b_m-b_(m-3)。Aの長さ一のHomと長さ二の積の核からQ(A)を得る。原稿`intrinsic_cubic_reconstruction.tex`の相対復元と、`algebraic_moduli_foundations.tex`の定義・比較定理を使う。

有限窓J_N=[-N,N]では、全Homの乗法の有限個の係数に結合律を課したaffine schemeを、各HomのGLの積で割る。全stackはこれらの2逆極限。AS正則性・noetherian性・無限個のHilbert rank条件の有限決定性は別に必要であり、逆極限表示を有限型代数性と呼ばない。

全対象同定付き圏の1射は(F,alpha_i:F(E_i)≅E'_i)、2射はbeta_i eta_i=alpha_i。Hom群oidは離散化され、厳密Z同型と一致する。同定を忘れると頂点スカラーrho_lambda(a_ij)=lambda_i lambda_j^(-1)a_ijが現れる。weak圏の自己同値の2同型類はAut_Z(A)/rho(T)、恒等自己同値の2自己同型は対角Gm。E_0の同定を残すとT0={lambda_0=1}で正規化でき、2慣性が消える。

相対弱い射は線束族L_iとphi:A→(A')^L、(A')^L_ij=L_i A'_ij L_j^(-1)で記述する。この規約ではF(E_i)≅E'_i⊗L_i。共通線束Lは代数式では相殺するが、圏ではtensor-by-Lとなる。自己同型商はfpqc商層であり、大域点集合の単純な商と同じとは限らない。weak 2-stack化では大域的な代数で表示できないtwisted formsも含み得る。証明は`categorical_moduli_comparison.tex`。

Q(A^L)=Q(A)^Lなので三次→ambientの射は全levelに降りる。ただし相対category比較にはHomの任意の基底変換、低次数saturation、相対section復元を仮定する。裸のAbel圏・導来圏・Kuznetsov成分のみからの復元は含まない。


### 1.2 構造対象だけを標識した問題

現在の主対象は `(C,O)`。許容な三次豊富列 `(E_i)`、E_0≅O の存在を条件とし、選択自体を記憶しない。1射はOを保つ全ての完全線型同値、2射はOの同定を保つ自然同型である。`M^pt` は列保存の条件を残していたので、今回の `M^O_cub` と区別する。全相対模型には底変更と降下を明示的に含める。アフィン上の標準Grothendieck模型の底変更は係数作用付き対象を用いる。任意の係数環上では大きいQGrを使い、小さいqgrはAbel性が保証される場合に限る。有限型atlasは未構成。定義と証明は `abel_marked_moduli.tex`。

**中心条件の位置。** 中心の階数2束EとP=Sym(E)に対するP-flatness、任意底変更後のZ(A)_2=Sym²(E)を満たす部分族で、R=A^(2)、D=P^(2)を使う。Z(A)_1=E、Z(R)_1=P_2は内在的で、P-flatnessから普遍的な交差 A=A[u^−1]∩A[v^−1] を得る。相対Isom層は

\[
\operatorname{Isom}_{gr}(A,A')
=\operatorname{Isom}_{gr}(R,R')\times_{\operatorname{Isom}_{gr}(D,D')}
\operatorname{Isom}_{gr}(P,P')
\]

である。従って偶数制限はμ2-torsor、次数スカラーの層商ではIsomが一致する。P-flatかつA非負次数、A0=OならP→Aは任意底変更後に単射となる。証明は同節 `lem:abel-universal-polynomial-embedding`。二次中心条件はA2/Sym²(E)→Hom(A1,A3)の最大rank開部分で普遍的に確認できるが、この命題からP-flatnessやsmooth proper性の開性は従わない。

可換三次点ではZ(A)_2=A2は15次元であり、上の中心条件を満たさない。したがってこの条件は全nc cubicの定義や可換点を含む近傍の条件ではなく、非可換部分族の復元に用いる。

**圏の射。** S≅(−2)[3]、section saturation、偶数豊富列の下で、Oを保つAbel同値はH=S^−1[3]の軌道環Rを保つ。偶数復元により

\[
\pi_0\operatorname{Eq}_O(qgr A,qgr A')
=\operatorname{Isom}_{gr}(A,A')/\mathbb C^\times.
\]

Nat(Id)=Cは豊富列から直接従い、O上の同定を残すと2慣性は消える。μ2は次数スカラーGmの部分群であり、追加の2慣性ではない。相対版 `thm:abel-relative-pointed-hom` は有限型C-schemeのfppf siteで、C1–C4を仮定した条件付き定理である。基底非正則の場合、Db(coh)全体へ通常のSerre双対を仮定せず、内在的な有限Tor振幅部分圏を使う。17係数族全体での入力は未確認。有限位数境界の四係数族で得られる範囲は§1.4に記す。

**具体的帰結。** 既存の剛体B_*の4係数regular tails開部分では、既存入力の下でO-marked圏はパラメータfごとに相異なり、Aut_O(qgr A_f)=1。証明は `cor:abel-rigid-four-family`。これは開埋込み、étale chart、bare categoryの相異性を含まない。

### 1.3 降下に関する二つの障害

固定R同型をAへ持ち上げる障害はH¹(T,μ2)。K=C[t,t^−1]上のR=K[u,v]^(2)の次数スカラーtは、A側でλ²=tを要求するため大域持上げを持たない。局所的に許容な偶数環であるRからAを貼り合わせる障害はH²(T,μ2)。Rの中心が二次曲線型であるだけでは、許容Aの存在・平坦性・Hilbert関数を保証しない。

対象の障害の具体例として、T=P¹_C、L=O_T(1)、R_n=Sym^(2n)(O_T²)⊗L^n と置く。局所的には二変数多項式環の偶数部分である。R≅(Sym E)^(2)ならProj R=P¹×TよりP(E)は自明なのでE≅M⊗O_T²。相対O(2)の偏極を比較してM²≅Lを得るが、Pic(P¹)=Zにより不可能である。障害はKummer類δ(L)∈H²(T,μ2)。ここでP(E)自明からのMは、射影同型を局所的にGL2へ持ち上げた遷移関数がスカラーになることで得られる。この例は三次三様体の例ではなく、偶数復元の大域降下に必要な最小の模型である。

相対Serre式に基底線束Lが入りS≅(−2)⊗L[3]となる場合、軌道環は⊕A_(2n)⊗L^(−n)となる。大域的にA^(2)と等置せず、局所自明化と次数スカラー降下で比較する。

### 1.4 有限位数楕円境界の四係数族の相対圏

証明は `finite_order_relative_categories.tex`、中心持上げは `central_pair_finite_order_regularity.tex` の `CSBGlem:global-center-lifting` に集約する。

P=C[a,b,c,d]、A_P=B_*⊗P/(G_*+a u³+b u²v+c uv²+d v³) とする。既存のPBW・中心正則元・位数6のTHCR境界を入力とし、gr_(x,y,z) A_P=H⊗P[u,v] を使う。これによりA_PはP[u,v]上自由である。

**有限中心模型。** Rains Thm2.13の仮定は標数零・滑らかな楕円代数・有限位数translationである。P[u,v]上の有限交換子行列の各閉点の核次元が一定となり、被約性からkernel bundleと中心symbolの全射を得る。斉次中心の有限個の持上げで C⊂Z(A_P) を作り、A_PはC上有限となる。一般の「grが中心上有限なら変形も中心上有限」という主張ではない。Weyl型の変形へ無条件に拡張しない。

B_*では二次中心の普遍条件も全係数基底上で成立する。A_2/Sym²(Pu⊕Pv)のrank12の交換子写像は全閉点で単射であり、Jacobson性から最大rank開部分が全体となる。従って任意のP代数Sで Z(A_S)_2=S u²⊕S uv⊕S v²。証明は `cor:central-model-universal-center-two`。

任意のP→Sで必要なのは中心準同型 C⊗S→Z(A_S) と有限加群性である。C⊗S→A_Sの単射や、全中心の任意底変更可換性は主張しない。SがNoetherianならA_Sは左右Noetherianとなる。

**射影模型とC1–C2。** 十分割り切れる偶数ℓについてD=C^(ℓ)、Y=Proj D、𝒜=˜(A_P^(ℓ))を使う。c∈D_1を可逆化すると、Aの次数一生成から1∈T_1T_−1かつ1∈T_−1T_1となり、強い次数付けを得る。この点を省略すると、重み付き中心のProjを使う際に次数剰余類を失い得る。従ってQGr(A_S)≃QCoh(Y_S,𝒜_S)、qgr≃coh。ℓを偶数に取ると通常のSerre生成性・消滅が偶数列へ移る。

全twistのsection飽和は M_m=A_S(m)^(ℓ) 上の中心正則列 u^ℓ,v^ℓ による H^0_(D_+)(M_m)=H^1_(D_+)(M_m)=0 から従う。全Noetherian底変更で同じ証明が使え、負次数Homも零となる。偶数列上のHom作用から完全同値を決定する証明では、列を射影対象と仮定しない。二つの表示を直和の共通全射で比較し、coherent部分からfiltered colimitで全体へ延長する。

**局所perfectと相対RHom。** 局所代数Λ=(A_S[c^−1])_0はS上平坦である。局所perfectなK,LのHom複体は、S平坦なΛの有限直和の直和因子を項とする。有限中心の射影模型とStacks Lem36.27.1により大域RHomはS-perfectとなる。任意底変更は有限Čech複体で確認する。ここで導来底変更は代数係数の拡張であり、Y_S自体がS平坦とは限らないので通常のO_Y-導来逆像と無条件に同一視しない。

**非空開上の内在的perfect圏。** Geometric generic tailsの有限大域次元を仮定する。既存 `CSBGthm:global-open` のPBW・AS体拡大条件の下で、B_*族はこれを満たす。中心アフィン開j:U→Yについて

\[
\operatorname{Ext}^i_{\mathcal A(U)}(M|_U,N|_U)
=\varinjlim_n\operatorname{Ext}^i_{\mathcal A}(M,N(n))
\]

を有限twist解消とČechで証明する。これにより全中心chartの一般ファイバーが有限大域次元を持つ。RSVの有限中心代数のsmoothnessと射影性拡張を使い、有限個のchartの相対対角を同時にperfectにする非空基底開P_pを得る。u≠0、v≠0の二chartだけでは楕円境界を覆わないため、全中心標準開被覆を使う。

相対対角の有限射影解消をK⊗^L_Λ−で使うと、有限S-Tor振幅から有限Λ-flat dimensionが従う。coherent性・Noetherian性で最後のsyzygyを有限射影にする。この順序により

\[
\operatorname{Perf}(Y_S,\mathcal A_S)
=\{K\in D^b_{coh}(\mathcal A_S):\operatorname{Toramp}_S(K)<\infty\}
\]

を全Noetherian P_p代数Sで得る。K⊗_SΛが有限生成射影とは限らないので、その誤った置換はしない。開集合は存在を示したもので、pの明示式や最大の正則開集合は未計算である。

| 相対Hom定理の入力 | 四係数族での状態 |
|---|---|
| C1：相対QGr模型・対象／射の降下 | 全係数基底上、Noetherian底変更について証明 |
| C2：全twist飽和・偶数列・復元・関手決定 | 同上 |
| C3：内在的有限Tor部分圏・導来底変更 | 一般正則性入力の下で非空開上に供給 |
| C4：perfect RHomと底変更 | 同じ非空開上に供給 |
| C4：相対Serre双対、S≅(−2)[3] | 未証明。現在の最優先 |

大域dg smooth性、全17係数族への拡張、有限型atlasは別の問題である。局所対角のperfect性だけからこれらを結論しない。

## 2. ファイバー、中心条件、正規条件

指定したBへの同型まで含む厳密2-fiberは、B_i,i+3の直線部分束L_iについて、左右の全乗法が部分束を与え、L_i B_i+3,i+4=B_i,i+1 L_i+1となる集合層。有限窓ごとに有限積の射影束の局所閉schemeで表せる。固定したk-同型類ならaction groupoid、fpqc局所形式も含めるなら[Inc/Aut0(B)]となる。

接空間は添字を保つHom_(B-B)(I,B/I)。次数付きかつ中心Gの問題なら全normal接空間はZ(B/(G))_3、中心直線だけを動かす部分はZ(B)_3/kGであり、一般には同じとは限らない。

可換B=check Sym(V)では、非被約基底でもnormalityが全L_iの一致を強制し、fiberはP(Sym³V)=P34。局所生成元F,GについてFV=GVからFx_j=G l_jを得て、正則性と係数比較でl_j=lambda x_j、F=lambda Gを示す。頂点スカラーを除いたAut0はPGL5。pointed category levelでBPGL5上へ底変更すれば[P34/PGL5]となり、smooth部分は通常の10次元cubic moduli。

相対中心incidenceはP(B3)上の交換子写像delta:B3→Hom(B1,B4)の零点。核の形成は一般の非平坦底変更に可換とは限らない。schemeとして一定rankを課した層で初めて核束となり、射影束になる。一次持上げ障害は[dot delta(G)]∈coker(delta)。証明は`ambient_incidence_morphism.tex`。

量子多項式の10次元qトーラスでは中心三次を持つ条件は35個の重みごとのcodim4部分トーラスの有限和だが、normal単項式は全点にある。このcodimを全Zモジュライやsmooth cubic部分のcodimと解釈しない。

## 3. 周期構造と有限な追加同一視

`ambient_periodicity.tex`では、左右global dimensionとuniform AS Ext条件を明記する。正規次数d族をsigmaで畳み込むd頂点orbit Dの中心正則元zを作り、Reyes–RogalskiのTheorem5.15、Lemma5.9(1)、Lemma4.5を適用する。Nakayamaはzを固定するので、unfoldしたN周期rhoも三次イデアルを保つ。N=5,d=3ならtheta=rho^(-1)sigma²により対・商が1周期化する。残る正規自己同型tau=rho³ sigma^(-5)が恒等とは限らず、大域族への降下は別問題。

中心性はgraded表示に依存する。smooth F=x0²x1+x1³+x2³+x3³+x4³とphi(x0)=−x0, phi(xj)=xj(j>0)では、S^phiのFは非中心正規だが、Z-algebra対は可換中心対と同型。中心商だけを全intrinsic定義にしてはいけない。

`period_forgetting_moduli.tex`ではPer_1(B)の共役商でgraded表示を比較する。Sierra Cor4.4は任意のZhang twisting systemを含む。単一の自己同型の冪によるtwistに限定しない。厳密fiber Per_1(B)と同型類上の共役商を混同しない。

H_R={(g,h)∈PGL5²:(g⊗h)R=R}の両射影が単射なら、Rを保つ両無限列の自己同型は、閉部分群の降鎖を安定化して得る有限型群K_Rで決まる。周期の同一視はka alpha(k)^(-1)。無限小周期変動はcoker(1-d alpha)。有限なgraded自己同型群だけから結論する前に、この有限次元化が必要。

本族ではPBW基底と中心一次変数u,vから両射影の単射性を証明した。さらにF0で作った150×50整数行列M(X,Y)=vec(Q(X⊗1+1⊗Y)R)には二つのスカラー核があり、48次minor mod1000003=815096である。したがってrank_Q M=48、一般H_Rは有限。行列は`verify_two_factor_stabilizer.py`、小証明書は`two_factor_stabilizer_certificate.json`。有限群の位数・周期忘却の次数は未計算。

この一般開部分では、13次元ambient族と17次元三次対族におけるZ同型による追加同一視は有限個。これは同型類の一般変動次元を保つ結果であり、全stackの有限型性・成分性を単独で証明しない。

## 4. 全normal fiberの形式的中心化

特殊Bに有限H_R、中心正則一次元u、中心正則三次元Gがあるとする。任意のgraded Artin変形B_T上のindexed normal liftで生成元G_iを選ぶと、G_i x=phi_i(x)G_i+1となる。正則性から(phi_i⊗phi_i+1)R_T=R_T。特殊H_RのLieが0なのでArtin帰納でphi_iはスカラーとなり、G_iを再規格化してG_i x=xG_i+1とする。

次数3へ延長してb=G_iを代入すればG_i+3=G_i。平均H=(G_0+G_1+G_2)/3は中心であり、差D_iはD_i u_T=u_T D_i+1を満たす。最初の非零m進層で特殊uの中心性と正則性を使い、d_iが全て等しく和0なので消える。帰納で全G_i=H。従ってindexed normal liftは単一の中心直線であり、逆写像はL_0なので自然性もある。

固定Bかつdim Z(B)_3=5なら、全normal厳密fiberの形式完備化はSpf k[[t1,t2,t3,t4]]。証明は同節のprop:indexed-normal-central-rigidityとcor:indexed-normal-four-dimensional-fibre。一般のZ ambient変形がgradedから来ることは仮定していないので、この結果から相対周期化そのものを結論しない。

同節の相対Nakayama剛性は、有限射影自己同型群からmu=xi_c、Frobenius trace不変性からc^5=1、c≡1からmu=1を得る。全成分が有限局所自由な標準AS族では、Koszul双対のFrobenius構造は下記の相対bar補題から自動的に得られる。相対双加群複体によるNakayama構成と、その次数一部分の双対公式は明示的な入力として残す。

## 5. 可換点の形式モジュライ

### 5.1 三次点の全Abel変形とOの標識

smooth cubic Xについて H¹(O_X(m))=H²(O_X(m))=0 は全整数mで成立する。超曲面完全列による証明と、De Deken–Lowen Thm4.5の全仮定の照合を `abel_cubic_deformations.tex` に置く。これは既知比較の直接適用であり、geometric helixやfull exceptional collectionを仮定しない。

任意の局所Artin C-代数Rで、Def_lin(check A;R)≃Def_ab(Qcoh X;R)≃Def_ab(coh X;R)。対象E_i=O_X(−i)の平坦持上げは同型類として一意で、Homは有限自由、次数一生成と右noetherian性も成立する。任意の可換R代数Sについて、Gabriel商とその右随伴をS-object圏へ移し、Qmod(S⊗b)≃Qmod(b)_Sを証明した。Sの有限性は不要である。全係数変更後の飽和と標準係数族のfpqc降下は§5.5に整理する。

O-markingの忘却は、自然同型で割った古典的1群oidで同値になる。還元の両立自然同型自体をframeとして保持しないLVdBの規約を使う。未切断2群oidではNatAut(Id)=R^×があり、Oの同定を保つと消えるため同値ではない。固定圏で還元frameを付けたOの持上げ群oidは連結だがAut=1+m_R。形式的持上げの一意性はOの大域的内在認識とは異なる。

### 5.2 次数三の障害と直接的な平坦性判定

bをsection Z-algebra変形とし、V_i=b_(i,i+1)、T=T_R(V_•)、K=ker(T→b)、R_i=K_(i,i+2)、B=Q(b)=T/(R_i)と置く。

- V_iは自由rank5、R_iは自由rank10。KはR_iと各位置一つの三次関係f_iで生成される。成分ごとの分裂自由性と冪零Nakayamaによる。
- J=ker(B→b)の三次成分はcyclic Rg_i。I_i=Ann(g_i)とすると B_(i,i+3)≅R³⁴⊕R/I_i。I_i=Fitt_34(B3)は125×100関係行列d_iの91次minor idealで、特殊rank90のunit blockを除くと35×10残余行列になる。その列はprimitiveな三次関係直線に入り、高々10係数でI_iを生成する。
- **全てのI_i=0と全次数平坦性は同値。** 非周期的なZ代数でも、多項式特殊ファイバーに対して次数三の平坦性だけでよい。降順対を書き換え、係数のm進深さと語の転倒数を辞書式に順序付けると、冪零性により停止する。次数三で非降順語が基底になることが全ての重なりを解消し、全長の基底を与える。一般原理は既知のKoszul変形原理であり、PP Chapter6 Thm7.3を参照する。
- **平方零基底では滑らかさ不要。** R=k⊕M、M²=0で、二次関係を交代関係のgraph q_i と書く。Schur残余は厳密に Θ_i=δ(q_(i+1)−q_i)。b3の平坦性からΘ_i=Fλ_i。δ²=0、F≠0、δ:Λ³V*→V⊗Λ⁴V*の単射性（dim V≥4）によりλ_i=0。全次数平坦性が従う。
- 任意Artin基底でもI_i⊂m²。Fitting idealの底変更と前項から従う。これは特異三次にも使える。高次ではSchur補正とJacobiatorが入り、一次のδ閉性をそのまま帰納してはならない。
- 全次数平坦性から正規正則三次核、Betti型(1,5,10,10,5,1)の相対Koszul解消、両側AS index5、noetherian性、基底上平坦な加群の射影次元≤5を得る。

完全な証明は `abel_cubic_deformations.tex` の `prop:abel-degree-three-obstruction`, `thm:abel-degree-three-propagation`, `thm:abel-square-zero-degree-three`, `thm:abel-relative-as-lift`。全位置iの条件を、周期性を示さず有限個の位置へ置き換えない。

相対ASは絶対global dimensionではない。R=C[ε]/ε²、B=check R[x0,…,x4] は相対定理を満たすが、頂点の剰余体Cの射影次元は無限である。無限Z頂点の双加群解消も大域的な有限生成性を意味しない。

### 5.3 滑らかな三次点の全Abel変形の二次包絡

**任意の局所Artin C-代数上で、滑らかな可換三次点の全Abel変形のQ(b)は全次数平坦。** 証明は `thm:abel-cubic-flat-envelope`。通常の次数付き表示を事前に仮定せず、次の順序で示す。

1. 三次式の形式slice F_t と定数二形式 a（五つの4×4 Pfaffian=0）から、i_ΠΩ=dF_t∧a で同次Poisson bivectorを作る。
2. CFTの有限なKontsevich公式に nilpotent Artin係数を代入する。基礎加群R⊗Sym(V)は自由、グラフの次数計算で積は同次、twisted chain identityでCasimir F_t が中心三次元wへ持ち上がる。関係核のNakayamaからBは二次、wの乗法のunit minorからA=B/(w)も平坦。
3. 実際のOre局所化が Ψ:h_T→D_Ass を与える。T=C[[t_1,…,t_10,a_ij]]/(Pfaffian_4(a))。相対Poisson計算とYekutieli Cor11.2により標的も同じTでprorepresentされる。これは単なるhullではない。
4. Ψの接写像が零なら、一次交換子からa=0となる。その場合は実際の可換三次変形だからt=0。接空間はいずれも20次元なので同型。Tの連続自己準同型は各有限次元随伴次数上で同型となり、完備性から自己同型になる。
5. Lowenのalgebroid模型とH¹,H²(O)=0による中立化で、全Abel変形を通常の代数層変形へ移す。中心商の局所化次数部分E_nはO_X(n)の持上げなので、個々の持上げの一意性とsection回復から b≅check A、Q(b)≅check B を得る。

同次代数変形の全gauge分類は証明の前提ではない。CFTによる具体的な族の構成と、Yekutieliによる標的関手の同定を分ける。量子化座標の選択は非標準的でも、内在的なb→Q(b)は任意の係数変更に自然である。各O(i)の持上げを同定する段階で、shift自己同値の持上げを仮定しない。

CFTの規約ではα=Π/2を代入し、一次交換子をΠに規格化する。中心性の逆向きが必要な補助補題では、D⁰の三次部分と、四次係数ベクトル場のD¹を生成元で評価する写像が還元恒等の有限自由行列であることを使う。中心の非平坦底変更を仮定しない。

**範囲。** 全平坦Abel Artin変形は、任意の係数変更後にも飽和・復元・相対AS条件を満たす標準相対模型を持つ。標準模型のArtin群oidと全Abel変形群oidの比較は証明済み。全stack化後の形式完備化との同定には、圏自体の有効降下とArtin大域模型の存在が残る。固定圏の対象・射の降下とは区別する。

### 5.4 形式局所環、ambient写像、P4との区別

構造対象付きAbel変形の同型類関手はTで表され、Krull次元17、接空間20。特殊ファイバーの有限Aut(X)は割らない。中心対の射影生成基底を残すとformal PGL5の24次元torsorになり、次元41・接空間44。証明は `cor:abel-cubic-formal-ring` と `thm:artin-central-pair`。H⁰(T_X)=0により、cubic側には標識を保つ形式的PGL stabilizerが残らない。

実際のambient射の接写像は(dot F,a)↦Π(F,a)_projで、核10・像10。原点の核10と、非零一般点のambient忘却fiber4は別である。独立に選んだaffine／projective量子化の座標で、全高次のactual mapが単に(F_t,a)↦Π(F_t,a)となることは未確認であり、上の存在・比較の証明には用いない。

P4ではPoisson変形はJacobi零点錐の原点完備化をPGL5_1で割る。接空間126。ε³上の π=εP と exp(εξ)π は二次で異なる代表となるため、接空間が同じだけでは錐とgauge商を同定できない。

有限Beilinson窓とHom(O,O(1))の射影基底を使うと、対象スカラーを除いた形式sliceが得られる。Pymの規格化CY芽と、この同じ関手のminimal hullの一意性を先に用い、その後で実際のQmod写像の接写像を照合する。帰結は集合値の標識付き全Artin関手の比較であり、2-stackや大域モジュライの同値ではない。

### 5.5 任意係数変更と標準相対模型

完全な証明は `abel_cubic_deformations.tex` の `subsec:abel-universal-coefficients`, `subsec:abel-coefficient-descent`, `thm:abel-canonical-relative-formal` に置く。

R線型Grothendieck圏Dについて、D_SはD内のS作用付き対象の圏である。忘却が核・余核・filtered colimitを作り、自由係数拡張S⊗_R−を左随伴に持つ。大きい圏ではSがR加群として有限表示である必要はない。次数一有限生成のtails torsionがlocalizingであることを確認し、Gabriel商と完全忠実な右随伴へ作用を移すとQmod(S⊗b)≃Qmod(b)_Sとなる。

Homの普遍性は、R-flat対象Eとk対象Nに対する

\[
\operatorname{Ext}^1_D(E,N)
\simeq\operatorname{Ext}^1_{D_k}(k\otimes_RE,N)
\]

をYoneda拡大の還元と引戻しで示すことから出発する。持上げたE_i同士の特殊ファイバーExt¹は零。有限長R加群Mの組成列で帰納し、その後E_jの有限表示性を使ってfiltered colimitへ移ると、**任意のR加群M**について

\[
M\otimes_R b_{ij}
\simeq\operatorname{Hom}_D(E_j,M\otimes_RE_i)
\]

となる。Ext¹そのものがfiltered colimitと可換であると仮定する必要はない。S作用の随伴から任意の係数環上の飽和を得る。変更後のE_iはS-flatかつ有限表示な生成族である。

忠実平坦S→Tに対する降下では、Lazard表示からT⊗_S−の完全性を得る。S→Tの純単射とT/Sの平坦性から対象M→T⊗Mも単射であり、保守性が従う。降下余作用δを持つNの等化子ker(δ−1⊗−)が降下対象となる。標準係数族の間の相対同値はRでの同値を作用へ移したものに一意に同型となり、証明では自由係数拡張の随伴mateを用いる。

自然同型を保持したHom群oidは降下する。O-markingにより2自己同型が消える三次模型では、同型類を取った後も固定模型間に新しい射は加わらない。一般の非標識圏で同型類だけを先に取ると、局所functor類の2-cocycle障害があり得るため同じ結論を主張しない。

**独立したČech計算。** `prop:artin-ore-universal-cohomology` は全twistのコホモロジーと任意底変更を計算する。n≥0はH0=(A_S)_n、n=−1は零、n≤−2はH3だけでrank h_(−n−2)の有限自由加群となる。線対象間の導来HomもS-perfectで任意底変更に可換。小拡大の有限自由性は、コホモロジー完全列とJ^h→R^h→(R/J)^hの比較で示す。単なる長さの一致や、特殊ファイバーへの全射だけでは自由性を結論しない。

二次関係の分裂核、三次正則列、Koszul解消とAS双対は各内部次数で分裂する有界自由複体なので、任意の非平坦係数変更後にも必要な完全性を保つ。非Noetherian底で有限表示対象全体を無条件にAbel圏と呼ばない。

## 6. 非可換P3の四頂点potential

証明は `projective_three_space_potentials.tex` に置く。対象域は標準14641型の二次Koszul・左右AS正則Z-algebraである。弱いASの定義だけから周期性を主張しない。体上のFrobenius標準周期とその選択独立性は、asz4 commit `91b45047739187fc5acb6f906b25e48f49a42c2d` の `thm:canonical-four` と照合した既存議論を再掲する。

**符号と次数。** 四頂点の向き付けられたcycleで、各隣接矢空間V_iは4次元。係数wはV0⊗V1⊗V2⊗V3の256次元空間にあり、W=w−cw+c²w−c³w。関係は長さ2の左経路微分である。普通の一階Jacobian代数では三次関係となり、符号なしcyclic wordの商ではW自体が零となる。Frobenius周期で畳んだ双対の通常対称traceを頂点符号(−1)^iで補正するとgraded対称traceとなり、4-CY性を得る。一般の4周期同型を任意に選ぶとtwistが残り得る。

**群の商。** 射影potentialではGL4^4の中心Gm4は自明に作用する。unrolled Z側の頂点スカラーが周期と可換になる条件はlambda_(i+4)/lambda_i=kappaがiに依存しないこと。このため四つの矢空間のスカラーは独立で、積1の制約はない。pointed levelで[U4^AS/PGL4^4]≃P3^ptとなる。strict Z-stackの無限個の頂点スカラーを残したままこの商と同定してはいけない。

**相対化。** 固定した内部長のnormalized barは有限locally free複体であり、全幾何学的fiberでhomologyがその長さの次数にのみ集中する。perfect複体の可逆小行列を消去して一項へ縮約でき、Torとその双対が任意の底変更と両立する。最高次数のlineと完全Frobenius対合を得る。全trace lineのframe束の無限積はaffine fpqcなので同時自明化できる。周期の補正は有限個の単元の積から定まり、無限積は使わない。このbarの議論は標準N次元にも通る。PGL torsorが大域GL torsorに持ち上がらない場合も、両側のstack化が受け止める。

**局所rank模型。** Z6⊂P255は二つの16×16 flatteningがrank6となる局所閉scheme。rankは7次minorの零と6次minorの単元を意味する。交代tensor w_altを特殊化とする任意の局所Artin点では、全微分空間W_pが自由となる。内部長mの正次数Koszul複体の項A_(m−p)⊗W_pはp≥1なので、既知の低次数自由性だけを使う。特殊fiberでH1しかないことからcoker d2=A_mが自由になり、全次数のflatnessと完全性を同時に帰納する。双加群複体と自己双対性も得る。非正則Artin基底上の「相対CY」であり、絶対global dimensionが4という主張ではない。

**接空間と有限検算。** 二つの線型化条件のrow spaceは各100次元、共通部分Sym⁴(k⁴)*は35次元なのでrank165。affine接空間91、射影接空間90。射影Lie安定化はX_i=H+c_i I、H∈sl4で19次元、GL4^4の射影軌道45、商接空間45。これは成分次元ではない。HH²(P3)=H⁰(Ω¹(4))についてEuler列から4·20−35=45も確認できる。`verify_p3_potentials.py` は符号、可換例のrank6、非AS例w_bad=Σx_a x_b x_a x_bのrank16、200×256条件行列のrank165、256×64軌道行列のrank46を有理数で厳密計算する。

**残る大域問題。** U4^ASは全次数の局所自由性とAS条件を課したfpqc部分関手として定義した。全係数空間P255の開部分と呼ばず、255−60をモジュライ次元としない。Z6の可換点完備化が正しいことも、Z6全体のAS性や一つのZariski開近傍での一様完全性を自動的には与えない。Pymの六族 L(1,1,1,1), L(1,1,2), R(2,2), R(1,3), S(2,3), E(3) は規格化CYの可換点の芽に関する既知分類であり、全Z-algebraモジュライの大域分類とは区別する。

**N次元とP4。** 統一trace符号は(−1)^((N−1)i)、potentialはW_N=Σ_i(−1)^((N−1)i)c^i wである。N(N−1)が偶数なので周期と両立し、(N−1)p≡p(N−p) mod2がgraded対称性を与える。標準binomial型の全成分locally freeな族では[U_N^AS/PGL_N^N]≃P_(N−1)^pt。N=5はP3124内の許容関手であり、三次側の二次包絡射の行き先をこの商に置き換えられる。五つの25×125 flatteningのrank10を課すとW2とその転置によるW3がrank10、可換点のunit minorからW4/W5/W1/W0がrank5/1/5/1となる。P3と同じArtin帰納法で全flatnessと相対5-CY性を得るため、P4可換点にも有限determinantal形式模型がある。五頂点の接空間行列は今回直接計算していない。

## 7. 三次側との比較と文献上の障害

`cubic_projective_three_comparison.tex` に十分な証明を置く。A=B/(G3)ではReesの補題からinjdim4・AS parameter2を得るが、H_A(t)^−1=(1−t)^4/(1+t+t²)が多項式でないためpd_A k=gldim A=∞。二次包絡はBなので、Aに必須な三次関係は二次関係から従わない。三次側の有限データは五次ambient superpotentialの三階微分と、B3の正規三次直線である。

五頂点では三次pathは閉路でなく、L_i V_(i+3)=V_i L_(i+1)というnormal incidenceとして保持する。一頂点表示は体上のgcd(5,3)=1から選べるが、選択の忘却と族での降下が残る。三頂点で正規族を中心化してもambientのNakayama頂点置換が+2となり、五次potentialのtwistを無条件に消せない。

可換smooth cubicではDb(X)=〈Ku(X),O,O(1)〉、S_Ku³=[5]。Ext³(O(2),O)=kなので三つの連続線束は例外列でない。さらにh21=h12=5からHH±1=k5であり、full exceptional collectionも通常の有限次元tilting代数もない。この否定は一般の非可換cubicすべてに拡張していない。T=⊕_(i=0)^4 O_X(i)はcompact generatorなので、五頂点のdg/A∞模型は可能。四頂点のcycle orbitと四対象Beilinson acyclic quiverも別の代数である。

**一次文献と適用範囲。**

- Bocklandt–Schedler–Wemyss, *Superpotentials and higher order derivations*, JPAA 214 (2010), 1501–1522, DOI 10.1016/j.jpaa.2009.07.013, [arXiv:0802.0162v3](https://arxiv.org/abs/0802.0162v3)。§1の符号、Theorem6.2・Lemmas6.4–6.5、同定理証明直後のtwisted版を確認。二次4-CYのtwisted版にはTheorem6.8だけを機械的に引用しない。
- Mori–Nyman, *A Categorical Characterization of Quantum Projective Z-spaces*, Appl. Categ. Structures 33, article14 (2025), DOI 10.1007/s10485-025-09806-2, [arXiv:2307.15253](https://arxiv.org/abs/2307.15253)。著者版 regV8.pdf のTheorem4.19、Lemma5.24、Theorems6.4/6.11を確認。ASとASF++の条件差を保持する。
- Bhatoy–Ingalls–LaRoche–Nookala, *Some components of the moduli space of Koszul Artin-Schelter regular algebras of dimension four*, [arXiv:2511.08390v1](https://arxiv.org/abs/2511.08390v1), 2025-11-11。§2.3のA4はHilbert(1+t)^4のgraded Frobenius代数でKoszul条件を課さず、GL4×GL6×GL4×Gmで割る。これは本稿のZhang/pointed同値関係と異なる。
- Bhatoy–Ingalls, *Discrete Invariants of Koszul Artin-Schelter Regular Algebras of Dimension four*, [arXiv:2602.13178v1](https://arxiv.org/abs/2602.13178v1), 2026-02-13。Introductionの不変量はZhang twist不変でない。既知77族を用いた比較を全モジュライの分類とは扱わない。後二文献の公刊情報は未確認。
- Cassidy–Conner–Kirkman–Moore, J. Algebra455 (2016), 137–163, DOI 10.1016/j.jalgebra.2016.01.037, [arXiv:1307.8415v1](https://arxiv.org/abs/1307.8415v1)。Reesはv1 Lemma4.4(3)、graded twisted MF↔stable MCM↔D_sgは公刊Theorem5.8。公刊4.4は別内容。左右noetherianなBとregular normal Gなら適用可能で、有限位数・中心性・tails smoothnessは不要。左加群の規約は反対環に適用して右加群へ移す。
- Orlov [arXiv:math/0503632v3](https://arxiv.org/abs/math/0503632v3), Definition2.1・Remark2.2・Theorem2.5(i)。connected graded noetherian、左右AS Gorensteinでparameter2なら二線対象とD_sgによる分解を得る。pd_A k=∞より特異圏は非零。Kuznetsov [arXiv:1509.07657v2](https://arxiv.org/abs/1509.07657v2), Corollary4.1で可換cubicのS³=[5]を確認し、[arXiv:0904.4330v1](https://arxiv.org/abs/0904.4330v1), Corollary7.5・Theorem8.3でHHの加法性とHKRを用いる。

**成分判定に必要な反例。** 2511.08390v1のProposition5.1/Theorem5.8で用いられる「整な部分多様体への接空間同型なら成分になる」という一般判定は、述べられたままでは成立しない。Y=A²、Z=V(y²−x³)、z=(0,0)とすると、Zは整でT_z Z→T_z Yは同型だがZはYの成分でない。接層のfiberとZariski接空間を同一視できない点が障害である。Zがその点で滑らかである等の追加条件なら通常の局所次元比較で修復できるが、各具体的な族への適用は別途確認を要する。この反例は同preprintの個々の族の結論を一律に否定するものではない。本研究の成分証明では、実際の像の次元と全ambient接空間の次元をそれぞれ独立に確保する。

## 8. 成分・像・次元の範囲

poisson-p4の参照mainはf118dfbfc5bb9b7a394d1985b4800b6228eebaf6。smooth cubic上のPoissonはJacobian P(F,L,M)へ一意延長し、ambient固定fiberはF+g(L,M)、二元三次gのA4開。これは既存入力を証明再掲したもの。

全Poisson微分Mは375×150、源の微分Sは150×37。整数MS=0とmod1000003の非零minor（M113=844194、S37=948131）で全接空間37を証明する。37次元既約像が通るのでRat113錐は全Poissonスキームの一般正則成分。全147分類や有限体での零の推論は使わない。

Pymのscheme/formal germ比較と実際のQmod比較により、Q113は射影基底付きAbel/Z形式模型の37次元成分でもある。頂点完備化が整域であることは斉次最低項の積で示し、一般正則性にはexcellenceを使う。中心三次incidenceの支配的成分の射影閉包を取り、可換ambientの全fiberに沿って完備化すると、flat base changeとformal functionsにより像の形式閉包はこの成分全体となる。特定の一点Fの完備化だけの支配性とは異なる。

閉包に現れる全特殊cubicは可換多項式環で非零正則なので、Artin持上げでも各乗法のunit minorから正則性と商の自由性が従う。この完備incidenceは正規三次型のモジュライへ写る。smooth properな三次部分だけが同じ成分を支配するかは未証明。

一般中心はk[a,b,c]、重み(1,1,3)。中心3次5次元からfiberP4、ambient37・incidence41、PGL軌道24を引いて13・17。GL商stackは共通Gmの慣性のため12・16。Poissonスカラー射影化では36。可換cubic忘却fiber7=6 moving plane+1 Poisson scaleと、ambient忘却fiber4を混同しない。

## 9. 保持する既存成果と次の技術的入口

17係数sliceの31次整数行列式−5538243375000、分離型余次元15、可換cubic忘却核7、全混合中心、相対Picard障害、偶数Veronese、構造対象を保つ導来復元、固定剛体ambientの4係数族と有限位数境界は現行原稿に保持する。完全な証明は重複しない。

可換点の二次包絡平坦性は§5.3、任意係数変更後の飽和・復元は§5.5で証明済みである。最優先は§1.4の四係数族の非空開上で相対Serre公式を証明し、全O保存同値の相対比較を完成させることである。全Artin残余射の形式幾何化（§10）と、17係数全混合族の非空smooth proper開集合は上位目標として保持する。相対dg模型・対角perfect性・基底変更を確保し、必要なJacobian開部分で正規三次イデアルを保つ周期降下と有限係数incidenceを扱う。P3のrank6模型の全分類や全AS5許容関手の代数性を、その前提にしない。

文献上の範囲：Sierraの厳密twist比較、AOUのAS3での内部O(n)認識、Behrend–Noohiの切断stackは一次資料を確認。AOUの裸のqgr復元をAS5/cubicへ無証明で一般化しない。新しい主張の初出・優先権と、保持した全旧証明の独立全面監査は未完了。実施した計算・組版・証明監査はvalidation.jsonで区別する。

## 10. 残余圏の形式幾何化：既知入力と条件付き積分解

### 10.1 一次文献で確定している入力

Xを滑らかな複素三次三様体、K=Ku(X)とする。Kuznetsov [KuzHH, Theorem 8.9] は
\[
HH^p(K)=
\begin{cases}
\mathbb C & p=0,\\
\mathbb C^{10} & p=2,\\
0 & p\ne0,2
\end{cases}
\]
を計算している。Jacovskis–Lin–Liu–Zhang [JLLZ, Theorem 4.4(2)] では、**実際の幾何的接写像** H^1(T_X)→HH^2(K) が同型であり、HH^2(K)からHom(H^{2,1}(X),H^{1,2}(X))への作用γは単射である。これらは既知結果であって本研究の新規成果ではない。

標識付きdg/Morita変形の制御定理とhullの存在を正しく適用すれば、HH^1=HH^3=0は、同型類の形式変形を10変数の滑らかなhullで表す強い根拠になる。しかし対象とする変形関手・enhancement・同値・基底変更を指定する必要がある。HH^0=\mathbb Cによるスカラーの2自己同型は残るので、同型類関手／scalar rigidificationと完全な2-stackを同一視しない。

### 10.2 Poisson一次方向の消失：既知結果からの推論

通常HKRで HH^2(X)=H^1(T_X)⊕H^0(∧^2T_X)、各直和因子の次元は10である。JLLZ Theorem 3.11のsqrt(td)補正HKRを用いた可換図式では、bivectorがH^1(Ω_X^2)に作用する先はH^1(O_X)=0である。γが単射なので、補正HKRでのbivector方向はHH^2(K)への制限で消える。

通常HKRへ戻す際、bivectorのH^1(T_X)方向へのTodd補正はc_1(T_X)とのcontractionの定数倍である。[Hitchin, §5.3, pp.41–42] のcanonical bundleのPoisson module構造により、各Poisson bivector πについて π⌟c_1(T_X)=0。H^2(O_X)方向への補正もFanoの消滅で零である。Poisson cone Gr(2,5)が全bivector空間を線形に張るので、全bivector方向でも補正の影響は零となる。従ってこの一次の消失は通常HKRでも読める。

これは文献の定理と上記contractionからの推論である。今回の有限係数非可換族からの残余写像を全次数で構成した証明ではない。また以下の積分解には、この一次核の同定自体は必要なく、幾何的s方向の可逆性だけを使う。

### 10.3 条件付き代数補題：実際の残余射ができれば積分解できる

A_0=k[[a_01,...,a_34]]/(Plücker(a))、R=A_0[[s_1,...,s_10]]とする。§5.3–5.4の証明により、三次側の古典的Abel Artin変形関手はこのRで実際に表される。ここではCFTとYekutieliの既知入力を用いるが、追加の未確認formality分類は仮定しない。

次の三つを追加の入力とする。

1. 可換cubicの標識付き形式変形と、Kの適切にrigidifyしたdg/Morita形式変形が、全Artin基底で同定される。
2. 三次側のactual deformationから残余圏を取る操作が、全Artin基底で自然な写像 r を定める。ここには相対dg enhancement、O,O(1)の持上げ、例外性、半直交性、admissibility、任意の底変更を含める。
3. 可換部分a=0に制限したrは、可換cubicをそのKuに送る幾何的写像と一致する。

このとき、受け皿をk[[t_1,...,t_10]]と書けば r^*(t)=f(s,a)であり、∂f/∂sの原点での行列は可逆である。A_0を固定してsをfへ送る連続自己写像は、形式逆写像定理によりRの自己同型となる。従って
\[
 R\simeq A_0[[t_1,\ldots,t_{10}]]
\]
がk[[t]]-代数として成立する。証明は、aを固定したまま形式的にsを(t,a)から解くことであり、Plücker(a)のイデアルは変わらない。A_0が特異でも、線型s係数の可逆性を使う次数帰納は成立する。

**結論の範囲**：上の入力が満たされれば残余射は非標準的な形式座標でproduct projectionとなり、fiberは7次元のGrassmannian coneの完備化、頂点接空間は10次元である。actual ambient射と独立Poisson座標の全高次互換性を先に解く必要はない。現在未構成なのは主として入力2の全Artin相対残余射であり、本節はそれを完成したとは宣言しない。入力1の制御定理の正確な適用も確認する。

形式的な積分解は、一般非零パラメータでのKu同値、代数化・収束・全2-stack比較を含まない。対象X_Aが原稿の係数Fで定義される古典cubicそのものであるとも結論しない。新しいt座標には高次の量子補正があり得る。

### 10.4 7方向と4方向、rotationと接合

二次包絡の一般17→13のfiber4は、固定B内の中心三次直線の選択である。将来の残余射17→10のfiber7は別の自由度であり、現状はまず形式的に扱う。

可換cubicではrotation R_rotとSerre関手Sについて R_rot^3=[2], S=R_rot^{-2}[3]、従ってR_rot=S[-1]である。同じ式が成立する中心CY三次商に対し、rotationを追加しただけで7方向を回復することは期待できない。一般正規商にnormal automorphismのtwistがある場合は、この式の適用を別に調べる。

[Feyzbakhsh–Liu–Zhang, Theorems 1.1/6.2 and 1.2/7.1] は可換del Pezzo三様体について、Q_X=ker(H^0(O_X(1))⊗O_X→O_X(1))、E_X=i^!Q_X∈Ku(X)というgluing objectを使うBrill–Noether復元と特徴づけを与える。これは接合データを調べる具体的入口となる。本研究の非可換7方向をE_X一個だけで記述できるとは未確認であり、例外pair側の5矢Kronecker圏と残余圏の接合双加群全体を候補とする。

## 11. 先行研究との差分と公表前の確認

以下は現在の研究方針に効く一次資料である。定理の全適用や新規性の網羅的確認を完了したという意味ではない。

| 識別子・一次資料 | 確認した結果・範囲 | 本研究で追加すべき内容 |
|---|---|---|
| [De Deken–Lowen, JNCG5 (2011), 477–505, DOI10.4171/JNCG/83](https://ems.press/content/serial-article-files/30497), Thm4.5 pp.495–496, Prop4.6 p.496 | 全twist Ext¹/Ext²消滅を満たすZ-generating列によるAbel/線型変形の比較とnoetherian性の持上げ | 三次点への適用は既知定理の帰結。二次包絡の平坦性はこの定理に含まれない |
| [Lowen–Van den Bergh, TAMS358 (2006), 5441–5483, DOI10.1090/S0002-9947-06-03871-2](https://win.uantwerpen.be/~wlowen/pdf%20papers/TAMS-DeformationTheory.pdf), §8.2, Thm8.8 p.5472, Props4.4/4.6/4.8 | 1群oidの規約、Ind/fp比較、係数作用による底変更 | 任意係数への大きいtails比較は本稿に直接証明。小さい圏の有限表示仮定と非切断2群oidを区別 |
| [Lowen, Comm.Algebra33 (2005), 3195–3223, DOI10.1081/AGB-200066155](https://win.uantwerpen.be/~wlowen/pdf%20papers/COMALG-ObstructionTheory.pdf), Thms6.11–6.12 pp.3218–3219 | 対象のExt²障害・Ext¹で測る持上げの差。flat版は双対 | Oの形式的持上げと、大域的なOの内在認識は別 |
| [Lowen–Van den Bergh, Adv.Math198 (2005), 172–221, DOI10.1016/j.aim.2004.11.010](https://win.uantwerpen.be/~wlowen/pdf%20papers/ADVANCES-Hochschild-cohomology.pdf), Thm3.1, Rem3.5, Thm6.1 | Abel変形のHochschild制御、char0のMC/gauge、導来enhancementとの比較 | homogeneous coordinate模型との比較は対象を一致させて適用 |
| [Barmeier–Wang, Algebraic Geometry11 (2024), 1–36, DOI10.14231/AG-2024-001](https://content.algebraicgeometry.nl/2024-1/2024-1-001.pdf), Thm1.2=3.11 | affine cover由来quiver relationsによる(Q)coh変形のexplicit L∞模型 | tilting版Thm3.18をcubicへそのまま使わない。一般Abel変形理論の新規性は主張しない |
| [Lowen, arXiv:math/0511197v2](https://arxiv.org/pdf/math/0511197), Thms3.14/3.26 | algebroid模型によるMod・Qcohの全Abel変形比較 | H¹,H²(O)=0による通常の代数層への移行を明示。周期性は推論しない |
| [Yekutieli, arXiv:0905.0488v5](https://arxiv.org/pdf/0905.0488), Cors7.5/11.2 | 通常／twisted変形、可換積も変形するPoisson／Ass関手の自然な全単射 | 固定層のstar productを扱うCor11.3との区別。全Artin基底を含む |
| [Cattaneo–Felder–Tomassini, arXiv:math/0012228v3](https://arxiv.org/pdf/math/0012228), §3, Prop3.3, Cor5.2(iv) | GL同変な普遍式、一次項・単位、Casimirの中心持上げ | Artin係数の有限代入、次数計算、実際の中心商族を本稿で補う。逆向きの全分類は不要 |
| [Polishchuk–Positselski, Quadratic Algebras, ULS37, AMS2005](https://doi.org/10.1090/ulect/037), Ch6 Prop7.2/Thm7.3 pp129–130 | Noetherian局所環上で、Koszul特殊ファイバーと次数1–3の自由性から全次数自由性 | 原著の該当頁を確認。非周期的Artin Z版には直接証明を与える。一般原理を新規成果としない |
| [Rains, arXiv:2107.13540v2](https://arxiv.org/pdf/2107.13540), Thm2.13 p16 | 有限位数translationの楕円代数の全filtered deformationの中心持上げ | 被約有限型係数環上の交換子行列へ適用。非被約基底へ文献を無条件拡張しない |
| [Rennemo–Segal–Van den Bergh, arXiv:1705.01366v2](https://arxiv.org/pdf/1705.01366), Prop2.1 steps3–6, Lems3.3–3.6, Cor3.9 | 有限中心代数の有限大域次元→対角smoothness、射影性のgeneric spread | 一般tailsから全中心アフィンchartへ移す段階を本稿で証明。分裂の分母払いを明示 |
| [Stacks 058G](https://stacks.math.columbia.edu/tag/058G), [023N](https://stacks.math.columbia.edu/tag/023N), [039Y](https://stacks.math.columbia.edu/tag/039Y) | Lazard、通常の加群降下 | Grothendieck圏内の等化子による降下は直接証明 |
| [Stacks 01YR](https://stacks.math.columbia.edu/tag/01YR), [08EV](https://stacks.math.columbia.edu/tag/08EV), [0FCL](https://stacks.math.columbia.edu/tag/0FCL) | Proj上の生成・消滅、proper pushforwardのperfect性、cohとQCohのExt比較 | 0A1Eは節番号、使用するLemma36.27.1の固有tagは08EV。底の平坦性を仮定しない適用を確認 |
| [Milne, Algebraic Groups, Prop20.7](https://www.jmilne.org/math/Books/iAG2022.pdf); [Stacks 03PK](https://stacks.math.columbia.edu/tag/03PK), [0CJZ](https://stacks.math.columbia.edu/tag/0CJZ), [0FY3](https://stacks.math.columbia.edu/tag/0FY3), [051E](https://stacks.math.columbia.edu/tag/051E) | 非被約C基底上もPGL2=Aut(P¹)、Kummer列、gerbe、Serreの一意性、Artin flat=free | 相対Veronese・Hom比較の一般入力。組合せの初出は未確認 |

| [Mayanskiy, arXiv:1303.5916](https://arxiv.org/pdf/1303.5916), Theorem 1 | 固定smooth cubicの射影Poisson空間Gr(2,5)。Loray–Pereira–Touzetに帰属。証明のSchouten式はPlücker二次式 | 17という数だけを新規性にしない。有限係数の非可換族・正しい同型類・圏の幾何を示す |
| [Cukierman–Pereira–Vainsencher, arXiv:0709.4072](https://arxiv.org/pdf/0709.4072), Theorem 2; AFST18(2009),685–715, DOI10.5802/afst.1221 | 有理葉層R(r,d_0,...,d_q)のfoliation schemeでの成分性・一般被約性。r=4,q=2,(1,1,3)を含む | decomposabilityを課さない**全Poisson scheme**の接空間、中心三次incidenceとの関係を明示する |
| [Corrêa–Muniz, arXiv:2207.12880v5](https://arxiv.org/pdf/2207.12880v5), Corollaries C/D and §5 | P4のrank2 Poisson locusにRat113/Rat122型。π∧π=0を課すlocusの成分を扱う | 全Poisson schemeの一般正則性・量子化moduliと区別。全分類完成の入力として機械的に使わない |
| [Pym, arXiv:1403.6444](https://arxiv.org/pdf/1403.6444), Definition2.8, Proposition2.9, Theorem2.10 | 一般Vの規格化Koszul CY変形芽とunimodular quadratic Poisson scheme、成分の局所比較 | 解析芽の存在をcanonical quantization map、大域stack、今回の実際の比較写像と同一視しない |
| [Mori–Smith, arXiv:1502.07403v2](https://arxiv.org/pdf/1502.07403v2), Theorem4.2(1) | 滑らかな平面三次からの対称化Jacobian量子代数は3-CY | 相対PBWと5次元ambientへの拡張、指定中心三次対のmoduliを分離して述べる |
| [Reyes–Rogalski, arXiv:1807.10249v2](https://arxiv.org/pdf/1807.10249v2), Theorem5.15, Lemmas5.9/4.5 | generalized ASとtwisted CYの比較、Nakayamaは中心を固定 | 指定した正規族を保つN周期の構成、可換なd周期とのgcd周期化、相対降下が本稿の組合せ |
| [Mori–Nyman, regV8](https://faculty.nymana.wwu.edu/regV8.pdf), Theorem4.19; [arXiv:2307.15253](https://arxiv.org/abs/2307.15253) | ASF++と周期的ASF+の関係 | 弱いAS条件と混同しない。gcd対定理の初出は引き続き要確認 |
| [Sierra, arXiv:math/0608791](https://arxiv.org/pdf/math/0608791), Proposition3.3, Corollary4.4 | principal Z-algebra、compression、Zhang twisting system | 周期の選択・共役・相対降下を別々に記述する |
| [Rains, arXiv:2107.13540v2](https://arxiv.org/pdf/2107.13540v2), Theorem2.13 | torsion translationの楕円代数のfiltered deformationでは中心もfiltered deformationになる | finite-order境界の入力。一般infinite-orderへそのまま適用しない |
| [Rennemo–Segal–Van den Bergh, arXiv:1705.01366v2](https://arxiv.org/pdf/1705.01366v2), Proposition2.1, proof(6)–(7) | 有限型可換代数上有限な代数のgeneric smoothnessと相対perfect diagonal | finite-center仮定を供給する。一般AS5やqgrのsmooth proper性への無条件の近道ではない |
| [KuzHH: Kuznetsov, arXiv:0904.4330](https://arxiv.org/pdf/0904.4330), Theorem8.9 | cubic3の残余圏の全HH^p表 | actual NC residual familyと幾何的変形への全次数写像が新たに必要 |
| [JLLZ: Jacovskis–Lin–Liu–Zhang, arXiv:2203.08187v3](https://arxiv.org/pdf/2203.08187v3), Theorems3.11 and4.4(2) | 幾何的接写像の同型、γ単射、補正HKRの図式 | 次元一致だけでなくactual mapを使う。形式/代数的な比較の区別を保つ |
| [Hitchin, arXiv:1008.0973](https://arxiv.org/pdf/1008.0973), §5.3 pp.41–42 | canonical bundleのPoisson module構造とπ⌟c_1(T)=0 | §10.2のTodd補正確認に使う |
| [Feyzbakhsh–Liu–Zhang, MPIM23-7](https://archive.mpim-bonn.mpg.de/id/eprint/4904/1/mpim-preprint_2023-7.pdf), Theorems1.1/6.2 and1.2/7.1 | 可換del Pezzo三様体のgluing objectとBrill–Noether復元 | 今回の非可換族で接合データが7方向をどう保持するかを調べる |
| [Matviichuk–Pym–Schedler, arXiv:2411.10425v1](https://arxiv.org/html/2411.10425v1), Introduction, Theorem1.1 | 適切な非退化条件を満たすq-symmetric/toric型から具体的な量子射影空間を作る | rank2 Rat113へ直接適用する定理ではない。有限係数成分構成の方法比較に使う |
| [Lin–Zhang, arXiv:2611.05915v1](https://arxiv.org/html/2611.05915v1), §2–3 | 幾何的相対admissible圏・perfect kernelを仮定する同値変形。新しいhypersurface Torelliの結果 | 任意のNC familyを幾何的とする定理ではない。今回の代数化入力と混同しない |

近接するfoliation文献とKu変形の文献は、公表用Introductionへ正確に反映する必要がある。現在のAbel変形比較については上記の確認済み一次資料をIntroductionとbibliographyに反映した。残余圏・foliationの関連入力は、公表時の中心定理に応じてさらに照合する。

## 12. 現在の検証範囲と外部課題との境界

全Abel変形の平坦二次包絡、次数三判定、平方零消滅、形式環の証明を保持する。今回の主な点検対象は任意係数変更のHom・復元・内部fpqc降下、全twistのČech計算、有限中心の射影模型、全中心アフィン片へのExt局所化、相対対角の拡張と内在的perfect部分圏である。主要な証明は別々に読み合わせた。相対Serre公式、全圏の有効降下、大域dg smoothnessを先取りしていない。第三者査読、新規性の網羅調査、全旧証明の独立再証明は未完了。正確な対象ファイル・一次資料・範囲は `validation.json`。

既存8計算は2026-11-16に実行され、横断slice行列式−5538243375000、Rat113の全Poisson接空間37、二因子stabilizer rank48、低次中心、中心三次式、軌道rank24、分離型codim15を再現した。3保存証明書も一致している。今回そのsourceは変更しておらず、これを今回の再実行と報告しない。

現行sourceの参照・引用の閉包を検査する。LuaLaTeXの実行は `lualatex.fmt` 不在で停止した。日本語クラス・luatexjaも実行環境で確認できず、今回のPDF生成・視覚確認は未完了。生成、静的検査、証明点検、組版、remote保存の各状態を区別する。

### H3/PI4の関連知識（本研究の定理の入力ではない）

以下は三次曲面側に属する情報であり、本研究の次の作業指示ではない。対応する現行ファイルの所在を移管元 `uedakazushi/nc-cubic-classification` のcommit `d9070ddd2352f54c1db243be11ec482d062b8a60` で確認した。内容を本研究へ引用して使う時は、仮定・式・証明をその一次ソースから点検する。

- point graphの規約はp yz+q zy−h x²に対する第一行(−hx,qz,py)であり、p,q逆順は逆translationを表す。[verify_cubic_integrated_envelope.py](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_integrated_envelope.py) が関連する検算である。
- 固定PI4族の有限Ext判定・48次元sliceは、[cubic_order4_ext_bound.tex](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/papers/sections/cubic_order4_ext_bound.tex) に属する。AS4のCCKM二周期性、次元≤4の単純加群対のExt6/7、中心2パラメータ上のgraded free性と基底次数≤8を用いる。この曲面側のH3判定をAS5三次三様体のsmooth proper性に転用しない。
- Du Val中心だけではH3の十分条件にならない例を保持する。中心のHessian rank2、核方向cubic零、形式Morseの初項次数4によりA3となる一方、odd Ext1が非H3を検出するという内容は、[cubic_order4_center.tex](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/papers/sections/cubic_order4_center.tex)、[全中心式証明書](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/cubic_order4_center_relation_certificate.json)、[局所検算](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_order4_bad_center.py) に対応する。
- 中心式を再構成する際の変換の知識：r1=(g−1)(g²−1)/2、r2=(g²−1)²/2、X_i=r_i Z_i（r3=1）で最高次をΣX_i³+(7g²−13)X1X2X3へ規格化し、pure squareを消すaffine shift後にu=X1+X2,v=X1−X2,z=X3を取ると、4F=f(u,z,D)+v²(3u−(7g²−13)z−B)となる型を使う。特異値はv=0枝と線形係数零の枝へ分け、二変数critical normと線上三次の判別式で調べる。ただし中心特異値とbad Dは同一視しない。関連する[対称中心検算](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_order4_symmetric_center.py)・[中心critical検算](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_order4_center_critical.py)を参照する。消失した作業用絶対パスを再開の前提にしない。
