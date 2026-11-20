# 研究ノート：非可換三次三様体と非可換P^4

2026-11-21 / research-notes-v18 / 主論文 manuscript-v23。現在有効な研究知識。詳細証明は主論文 `papers/nc-cubic-threefold.tex` とその `papers/sections` に保持する。H3/PI4曲面の関連知識は§12で本研究の入力と区別する。

## 0. 三次三様体に固有の現行成果と研究間の接続

点スキームの詳細な二論文 `papers/mixed-cubic-point-schemes.tex`・`papers/diagonal-cubic-point-geometry.tex` を同じrepoの正本とした。特殊混合族の非被約長さ24部分・零極限、対角族の標準種数5曲線上の次数24因子と次数56衝突判別式はこれらの独立稿に証明を保持する。研究ノート `notes/point_schemes.md` と `computations/point/` に詳しい適用条件・検算・障害がある。主原稿 `papers/sections/point_scheme_poisson.tex` の全O-marked moduliへの応用と、指定特殊族の局所計算を混同しない。



本repo `uedakazushi/nc-cubic-threefold` の主原稿は `papers/nc-cubic-threefold.tex`。全次元一ブロック論文 [nc-cubic](https://github.com/uedakazushi/nc-cubic/blob/main/papers/nc-cubic.tex)、古典正規形 [poisson-cubic](https://github.com/uedakazushi/poisson-cubic/blob/main/papers/poisson-cubic.tex)、量子化 [cubic-quantization](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex) を独立した外部入力とし、証明の正本を重複させない。

**三様体固有の中心：** 可換点の全O-marked Abel圏framed Artin群oidは `abel_cubic_deformations.tex` と `abel_formal_descent.tex` により十次元形式円板×Gr(2,5)錐の頂点完備化であり、Krull次元17・接空間次元20。実際の残余操作と相対Poisson忘却の形式射への両立は `poisson_cubic_lifts.tex`。17次元Jacobian部分stack `jacobian_moduli_chart.tex` と十次元可換三次モジュライへのρ（相対次元7） `kuznetsov_moduli_morphism.tex` は、全次元の良い一ブロックの特殊化と開の条件を要照合。

**一般次元からの引用（本稿固有の再証明はしない）：** `nc-cubic` の (n=3) では良い一ブロックstackの次元17、周囲stack13、中心三次選択のrank4 torsor、残余Poisson射の一般次数9と符号商18、点型比較核の一般split体上のPicard index三が得られる。三様体についてfull比較classの降下・最小次数三も同論文の指定仮定の下で主張される。これらを本稿の全Abel Artin近傍や全intrinsic成分へ自動的に拡張しない。

**最優先の比較：** `nc-cubic` の良い一ブロックstackとの実際の共通開で、O-全同値・PBW/AS・中心・étale条件を合わせる。両方で比較が成立する場合も、ρが `forget∘Ψ_res^sc` に一致することは現在未証明である。比較核の全同型類とscalar gerbe、標識付き周期を混同しない。点スキーム固有の退化の正本は本repo内の二つの独立点スキーム論文、Pfaffian・Brill--Noetherの正本は `pfaffian-brill-noether`、一般相対復元の正本は `nc-cubic2`。

## 1. 何をモジュライのデータに含めるか

### 1.1 豊富列を保持する座標模型

二つの座標代数stackは、各成分が局所自由な正の連結Z-algebraのfpqc stackの部分問題として定義する。ambient Bはb_m=binom(m+4,4)、cubic Aはh_m=b_m-b_(m-3)。Aの長さ一のHomと長さ二の積の核からQ(A)を得る。原稿`intrinsic_cubic_reconstruction.tex`の相対復元と、`algebraic_moduli_foundations.tex`の定義・比較定理を使う。

有限窓J_N=[-N,N]では、全Homの乗法の有限個の係数に結合律を課したaffine schemeを、各HomのGLの積で割る。全stackはこれらの2逆極限。AS正則性・noetherian性・無限個のHilbert rank条件の有限決定性は別に必要であり、逆極限表示を有限型代数性と呼ばない。

全対象同定付き圏の1射は(F,alpha_i:F(E_i)≅E'_i)、2射はbeta_i eta_i=alpha_i。Hom群oidは離散化され、厳密Z同型と一致する。同定を忘れると頂点スカラーrho_lambda(a_ij)=lambda_i lambda_j^(-1)a_ijが現れる。weak圏の自己同値の2同型類はAut_Z(A)/rho(T)、恒等自己同値の2自己同型は対角Gm。E_0の同定を残すとT0={lambda_0=1}で正規化でき、2慣性が消える。

相対弱い射は線束族L_iとphi:A→(A')^L、(A')^L_ij=L_i A'_ij L_j^(-1)で記述する。この規約ではF(E_i)≅E'_i⊗L_i。共通線束Lは代数式では相殺するが、圏ではtensor-by-Lとなる。自己同型商はfpqc商層であり、大域点集合の単純な商と同じとは限らない。weak 2-stack化では大域的な代数で表示できないtwisted formsも含み得る。証明は`categorical_moduli_comparison.tex`。

Q(A^L)=Q(A)^Lなので三次→ambientの射は全levelに降りる。ただし相対category比較にはHomの任意の基底変換、低次数saturation、相対section復元を仮定する。裸のAbel圏・導来圏・Kuznetsov成分のみからの復元は含まない。


### 1.2 構造対象だけを標識した問題

現在の主対象は `(C,O)`。許容な三次豊富列 `(E_i)`、E_0≅O の存在を条件とし、選択自体を記憶しない。1射はOを保つ全ての完全線型同値、2射はOの同定を保つ自然同型である。`M^pt` は列保存の条件を残していたので、今回の `M^O_cub` と区別する。全相対模型には底変更と降下を明示的に含める。アフィン上の標準Grothendieck模型の底変更は係数作用付き対象を用いる。任意の係数環上では大きいQGrを使い、小さいqgrはAbel性が保証される場合に限る。全Mの有限型atlasは未構成であり、Jacobian型全部分stackのatlasは§1.7で構成する。定義と証明は `abel_marked_moduli.tex`。

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

Nat(Id)=Cは豊富列から直接従い、O上の同定を残すと2慣性は消える。μ2は次数スカラーGmの部分群であり、追加の2慣性ではない。相対版 `thm:abel-relative-pointed-hom` は有限型C-schemeのfppf siteで、C1–C4を仮定した条件付き定理である。基底非正則の場合、Db(coh)全体へ通常のSerre双対を仮定せず、内在的な有限Tor振幅部分圏を使う。一般17係数族の明示Δ開では、compact対象と有限Koszul対角解消を用いることで、全ての可換係数環上の比較を得た（§1.6）。四係数族の有限中心による比較は§1.4–1.5に保持する。

**具体的帰結。** 剛体B_*の全四係数族で、O-marked圏はパラメータごとに相異なる。さらに有限型C基底上の相対同値についてA4→M^Oはmonomorphismとなる。既存PBW・AS・CY・剛体性入力を明記した証明は `prop:rigid-four-family-monomorphism`。正則開上の体上の系 `cor:abel-rigid-four-family` も保持する。これは開埋込み、étale chart、bare categoryの相異性を含まない。

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

**射影模型とC1–C2。** 十分割り切れる偶数ℓについてD=C^(ℓ)、Y=Proj D、𝒜=˜(A_P^(ℓ))を使う。c∈D_1を可逆化すると、Aの次数一生成から1∈T_1T_−1かつ1∈T_−1T_1となり、強い次数付けを得る。この点を省略すると、重み付き中心のProjを使う際に次数剰余類を失い得る。任意のP代数SについてQGr(A_S)≃QCoh(Y_S,𝒜_S)であり、全twistの切断加群を使う逆構成はStacks0AG5による。SがNoetherianならqgr≃cohに制限され、大きい圏はlocally Noetherianとなる。ℓを偶数に取ると、このNoetherian底で通常のSerre生成性・消滅が偶数列へ移る。

全twistのsection飽和は M_m=A_S(m)^(ℓ) 上の中心正則列 u^ℓ,v^ℓ による H^0_(D_+)(M_m)=H^1_(D_+)(M_m)=0 から従う。全Noetherian底変更で同じ証明が使え、負次数Homも零となる。一般のSは有限型P部分代数のfiltered colimitと書き、標準対象の有限表示性と自由係数作用の随伴から同じ式を得る。従って飽和とVeronese同値は任意係数で成立する。`prop:central-model-even-sequence` (1),(3)の豊富性と関手決定はNoetherian Sで述べ、列を射影対象と仮定しない。二つの表示を直和の共通全射で比較し、coherent部分からfiltered colimitで全体へ延長する。

**compact対象の範囲。** BDG Definitions3.1/3.13・Theorem3.14はquasi-compact separatedなYとquasi-coherent代数層に適用できる。従ってD(QGr(A_S))^c≃Perf(Y_S,𝒜_S)は任意のSで成り立つ。Noetherian性やfiberの正則性をこの同定へ追加する必要はない。下記の有限S-Tor部分圏との一致は、別の非空開上の結果である。

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
| C1：相対QGr模型・対象／射の降下 | 任意係数でbig QGr≃QCohと固定模型のHom降下。qgr≃cohとlocally Noetherian性はNoetherian底 |
| C2：全twist飽和・偶数列・復元・関手決定 | 飽和は任意係数、豊富列による全射比較はNoetherian底 |
| 元のC3：有限係数Tor部分圏=局所Perf | 一般正則性入力の下で非空開上 |
| compact版C3：D(QGr)^c=局所Perf | BDG Thm3.14により全係数基底。全Abel同値が保存 |
| C4：perfect RHom・相対Serre・底変更 | 局所Perf上で全四係数基底、S≅(−2)[3]。任意Noetherian底変更 |
| 全相対Homとモジュライ射 | 有限型CサイトでIsom_gr/Gm≅Eq_O、剛体性入力下でA4→M^Oはmonomorphism |

一般17係数族の明示Δ開への相対Serre・Hom比較は、有限Koszul解消を用いる§1.6で完成した。有限型atlasと大域dg smooth性は別の問題であり、局所対角のperfect性だけから結論しない。有限位数境界上の大域対角と相対smooth proper性は§1.8で別に証明する。

### 1.5 相対Serre双対と全四係数族の忠実性

詳細な証明は `relative_serre_duality.tex` に集約する。ここでは再利用する構成と、誤用を防ぐ条件だけを記す。

**体上の双加群同定。** 中心Veroneseの生成元から重みℓの多項式環Tを選ぶと、AはT上有限である。Yekutieli1992 Prop5.2と、torsion-of-injectives・balanced一意性を使い、RHom_T(A,R_T)をAのbalanced dualizing complexと**両側加群として**同定する。R_A=A(−2)[4]の入力は既存B_*のCY・AS5と中心正則三次商から供給する。ℓ-Veroneseと層化の後のシフトは[−1]で、射影模型の双対はE_−2[3]となる。体上の片側のSerre対象の一意性だけでは、両側作用の同定を代替できない。

任意の拡大体kでのB_*⊗kのNoetherian性も確認した。f=0の商が有限中心模型からNoetherianであること、G_*が正次数の中心正則元であることを使う。G_*進filtrationの随伴次数付き代数からの斉次イデアル生成元の持上げは、固定した全次数で停止する。任意のNoetherian代数の体拡大がNoetherianである、と仮定しない。

**相対化。** P=C[a,b,c,d]、j:Y→Z=P^N_Pに対し、

\[
\mathscr D_P=R\mathcal Hom_{\mathcal O_Z}(j_*\mathscr A,\omega_{Z/P}[N])
\]

を作る。Zは正則、𝒜はP-flatなので、有限O_Z射影分解は任意の係数変更後にも分解である。全residue fieldでの双加群公式とStacks00MIからD_P=W[3]、WはP-flatとなる。V=Hom_𝒜(E_−2,W)に07VKを適用し、RΓ(V)=L[0]（Lは基底直線束）を得る。ここではRΓ(𝒜_s)=κ(s)も必要であり、AS局所コホモロジーで示す。評価L⊗E_−2→Wは各fiberで同型なので大域的にも同型。Pic(P)=0で右加群同型を選び、generic fibreでの双加群同型との差がスカラーであること、WがP-torsion-freeであることから左作用の両立を得る。

**底変更の注意。** 初期のD_Pの底変更はunderlyingなD(O_Z)で作り、左右の乗法への自然性を保持する。𝒜^op⊗_(O_Z)𝒜のP-flatnessは仮定しない。D_P=W[3]とWのflatnessを得た後、H^−3を取った比較がW⊗SとH^−3(D_S)の通常の双加群同型になる。この順序で全係数の真正な双加群同型を得る。Y/P自身のflatnessも不要である。

**Serreとcompact。** 局所𝒜-perfectなK,LのHomはambient O_Z-perfectでもある。射影空間上のGrothendieck双対と有限射影tensor–Homにより、相対Serre式とtraceが自然に得られる。Stacks0B91でproper Homと任意底変更を確認する。BDG Thm3.14により局所Perf=D(QGr)^cなので、完全Abel同値がこれを保つ。Serre同定の選択差は標準線対象上で一つのスカラーとなり、その冪が次数スカラー商に吸収される。Perf圏の全ての自然自己同型がスカラーである、と余分に主張する必要はない。

このcompact版と元の有限係数Tor版C3は別である。体上では全coherent対象が底に関してTor振幅零だが、特異代数層上では全てperfectとは限らない。この例が両者を混同できない理由である。全四係数族のHom比較にgeneric regularityは使わない。

**群スキームとmonomorphism。** Aut_gr(B_*)は二次関係のstabilizerとしてGL5の有限型閉部分群スキームである。標数零のCartierの定理と既存の複素点の剛体性から、群スキームとしてGmに等しい。従って任意のC代数SでA_f≅_gr A_gなら、二次包絡の自己同型は次数スカラーである。三次核の最高symbolγの係数を比較するとf=gが従い、非被約基底でも追加同一視はない。

相対Hom比較と合わせ、有限型C基底T上で射の層は二つの係数写像の閉等化子Eq_T(f,g)が表す層となる。全fpqc stack化後にも、固定模型のHomの任意fpqc降下と標識付き2慣性の自明性から射は増えない。後者だけでは降下の有効性の代わりにならない。従ってA4→M^Oはこのsite上でmonomorphismであるが、開埋込み・成分性・atlasではない。

### 1.6 一般Jacobian族の相対双対と全同値

証明は `koszul_relative_duality.tex` と `jacobian_abel_comparison.tex` に置く。前者は相対入力からの定理、後者は実際の17係数族が入力を満たすこととモジュライへの適用である。

**四つの相対入力。** Bの次数成分が係数有限射影、長さ5の有限射影Koszul双加群解消、任意底変更に両立する真正な双加群同型 Θ_(B/P)=B(5)[−5]、中心三次商A=B/(w)の次数ごとの分裂完全性を要求する。有限中心・Noetherian性・楕円自己同型の有限位数性は要求しない。相対CYは各fiberのCYという述語だけでは代替できない。

**局所双対の構成。** B/B_≥nを有限対角解消にtensorすると、torsion関手を計算する幅5の複体が得られる。非有界導来Gabriel商の同定は、商関手πの完全性と右随伴ωのK-injective保存から得る。有限Koszul模型の各項がexactで直和・filtered colimitを保つこと、torsion加群上で恒等になることにより、導来torsionの有限幅性とRωの直和保存を得る。Bの有限係数加群のtensor–Hom双対からRΓ_B(B)=B^∨(5)[−5]を計算する。三次商ではTor¹_B(B/B_≥n,A)の遷移がnを3増やすと零になるため、AとBのtorsion導来関手を比較できる。

Rees随伴によりRΓ_A(A)=A^∨(2)[−4]を得る際、初めに残るのはB–A作用である。単一次数集中後のheartでB→Aの全射性を用いて、真正なA双加群の同型へ戻す。導来restrictionが完全忠実である、という誤った置換はしない。

**五つのcompact generatorとSerre。** O_A,…,O_A(4)はcompact generatorである。n=j−iとして

\[
R\operatorname{Hom}(O_A(i),O_A(j))=
\begin{cases}
A_n[0]& n\ge0,\\
0&n=-1,\\
A_{-n-2}^{\vee}[-3]&n\le-2.
\end{cases}
\]

この同型は全係数変更に両立し、全compact間のHomは係数perfectとなる。次に左A作用付きinjective解消からstrict dg代数A→Qを作り、Q⊗^L_AQ=Qを示す。局所化三角を係数双対化し、両側へQをtensorする。A^∨はtorsionなので消え、Q^∨=Q(−2)[3]を**Q双加群として**得る。この同型と評価が、全compact上の自然なSerre pairingとtraceを与える。線対象間Extの階数だけからpairingや高次作用を推定しない。証明は `thm:koszul-cubic-relative-serre`。

**具体的な基底。** 最高次式をa(x³+y³+z³)+bxyzとし、p=2−b、q=−(2+b)、r=−6aを用いる。楕円境界判別因子D_E、三回反復を除外するL_6と

\[
\Delta=a(27a^3+b^3)pqrD_E(p^3-q^3)(q^3-r^3)(r^3-p^3)L_6
\]

を `eq:general17-coefficient-ring` に明示した。P=C[a,b,Δ^−1][α,β,9個のm_ij,4個のg_j]は17次元である。a=1/6,b=0で七因子は1/48,4,−1729,16,−7,−9,193となる。既存slice開との共通部分が非空である理由は、二つの非零多項式の積が整域上で非零だからである。この数値点でslice横断性まで検算したとはしない。

楕円曲線Eのbilinear graphを相対的に構成し、σ,σ²,σ³≠1を明示式で保証する。正次数1–3のTHCR中心は消え、Rains中心式ΩによりS_top/(Ω)=Hとなる。閉点上のPBWと有限行列の定階数からB,AをP[u,v]上射影にし、中心三次元wの普遍正則性を得る。Rains公式の分母は全てΔの単元である。

**閉点検出の使用範囲。** 普遍PBWの証明は、被約な有限型環P₀およびQ=P[u,v]での一定階数行列と有限射影切断の閉点検出に依存する。選んだ語の持上げの間の関係は、有限個の射影summand内で零と判定する。その後に各濾過段階を分裂して任意係数へ移すため、非被約・非Noetherianな変更先で閉点検出を繰り返す必要はない。正確な濾過付き写像ηと次数別の議論は `prop:general17-universal-pbw`。

**相対CYの実際のorientation。** P[u,v]上の三変数potential複体はcyclic Hessianのflip恒等式によって自己双対である。双加群をD=B⊗_Q B^opの左加群で書き、右加群をτ_Dで戻す。cochain双対の微分d^j(f)=(−1)^(j+1)f d_Kに対する符号は(+,-,+,-)であり、全基底対応を `eq:general17-cy-chain-signs` に置く。中心差u_L−u_R,v_L−v_Rの順序付きKoszul双対はD(2)[−2]を与え、Θ_(B/P)=Θ_(B/Q)(2)[−2]=B(5)[−5]となる。左D作用は右掛算への前合成から計算し、単なる片側同型で代用しない。指定した有限二次Koszul解消でもorientationをchain mapで表し、その有界P-flat acyclic coneにより任意底変更を確認する。

`computations/verify_relative_cy.py` と `relative_cy_certificate.json` は、active次数0–3の全40自由語に対する合成、flip Hessian、cochain符号、規格化の恒等式を保持する。potentialへの線型性により任意の中央係数を含む。これはPBWや解消の完全性の計算証明ではなく、完全性は次数別の有限射影分裂と有限濾過で証明する。

**許容性と全同値。** P[u,v]上のflatnessからČech交わりとtorsion拡大の分裂を使って全shift飽和を得る。二次中心のrank12交換子写像は分裂単射なので、Z(A_S)_2=Sym²(Su⊕Sv)は任意Sで成立する。偶数Veronese同値QGrA≃QGrA^(2)は次数一生成から直接証明し、全偶数線とHom・合成によるGabriel右随伴が実際の同値を決定する。豊富列を射影列と仮定しない。

Noetherian係数では、degree3nの楕円線束列をKeelerの訂正版のample filter判定へ適用し、H、S_top、B、Aの左右Noetherian性を得る。Γ_Bの幅5と六段の有限自由部分解消で高次数のΓコホモロジー消滅を示し、通常列・偶数列の豊富性を得る。これは一般Abelモジュライへ実際の相対模型を送るための確認である。

Serreの一意性から全O保存完全同値はH=Serre^−1[3]=(2)の一貫した軌道を保つ。正負の整合的な反復からα_i:F(H^−iO)→H′^−iO′を選ぶと、全てのi≤jでsection Z代数に誘導する写像が同じφ_(R,j−i)となる（`eq:abel-even-section-coherence`）。零番の行だけの比較で同値を結論しない。偶数切断を復元し、μ2-torsorで次数一へ局所的に持ち上げる。Serre表示の差は、体上の有界Serre版ではheartに、任意係数のcompact版では全偶数軌道対象に制限してスカラーと判定する。選択差は次数スカラーであり、marked自然2自己同型は自明。固定模型のHomは既に層なのでstack化は新しい射を加えないが、捩れた対象は加わり得る。従って `thm:general-relative-pointed-hom` は任意C代数上でfpqc層としてEq_O=Isom_gr/Gmを与える。

さらにA₁=A′₁=S⁵なら、I₂=ker(V²→A₂)のrankは10、I₃=ker(V³→A₃)のrankは91である。Eq_OはPGL₅内でg^⊗2 I₂=I′₂、g^⊗3 I₃=I′₃を満たす閉部分スキームであり、S上有限表示である。全同値の比較によって既存17次元Rosenlicht変動がO-marked Abel圏にも移り、二次包絡の17→13射が全同値に自然となる。

**主張の境界。** 有限表示Isomだけから全Mのatlasや代数性は従わない。具体的な飽和開を用いた代数的部分モジュライは次項で構成する。Compact proper・Serreとdg smoothness、O-markedとOを忘れた圏、graded ambientとambientの全Abel同値は別である。相対構成の初出は未確認。


### 1.7 代数的Abel部分モジュライと相対四次元torsor

完全な証明は `jacobian_moduli_chart.tex`。滑らかな有限型DM stack

\[
\mathfrak C_{\mathrm J}=[J/\mathrm{PGL}_5]
 \longrightarrow \mathfrak B_{\mathrm J}=[Y/\mathrm{PGL}_5]
\]

を構成した。次元は17と13であり、射は階数4ベクトル束のtorsor、スキームで表現可能、アフィン、滑らか、全射である。`C_J→M^O` は任意係数環で完全忠実で、本質像は指定したatlasの模型へfpqc局所的に戻る族からなる。これは幾何ファイバーごとの条件だけではない。

**étale atlasの作り方。** `P_B=C[a,b,Δ^−1][α,β,9個のm_ij]`、`T_B=Spec P_B` とする。G=PGL5、既存の37次元関係graph成分Q113に対して `a:G×T_B→Q113` は支配的で等次元。標数零の函数体拡大の分離性から非空étale locus Eを持つ。平坦底変更と群移動によってEの不変性を開部分スキームとして確認すると `E=G×T_B^e`。étale射は開なのでY=a(E)は非空不変開となる。`T_B^e→[Y/G]` のYへの引戻しがE→Yだから、これが実際のétale atlasである。商の代数性、étale判定、アフィン降下はStacks Projectの既知入力であり、新一般理論とはしない。Pymの解析的・形式的比較はこのatlas構成には不要である。

**一つの明示点で両方の開条件を確認する。**

\[
(a,b,\alpha,\beta)=(3,5,2,3),\qquad
(m_{ij})=\begin{pmatrix}1&1&2\\2&3&1\\1&4&5\end{pmatrix}.
\]

これは既存Rat113証明書のF_*と同じ点である。25個のGL方向と13個のslice方向を合わせた150×38整数行列Dについて、37次minorは127524 mod1000003。5個のGL対角方向の和が整数上で零なのでkernelはちょうど同時スカラー1方向である。全Jacobi・発散の375×150微分MについてMD=0を整数上で確認し、既存113次minor=844194 mod1000003を再計算した。したがってQ113の接空間は37次元で、既知の像の次元37と合わせてこの点でのsmooth性を得る。PGLへ移ったdaは同型である。

同じ点でΔの七因子は2562, −378, −237100440304, 316, 5489, −5805, 31963501で、全て非零。従ってこの点はT_B^eに属する。再現は `computations/verify_jacobian_etale_point.py`、小証明書は同じディレクトリの `jacobian_etale_point_certificate.json`。行列の組立ては旧 `verify_rat113_tangent.py` の多項式helperと既存証明書の入力を再利用し、同一入力であることとhashを照合する。数値検算はこの有限入力の証明であり、stack降下やdg smooth性の代替ではない。

**普遍中心とtorsor。** 任意のP_B代数Sについて

\[
Z(B_S)_1=Su\oplus Sv,\qquad
Z(B_S)_3=S\mathcal G\oplus\operatorname{Sym}^3(Su\oplus Sv).
\]

低次数THCR中心の消滅、active最高記号とPBW分裂により閉点上の中心を計算する。候補中心を除いた有限射影加群の交換子写像は各閉点で単射なので、Jacobson基底上で局所分裂単射となる。この分裂により非平坦・非被約な底変更も扱える。中心のファイバー次元一定だけを用いる証明ではない。

Y上では普遍二次代数が存在する。`GL5×T_B^e→Y` のfpqc被覆でslice模型へ比較して、中心束U,EとW=Sym³U、L=E/Wを降下する。普遍PGL行列が大域的にGLへ持ち上がるとは仮定しない。階数は2,5,4,1。`J=P_Y(E)\P_Y(W)` は完全列 `0→W→E→L→0` の分裂の層である。二つの分裂の差はHom(L,W)なのでJはその加法群のtorsorとなる。T_B^e上ではRains中心元Gが分裂を与え、`J×_Y T_B^e=T_B^e×A4` となる。

**中心重みを忘れない。** GLの中心はUに重み1、W,E,Lに重み3で作用する。U,E,L自体はPGL商上の通常の束とはしていない。Hom(L,W)だけは重み0で、J上の作用も中心が自明なためPGLへ降下する。これにより本当の階数4ベクトル束とtorsorを商上に得る。大域的原点を選ぶ証明はないので、torsor自体を自明なA4束や零切断付きベクトル束とは記さない。

**全Abel同値との接続。** Jは `Gr(10,V²)×Gr(91,V³)` へ局所閉埋込みされる。二次関係からB₃の核K₃（rank90）を作り、三次直線をI₃/K₃として任意基底で復元する。これでPGL transporterがIsom_gr/Gmに一致し、§1.6の全Hom比較を適用できる。次数スカラーε_λの構造移送には `m_d⊗b↦λ^d m_db` というOの標識を保つ自然同型があり、合成にも両立する。したがってPGL torsorの降下後に大域的な次数付き代数がなくても、M^Oの対象は定まる。

**以後の課題の境界。** C_Jの対角はアフィン・有限表示・非分岐であり、幾何学的stabilizerは有限。自明性、有限対角、分離性は未証明。全M内での開性・局所閉性・成分性・形式的な全変形との一致も未証明である。有限関係窓の商内での局所閉性とは区別する。Oは降下するがO(1)と無捩れなSerre式(−2)[3]はatlas上での表示として扱う。パラメータstackのsmooth性は、個々のcompact圏のdg smooth性を意味しない。

固定Bとその同定を含む2-fiberはA4 torsorだが、Bの同型類だけを固定した同型類には有限Aut_gr(B)/Gmの作用が残り得る。B_Jの射はprojectively graded同型であり、周囲の全O保存Abel同値を分類したとはしない。

### 1.8 相対 dg smooth proper な部分族と一般点の幾何化

**現在の確定範囲。** 詳細証明は `papers/sections/dg_smooth_torsion_families.tex`。固定有限位数ambientではA4、境界(a,b)だけを固定して混合11係数も動かすとA15、それをHesse族のtorsion曲線Z上で動かすとZ×A15の非空開に相対dg smooth proper性が成立する。全て任意の可換係数変更と両立する。17次元atlasの任意の非空開Wの中にも、後者の16次元族の非空開を取れる。従ってsmooth proper複素点はatlasとC_Jに稠密である。さらに17次元一般点のsmooth性とその非空開は、§10と `kuznetsov_moduli_morphism.tex` の残余射の定理で証明した。有限位数の稠密性から一般点へ推論するものではない。

**証明の構造。** `prop:seed-finite-central-global-smooth` は完全体上の有限型分離Yとcoherent代数Aについて、左右Dbcoh=Perfから大域dg smooth性を得る。YとY×YはNoetherian、YはJ-2であり、ELS4.18(b)により任意に選んだgeneratorのG∨⊠Gが外積代数のDbcohを生成するため、対角δ_*Aがそのthick閉包に入る。Künneth・有限Čech・有限射影tensor–Homにより、dg Moritaで対角E∈Perf(E^op⊗E)へ移す。右加群の作用はm·(a^op⊗b)=ambであり、Hom比較でこの作用を追う。O_Y-flat性は仮定しない。局所affine対角のperfect性と大域対角を省略して同一視しない。

`lem:dg-generic-spreading` はR-perfectなEの一般点がsmoothなら非空主開上でも相対smooth properであることを証明する。TV2.10／Toën F4により一般点のperfect対角をPへ降ろし、**source Pのcompact性だけ**でP→Eを降下する。coneはR-perfectなので一般点での零性を有限個の分母払いで開上へ広げられる。Eが既に包絡dg代数上perfectであるとは仮定しない。`lem:dg-smooth-field-descent` は任意の体拡大からのsmooth性の降下を与える。一般点を証明済みの場合に使う補題であり、閉点からの開性定理ではない。

**体の仮定。** 固定ambientの正則開 `CSBGthm:global-open` と中心持上げ補題を、代数閉標数零体k上で述べ直した。全係数u-chartはD_u[g1,g2,g3]なので有限大域次元を持ち、Rains2.13、被約Jacobson環の一定階数、RSV2.1から相対有限対角を得る。very-general点や非可算性を使わない。これによりF=Frac(O(Z))(混合11係数)、K=F(g0,…,g3)、Fbar⊂Kbarという順序で、固定ambientの定理をFbar上に適用できる。gはFbar上でも独立である。有限中心模型は幾何学的一般点でだけ必要で、Z×A15全体での一様な中心選択は仮定しない。

RSV Proposition2.1は、Noetherian整域の係数環R、有限型可換R代数C、C上有限で有限大域次元のAを入力とする。Cの正規性やA=End(M)というNCRの追加仮定は不要である。開上で得た有限相対対角解消では各項と対角AがR-flatなので、全syzygyもR-flatとなる。従って任意の体値へのテンソル後も完全であり、全幾何学的fiberに有限大域次元を与える。tailsの正確な次元3には、CCKMの中心正則商のRees補題、YZのbalanced双対、ChenのSerre消滅を別に用いる。

**torsion曲線と位数6の例。** p=2−b、q=−(2+b)、r=−6a、p−q=4により、T0はHesse elliptic schemeの開部分である。逆写像はa=−2r/[3(p−q)]、b=−2(p+q)/(p−q)。µ=(p³+q³+r³)/(pqr)で、境界のσは原点[1:−1:0]の下でP=[p:q:r]による平行移動。各E_µのtorsion点は稠密であり、E[n]∩T0の非空連結成分はsmooth integral affine曲線になる。相対[n]の微分はn倍で可逆、properかつ有限fiberなので有限étale。Z×A15の次元は16である。B_*は(a,b)=(1/3,0)、(p,q,r)=(2,−2,−2)でq³−r³=0となるため指定Δ開の外にある。B_*の位数6は `CSBGlem:gluing-order-six` の弦接線計算だけで証明でき、外部計算出力に依存しない。

#### 1.8.1 17次元一般点へ届く量子化の係数変換

代数的18係数橋渡し族の完全な証明は `kuznetsov_moduli_morphism.tex` の `prop:kuznetsov-algebraic-bridge` にある。以下は規格化を再開時に確認するための要点である。係数a,b,α,β,m_ij,g_jを代数的独立に取り、その函数体をKとする。既存 `central_pair_explicit_centers.tex` の一様な有限係数量子化をR=K[[h]]へ移すと、B_h/(h)=K[x,y,z,u,v]、中心三次w_hの還元は一般三次Fとなる。

Fの幾何学的smooth性には明示的な証人

\[
F_*=x^3+y^3+z^3+u x^2+u^3+v^3
\]

を使える。この17係数族に属し、偏微分の同時零点ではy=z=v=0、x(3x+2u)=0、x²+3u²=0。x=0ならu=0、x=−2u/3でも31u²/9=0となり、射影空間には特異点がない。射影Jacobian判別条件により一般Fは幾何学的に滑らか。これは代数的な計算による証明であり、計算コードの実行結果ではない。

Rainsの式への代入は

\[
q=\frac{2+hb}{2-hb},\quad t=\frac{6ha}{2-hb},\quad
\lambda=\frac b{3a},\quad
(L_1,L_2,L_3)=\frac{(2u,2\alpha v,2\beta(u+v))}{3a},
\quad \widetilde M_i=M_i/(3a).
\]

q=1+λtであり、分母q(q³−t³)(q+1)(1+t³)のh=0での値は2。active定数項0のRains中心G_t^Rはh=0で(F−g)/(3a)となるから、w_h=3aG_t^R+gはw_0=Fを満たす。

h≠0でu'=hu、v'=hvと置くと

\[
a'=ha,\quad b'=hb,\quad \alpha'=\alpha,\quad
\beta'=\beta,\quad m'_{ij}=h^{-1}m_{ij}.
\]

canonicalな未スケールRains中心を用い、三次関係を3aで割る規約ではg'_j=g_j/(3ah³)。中心を3a'倍する規約ではg'_j=h^−2g_jとなる。同じ三次直線を表すが、中心の規格化とgの変換を必ず同時に行う。前者の逆写像はa=a'/h、b=b'/h、m_ij=hm'_ij、g_j=3a'h²g'_j。C(h)上で可逆なので一般17係数の函数体はK((h))へ単射となり、atlasの一般点を与える。

橋渡し族は形式係数だけでなく、有限の分母を反転した被約な18次元係数環上に構成する。p_h=2−hb、q_h=2+hb、r_h=6haとし、d(h)=p_h q_h(q_h³−r_h³)(p_h³+r_h³)を用いるとd(0)=256。Mori–Smith Thm4.2(1)はh=0を含む全幾何学的ファイバーに適用できる。全fiberで一定のHilbert rankと被約性により、同じ基底上で全次数の射影性を得る。Rains中心の最高記号が非零であること、fiberの整域性、PBW、potentialの真正な自己双対から、普遍的中心正則性と相対CY/Koszul入力を得る。次数ごとの開集合を無限に交差しない。有限の対角解消・CYの詳細は現行論文へ集約する。

**橋渡しの開条件と量子楕円開の差。** h≠0で一致するのは17係数族の関係式である。指定Δ開およびétale chart開の逆像へはさらに制限する。この逆像は係数変換の支配性から非空であり、一般点を用いる残余射の証明には十分である。一方、d(h)≠0だけから量子楕円境界の滑らかさは従わない。実際、a=1/6、b=0ならp_h=q_h=2、r_h=hであり、境界の三係数は(p,q,r)=(2,−2,−h)となる。従って

\[
d(h)=256-4h^6,\qquad
D_E=(p^3+q^3+r^3)^3-(3pqr)^3=-h^3(h^6+1728).
\]

h⁶=−1728ではd(h)=7168≠0、a(27a³+b³)=1/48≠0だがD_E=0である。この例は追加の開条件を省略できないことを示す。SymPyでの再現は次の通りであり、両多項式の剰余を有理数上で検算できる。

```python
import sympy as s
h = s.symbols("h")
p, q, r = s.Integer(2), s.Integer(-2), -h
d = 4 * (8 - h**3) * (8 + h**3)
disc = s.expand((p**3 + q**3 + r**3)**3 - (3*p*q*r)**3)
assert s.rem(d, h**6 + 1728, h) == 7168
assert s.rem(disc, h**6 + 1728, h) == 0
```

#### 1.8.2 形式効果性・生成性・smoothness に対する反例

以下では \(k\) は体、\(R=k[[h]]\)、\(R_n=R/(h^n)\)（\(n\ge1\)）、\(K=k((h))\) とし、cohomological grading と右 dg 加群を用いる。`perfect` は有限 cell 加群の retract であることを意味する。underlying graded 加群が有限自由であることとは区別する。以下の三例は、それぞれの記載した仮定の下で反例となることを直接検証した。可換三次への射の証明は、これらが否定する一般原理を使用しない。

**(a) proper な dg 代数上の compact 加群の形式系は、一般には compact 加群として効果化できない。**

次の dg 代数と右 dg 加群を取る。

\[
 \Gamma_R=R\oplus R\varepsilon,
 \qquad |\varepsilon|=1,\quad\varepsilon^2=0,\quad d_\Gamma=0,
 \qquad M_R=(\Gamma_R,d_M),\quad d_M(1)=h\varepsilon,
 \quad d_M(\varepsilon)=0.
\]

\(\Gamma_R\) と \(M_R\) はともに \(R\)-perfect である。\(M_n=M_R\otimes_R R_n\)、\(\Gamma_n=\Gamma_R\otimes_R R_n\) と置くと、\((M_n)_n\) は互換的な形式系であり、**各 \(M_n\) は \(\Gamma_n\)-perfect だが、\(M_R\) は \(\Gamma_R\)-perfect ではない**。

各有限段階の perfectness を示す。\(C_n=R_n[t]\)、\(N_n=C_n/(t)\) とし、\(N_n\) の自由解消

\[
 P_n=[C_n\xrightarrow{t}C_n]
\]

を次数 \(-1,0\) に置く。スカラーを対角作用に、\(\varepsilon\) を次数一の写像 \(P_n^{-1}\to P_n^0\) の恒等行列に送る写像

\[
 \Gamma_n\longrightarrow\operatorname{End}_{C_n}(P_n)
\]

は dg 代数の quasi-isomorphism である。実際、右辺のコホモロジーは次数 \(0,1\) でそれぞれ \(R_n\)、他では零であり、この写像はその二つの生成元を与える。

\(L_n=C_n/(t+h)\) と置く。\(t+h\) は monic なので非零因子であり、\(L_n\in\operatorname{Perf}(C_n)\) である。\(C_n/(t^n)\) の \(t\)-進 filtration の各商は \(N_n\) だから

\[
 C_n/(t^n)\in\operatorname{thick}(N_n).
\]

\(L_n\) が perfect であることから、これを tensor する操作は

\[
 L_n\otimes_{C_n}^{\mathbf L}C_n/(t^n)
 \in\operatorname{thick}(C_n/(t^n))
 \subset\operatorname{thick}(N_n)
\]

を与える。左辺は \(t^n:L_n\to L_n\) の cone である。\(L_n\) 上で \(t=-h\) かつ \(h^n=0\) なので、この cone は \(L_n\oplus L_n[1]\) であり、retract を取って \(L_n\in\operatorname{thick}(N_n)\) を得る。

従って \(\mathbf R\operatorname{Hom}_{C_n}(N_n,L_n)\) は、\(N_n\) を \(\Gamma_n\) へ送る Hom 関手により \(\Gamma_n\)-perfect となる。これは次数 \(0,1\) の複体

\[
 [R_n\xrightarrow{h}R_n]
\]

であり、\(\varepsilon\) は次数零項から次数一項への恒等写像として作用する。符号については Hom 複体の微分が \(-t\) で、\(L_n\) 上では \(t=-h\) であることを使った。従って、この右 \(\Gamma_n\)-加群は指定した \(M_n\) そのものである。

一方、\(M_R\) が \(\Gamma_R\)-perfect だと仮定する。augmentation \(\Gamma_R\to R\) に沿って

\[
 Q=M_R\otimes_{\Gamma_R}^{\mathbf L}R
\]

を作ると \(Q\) は \(R\)-perfect である。特殊ファイバーでは \(M_R\otimes_R k=\Gamma_k\) なので \(Q\otimes_R^{\mathbf L}k\simeq k\) である。一般ファイバーでは \(M_R\otimes_RK=[K\xrightarrow{h}K]\simeq0\) なので \(Q\otimes_RK=0\) である。有限自由複体で表せる \(R\)-perfect 複体の Euler characteristic は特殊・一般ファイバーで等しいはずだが、ここではそれぞれ \(1,0\) となり、矛盾する。

別の compact 加群による同じ形式系の効果化も存在しない。もし \(Q'\in\operatorname{Perf}(\Gamma_R)\) が compatible な同型 \(Q'\otimes_R^{\mathbf L}R_n\simeq M_n\) を持てば、\(\Gamma_R\) の \(R\)-perfectness により \(Q'\) も \(R\)-perfect である。\(Q'\) と \(M_R\) は導来 \(h\)-完備なので、作用を含めて逆極限を取り

\[
 Q'\simeq\mathbf R\varprojlim_nM_n\simeq M_R
\]

となり、上の非 perfectness に反する。従って
\(\operatorname{Perf}(\Gamma_R)\to\varprojlim_n\operatorname{Perf}(\Gamma_n)\)
は essentially surjective ではない。\(\operatorname{Perf}(R)\) 自体についての形式効果性とは矛盾しない。

**(b) smooth proper な幾何的圏の中でも、与えた perfect 対象が generator である locus は一般に開ではない。**

\(Y=\mathbb P^1_k\times\mathbb A^1_k\) とし、第二因子の座標を \(h\) とする。\(p\in\mathbb P^1(k)\) を固定し、その点で消える切断 \(s\in H^0(\mathbb P^1,\mathcal O(1))\) を取る。次の余核で perfect な coherent sheaf \(\mathcal E\) を定める。

\[
 0\longrightarrow\mathcal O_Y
 \xrightarrow{(h,s)}\mathcal O_Y\oplus\mathcal O_Y(1)
 \longrightarrow\mathcal E\longrightarrow0.
\]

これは \(0\to\mathcal O_Y\to\mathcal E\to\mathcal O_{p\times\mathbb A^1}\to0\) も満たすので、\(\mathbb A^1\) 上平坦である。ファイバーは

\[
 \mathcal E_0\simeq\mathcal O\oplus k_p,
 \qquad \mathcal E_h\simeq\mathcal O(1)\quad(h\ne0)
\]

である。\(P=\mathcal E\oplus\mathcal O_Y(1)\) と置くと、\(P_0\) は \(\mathcal O\oplus\mathcal O(1)\) を直和因子に持つので \(\operatorname{Perf}(\mathbb P^1_k)\) の generator である。しかし \(h\ne0\) では \(P_h\simeq\mathcal O(1)^{\oplus2}\) となり、

\[
 \mathbf R\operatorname{Hom}_{\mathbb P^1}(\mathcal O(1),\mathcal O)
   =\mathbf R\Gamma(\mathbb P^1,\mathcal O(-1))=0
\]

なので generator でない。従って、特殊ファイバーで generator であることだけから一般ファイバーの生成性を推論できない。

**(c) 係数 perfect な proper dg 族に対する一般的な特殊 smoothness から一般 smoothness への推論は偽である。**

\(X=\mathbb P^1_R\)、\(G=\mathcal O_X\oplus\mathcal O_X(1)\)、\(p_R=p\times\operatorname{Spec}R\) と置き、

\[
 T=\operatorname{cone}(h:G\to G)\oplus\mathcal O_{p_R},
 \qquad E_R=\mathbf R\operatorname{End}_X(T)
\]

を取る。\(T\) は \(X\)-perfect で、\(X/R\) は smooth proper だから、\(E_R\) は \(R\)-perfect であり、任意の導来係数延長に沿う自己 Hom の比較が成立する。

特殊ファイバーは \(T_0\simeq G_0\oplus G_0[1]\oplus k_p\) なので generator であり、\(E_R\otimes_R^{\mathbf L}k\) は \(\operatorname{Perf}(\mathbb P^1_k)\) と Morita 同値で、dg smooth proper である。さらに **すべての有限段階** \(R_n\) でも \(T_n\) は generator である。実際、octahedral axiom により

\[
 \operatorname{cone}(h^n:G_n\to G_n)
 \in\operatorname{thick}\bigl(\operatorname{cone}(h:G_n\to G_n)\bigr).
\]

\(h^n=0\) なので左辺は \(G_n\oplus G_n[1]\) である。相対 Beilinson 解消により \(G_n\) は \(\operatorname{Perf}(\mathbb P^1_{R_n})\) を生成するため、

\[
 \operatorname{Perf}(E_R\otimes_R^{\mathbf L}R_n)
 \simeq\operatorname{Perf}(\mathbb P^1_{R_n})
\]

となる。

一般ファイバーでは \(h\) が可逆なので \(T_K\simeq k_{p_K}\) であり、

\[
 E_R\otimes_RK
 \simeq\mathbf R\operatorname{End}_{\mathbb P^1_K}(k_{p_K})
 \simeq K\oplus K\varepsilon,
 \qquad |\varepsilon|=1,\quad\varepsilon^2=0,
 \quad d=0.
\]

最後の dg 代数としての同値は、\(p_K\) を含む affine 座標 \(t\) 上の解消 \([K[t]\xrightarrow{t}K[t]]\) に対する (a) と同じ自己 Hom 計算で得られる。この exterior dg 代数 \(\Gamma_K\) は smooth ではない。実際、その augmentation 加群 \(K\) の半自由解消は

\[
 F=\bigoplus_{j\ge0}e_j\Gamma_K,
 \qquad |e_j|=0,\quad d(e_0)=0,\quad
 d(e_j)=e_{j-1}\varepsilon\ (j\ge1)
\]

で与えられる。\(e_0\) を \(1\)、他を零に送る augmentation の下で \(H^0(F)=K\)、\(H^1(F)=0\) であり、他の次数には項がない。\(j\) による filtration は半自由 filtration である。\(K\) と tensor すると微分が零になるため、

\[
 K\otimes_{K\oplus K\varepsilon}^{\mathbf L}K
 \simeq\bigoplus_{r\ge0}K
\]

となる。各 summand は次数零にある。従って右辺は \(K\)-perfect ではなく、augmentation 加群 \(K\) は exterior dg 代数上 perfect ではない。一方、smooth な dg \(K\)-代数では係数上 perfect な加群は perfect 対角の tensor 表示によりその代数上 perfect となるので、smoothness に矛盾する。

以上により、一般の係数 perfect な dg 代数についての含意

\[
 E_R\otimes_R^{\mathbf L}k\text{ が dg smooth}
 \quad\Longrightarrow\quad
 E_R\otimes_RK\text{ が dg smooth}
\]

は成立しない。全 Artin 切断が smooth proper な幾何的圏と Morita 同値であるという条件を追加しても、同じ例で成立しない。ここでは \(H^*(E_R)\) の \(R\)-平坦性を仮定しておらず、その平坦性を要求する別の命題まで否定してはいない。実際、この例の \(\operatorname{cone}(h:G\to G)\simeq G/hG\) の恒等射は、\(H^0(E_R)\) の非零の \(h\)-torsion 直和因子に属するので、コホモロジーの係数平坦性は成立しない。

**現在の証明が用いる追加構造。** `papers/sections/kuznetsov_moduli_morphism.tex` の `prop:kuznetsov-effective-serre-embedding` は、形式的 kernel をまず係数環 \(R\) 上の perfect 複体として効果化する。幾何的 target の smoothness から片側 perfectness を得るので、(a) の否定する \(\Gamma\)-perfect な効果性を仮定しない。生成性も (b) のような一般の開性からは導かず、相対 Serre 比較を効果化して像を target の Serre 関手で安定にし、`lem:kuznetsov-graded-thick-simple` の三次成分に固有の生成性を使う。一般ファイバーの非零性は別途 Euler pairing で保証する。

(c) の target \(\operatorname{Perf}(\mathbb P^1_K)\) には、非零で真の Serre 安定な thick 部分圏 \(\operatorname{thick}(k_{p_K})\) が存在する。実際、Serre 関手は \(-\otimes\mathcal O(-2)[1]\) なので \(k_{p_K}\) を \(k_{p_K}[1]\) へ送る。三次の Kuznetsov 成分について証明した「非零の Serre 安定な thick 部分圏は全体」という性質が、この例のような退化を排除する。したがって三つの反例は、現在の Serre 比較と三次成分の生成性を用いる証明に抵触しない。

文献の適用範囲も区別する。Toën–Vaquié Cor2.13/Prop2.14のsmooth proper⇒hfp⇒smoothを、hfp未証明の族へ適用しない。[Toën, Finitude homotopique…](https://www.math.univ-toulouse.fr/~btoen/dgalgsat.pdf), Lem3.14はbounded smooth部分前層のquasi-compactnessである。BKPのcompact generatorの形式変形定理は通常の包絡代数上の対角perfectnessを無条件に与えない。一方、BKP §3.3に記載されたLurieの比較は§10.1で対象を指定して使用する。

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
2. CFTのKontsevich公式に nilpotent Artin係数を代入する。固定する可換積は周囲の多項式環R[x_0,…,x_4]の積であり、三次の可換変形は変動するF_tに保持する。基礎加群は自由、グラフの次数計算で積は同次、twisted chain identityでCasimir F_t が中心三次元wへ持ち上がる。関係核のNakayamaからBは二次、wの乗法のunit minorからA=B/(w)も平坦。
3. 実際のOre局所化が Ψ:h_T→D_Ass を与える。T=C[[t_1,…,t_10,a_ij]]/(Pfaffian_4(a))。相対Poisson計算とYekutieli Cor11.2により標的も同じTでprorepresentされる。ここでPoisson側の可換代数層の積も変形を許し、両側を同じ完備局所環で表す。これは単なるhullや接次元の比較ではない。
4. Ψの接写像が零なら、一次交換子からa=0となる。その場合は星積が通常の積に戻り、商は実際の可換三次変形F_t=0だからt=0。接空間はいずれも20次元なので同型となる。標的の表現環との同型を一つ選ぶとΨはTの連続自己準同型を与える。余接空間上の可逆性と次数一生成性から各有限次元随伴次数上で同型となり、完備性・分離性から自己同型になる。異なる特異環の接次元が等しいだけではこの結論を得られない。
5. Lowenのalgebroid模型とH¹,H²(O)=0による中立化で、全Abel変形を通常の代数層変形へ移す。中心商の局所化次数部分E_nはO_X(n)の持上げなので、個々の持上げの一意性とsection回復から b≅check A、Q(b)≅check B を得る。

同次代数変形の全gauge分類は証明の前提ではない。CFTによる具体的な族の構成と、Yekutieliによる標的関手の同定を分ける。前者は `lem:artin-homogeneous-casimir-quantization`、相対Poisson環は `lem:artin-relative-poisson-sheaf`、実際のΨの比較は `lem:artin-constructed-family-comparison` に証明を置く。量子化座標の選択は非標準的でも、内在的なb→Q(b)は任意の係数変更に自然である。各O(i)の持上げを同定する段階で、shift自己同値の持上げを仮定しない。

**係数環と引用の射程。** CFT §3 Theorem3.1の多重線型恒等式とProposition3.3直後の普遍多項式性により、極大イデアルに入る係数を代入した和は有限になる。従って一変数の形式パラメータに限らず、任意の局所Artin C-代数とその任意の準同型に自然である。F_tも同じ係数変更で動くため、固定ambientの星積を使っても十次元の三次変形方向は失われない。Yekutieli Cor11.2はH¹(O_X)=H²(O_X)=0の下で可換積も変形するPoisson/Ass代数層のgauge同値類を比較し、係数準同型への自然性を保証する。固定層上のbracket/star productを扱うCor11.3のH¹(T_X)=0は使わない。Lowen Thms3.14/3.26への適用では、Xの分離性から有限アフィン被覆の交叉もアフィンとなることと、準連接層の制限が局所化であることを用いる。

CFTの規約ではα=Π/2を代入し、一次交換子をΠに規格化する。中心性の逆向きが必要な補助補題では、D⁰の三次部分と、四次係数ベクトル場のD¹を生成元で評価する写像が還元恒等の有限自由行列であることを使う。中心の非平坦底変更を仮定しない。

**範囲。** 全平坦Abel Artin変形は、任意の係数変更後にも飽和・復元・相対AS条件を満たす標準相対模型を持つ。標準模型と全Abel変形の比較に加え、§5.6で全stack化後のArtin対象の大域模型も構成した。固定圏の内部の降下と区別して証明しており、一般の圏2降下を仮定していない。

### 5.4 形式局所環、ambient写像、P4との区別

構造対象付きAbel変形の同型類関手はTで表され、Krull次元17、接空間20。さらに§5.6のframed自己同型消滅により、全stack化後のframed群oid自体が離散なSpf Tと同値である。特殊ファイバーの有限Aut(X)は割らない。中心対の射影生成基底を残すとformal PGL5の24次元torsorになり、次元41・接空間44。証明は `cor:abel-cubic-formal-ring` と `thm:artin-central-pair`。H⁰(T_X)=0により、cubic側には標識を保つ形式的PGL stabilizerが残らない。

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

### 5.6 全stack化後の大域Artin模型と離散形式近傍

証明は `abel_formal_descent.tex`。主要な結論は `thm:abel-stackified-relative-formal` と `cor:abel-full-stack-discrete-formal` である。

**結論。** Xを固定した滑らかな複素三次三様体とし、特殊ファイバーへの同一視を保つ射を使う。定義したO-marked fpqc stackのArtin形式群oidは、全平坦Abel変形の群oidと同値であり、さらに

\[
\widehat{\mathfrak M}^{O}_{\mathrm{cub},X}
\simeq\operatorname{Spf}
\frac{\mathbb C[[t_1,\ldots,t_{10},a_{ij}\ (0\le i<j\le4)]]}
{(a_{ij}a_{kl}-a_{ik}a_{jl}+a_{il}a_{jk}\mid i<j<k<l)}
\]

と群oid値関手として同定される。座標同定は非標準的である。全ての構造対象付き完全同値を含めた結果であり、豊富列保存の射へ制限した結果ではない。

**任意の平坦被覆上での局所模型。** RをArtin、mを極大イデアル、Sを任意の平坦R代数、Q=S/mSとする。S自体はArtin・noetherian・coherentとは限らない。元のR→Cに対する変形としてDの特殊圏QCoh(X_Q)をC線型圏と見る。DDL Thm4.5はHomのC有限次元性や圏のnoetherian性を要求しないため、O(-i)をR-flatに持ち上げられる。局所tails圏のR-flatnessは、R-flatなHomを持つ線型圏のGabriel商がflatであることから直接示す。

section Homの還元はQの有限自由加群である。基底を持ち上げたS^h→Homは、両側のR-flatnessと有限m-filtrationの全商の比較によって同型になる。ここでR上の有限生成性を誤って使わない。その後、S-freeなrepresentableのexact S-linear Gabriel商としてE_iのS-flatnessを得る。この順序なら、平坦性と有限自由性を循環して仮定しない。

任意のS加群Mに対するHom比較とExt¹消滅は、有限mS-filtrationの商を使う。Q上の係数Mについては、Xの有限affine Čech複体をM⊗_C−で計算するため、MのQ-flatnessは不要である。有限表示性にはLVdB Prop4.7の双対版による全次数Ext還元とfiltered colimitを使う。詳細は `lem:abel-flat-cover-reconstruction`。対角EndはSであり、還元frameを保つ線対象の自己同型は正確に1+mSとなる。

**降下の核心。** ξを全stackのR対象とし、還元frameを固定する。ある忠実平坦R→S上で局所模型Dを選ぶ。既存のHom降下でoverlap上の射と特殊ファイバーのframeを実際の同値に実現できる。O-marked 2慣性の自明性からassociatorは一意で、pentagonも成立する。

各E_iのoverlap比較を選ぶと、三重交叉でのずれc_iは1+m S^(⊗3)に入る。有限log/expはこの余単体群をm⊗_R S^(⊗•)に移す。拡大Amitsur複体の完全性（Stacks023M）でc_iを一次cochainのcoboundaryに書き、比較同型を補正する。E_0=Oの既存降下は変更しない。全iに同じ被覆を用い、無限積の群のquasi-coherenceや一斉有限表示自明化を仮定しない。

補正後にHomと合成だけを通常の加群降下で貼り合わせ、有限自由R線型Z代数bを得る。b⊗C=check A_Xであり、Qmod(b)はDDLにより全Abel Artin変形となる。それから既存の平坦二次包絡・普遍的三次条件を適用するので、新しく持ち上げた局所列の三次性を先取りしていない。H(M)_i=Hom(E_i,M)の成分ごとの自然性により、復元同値は元のactual transitionまで再現する。これは単に各局所圏の同値類が一致するという主張より強い。

**Framed自己同値の消滅。** `lem:abel-cubic-section-derivations` は、a=check(Sym(V)/(F))の全頂点固定導分が λ_i−λ_j による内的導分で、λ_0=0と取れることを示す。二次関係は隣接成分D_i−D_(i+1)をscalarに制限する。頂点scalarを除いた一様MにはD_M(F)∈CFが課される。Euler導分を差し引くと五つの二次偏微分の一次係数syzygyとなるが、Fがsmoothなので偏微分は正則列であり、そのようなsyzygyは零である。

小拡大R→R/J、mJ=0について、還元上のmarked自然同型に各線対象の同定を単元持上げで合わせる。section自己同型の差はJ値の上記導分なので内的に消せ、Hの自然性で全圏へ延長する。λ_0=0によりOの標識を保つ。この帰納が `prop:abel-framed-artin-automorphisms`。線対象の持上げには1+mの自己同型があるが、圏のframed自己同値の自然同型類は自明になる、という違いを保持する。

**具体的障害。** a_01=a_23=ε、他のaとtは零とすれば双対数上の変形があるが、ε³=0への持上げのPf_0123はε²となる。従ってこの一次方向は二次で障害を持つ。五つの独立な二次関係と余次元3から形式環は完全交叉ではない。証明は `rem:abel-formal-quadratic-obstruction`。

**適用境界と再発防止。** S→Qにcoherent基底の変形定理を直接適用しない。GmのH²消滅を無条件に仮定せず、実際のband 1+mを固定被覆のAmitsur複体で扱う。持上げの同型類の一意性だけでcocycleを済ませない。固定模型の内部降下だけで圏の2降下を宣言しない。全stack比較後にも、無標識Aut(X)、一般非可換点、代数化、有限型atlasは別である。既知一般定理のこの具体的適用の初出は未確認。

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
- Cassidy–Conner–Kirkman–Moore, J. Algebra455 (2016), 137–163, DOI 10.1016/j.jalgebra.2016.01.037, [arXiv:1307.8415v1](https://arxiv.org/abs/1307.8415v1)。Reesはv1 Lemma4.4(3)、graded twisted MF↔stable MCM↔D_sgはv1 Theorems4.7/5.5、公刊Theorem5.8。公刊4.4は別内容。左右noetherianなBとregular normal Gなら適用可能で、有限位数・中心性・tails smoothnessは不要。左加群の規約は反対環に適用して右加群へ移す。
- Orlov [arXiv:math/0503632v3](https://arxiv.org/abs/math/0503632v3), Definition2.1・Remark2.2・Theorem2.5(i)。connected graded noetherian、左右AS Gorensteinでparameter2なら二線対象とD_sgによる分解を得る。pd_A k=∞より特異圏は非零。Kuznetsov [arXiv:1509.07657v2](https://arxiv.org/abs/1509.07657v2), Corollary4.1で可換cubicのS³=[5]を確認し、[arXiv:0904.4330v1](https://arxiv.org/abs/0904.4330v1), Corollary7.5・Theorem8.3でHHの加法性とHKRを用いる。

**成分判定に必要な反例。** 2511.08390v1のProposition5.1/Theorem5.8で用いられる「整な部分多様体への接空間同型なら成分になる」という一般判定は、述べられたままでは成立しない。Y=A²、Z=V(y²−x³)、z=(0,0)とすると、Zは整でT_z Z→T_z Yは同型だがZはYの成分でない。接層のfiberとZariski接空間を同一視できない点が障害である。Zがその点で滑らかである等の追加条件なら通常の局所次元比較で修復できるが、各具体的な族への適用は別途確認を要する。この反例は同preprintの個々の族の結論を一律に否定するものではない。本研究の成分証明では、実際の像の次元と全ambient接空間の次元をそれぞれ独立に確保する。

## 8. 成分・像・次元の範囲

poisson-p4の参照mainはf118dfbfc5bb9b7a394d1985b4800b6228eebaf6。smooth cubic上のPoissonはJacobian P(F,L,M)へ一意延長し、ambient固定fiberはF+g(L,M)、二元三次gのA4開。これは既存入力を証明再掲したもの。

全Poisson微分Mは375×150、源の微分Sは150×37。整数MS=0とmod1000003の非零minor（M113=844194、S37=948131）で全接空間37を証明する。37次元既約像が通るのでRat113錐は全Poissonスキームの一般正則成分。全147分類や有限体での零の推論は使わない。

Pymのscheme/formal germ比較と実際のQmod比較により、Q113は射影基底付きAbel/Z形式模型の37次元成分でもある。頂点完備化が整域であることは斉次最低項の積で示し、一般正則性にはexcellenceを使う。中心三次incidenceの支配的成分の射影閉包を取り、可換ambientの全fiberに沿って完備化すると、flat base changeとformal functionsにより像の形式閉包はこの成分全体となる。特定の一点Fの完備化だけの支配性とは異なる。

閉包に現れる全特殊cubicは可換多項式環で非零正則なので、Artin持上げでも各乗法のunit minorから正則性と商の自由性が従う。この完備incidenceは正規三次型のモジュライへ写る。実際のJacobian成分では§10によりdg smooth properな非空開を得たので、その17→13の像はambientの非空開を含む。任意の形式incidenceや全AS成分について同じ結論を主張しない。

一般中心はk[a,b,c]、重み(1,1,3)。中心3次5次元からfiberP4、ambient37・incidence41、PGL軌道24を引いて13・17。GL商stackは共通Gmの慣性のため12・16。Poissonスカラー射影化では36。可換cubic忘却fiber7=6 moving plane+1 Poisson scaleと、ambient忘却fiber4を混同しない。

## 9. 保持する既存成果と次の技術的入口

17係数sliceの31次整数行列式−5538243375000、分離型余次元15、可換cubic忘却核7、全混合中心、相対Picard障害、偶数Veronese、構造対象を保つ導来復元、固定剛体ambientの4係数族と有限位数境界は現行原稿に保持する。完全な証明は重複しない。

可換点の二次包絡平坦性・任意係数飽和・全stack化後のframed形式群oidは§5で完成した。一般17係数族の相対Serre・全Hom比較も明示Δ開上で§1.6に完成した。代数的部分モジュライと相対二次包絡射は§1.7で構成した。相対smooth properな16次元族とその稠密性は§1.8で完成した。§10の残余射により17次元の非空開上のdg smooth proper性と可換三次への17→10射も完成した。全Abel形式近傍の残余射とPoisson形式fiberも§10.3で完成した。point schemeからambient Poisson直線とCasimir空間を復元する部分は§10.7で完成した。次は量子中心に対応する特定のCasimir直線、ρとの両立、一般fiberの接合データ、全Mとの局所比較を扱う。有限中心の局所対角の証明を無限位数の楕円境界へ無条件に転用しない。P3のrank6模型の全分類や全AS5許容関手の代数性を前提にしない。

文献上の範囲：Sierraの厳密twist比較、AOUのAS3での内部O(n)認識、Behrend–Noohiの切断stackは一次資料を確認。AOUの裸のqgr復元をAS5/cubicへ無証明で一般化しない。新しい主張の初出・優先権と、保持した全旧証明の独立全面監査は未完了。実施した計算・組版・証明監査はvalidation.jsonで区別する。

## 10. Kuznetsov残余射とPoissonモジュライ

### 10.1 全Artin基底上の幾何的認識

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

**全Artin認識。** `prop:kuznetsov-formal-recognition` は任意のk/Cと通常の局所Artin k-代数Tについて、幾何的Def_X(T)と実際のcompactly generated dg圏変形のπ0を同定する。proper compact圏はLurie DAG X Definition5.3.20のtame条件を満たす。Proposition5.3.21/Theorem5.1.9により実変形から形式hullへの射は(−1)-truncatedであり、π0上単射、各点のπ_i（i≥1）上同型である。Theorem5.3.16とHH[1]の極小L∞模型を用いると、コホモロジーが次数−1,1のみなので高次演算は次数の偶奇から全て零となる。hullのπ0は十次元形式円板であり、JLLZの実際の接写像と形式逆写像定理から幾何的変形がこれを尽くす。

**高次スカラーを保持する範囲。** 各Artin点でπ1=0だが、π₂≃HH⁰(K)⊗_k m_T≃(m_T,+)が残る。標数零の有限log/expにより、これは乗法群1+m_Tと同定される。従って同定するのは通常Artin基底上のπ0であり、圏の変形空間全体を離散群oidと同一視しない。§5.6のO-marked Abel形式群oidの離散性は、自然同型類を射とした1群oidについて別に証明する結果である。

### 10.2 実際の17係数族：相対構成、効果化、開上への降下

**相対残余圏。** `kuznetsov_relative_category.tex` では任意係数上で二例外対象O,O(1)を取り、P=L_O L_O(1)により残余圏Kを構成する。O(1)に基底直線束をtensorしても評価が相殺するので、残余圏は全O-marked Abel同値に自然で、C_Jへ降下する。両側随伴とenriched相対Serreも構成する。generatorはG=P(O(2)⊕O(3)⊕O(4))。G2=P(O(2))に対しχ(G2,G2)=−9、G自身にはχ(G,G)=−2925であり、すべての体fiberの非零性が従う。全tailsがsmoothであることとKがsmoothであることは、相対Kronecker5成分とのgluingから同値である。

**Hilbert関数とEuler数。** h_n=dim A_nはn<0で零となるが、χ(O(i),O(j))をこの零延長で計算してはならない。d=j−i≥0ならχ=h_d、d=−1なら零、d≤−2なら線コホモロジーの双対性からχ=−h_(−d−2)である。例えばχ(O(2),O)=−1が上の−9に必要となる。整数Euler行列と証明は `lem:relative-kuznetsov-nonzero-euler` に置く。

**効果化の順序。** `prop:kuznetsov-effective-serre-embedding` でR=k[[h]]、R-perfect E、相対dg/enriched Serre、特殊fiber Ku(X0)を仮定する。全Artin認識で互換的な三次X_nとMorita kernel P_nを得る。三次方程式はX_Rへ効果化できる。Bhatt Lem4.2によってP_nのunderlying係数perfect複体をPへ効果化し、導来完備なEnd_R(P)への作用写像を極限で効果化する。まだ包絡代数上のcompact性は主張しない。target D=End(Ku(X_R)のgenerator)がsmoothなので右D-perfect性が従う。E→End_D(P)のconeは係数perfectかつ特殊fiberで零だから、Nakayamaにより完全忠実なΦ:Perf E→Ku(X_R)を得る。

**Serre安定性と全射性。** 完全忠実性と両側のenriched Serre双対から、sourceのNの関手RHom_D(ΦN,S_DΦM)がRHom_C(N,S_CM)で表される。N=S_CMで恒等射に対応する射を取り、dg/enriched Yonedaにより自然変換α_M:ΦS_CM→S_DΦMを構成する。この段階ではS_DΦMがΦの像に入ることを仮定せず、source上の関手の表現性だけを使う。特殊fiberでα_Mは同型であり、そのconeはD-perfect、従って係数perfectなので、導来Nakayamaにより全体で同型となる。この順序で像のSerre安定性を得る。一般fiberの像の両側Serre安定性はgenerator EとS_C^{-1}Eで確認すれば足り、全generic対象の持上げは不要である。

`lem:kuznetsov-graded-thick-simple` は滑らかな三次XのKu(X)の非零Serre安定thick部分圏が全体であることを証明する。R_f=k[x₀,…,x₄]/(f)とし、Stevenson Thm3.1(3)・Notation3.2でKar D_sg(R_f)=S(R_f)^cと同定する。Thm6.13は全localizing部分圏を分類するので、孤立特異点の場合に非零compact対象MはLoc(M)=S(R_f)を満たし、Neeman Lem2.2からthick(M)=S(R_f)^cとなる。Orlov math/0302304v2 Thm3.9がungraded MFへの橋である。k[t]→k[x], t↦fのtorsion-free性から平坦性を確認する。graded側にはGF(P)=⊕P(a)で戻し、有限階数MFのcompact性から有限thick生成を得る。graded Orlov比較とrotation R=S[−1]によりSerre安定性が全内部次数シフト安定性になる。これは既知の分類・比較定理から導く補題として位置付け、独立の分類原理の新規性は主張しない。Euler−9による非零性と合わせ、generic ΦはMorita同値である。一般(FS)やgeneratorの開性は使わない。

**17係数一般点と開集合。** §1.8.1の代数的橋渡しと函数体単射を用い、実際の17次元atlasの一般点が体拡大後に幾何的Kuとなる。まずsmooth性を体降下し、perfectな同値核・逆核・unit・counitを有限生成部分環へ降ろす。その閉点から有限拡大K'/Kを取り、標数零で有限étale被覆へ広げる。TV Lem2.10の連続性と係数perfect coneの消滅により、非空開の被覆上で相対Morita同値を得る。

BMMS Thm1.1のcategorical Torelliにより二重交差上の三次の粗モジュライ値は幾何点ごとに一致する。二重交差は被約、targetは分離的なので射として一致し、étale降下する。同じ議論をatlasのgroupoidにも適用して、C_Jの非空開U上のρ:U→M_cubを得る。複素数上のTorelliの拡大体版は有限生成被約C代数へのspreadingで確認する。

**支配性と七次元。** 17係数の古典FとGL5軌道の微分は35×42行列である。`verify_commutative_dominance.py` は35次minor=752849 mod1000003と整数Euler関係を確認する。一般Fはsmoothであり、古典族はM_cubを支配する。ρの像の閉包はh-adic三次族のgeneric値を含むのでspecial値[V(F)]も含む。従ってρは支配的である。自己同型が自明な非空開M_cub°へ移り、generic smoothnessでsourceを縮めると、ある非空開Vへの相対次元7の滑らかな全射となる。相対Kuと全tailsのdg smooth proper性は任意導来底変更に両立する。

**境界。** 三次族・相対Morita核はétale局所で得る。大域の核、全Mの代数性・開性、全17係数点での幾何性、ρの出力が入力Fそのものであることは主張しない。自己同型が自明なtargetでは粗モジュライと三次モジュライstackが一致するため、ρはstackへの射でもある。targetの普遍三次族のambient B→Vは、三次因子Dに対してω_B/V(2D)がfiberwise O(1)となるので、実際に射影束へ分裂する（`prop:relative-poisson-cubic-cone`）。Zariski局所で射影座標を選べる。source上のO(1)の大域降下とは別の結論である。

### 10.3 全Abel残余射とPoisson形式近傍

**全Abel Artin近傍上の残余射は証明済み。** `prop:abel-artin-actual-residual` は、滑らかな可換三次Xのframed変形に対し、r:Def_ab^O(Qcoh X)→Def_Xを構成する。入力は次の通りであり、詳細な証明は `poisson_cubic_lifts.tex` に置く。

1. `thm:abel-cubic-flat-envelope(iii)` による通常の中心商A_R=B_R/(w_R)の表示。全Abel模型に存在するため、非周期的Z代数表示を直接扱う必要はない。
2. `cor:abel-universal-relative-cubic` の有限Koszul解消と、CY orientationを使わない `lem:relative-koszul-torsion-model`。非有界Gabriel商の同定にはπの完全性とωのK-injective保存を用いる。これとは別に、`lem:relative-cubic-torsion-comparison` のTor₁遷移消滅からA側の導来torsionを有限幅のB側模型で計算する。右加群の左随伴は−⊗_B^L Aであり、保守的な右随伴から五線compact generatorを得る。
3. `prop:artin-ore-universal-cohomology` の係数perfect Homと任意導来底変更。二例外対象の有限左mutationで残余K_Rと係数perfectなEnd(G_R)を得る。右随伴・相対Serre・source smoothnessはこの構成に不要。
4. O_X(1)の平坦持上げの同型類の一意性。比較のスカラーは評価で相殺し、全framed O保存同値に自然となる。Ind K_Rの指定Morita framingが `prop:kuznetsov-formal-recognition` の実変形の仮定を満たす。可換変形上でrはその三次自身を返す。

**rに両立する形式同型。** A₀=C[[a_ij]]/(Pfaff₄(a))、R_X=A₀[[s₁,…,s₁₀]]とする。既存量子化比較Q:Poisson形式近傍→全Abel形式近傍を一つ選び、rQをt=f(s,a)と書く。可換部分でf(s,0)=sなので、Θ(s,a)=(f(s,a),a)は特異な係数環A₀上でも形式自己同型となる。`cor:abel-poisson-formal-lift` の同型はΘQ⁻¹であり、rとPoisson忘却に両立し可換部分で恒等である。

従ってrの形式fiberはGr(2,5)のアフィンPlücker錐の頂点完備化で、次元7・頂点接空間10。ここでは特殊fiberのframeを固定し、自然同型で割った1群oidを用いる。元のQ⁻¹そのもののrとの両立、選択した形式同型の代数化・収束、有限Aut(X)作用や未切断2-stackは結論していない。形式的な幾何座標f(s,a)は高次補正を含み得る。

### 10.4 7方向と4方向、rotationと接合

二次包絡の一般17→13のfiber4は、固定B内の中心三次直線の選択である。実際の残余射17→10は非空開上で滑らかな七次元fiberを持つ。可換点におけるrの形式fiberは§10.3のPlücker錐であるが、一般の代数的fiberが同じ錐と双有理とは未証明である。7方向と4方向は異なる自由度であり、ρが固定ambientの四次元torsor上で定数であるかも未確認である。

可換cubicではrotation R_rotとSerre関手Sについて R_rot^3=[2], S=R_rot^{-2}[3]、従ってR_rot=S[-1]である。参照はKuznetsov, Calabi–Yau and fractional Calabi–Yau categories, §3.3, Corollary3.18, Lemma3.19であり、Corollary4.1の分数CY等式S³=[5]だけからrotationの同定を推論しない。同じ二つの式が成立する中心CY三次商に対し、rotationを追加しただけで7方向を回復することは期待できない。一般正規商にnormal automorphismのtwistがある場合は、この式の適用を別に調べる。

[Feyzbakhsh–Liu–Zhang, Theorems 1.1/6.2 and 1.2/7.1] は可換del Pezzo三様体について、Q_X=ker(H^0(O_X(1))⊗O_X→O_X(1))、E_X=i^!Q_X∈Ku(X)というgluing objectを使うBrill–Noether復元と特徴づけを与える。これは接合データを調べる具体的入口となる。本研究の非可換7方向をE_X一個だけで記述できるとは未確認であり、例外pair側の5矢Kronecker圏と残余圏の接合双加群全体を候補とする。

### 10.5 Poisson一次方向の消失：既知結果からの推論

通常HKRで HH^2(X)=H^1(T_X)⊕H^0(∧^2T_X)、各直和因子の次元は10である。JLLZ Theorem 3.11のsqrt(td)補正HKRを用いた可換図式では、bivectorがH^1(Ω_X^2)に作用する先はH^1(O_X)=0である。γが単射なので、補正HKRでのbivector方向はHH^2(K)への制限で消える。

通常HKRへ戻す際、bivectorのH^1(T_X)方向へのTodd補正はc_1(T_X)とのcontractionの定数倍である。[Hitchin, §5.3, pp.41–42] のcanonical bundleのPoisson module構造により、各Poisson bivector πについて π⌟c_1(T_X)=0。H^2(O_X)方向への補正もFanoの消滅で零である。Poisson cone Gr(2,5)が全bivector空間を線形に張るので、全bivector方向でも補正の影響は零となる。従ってこの一次の消失は通常HKRでも読める。

これは文献の定理と上記contractionからの推論である。§10.2の実際の17係数残余射とは別に、可換点の全Abel形式近傍の接写像を調べる入力である。また§10.3の積分解には、この一次核の同定自体は必要なく、幾何的s方向の可逆性だけを使う。

### 10.6 実際のPoisson持上げと内在的復元の障害

`prop:relative-poisson-cubic-cone` は自己同型のない可換三次の開モジュライV上で、相対Poisson錐P→VがZariski局所的にGr(2,5)のアフィン錐との積になることを示す。Mayanskiy §2.2のSchouten式と、五つの∂_iFが張る写像の局所分裂単射性を用いるため、非被約底変更を含むschemeとしての同定である。非零部分P×は相対次元7、a₀₁≠0のchartはA⁶×G_m。Poissonの尺度を記憶したモジュライは17次元、射影化したものは16次元となる。

`thm:noncanonical-poisson-cubic-lift` はK=C(V)⊂L=C(C_J)の相対超越基底t₁,…,t₇を選び、上のchartの六座標と尺度へ割り当てる。極とt₇=0を除く不変開で、ρに両立する支配的な射が商stackそのものへ降下する。函数体拡大は有限分離で、17次元scheme atlasからの合成は縮小後étale。sourceの有限慣性を除くとは主張せず、射のrepresentability、全体の有限性、次数1、双有理性は結論しない。選択後の射は全O保存同値と底変更に両立するが、非可換構造から指定されたPoisson構造を抽出したものではない。

**量子中心の同定。** 二次関係がΛ²V→Sym²Vのgraphとなる開では、ambientの二次双ベクトルΠをGL(V)-同変に読み取れる。Jacobian成分でΠはPoissonである。しかし中心三次wを古典Casimirへ対応させる操作は別に必要である。

`prop:poisson-naive-symmetrization-fails` はu,v中心、[x,y]=h z²,[y,z]=h x²,[z,x]=h y²のFermat族で、中心元w=f−h²T/9+u³+v³の対称化逆像H=f−2h²xyz/3+u³+v³が失敗することを示す。{x,H}=−2h³x(z³−y³)/3は(H)に入らず、u≠0の射影chartでもH/u³がv/uについてmonicなので失敗が残る。一般のHは滑らかである。中心性は現行の明示公式 `thm:pair-full-fermat-center` に依存し、新たな中心の数値検算ではない。反例の詳細証明は論文に置き、ここでは障害を保持する。

中心規格化の自由度も残る。現行の記法ではRains型と選択したFermat中心の差は
\[
G_h^{\mathrm R}-W_h=
\frac{h^2}{12}L_1L_2L_3+
\frac{h^3}{6}(L_1m_1-L_2m_2+L_3m_3)
\]
である。binary cubicの加算を含むこの変換則を無視して入力Fを復元すると、座標変更に対する同変性を失い得る。補正した中心対応の構成と、その出力がKuのρに一致することが次の核心である。反例はこの補正の不存在を示していない。

**文献の射程。** Pym Theorem 2.3のArtin近似による解析芽同型は、元のKontsevich形式同型とは異なり得る。Proposition 2.9/Theorem 2.10は規格化Koszul CY芽とunimodular Poisson錐の局所比較・成分の全単射である。Yekutieli Cor11.2は完備局所parameter algebra上のgauge同値類を比較し、可換積の変形も許す。固定層上のbracket/star productを扱うCor11.3にはH¹(T_X)=H¹(D_X)=0も必要で、h¹(T_X)=10の三次には直接適用しない。これらの定理の結論には、一般非可換点での標準的な代数的逆量子化、量子中心と古典Casimirの同変対応、指定したρとの両立は含まれていない。

### 10.7 Point scheme、零点scheme、Poisson構造の復元

詳細な証明は `papers/sections/point_scheme_poisson.tex` に統合した。以下は研究を再開するための入力・境界・未解決箇所であり、証明全文は重複させない。

**一次持上げ。** R=k[ε]/ε²、B_Rが平坦な二次変形、[x_i,x_j]=εq̃_ij、Π=Σq_ij∂_i∧∂_jがPoisson、w_εが中心三次、X=V(F) smoothという仮定の下で、M(p)が平坦な点加群へ持ち上がることとπ_X(p)=0は同値（`prop:first-order-point-poisson-zero`）。任意の非被約Tでも、局所的な持上げ可能点の部分関手はZ(π_X)で表される。持上げそのもののモジュライ、一意性、全次数への持上げとは異なる。

作用係数をa_n=p+εb_nとするとq(p)=p∧(b_{n+1}−b_n)。projective零点はΠ(p)=0というaffine条件より弱い。十分性にはa_n=p+ε(b+nc)を用い、中心三次の作用をε(dF(b)+(n+1)dF(c)+G(p))と計算する。中心性とEulerからdF(c)=0、smoothnessからdF(b)=−G(p)を解く。一次結合性だけでJacobiを結論しない。特異Xでは、w=x³+εy³、p=[0:1]がπ=0なのに持ち上がらない反例になる。

**古典・量子のscheme構造。** X=V(F) smooth、E=X∩{u=v=0} smooth、α=vdu−udvに対応するπについて
\[
Z(\pi)=E\amalg D,\quad D=V(F,F_x,F_y,F_z),\quad \operatorname{length}D=24.
\]
これは一般点だけの主張ではない。Gauss写像の有限性とpencilのBertiniによりDは有限、正則列から型(2,2,2,3)となる。一般Dは被約で、明示例F=Σx³/3−u²(x+4y+16z)+u³+v³は24個の相異なるLefschetz臨界値を与える。

量子側ではu,v中心、[y,z]=h sym(F_x)と巡回関係、境界対応が固定点なしの滑らかな楕円graph、中心三次wがその点加群を消すという仮定の下で
\[
\operatorname{Pt}(B)=E_h\amalg C,\quad C=V(F_x,F_y,F_z),
\qquad\operatorname{Pt}(B/(w))=E_h\amalg D_w,
\quad D_w=V(F_x,F_y,F_z,w_{\rm ab}).
\]
Cは次数8の完全交叉曲線、真の三次切断D_wは長さ24である（`prop:central-two-point-scheme`）。shiftはE_h上のσ、CとD_w上ではid。中心座標が単元のchartと非対角minorが単元のchartで証明するため、nilpotentも含む。全O保存同値への自然性は既存のEq_O=Isom_gr/Gmを使う帰結であり、一般Abel圏で点対象を新たに内在認識したわけではない。

**shiftを付けた有限係数の復元。** Γ_A=Γ_σ⊔Δ_D⊂P⁴×P⁴について
\[
H^0(I_{\Gamma_A}(1,1))=R_B
\]
を証明した（`prop:point-correspondence-quadratic-recovery`）。対角Dで消えるtensorはAlt²V⊕sym(Q)の13次元。中央二変数を含むantisymmetric部分7次元を除くと6次元候補となり、楕円graphの全bilinear kernelが3次元であることから残るkernelが正確にSklyaninの3関係となる。後者はdeg3線束L,Mの乗法H⁰(L)⊗H⁰(M)→H⁰(LM)の全射性で証明する。L≠Mはpencil trick、L=Mは平面三次に二次関係がないことを使う。

従ってpoint schemeとshiftから二次包絡Bそのものを復元する。skew/symmetric graph開で[x_i,x_j]=sym(q_ij)のq_ijを一意に読み、Π_fin=Σq_ij∂i∧∂j=hΠ_Fを尺度込みで得る。GL同変で全O保存同値に自然、相対版も線束コホモロジーの底変更とunit minorにより成立する。non-ST条件はこのshift付き復元には不要で、下のbare scheme復元にだけ必要。有限σのlogを取らずに尺度が得られる点が有用である。Π_finと、指定経路でhを除いた半古典Π_Fを区別する。

**有限点データからの肯定的復元。** 埋込みschemeからU=I(E_h)_1、W=ann(U)、Q=I(D_w)_2を取る。完全交叉によりQ=〈F_x,F_y,F_z〉。古典境界f₃=Σx³/3+λxyzに対し、smoothness 1+λ³≠0と非ST条件λ(λ³−8)≠0の下で
\[
R_Q=\{G\in\operatorname{Sym}^3V:\partial_WG\subset Q\}
=\mathbb C F\oplus\operatorname{Sym}^3U,
\qquad\dim R_Q=5.
\]
M Hess(f₃)が対称となるMはスカラーだけである。二つの三項cycleによる証明は任意係数環上でも単元条件の下で成立し、対応する9×9系の8次minorはλ²(λ³−8)²。これはUeda–YoshinagaのJacobian Torelliの特殊例であり、Hwangのsymmetrizerの枠組みでも説明される。新規性の確認が必要なのはpoint schemeからの抽出と本族への相対的応用である。

R_Qは実際に全ての三次affine Casimirの空間である。中心条件から分数体上で∇G=r∇F、三偏微分のgcd=1からrの分母が消え、次数からrは定数。Casimir空間が五次元という部分自体は非ST条件を要しない。非ST条件はR_Qとの同定に使う。λ=0,λ³=8ではHesseだけの可積分系がrank6となるが、mixed項でrank8に戻る可能性は残る。

商直線R_Q/Sym³Uからι_ΠΩ=dF∧du∧dvにより[Π]を復元する。F→cF+g(u,v)、Uの基底変更、体積形式の変更はΠのスカラー倍しか変えない。既存Jacobian locus内の開上でkernelは階数5の部分束となり底変更に両立する。全Grassmannianでrank5が開という主張ではない。中心重みのあるU,R_QをそのままPGL商上の通常の束とはしない。

**有限パラメータの障害。** Hesse境界は正確に
\[
E_h=V(u,v,e_h),\quad e_h=A\Sigma x^3+Bxyz
=3\bigl(f_3+h^2\det\operatorname{Hess}(f_3)/24\bigr),
\]
\[
A=1-\lambda^2h^2/4,\quad
B=3\lambda+(1+\lambda^3/4)h^2.
\]
仮にE_h⊔D_wを同じP⁴のsmooth cubic V(G)のPoisson零点にできると、唯一の曲線成分から基底平面が強制され、G|plane=ce_h、G_x∈Qとなる。平方項とyzの係数比較はB=3λAを要求するが、B−3λA=h²(1+λ³)≠0。従ってh≠0で古典・量子境界smooth、D_wがCIという開全体で不可能（`prop:hesse-point-zero-nonrealization`）。これは埋込みを保つ同一視の障害であり、任意の抽象scheme同型や補正付き対応の不存在を示さない。

**Fermatの平坦極限。** [x,y]=hz²と巡回関係、w_h=f−h²T/9+u³+v³では
\[
E_h=V(u,v,x^3+y^3+z^3+h^2xyz),\quad
D_h=V(x^2,y^2,z^2,u^3+v^3-2h^2xyz/3).
\]
D_hは24個の被約点ではなく、三つの台の各点に長さ8を持つ。u=1で基底x^iy^jz^kv^ℓ（i,j,k≤1、ℓ≤2）があり、hに関して平坦である。一般point schemeの平坦閉包のh=0 fiberはE₀⊔D₀=Z(π₀)だが、可換代数A₀の全point schemeはX₀全体となる。π₀は交換子をhで割ってから還元した非零の半古典構造である。Hesseのj式はh⁶(216−h⁶)³/(27+h⁶)³なので、一般E_hはE₀と抽象的にも同型でない。

**shiftと尺度。** 固定XではE⊂Xから[π]、さらにη=Res_mod⁰(π)|Eからπ自身を復元できる（ηは至る所非零）。Jacobian括弧の指定した規格化・右点加群の規約で
\[
\sigma'_0=\tfrac12\operatorname{Res}_{\rm mod}^0(\pi)|_E.
\]
局所的にf=F(x,y,1,0,0)なら速度はf_y∂_x−f_x∂_y。Fermatではy²∂_x−x²∂_yで、dx/y²の双対である。E_hとD_hはh↦−hで変わらないがσ_{−h}=σ_h^{-1}。point scheme単独が失う符号と一次尺度は点対応に残る。ただしこれは指定した量子化経路の一次情報であり、有限σから代数的な対数を定めていない。

**次の未解決箇所。** shift付きでは尺度込みambient Π_finまで復元できたが、R_QからFを選ぶ際にはbinary cubicだけ変える四次元の曖昧さが残る。D_wの三次イデアルI(D_w)_3/(V·Q)が量子中心の可換像の直線を与えるので、これを古典Casimir直線へ補正する同変写像を探る。対称化逆像の失敗とHesseの零点非実現性を制約として使う。特定のCasimirとρが復元する三次との一致まで示して初めて、当初の内在的Poisson cubicへの射に達する。現段階の[Π]復元をその完成と呼ばない。

## 11. 先行研究との差分と公表前の確認

以下は現在の研究方針に効く一次資料である。定理の全適用や新規性の網羅的確認を完了したという意味ではない。

| 識別子・一次資料 | 確認した結果・範囲 | 本研究で追加すべき内容 |
|---|---|---|
| [Behrend–Noohi, Math. Ann.371 (2018),1375–1408](https://doi.org/10.1007/s00208-017-1624-1), 刊行版§§2.3/2.5/3.1.2/4.4.1/4.5.3 | 次数付き乗法の商stack、次数重みのscalar gerbe、有限切断、自己同値を保持する偏極付き圏。安定な有限切断はDM。無限次数の一般的有限決定性は§4.5.3の課題 | 有限関係窓から本族の全O保存Hom層へ比較し、指定部分stackの有限型性を直接証明する |
| [Abdelgadir–Okawa–Ueda, arXiv:1411.7770v1](https://arxiv.org/pdf/1411.7770v1), Thm7.3, CorA.7, ThmA.8, CorA.10 | 標数≠3の代数閉体上、三次元二次AS正則代数のqgrから標準列をshiftまで、Z代数を同型まで復元。generic制限はなく、Zhang twistとも同値。Appendix AはSmith–Van den Berghに帰属する復元の証明を収める | 無標識Abel圏の復元自体を本稿の新規性としない。本稿では三次商の任意係数上のfpqc Hom比較、17次元全部分stackとrank4二次包絡torsorを構成する |
| [De Deken–Lowen, JNCG5 (2011), 477–505, DOI10.4171/JNCG/83](https://ems.press/content/serial-article-files/30497), Thm4.5 pp.495–496, Prop4.6 p.496 | 全twist Ext¹/Ext²消滅を満たすZ-generating列によるAbel/線型変形の比較とnoetherian性の持上げ | 三次点への適用は既知定理の帰結。二次包絡の平坦性はこの定理に含まれない |
| [Lowen–Van den Bergh, TAMS358 (2006), 5441–5483, DOI10.1090/S0002-9947-06-03871-2](https://win.uantwerpen.be/~wlowen/pdf%20papers/TAMS-DeformationTheory.pdf), §8.2, Thm8.8 p.5472, Props4.4/4.6/4.8 | 1群oidの規約、Ind/fp比較、係数作用による底変更 | 任意係数への大きいtails比較は本稿に直接証明。小さい圏の有限表示仮定と非切断2群oidを区別 |
| [Stacks023M](https://stacks.math.columbia.edu/tag/023M), [023N](https://stacks.math.columbia.edu/tag/023N), [058S](https://stacks.math.columbia.edu/tag/058S) | 任意加群の拡大Amitsur完全性、加群降下、有限射影性の降下 | 対数でframed band 1+mを加法化し、section Homと合成を降下する。一般のBrauer消滅は使用しない |
| [Lowen, Comm.Algebra33 (2005), 3195–3223, DOI10.1081/AGB-200066155](https://win.uantwerpen.be/~wlowen/pdf%20papers/COMALG-ObstructionTheory.pdf), Thms6.11–6.12 pp.3218–3219 | 対象のExt²障害・Ext¹で測る持上げの差。flat版は双対 | Oの形式的持上げと、大域的なOの内在認識は別 |
| [Lowen–Van den Bergh, Adv.Math198 (2005), 172–221, DOI10.1016/j.aim.2004.11.010](https://win.uantwerpen.be/~wlowen/pdf%20papers/ADVANCES-Hochschild-cohomology.pdf), Thm3.1, Rem3.5, Thm6.1 | Abel変形のHochschild制御、char0のMC/gauge、導来enhancementとの比較 | homogeneous coordinate模型との比較は対象を一致させて適用 |
| [Barmeier–Wang, Algebraic Geometry11 (2024), 1–36, DOI10.14231/AG-2024-001](https://content.algebraicgeometry.nl/2024-1/2024-1-001.pdf), Thm1.2=3.11 | affine cover由来quiver relationsによる(Q)coh変形のexplicit L∞模型 | tilting版Thm3.18をcubicへそのまま使わない。一般Abel変形理論の新規性は主張しない |
| [Lowen, Trans. Amer. Math. Soc.360 (2008),1631–1660](https://win.uantwerpen.be/~wlowen/pdf%20papers/TAMS-AlgebroidPrestacksRingedSpaces.pdf), Thm3.14 p.1654, Thm3.26 pp.1658–1659; arXiv:math/0511197v2 | locally flatなalgebroid、acyclic basisと有限交叉で閉じた被覆、準連接制限のlocalization性を用いたMod・QcohのAbel変形比較 | 分離的三次のアフィン被覆で仮定を満たし、H¹,H²(O)=0で通常の代数層へ移る。周期性はこの引用から推論しない |
| [Yekutieli, Adv. Math.268 (2015),241–305, DOI10.1016/j.aim.2014.09.003; arXiv:0905.0488v5](https://arxiv.org/pdf/0905.0488), Cor7.5 p.35, Thm11.1/Cor11.2 pp.45–47 | 完備局所Noetherian parameter algebra上で通常／twisted変形を比較し、可換積も変動するPoisson／Assのgauge同値類に係数準同型と可換な全単射を与える | 全局所Artin基底を含む。固定層のstar productを扱うCor11.3は追加のH¹(T_X),H¹(D_X)消滅を要し、本稿では適用しない |
| [Cattaneo–Felder–Tomassini, Duke Math. J.115 (2002),329–352; arXiv:math/0012228v3](https://arxiv.org/pdf/math/0012228), §3 Thm3.1, Prop3.3と直後のRemark, Cor5.2(iv) | GL同変な普遍多項式公式、一次項・単位、Casimirの中心持上げ | 固定ambientに多パラメータArtin係数を代入し、動くF_tの中心商を作る。中心性の逆向きは有限自由行列で証明し、全同次変形のgauge分類は仮定しない |
| [Polishchuk–Positselski, Quadratic Algebras, ULS37, AMS2005](https://doi.org/10.1090/ulect/037), Ch6 Prop7.2/Thm7.3 pp129–130 | Noetherian局所環上で、Koszul特殊ファイバーと次数1–3の自由性から全次数自由性 | 原著の該当頁を確認。非周期的Artin Z版には直接証明を与える。一般原理を新規成果としない |
| [Rains, arXiv:2107.13540v2](https://arxiv.org/pdf/2107.13540v2), Thm2.13 p16 | 標数零・有限位数translationの楕円代数のfiltered deformationでは中心もfiltered deformationになる | 被約有限型係数環上の交換子行列へ適用。非被約基底の閉点判定や一般infinite-orderへ無条件に拡張しない |
| [Elagin–Lunts–Schnürer, arXiv:1810.07626v2](https://arxiv.org/pdf/1810.07626v2), Thms4.15,4.18(b), pp26–27; Moscow Math. J.20:2 (2020),277–309 | 完全体上のNoetherian J-2スキームとcoherent代数、積もNoetherianの下で、任意に選んだclassical generatorの外積がDbcohを生成 | 左右Dbcoh=Perfを別に供給し、反対代数で右加群の規約へ移し、対角kernelのMorita比較で大域smooth性を得る |
| [Toën–Vaquié, ASENS40 (2007),387–444](https://www.numdam.org/article/ASENS_2007_4_40_3_387_0.pdf), Lem2.10; [Toën, Anneaux de définition…](https://www.math.univ-toulouse.fr/~btoen/defdgalg.pdf), F4 | perfect dg加群のfiltered colimitとの可換性 | F4はhfp不要。一般点からの拡張に用い、closedpointからのopennessとはしない |
| [Walton–Wang–Yakimov, arXiv:1704.04975v3](https://arxiv.org/pdf/1704.04975), Def–Lem2.13 p9; Proc. LMS118 (2019),1471–1500 | SklyaninのHesse曲線と平行移動点[p:q:r] | 関係式の規約と原点[1:−1:0]を確認。原典ATVへの帰属を保持 |
| [Stacks0BFG](https://stacks.math.columbia.edu/tag/0BFG), [0BFH](https://stacks.math.columbia.edu/tag/0BFH) | 体上の乗法[n]の次数n²・有限性・étale性 | Hesse族では相対微分とpropernessの証明を加え、torsion曲線の次元1を得る |
| [Rennemo–Segal–Van den Bergh, arXiv:1705.01366v2](https://arxiv.org/pdf/1705.01366v2), Prop2.1 proof(1)–(8), Lems3.3–3.6/3.8, Cor3.9 | 有限型可換中心代数上有限な代数の、有限大域次元から対角smoothnessとgeneric spreadへ。Prop2.1は中心の正規性やNCR表示を要求しない | 一般tailsから全中心アフィンchartへ移す段階と分裂の分母払いを本稿で証明。係数flatなsyzygyにより全幾何学的fiberへ移す。一般AS5や大域dg smoothnessの無条件の近道にしない |
| [Stacks 058G](https://stacks.math.columbia.edu/tag/058G), [023N](https://stacks.math.columbia.edu/tag/023N), [039Y](https://stacks.math.columbia.edu/tag/039Y) | Lazard、通常の加群降下 | Grothendieck圏内の等化子による降下は直接証明 |
| [Stacks 01YR](https://stacks.math.columbia.edu/tag/01YR), [0AG5](https://stacks.math.columbia.edu/tag/0AG5), [08EV](https://stacks.math.columbia.edu/tag/08EV), [0FCL](https://stacks.math.columbia.edu/tag/0FCL) | Proj上の生成・消滅、quasi-compact Proj上の任意準連接層のsection復元、proper pushforwardのperfect性、cohとQCohのExt比較 | 0AG5はNoetherian仮定なし。08EVのLemma36.27.1は有限底Tor振幅を用い、背景スキームの平坦性は要求しない |
| [Milne, Algebraic Groups, Prop20.7](https://www.jmilne.org/math/Books/iAG2022.pdf); [Stacks 03PK](https://stacks.math.columbia.edu/tag/03PK), [0CJZ](https://stacks.math.columbia.edu/tag/0CJZ), [0FY3](https://stacks.math.columbia.edu/tag/0FY3), [051E](https://stacks.math.columbia.edu/tag/051E) | 非被約C基底上もPGL2=Aut(P¹)、Kummer列、gerbe、Serreの一意性、Artin flat=free | 相対Veronese・Hom比較の一般入力。組合せの初出は未確認 |
| [Mayanskiy, arXiv:1303.5916](https://arxiv.org/pdf/1303.5916), Theorem 1、§2.2 Lemma2 | 固定smooth cubicの射影Poisson空間Gr(2,5)。Loray–Pereira–Touzetに帰属。Schouten式を再確認 | 勾配写像の局所分裂により相対scheme方程式へ適用。17という数や錐の同定自体を新規性にしない |
| [Cukierman–Pereira–Vainsencher, arXiv:0709.4072](https://arxiv.org/pdf/0709.4072), Theorem 2; AFST18(2009),685–715, DOI10.5802/afst.1221 | 有理葉層R(r,d_0,...,d_q)のfoliation schemeでの成分性・一般被約性。r=4,q=2,(1,1,3)を含む | decomposabilityを課さない**全Poisson scheme**の接空間、中心三次incidenceとの関係を明示する |
| [Corrêa–Muniz, arXiv:2207.12880v5](https://arxiv.org/pdf/2207.12880v5), Corollaries C/D and §5 | P4のrank2 Poisson locusにRat113/Rat122型。π∧π=0を課すlocusの成分を扱う | 全Poisson schemeの一般正則性・量子化moduliと区別。全分類完成の入力として機械的に使わない |
| [Pym, arXiv:1403.6444](https://arxiv.org/pdf/1403.6444), Theorem2.3と直後、Definition2.8, Proposition2.9, Theorem2.10 | 一般Vの規格化Koszul CY変形芽とunimodular quadratic Poisson scheme、成分の局所比較 | 解析芽の存在をcanonical quantization map、大域stack、今回の実際の比較写像と同一視しない |
| [Mori–Smith, arXiv:1502.07403v2](https://arxiv.org/pdf/1502.07403v2), Theorem4.2(1) | 滑らかな平面三次からの対称化Jacobian量子代数は全量子化係数λ（0も含む）で3-CY | 相対PBWと5次元ambientへの拡張、指定中心三次対のmoduliを分離して述べる |
| [Reyes–Rogalski, arXiv:1807.10249v2](https://arxiv.org/pdf/1807.10249v2), Theorem5.15, Lemmas5.9/4.5 | generalized ASとtwisted CYの比較、Nakayamaは中心を固定 | 指定した正規族を保つN周期の構成、可換なd周期とのgcd周期化、相対降下が本稿の組合せ |
| [Mori–Nyman, regV8](https://faculty.nymana.wwu.edu/regV8.pdf), Theorem4.19; [arXiv:2307.15253](https://arxiv.org/abs/2307.15253) | ASF++と周期的ASF+の関係 | 弱いAS条件と混同しない。gcd対定理の初出は引き続き要確認 |
| [Sierra, arXiv:math/0608791](https://arxiv.org/pdf/math/0608791), Proposition3.3, Corollary4.4 | principal Z-algebra、compression、Zhang twisting system | 周期の選択・共役・相対降下を別々に記述する |
| [KuzHH: Kuznetsov, arXiv:0904.4330](https://arxiv.org/pdf/0904.4330), Theorem8.9 | cubic3の残余圏の全HH^p表 | 相対NC residualと全Artin認識を本稿で構成し、効果化・降下で開集合の射へ移す |
| [JLLZ: Jacovskis–Lin–Liu–Zhang, arXiv:2203.08187v3](https://arxiv.org/pdf/2203.08187v3), Theorems3.11 and4.4(2) | 幾何的接写像の同型、γ単射、補正HKRの図式 | 次元一致だけでなくactual mapを使う。形式/代数的な比較の区別を保つ |
| [Lurie, DAG X](https://www.math.ias.edu/~lurie/papers/DAG-X.pdf), Def5.3.20, Thms5.1.9/5.3.16, Prop5.3.21; [Blanc–Katzarkov–Pandit, arXiv:1705.00655](https://arxiv.org/pdf/1705.00655), §3.3 | tame compactly generated変形からhullへの(−1)-truncated比較、centerによる形式変形制御 | π0単射と実際の幾何的KSを組み合わせ、通常Artin基底で全認識。π₂=HH⁰⊗m≃1+mを保持し、群oid全体の離散化は主張しない |
| [Bhatt, arXiv:1404.7483](https://arxiv.org/pdf/1404.7483), Lem4.2 | 完備環上のPerfとArtin切断の∞圏極限の同値 | underlying係数perfect複体と作用を効果化。包絡dg代数上のcompact性の効果化とはしない |
| [Stevenson, arXiv:1105.4698v3](https://arxiv.org/pdf/1105.4698), Thm3.1(3), Notation3.2, Lem3.10, Thm6.13 | Noetherianかつ局所的にhypersurfaceなaffine環の全localizing特異部分圏を分類。compact部分はKar D_sgと同値で、tensor作用安定性は自動 | 孤立特異点では非零compact対象が全体を生成。冪等完備化を経由してgraded化とcompactnessへ接続 |
| [Orlov, arXiv:math/0302304v2](https://arxiv.org/pdf/math/0302304), §3.1, Thm3.9 | 正則affine空間と平坦な函数Wについて、有限階数ungraded MFと零ファイバーの特異圏が同値 | 本稿ではW=f。非定数fによるk[t]→Sとtorsion-free性から平坦性を得る。全critical fiberをまとめるCor3.10とは区別 |
| [Orlov, arXiv:math/0503632v3](https://arxiv.org/pdf/math/0503632), Thms2.5/3.10–3.11; [Neeman, Ann. Sci. ENS25 (1992),547–566](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/neeman-loc.pdf), Lem2.2 | graded MF・特異圏・Fano残余圏の比較、compact生成localizing圏のcompact部分 | windowを合わせ、rotation=Serre[−1]で三次成分のSerre安定thick生成を得る |
| [Kuznetsov, J. reine angew. Math.753 (2019),239–267; arXiv:1509.07657v2](https://arxiv.org/pdf/1509.07657), §3.3, Cor3.18, Lem3.19, Cor4.1 | 滑らかなFano hypersurfaceのrotationとSerre関手の公式。三次三様体ではR_rot³=[2], S=R_rot⁻²[3] | 二つの式からR_rot=S[−1]を得て、Serre安定性をgraded shift安定性に移す。S³=[5]だけで同定しない |
| [Bernardara–Macrì–Mehrotra–Stellari, arXiv:0903.4414v2](https://arxiv.org/pdf/0903.4414v2), Thm1.1 | 滑らかな三次三様体はKuznetsov成分の同値から一意に復元 | 有限表示spreadingで拡大体へ適用。被約な二重交差上で粗モジュライ射を降下 |
| [Poonen, Finite Fields Appl.11 (2005),230–268](https://math.mit.edu/~poonen/papers/projaut.pdf), Thms1.1/1.5/1.6, Cor1.9 | 自己同型が自明なsmooth hypersurfaceの非空開 | targetで粗モジュライとstackを同一視し、相対次元7の滑らかな全射に制限 |
| [Allcock, J. Algebraic Geom.12 (2003),201–223](https://web.ma.utexas.edu/users/allcock/research/3foldgit.pdf), Thm1.1 | cubic threefoldのGIT安定性判定。smooth cubicは安定 | 分離的な十次元粗モジュライを用いる。author PDFの定理を画像で確認 |
| [Hitchin, arXiv:1008.0973](https://arxiv.org/pdf/1008.0973), §5.3 pp.41–42 | canonical bundleのPoisson module構造とπ⌟c_1(T)=0 | §10.5のTodd補正確認に使う |
| [Feyzbakhsh–Liu–Zhang, MPIM23-7](https://archive.mpim-bonn.mpg.de/id/eprint/4904/1/mpim-preprint_2023-7.pdf), Theorems1.1/6.2 and1.2/7.1 | 可換del Pezzo三様体のgluing objectとBrill–Noether復元 | 今回の非可換族で接合データが7方向をどう保持するかを調べる |
| [Matviichuk–Pym–Schedler, arXiv:2411.10425v1](https://arxiv.org/html/2411.10425v1), Introduction, Theorem1.1 | 適切な非退化条件を満たすq-symmetric/toric型から具体的な量子射影空間を作る | rank2 Rat113へ直接適用する定理ではない。有限係数成分構成の方法比較に使う |
| [Lin–Zhang, arXiv:2611.05915v1](https://arxiv.org/html/2611.05915v1), Thm1.7, §2 | 滑らかな既約基底上の滑らかな射影族、底変更に両立するperfect射影核を持つ相対admissible圏、特殊点での既存の同値を仮定する。幾何的KS写像の全射性と負次数HHの消滅の下で、両基底へ滑らかに写る共通基底上に同値核を変形する | 本稿で必要なNC族の幾何的認識を供給する定理ではない。幾何的targetを得る前の係数perfectな効果化・Serre安定性・生成性と対象を区別する |
| [Yekutieli, Dualizing complexes (1992)](https://www.math.bgu.ac.il/~amyekut/publications/dual-com/dual-com.pdf), Def4.1, Props4.6/5.2, Cor5.5, Rem5.7 | balanced双対複体の一意性、有限中心写像、商、trace | 体上で両側加群の同定に使う。次数零部分がPの相対定理として直接引用しない |
| [Burban–Drozd–Gavran, arXiv:1501.06023v2](https://arxiv.org/pdf/1501.06023v2), Defs3.1/3.13, Thm3.14 | quasi-compact separatedな基礎スキームとquasi-coherent代数層で非有界導来圏のcompact=局所Perf。Noetherian性は不要 | Abel同値が保存する内在的部分圏。正則開上の有限係数Tor圏との一致とは別 |
| [Stacks00MI](https://stacks.math.columbia.edu/tag/00MI), [07VK](https://stacks.math.columbia.edu/tag/07VK), [0B91](https://stacks.math.columbia.edu/tag/0B91), [0A9W](https://stacks.math.columbia.edu/tag/0A9W), [0B6J](https://stacks.math.columbia.edu/tag/0B6J), [0B6S](https://stacks.math.columbia.edu/tag/0B6S) | flatness、proper base change、射影空間の双対・trace | 有限中心模型の相対化。非平坦な中心Y自体の双対公式を仮定しない |
| [Stacks047N](https://stacks.math.columbia.edu/tag/047N) | 標数零の有限型群スキームのsmoothness | 既存の複素点剛体性をAut_gr(B_*)=Gmという群スキームの主張へ移す |
| [Berger–Taillefer, arXiv:math/0610112v2](https://arxiv.org/pdf/math/0610112v2), Thms3.1/3.6, pp9–12 | potentialのPBW変形とCY複体、cyclic Hessianの自己双対 | 相対射影性と普遍完全性を先に証明し、明示式を係数環上に構成する |
| [Etingof–Ginzburg, arXiv:0709.3593v4](https://arxiv.org/pdf/0709.3593v4), Prop7.3.1(ii) | CY最高次potentialの任意低次cyclic摂動のPBW性 | 全閉点で適用し、被約係数環上の射影分裂により非平坦底変更まで拡張 |
| [Reyes–Rogalski, arXiv:1807.10249v2](https://arxiv.org/pdf/1807.10249v2), Prop4.12 | 係数有限次元加群のCY tensor–Hom双対 | 有限射影係数で必要な項別計算を直接行う |
| [CCKM, arXiv:1307.8415v1](https://arxiv.org/pdf/1307.8415v1), Lem4.4(3), Thms4.7/5.5 | Rees補題、中心正則商のExt shift、有限syzygy後の行列因子化と特異圏 | v1の番号を公刊版と区別。A側の有限torsion模型・真正な双加群作用・任意底変更とchartの貼合せは本文で構成 |
| [Yekutieli–Zhang, Proc. AMS125 (1997),697–707](https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/paper.pdf), Thm4.2/Cor4.3と直前; [Chen, arXiv:math/0610258v3](https://arxiv.org/pdf/math/0610258v3), Thm3.10 | AS–Gorenstein代数のbalanced双対複体と有限射影次元部分の一般化Serre双対。左右χと有限局所コホモロジー次元を仮定 | 中心正則商で仮定を供給し、twistによる厚い生成と組み合わせてtails大域次元が正確に3となることを証明 |
| [Keller, arXiv:math/0601185v5](https://arxiv.org/pdf/math/0601185v5), §2.1, Thms3.4/3.8(c), §3.8 | 可換基底上のdg Morita、compactのthick生成 | strict A→Q、Rωとの整合、両側局所化とtraceを具体的に記述 |
| [Keeler, arXiv:math/0108068v5](https://arxiv.org/pdf/math/0108068v5), Thm1.3, Prop2.7, Thm7.14 | 一般Noetherian底上のample filterとTHCR Noetherian性。2018年訂正版 | 楕円曲線上のdegree3nから仮定を満たす。有限位数は不要 |
| [Mizuno, arXiv:2509.13073v3](https://arxiv.org/pdf/2509.13073v3), §2, Thm5.8 | Z-algebra双対、係数体と有限qgr global dimensionの仮定 | 今回の任意可換係数・compact版へ直接適用しない。2026-09-04版を確認 |
| [Brown–Sridhar, arXiv:2410.07204v2](https://arxiv.org/pdf/2410.07204v2), §2 | 体上のdg Serre双対 | 2025-08-15版。相対任意係数への拡張とは区別 |
| [Brown–Soto Levins–Sridhar, arXiv:2506.02398v1](https://arxiv.org/pdf/2506.02398v1), Notation1.4, Setup2.1, Cor1.3 | balanced dg双対の存在とperfect tailsのSerre双対、係数体 | 本稿の局所双対→tails双対という方法の近接文献。相対構成の初出は未確認 |
| [Stacks Project](https://stacks.math.columbia.edu/), Tags03WT/02GU/0476/06FI/06N3/04UV/0245 | étale locusの平坦底変更と開性、商stackの代数性・torsor表示、étale atlasとDM性、fpqcアフィン降下 | 一般理論は既知。Q113の飽和開と普遍中心に適用し、全O保存Abel同値との一致を別に証明。2026-11-19原文確認 |
| [Vancliff, Non-commutative Spaces for Graded Quantum Groups and Graded Clifford Algebras, Progress in Physics18 (2000),303–320, DOI10.1007/978-1-4612-1368-0_16](https://bpb-us-e1.wpmucdn.com/websites.uta.edu/dist/0/5123/files/2022/10/cliff.pdf), §6 Props6.17/Thm6.18/Example6.12 | projective零点の三次式、非零パラメータでpoint scheme一定という仮定の下の包含、一般の等号失敗 | 本族は境界がh²で動く。一次持上げ・中央三次商・埋込み非実現性と範囲を分ける |
| [Le Bruyn–Smith–Van den Bergh, Math.Z.222 (1996),171–212, DOI10.1007/PL00004532](https://sites.math.washington.edu/~smith/Research/Central-extns.pdf), Thm4.2.2/Props4.2.5,4.3.7(1) | 一中心変数のSklyanin拡大は一般に楕円曲線＋8点、中心超平面外でshift=id、点対応からrelations復元 | 二中心変数と中心三次商のE⊔長さ24、三次商後の包絡復元 |
| [Pym, LMP108 (2018),573–632, DOI10.1007/s11005-017-0984-5](https://arxiv.org/pdf/1701.08852), §3.2.2 | pencilの基底と特異fiber点、Euler局所形 | smooth cubicで極完全交叉の長さ24、一般の被約性を具体化 |
| [Gualtieri–Pym, PLMS107 (2013),627–654, DOI10.1112/plms/pds090](https://arxiv.org/pdf/1203.4293), Def4.16/Thm7.2/Example7.4 | modular residue=−Tr(Dπ)、Euler形で−2∂z | 本Jacobian族の右point shift速度との係数1/2比較 |
| [Ueda–Yoshinaga, Hokkaido Math.J.38 (2009),409–415, DOI10.14492/hokmj/1258553970](https://www.math.sci.hokudai.ac.jp/hmj/page/38-3/pdf/HMJ38_0409-0415.pdf), §3 Lemma3 p412 | 非STのsmooth hypersurfaceはJacobi idealから復元 | 24点の二次イデアルからpartial-gradient netを抽出し中心二変数を残す |
| [Hwang, JMSJ78(1) (2026),55–62, DOI10.2969/jmsj/93469346](https://arxiv.org/pdf/2501.08633), Def2.1/Thms1.3,1.5–1.6 | symmetrizer algebra/groupとJacobian mapのfiber | HesseのM Hess対称の明示rank8判定はこの既知原理の特殊例 |
| [Artebani–Dolgachev, Enseign.Math.55 (2009),235–273, DOI10.4171/LEM/55-3-3](https://arxiv.org/pdf/math/0611590), §2 eqs(6)–(8) | HesseのWeierstrass係数とj | Fermat境界E_hのj変動を具体的に代入計算 |

Abel変形比較・Ku残余射・point schemeについて上記の一次入力をIntroductionとbibliographyに反映した。これらの既知定理そのものを新規成果とせず、具体的な17係数族の相対構成・効果化・開集合への降下が追加部分である。近接するfoliation文献も含め、初出・新規性の網羅的照合は未完了である。

## 12. 現在の検証範囲と外部課題との境界

全Abel変形の平坦二次包絡、次数三判定、平方零消滅、全stackのframed形式環、一般族の相対双対・全Hom比較・代数的部分stack・17→10射、全Abel残余とPoisson形式同型を、詳細証明付きの現行成果として保持する。証明の所在と、この公表準備で実際に点検した範囲は区別する。

**重点監査の範囲。** Jacobian atlasの飽和開・普遍中心・スカラー重み・階数四torsor、可換点の平坦包絡・任意係数変更・framed形式降下、CFT–Yekutieliの適用仮定を点検した。相対双対では有界幅Koszul torsion模型、A/BのTor比較、真正な双加群作用、両側dg局所化からSerre traceへの鎖を点検した。普遍PBW/CYでは閉点の一定階数から係数射影分裂への移行、potential解消の全微分と双対符号、中心差のKoszul双対、五次元Koszul解消の任意底変更を読み合わせた。

全O保存Homの上流4節は全体を通読し、相対Veronese交差、平方根被覆、線束の捩れ、偶数section Z代数、固定模型のHom降下とstack化を点検した。残余側では全Artin認識、係数perfectな核と高次作用の効果化、非循環なSerre比較、冪等完備化を含む生成性、有限表示とTorelli降下を点検した。点データ側では§10.7の一次持上げ、scheme分解、二次包絡・Casimir復元、Hesse非実現性、modular residue比較を点検した。これらは指定範囲の別々の読み合わせであり、外部基礎定理の全証明の再証明、形式的証明検証、全文献の優先権調査ではない。主要な主張は本文に明記した相対PBW/CY・proper/Serre等の入力に依存し、全証明の独立全面監査と外部査読は未完了である。

本版で全体を通読したのは有限中心・相対圏・大域smoothnessを扱う三節である。Rains→一定rank→中心持上げ、RSV→相対対角→幾何学的fiber、CCKM/YZ/Chen→chart貼合せと次元3、ELS→大域対角、任意底のbig QGrとNoetherian coherent部分の違いを点検した。主定理A–Dと各証明の適用範囲も比較し、通常の係数環、projectively gradedなB_J、全Mの可換形式点、点復元開C_J,ptを序論に明記した。橋渡し命題(iv)は関係式の一致とΔ開への制限を区別する。主定理Bの証明はこの制限を既に含む。以上の今回の範囲と累積の通読範囲は `validation.json` で分ける。

近接するモジュライ構成ではBehrend–NoohiとAbdelgadir–Okawa–Uedaの上表の箇所を原文照合し、体上の復元と本稿の相対Hom層・三次商族との相違を序論に明記した。特定の比較文の確認であり、全先行研究を網羅した初出確認ではない。

**厳密計算の現在の状態。** 本版で実行したのは§1.8.1の橋渡し開条件の具体例であり、有理多項式の剰余d≡7168、D_E≡0を確認した。既存の計算コード・小証明書は変更せず、再実行もしていない。次の実行済み結果を保持する。

| 対象 | 実行結果と範囲 |
|---|---|
| `computations/verify_relative_cy.py` | 全40自由語に対する六項目が成功し、`relative_cy_certificate.json` と出力がbyte単位で一致した検証情報を保持。完全性・PBW・射影性は本文の証明による |
| `computations/verify_central_pair_centers.py` | 339語・162関係・rank144、三交換子、三つの41項中心恒等式、平行移動・Rains差、三次minorが成功 |
| `computations/verify_general17_open.py` | 明示したΔの非消滅点と九項目が成功。既存証明書とのbyte一致は追加検査していない |

点・Poissonの九項目、étale点のrank37/113、Euler行列のχ(G₂,G₂)=−9とχ(G,G)=−2925には実行済みの検証情報を保持するが、本版で再実行したとは扱わない。これらを含め、ソース・証明書のhashと実行日は `validation.json` を参照する。point functorの表現可能性、scheme分解、圏論的降下の証明は有限計算とは別である。

**組版と配布時の状態。** 主稿manuscript-v22の最終LuaLaTeX組版は、全33入力を含む265ページのPDF生成に成功した。最終logでoverfull hbox、未定義の参照・引用、欠字はいずれも零であり、全265頁のPDF抽出テキストのページ外bboxも零である。静的検査はlabel 564、参照738、引用233、文献83件を対象とした。32節の入力と既存ラベルを保持し、254個の証明環境と全結果環境の保持を確認した。最終PDFの序論、橋渡し族、Jacobian Torelliに関する注意、今回通読した有限中心関係の三つの付録、文献を含む代表36頁を画像化して目視し、文字切れ・重なり・欠字がないことと、目次・見出しのページ整合を確認した。序論は8頁で終わり、第I部は9頁から始まる。全文265頁を一行ずつ目視したわけではない。小サイズ数式フォントの代替と既存の旧式フォント命令に関する警告は残るが、検査した画像に表示上の問題は見られなかった。最終確認結果は `validation.json` に記録した。生成、静的検査、証明点検、計算実行、組版、保存は別々の状態として記録する。

### H3/PI4の関連知識（本研究の定理の入力ではない）

以下は三次曲面側に属する情報であり、本研究の次の作業指示ではない。対応する現行ファイルの所在を移管元 `uedakazushi/nc-cubic-classification` のcommit `d9070ddd2352f54c1db243be11ec482d062b8a60` で確認した。内容を本研究へ引用して使う時は、仮定・式・証明をその一次ソースから点検する。

- point graphの規約はp yz+q zy−h x²に対する第一行(−hx,qz,py)であり、p,q逆順は逆translationを表す。[verify_cubic_integrated_envelope.py](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_integrated_envelope.py) が関連する検算である。
- 固定PI4族の有限Ext判定・48次元sliceは、[cubic_order4_ext_bound.tex](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/papers/sections/cubic_order4_ext_bound.tex) に属する。AS4のCCKM二周期性、次元≤4の単純加群対のExt6/7、中心2パラメータ上のgraded free性と基底次数≤8を用いる。この曲面側のH3判定をAS5三次三様体のsmooth proper性に転用しない。
- Du Val中心だけではH3の十分条件にならない例を保持する。中心のHessian rank2、核方向cubic零、形式Morseの初項次数4によりA3となる一方、odd Ext1が非H3を検出するという内容は、[cubic_order4_center.tex](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/papers/sections/cubic_order4_center.tex)、[全中心式証明書](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/cubic_order4_center_relation_certificate.json)、[局所検算](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_order4_bad_center.py) に対応する。
- 中心式を再構成する際の変換の知識：r1=(g−1)(g²−1)/2、r2=(g²−1)²/2、X_i=r_i Z_i（r3=1）で最高次をΣX_i³+(7g²−13)X1X2X3へ規格化し、pure squareを消すaffine shift後にu=X1+X2,v=X1−X2,z=X3を取ると、4F=f(u,z,D)+v²(3u−(7g²−13)z−B)となる型を使う。特異値はv=0枝と線形係数零の枝へ分け、二変数critical normと線上三次の判別式で調べる。ただし中心特異値とbad Dは同一視しない。関連する[対称中心検算](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_order4_symmetric_center.py)・[中心critical検算](https://github.com/uedakazushi/nc-cubic-classification/blob/d9070ddd2352f54c1db243be11ec482d062b8a60/computations/verify_cubic_order4_center_critical.py)を参照する。消失した作業用絶対パスを再開の前提にしない。
