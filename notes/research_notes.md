# 研究ノート：非可換三次三様体と非可換P^4

2026-11-16 / migration-v1。現在有効な研究知識。詳細証明は主論文とその `papers/sections` に保持する。H3曲面の分類メモは移管対象外。

## 1. 何をモジュライのデータに含めるか

二つの座標代数stackは、各成分が局所自由な正の連結Z-algebraのfpqc stackの部分問題として定義する。ambient Bはb_m=binom(m+4,4)、cubic Aはh_m=b_m-b_(m-3)。Aの長さ一のHomと長さ二の積の核からQ(A)を得る。原稿`intrinsic_cubic_reconstruction.tex`の相対復元と、`algebraic_moduli_foundations.tex`の定義・比較定理を使う。

有限窓J_N=[-N,N]では、全Homの乗法の有限個の係数に結合律を課したaffine schemeを、各HomのGLの積で割る。全stackはこれらの2逆極限。AS正則性・noetherian性・無限個のHilbert rank条件の有限決定性は別に必要であり、逆極限表示を有限型代数性と呼ばない。

全対象同定付き圏の1射は(F,alpha_i:F(E_i)≅E'_i)、2射はbeta_i eta_i=alpha_i。Hom群oidは離散化され、厳密Z同型と一致する。同定を忘れると頂点スカラーrho_lambda(a_ij)=lambda_i lambda_j^(-1)a_ijが現れる。weak圏の自己同値の2同型類はAut_Z(A)/rho(T)、恒等自己同値の2自己同型は対角Gm。E_0の同定を残すとT0={lambda_0=1}で正規化でき、2慣性が消える。

相対弱い射は線束族L_iとphi:A→(A')^L、(A')^L_ij=L_i A'_ij L_j^(-1)で記述する。この規約ではF(E_i)≅E'_i⊗L_i。共通線束Lは代数式では相殺するが、圏ではtensor-by-Lとなる。自己同型商はfpqc商層であり、大域点集合の単純な商と同じとは限らない。weak 2-stack化では大域的な代数で表示できないtwisted formsも含み得る。証明は`categorical_moduli_comparison.tex`。

Q(A^L)=Q(A)^Lなので三次→ambientの射は全levelに降りる。ただし相対category比較にはHomの任意の基底変換、低次数saturation、相対section復元を仮定する。裸のAbel圏・導来圏・Kuznetsov成分のみからの復元は含まない。

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

P4とsmooth cubic XはH1(O(j))=H2(O(j))=0を全jで満たす。De Deken–Lowen Theorem4.5によりAbel変形とsection Z-algebraの線型変形を比較でき、O(i)は同型類として一意に持ち上がる。自己同型1+mは残り、対象の持上げからshift自己同値の持上げを自動的に得ない。Lowenのringed-space/algebroid比較とYekutieli Cor11.2により、全Artinで構造代数層とPoisson変形のgauge類へ比較する。詳細と一次参照は`formal_ambient_comparison.tex`。

P4ではPoisson変形関手は、Jacobi零点錐の原点完備化をPGL5_1で割ったもの。接空間は126。epsilon³上でpi=epsilon Pとexp(epsilon xi)piは二次で異なる代表となるため、接空間が等しいだけでは裸の錐とgauge商を同定できない。

有限Beilinson窓O,…,O(4)にHom(O,O(1))の射影基底を指定し、対象スカラーを除くと特殊点の無限小固定群が消える。形式陰関数定理でsliceができ、射影基底付きAbel変形をprorepresentする。frame忘却とPoisson錐は同じ関手のminimal hull。Pymの規格化CY芽との比較から両完備局所環が抽象的に同型と分かり、その後に実際のQmod自然写像の接空間同型を使って実際の写像の同型を証明する。この順序が重要であり、接空間だけの推論ではない。

帰結：規格化CY芽と射影基底付きAbel/Z形式模型は全Artinで一致。frameを忘れるとPGL5_1を割る。集合値の標識付き変形関手についての結論であり、2-stackや全大域モジュライの同値ではない。

smooth cubicのArtin局所環は、明記した同次formality入力の下でk[[s1..s10,a01..a34]]/(Pluecker5式)、次元17・接空間20。全framed中心対の41/44模型とは区別する。実際のambient写像の接写像は(dot F,a)↦Pi(F,a)、dot F方向の核10・像10。H0(T_X)=0であるためcubic側にP4と同じ24次元の形式gaugeは残らない。

独立に選んだ射影とaffine formalityの座標で、全高次のactual mapが(F_R,a)↦Pi(F_R,a)という式と一致することは未確認。写像自体の存在と一次式、中心対局所環の記述はこの未確認点を前提にしない。

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

次の技術的入口は、P3のrank6形式模型の既約枝とPym六族の比較、および一般H_R有限なP4点の相対helix再構成である。相対Koszul–Frobeniusの存在は全成分の局所自由性から得られたので、正規三次イデアルを保つ周期降下と有限係数incidenceに焦点を置く。smooth proper部分の開性には、相対dg模型と対角のperfect性の有限検査が必要。

文献上の範囲：Sierraの厳密twist比較、AOUのAS3での内部O(n)認識、Behrend–Noohiの切断stackは一次資料を確認。AOUの裸のqgr復元をAS5/cubicへ無証明で一般化しない。新しい主張の初出・優先権と、保持した全旧証明の独立全面監査は未完了。実施した計算・組版・証明監査はvalidation.jsonで区別する。

point graph規約の訂正：p yz+q zy-h x²に対する行列は(-hx,qz,py)を第一行とする。以前のp,q逆順は逆translationを表していた。`verify_cubic_integrated_envelope.py` に関係式からの直接検算を加えた。E、位数4条件、character余因子判定、既得bad Dは不変。

固定PI4族の有限Ext判定も `cubic_order4_ext_bound.tex` に証明した。CCKM Theorem4.7をAS4右加群（oppositeで適用）に使うとdehomogenization後Extはi>=6で2周期。全単純加群の組（次元<=4）のExt6,7が零 iff H3。有限中心の完備化、左右双対、semiperfect最小解消による証明。普遍表現の8段有限自由解消は基底上平坦syzygyを持ち、単純性の有限開条件とExt非零の有限階数条件からbad像はconstructible。超越的Dが全てgoodなので像は有限。この有限データの全生成とbad多項式計算は未実行。
48次元sliceの停止保証は `lem:order4-fortyeight-slice`：HのAS Gorenstein local dualityから中心2パラメータ上graded free、基底次数<=8。Uのfiltered基底を持ち上げると全(D,c1,c2)でrank48、次数9までで正則表現を得る。重み付き再構成は17ケース全完了と係数空間の可逆性が揃うまで未完として扱う。

中心式再構成は完了。独立なDstar・character中心点の代入でF=gradF=0を確認し、Hessian rank2、核方向cubic0、形式Morseの最初の非零次数4。中心はA3である（quartic Schur補でも同じ係数）。非H3は既証のodd Ext1なので、Du Val中心だけを十分条件にしない。全中心式・全17評価・全係数空間は `cubic_order4_center_relation_certificate.json`、局所確認は `verify_cubic_order4_bad_center.py` とcertificate。
次の消去計算に有用な厳密変換（作業用 /workspace/work/clifford_cubic/normalize_order4_center.py）：先頭Phiのcube係数はr1^3,r2^3,1、r1=(g-1)(g²-1)/2,r2=(g²-1)²/2。X_i=r_i Z_iで先頭はSigma X_i³+(7g²-13)X1X2X3。各pure square係数を消す一意のaffine shift後、全中心式はX1,X2に対称となることを計算で確認した。まだ原稿化・追跡validator化していないので次の作業で再検算する。u=X1+X2,v=X1-X2,z=X3とすると4F=f(u,z,D)+v²*(3u-(7g²-13)z-B)の形。全中心特異値をv=0枝と線形係数=0枝へ分けられる。前者は二変数cubicのcritical norm、後者は線上への制限cubicの判別式で計算できる見込み。これらの零点を即bad Dと同一視しない。

