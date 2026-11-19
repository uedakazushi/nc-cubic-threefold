# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v13。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回の変更前の確認済み基点は `76382805d3b0c4e6ed5b0d6fe9dfd0a133baca31`。証明は `papers/nc_cubic_threefold_moduli.tex`（v19）と入力節、補助的知識は `notes/research_notes.md`、検証範囲は `validation.json` に置く。

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究全体の価値を最大化することを最優先する。特定の方法・定理名・当初の完成像を守ること自体を目的にしない。重要な変更は、現在有効な理由、解決したこと、残った核心を整理して方針を書き直す。時系列の方針変更履歴は蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算観察、既知文献の入力を区別する。原稿に証明があること、今回読んだ範囲、計算を再実行したこと、第三者査読を同一視しない。仮定・依存結果・証明の所在を明示し、誤りは依存する本文・要約・方針に反映する。将来役立つ反例や障害は研究ノートに残す。一次資料で重要な引用の仮定を確かめ、既存結果との差をIntroductionに書く。初出・新規性が未確認ならその旨を明記する。

論文は日本語LuaLaTeXを基本とし、研究経緯ではなく現在の論理順で構成する。公表価値のある結果と証明を削除・要約して軽量化しない。研究ノートは現在有効な補題、例、計算、文献比較、障害を記す。研究継続用bundleは本方針、ノート、現行論文、必要なコード・小証明書・再現手順の自己完結的な一式とする。旧ZIP、旧稿、バックアップ、編集履歴、外部文献PDFの大量収録は不要。

研究区切りでの承諾不要の保存は許可済み。本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存し、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・中間物・キャッシュはGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Library上の既存ファイルの削除は許可された保存と別の操作であり、行わない。生成・検算・組版・commit・remote到達確認は別の状態として報告する。

以下はこの一般原則と区別した、現在の具体的な研究計画である。

## 2. 現在の目標と定義

**構造対象だけを標識したAbel圏 `(C,O)` のモジュライとして非可換三次三様体を扱い、そのKuznetsov成分から可換三次を復元し、失われる七次元の幾何を明らかにする。** 一般Jacobian族の滑らかな有限型17次元Deligne–Mumford stack `C_J=[J/PGL5]` と、全O-marked問題への完全忠実な射を構成した。その非空開 `U` から滑らかな可換三次の10次元粗モジュライ `M_cub` への支配的な射 `ρ` を証明した。さらに自己同型が自明なtargetの非空開 `V` とsourceを選べば `ρ:U→V` は相対次元7の滑らかな全射となる。étale局所的には三次族と相対dg Morita同値を持ち、残余圏・全compact tailsはいずれも相対dg smooth properである。

別に、13次元の滑らかなDM stack `B_J=[Y/PGL5]` への二次包絡射は階数4ベクトル束のtorsorである。17→10の七次元fiberと17→13の四次元fiberを区別する。可換三次点の全fpqc stack化後のframed Abel形式群oidは、17次元・接空間20次元のPfaffian形式環で表される。これらと固定剛体ambientの全四係数monomorphism、有限位数境界の4・15・16次元smooth proper族は有効な成果として保持する。

対象には許容三次豊富列の存在を要求し、その選択は記憶しない。射はOを保つ全完全線型同値である。標準模型の底変更は係数作用付き対象の圏で定義し、非Noetherian底では大きいQGrを用いる。内在的compact圏は `D(QGr A)^c`。中心二変数・二次中心rank3は非可換部分族の復元条件であり、可換点を全体の定義から除外しない。

全Abel Artin形式近傍にも実際の残余射rを構成した。既存の全Artin中心商表示と、CY orientationを必要としないcompact/proper模型を用いる。rに両立するPoisson形式近傍との非標準的同型があり、形式fiberは7次元・頂点接空間10次元のGr(2,5)アフィン錐である。また、ρ上の相対有理座標を選べば、実際の17次元非空開から非零Poisson構造付き三次の17次元モジュライへの支配的な射も存在する。選択を固定した後には全O保存同値と底変更に両立する。

point schemeの方向では、一次持上げ可能点をPoisson零点schemeと同定した。有限係数では楕円曲線と長さ24の完全交叉に分かれ、一般の埋込みpoint schemeからambient Poisson直線と五次元三次Casimir空間を復元できる。さらにshiftを付けた点対応からは二次包絡を復元し、有限係数のambient Poisson構造を尺度込みで回復できる。有限Hesse族のpoint schemeを零点schemeそのものにする方法には障害がある。

現在の核心は、このCasimir空間の中から量子中心に対応する三次直線を選び、補助的な選択を不要とし、非可換構造の量子化としての意味を保つPoisson持上げである。形式同型と実際の有理座標による射の一致・代数化、ρの一般fiberの双有理型、全Abelモジュライ内でのJacobian部分stackの位置は残る。尺度を忘れた射影Poissonモジュライは16次元であり、対象を混同しない。

## 3. 到達点・仮定・証明所在

| 内容 | 現行の証明所在 | 適用範囲と依存 |
|---|---|---|
| Oだけを標識した定義と全同値 | `abel_marked_moduli.tex` | 許容列の存在を要求し選択を忘れる。相対HomはC1–C4またはcompact版 |
| 全Artin Abel／section比較 | `abel_cubic_deformations.tex`, `thm:abel-cubic-all-artin` | DDL Thm4.5の適用。持上げの一意性は同型類の一意性 |
| 全Abel変形の平坦二次包絡 | 同節 `thm:abel-cubic-flat-envelope` | 滑らかな可換三次点。CFTの構成、実際の局所化、Yekutieli比較 |
| 任意係数の飽和・復元・相対AS | 同節 `cor:abel-universal-artin-model`, `cor:abel-universal-relative-cubic` | 非平坦・非Noetherian底変更を含む |
| 標準相対模型のArtin群oid | 同節 `thm:abel-canonical-relative-formal` | 全O-marked Abel変形群oidと同値 |
| 任意の平坦被覆上の線対象・復元 | `abel_formal_descent.tex`, `lem:abel-flat-cover-reconstruction` | 元のR→CにDDLを適用。Sのcoherent性不要、全係数Homと有限表示性も証明 |
| 全stack化後のArtin対象の大域模型 | 同節 `thm:abel-stackified-relative-formal` | 1+mの有限対数とAmitsur完全性、Hom・合成の通常の降下。一般の圏2降下を仮定しない |
| Framed自己同型の消滅・形式群oidの表示 | 同節 `prop:abel-framed-artin-automorphisms`, `cor:abel-full-stack-discrete-formal` | 二次関係と三次勾配のKoszul syzygyによる導分計算、小拡大帰納。未確認のHH¹制御定理は不要 |
| 可換点の形式環 | 同系と `cor:abel-cubic-formal-ring` | `C[[t_1,…,t_10,a_ij]]/(Pfaffian_4(a))`。次元17、接空間20、特殊ファイバー固定。完全交叉でない |
| 全twistの線対象コホモロジー | `central_pair_artin_formal_moduli.tex`, `prop:artin-ore-universal-cohomology` | 任意底変更、perfect RHom。n≥0はH0、n=−1は零、n≤−2はH3 |
| 四係数族の有限中心・普遍的中心と飽和 | `finite_order_relative_categories.tex` | PBW・有限位数THCR境界を入力。全中心の底変更可換性は要求しない |
| 全四係数族の相対SerreとHom | `relative_serre_duality.tex`, `thm:relative-serre-projective`, `cor:central-model-relative-hom` | 局所Perf上でS≅(−2)[3]、Noetherian底変更。既存PBW・AS・CY入力 |
| 四係数空間のmonomorphism | 同節 `prop:rigid-four-family-monomorphism` | 全A4、非被約な有限型C基底を含む。既存複素点剛体性とCartier |
| 非空開上の元のC3 | `finite_order_relative_categories.tex`, `prop:central-model-intrinsic-perfect-open` | 一般正則性の入力下で有限係数Tor圏=局所Perf |
| 直接的平坦性判定・平方零消滅 | `abel_cubic_deformations.tex`, `thm:abel-degree-three-propagation`, `thm:abel-square-zero-degree-three` | 非周期的Z代数。平方零ではF≠0のみ。全Artin定理と独立の証明を保持 |
| 有限係数族・周期性 | 主原稿 `thm:17`, `thm:pair-route-gcd` 等 | 41→37、17→13、一般fiber4、gcd周期性の有効な証明を保持 |
| 有限中心なしの普遍的相対Serre | `koszul_relative_duality.tex`, `thm:koszul-cubic-relative-serre` | 有限射影Koszul対角解消、指定CY5同型、中心正則三次商の四入力。任意の可換係数環、compact全体で成立 |
| 実際の17係数族の相対入力 | `jacobian_abel_comparison.tex`, `prop:general17-universal-pbw`, `prop:general17-relative-cy-koszul` | 明示したΔ≠0上。potential複体の自己双対と中心二変数のKoszul複体。有限位数性・有限中心を使わない |
| 普遍二次中心・偶数Gabriel・許容性 | 同節 `prop:general17-universal-saturation-center`, `lem:general-even-gabriel-reconstruction`, `prop:general17-abel-admissible` | 飽和と復元は任意係数。Noetherian係数ではstrong noetherian・豊富性。実際の標準相対模型を与える |
| 一般族の全O保存同値と有限表示 | 同節 `thm:general-relative-pointed-hom`, `cor:general-relative-isom-scheme` | 任意C代数上のfpqc層 Eq_O=Isom_gr/Gm。二次・三次関係を保つPGL5の閉部分スキーム |
| 17次元Abel圏変動と17→13の両立 | 同節 `cor:general17-abel-moduli-comparison` | Δ開と既存slice開の共通部分。同型類のRosenlicht次元17。二次包絡は全O保存同値に自然 |
| 代数的ambientのétale atlas | `jacobian_moduli_chart.tex`, `prop:jacobian-ambient-etale-chart` | `PGL5×T_B→Q113` のétale locus、非空不変開Y。13次元DM stack。指定有理点の微分同型を厳密検算 |
| 一次・三次中心の任意底変更 | 同節 `prop:general13-universal-centers` | Δ開の低次THCR中心、PBW分裂、交換子写像の局所分裂単射。非平坦底変更を含む |
| 実際の17→13射 | 同節 `prop:jacobian-affine-four-morphism` | 中心完全列の分裂torsor。中心重みの相殺により階数4ベクトル束がPGL商へ降下 |
| 17次元の代数的Abel部分モジュライ | 同節 `thm:jacobian-algebraic-abel-substack` | 有限関係窓と全Hom比較、PGL scalar coherence。任意係数で完全忠実、全M内の開性・局所閉性・成分性は未証明 |
| 有限中心模型の大域dg smooth性 | `dg_smooth_torsion_families.tex`, `prop:seed-finite-central-global-smooth` | 完全体上有限型分離Y、coherent代数、左右Dbcoh=Perf。ELS4.18の外積生成と対角kernelのdg Morita比較 |
| 一般点からの相対smooth proper開 | 同節 `lem:dg-generic-spreading`, `lem:dg-smooth-field-descent` | 係数上perfectなdg代数。TV2.10の連続性、compactなsourceからの射降下、係数-perfect cone。hfpを仮定しない |
| 有限位数境界上の4・15次元相対開 | 同節 `prop:seed-fixed-ambient-relative-smooth`, `prop:seed-torsion-base-relative-smooth` | 固定ambient、または固定境界の全混合係数。左右の幾何学的一般正則性、有限中心模型、一般点の対角、任意係数変更 |
| 稠密に分布する16次元smooth proper族 | 同節 `thm:seed-sixteen-dimensional-dense-families` | Hesse族のtorsion曲線Z上でZ×A15の非空開。atlasの任意の非空開W内にもそのような16次元族がある |
| smooth proper複素点の稠密性 | 同節 `thm:seed-smooth-points-dense` | 17次元atlasおよびC_Jで成立。一般点のsmooth性は下記の残余射により別に証明 |
| 相対Kuznetsov成分・Serre・降下 | `kuznetsov_relative_category.tex`, `thm:relative-kuznetsov-projector` 等 | 二例外対象の有限mutation、両側随伴、係数perfect generator、任意導来底変更。O(1)の基底線束twistは評価で相殺 |
| 可換三次成分の全Artin認識 | `kuznetsov_moduli_morphism.tex`, `prop:kuznetsov-formal-recognition` | Kuznetsovの全HH表、JLLZの実際のKS同型、Lurieのtame比較。π0の同定でありscalar π2は残る |
| 形式同値の効果化と生成性 | 同節 `prop:kuznetsov-effective-serre-embedding`, `lem:kuznetsov-graded-thick-simple` | Bhattの係数Perf効果化、相対dg Serre比較、Stevensonの孤立hypersurface分類とgraded化。一般的なcompact-kernel効果性やgenerator開性は不使用 |
| 17→10の支配的な射・滑らかな七次元fiber | 同節 `thm:kuznetsov-cubic-moduli-morphism` | 実際の代数的量子化族、Euler−9、函数体単射、perfect核の有限表示降下、categorical Torelli、35次minor |
| 17次元族の非空開上のdg smooth proper性 | 同定理と `kuznetsov_relative_category.tex` | 幾何的Kuとのétale局所Morita同値、相対Kronecker5 gluing、任意導来底変更 |
| 全Abel Artin近傍上の実際の残余射 | `poisson_cubic_lifts.tex`, `prop:abel-artin-actual-residual` | 全Artin中心商模型、CYを用いないKoszul/torsion生成性、普遍線Hom、O(1)持上げ一意性、Ku全Artin認識 |
| 残余射に両立するPoisson形式同型 | 同節 `cor:abel-poisson-formal-lift` | 量子化比較Qと形式逆写像Θ。rのfiberはGr(2,5)錐の完備化、次元7・接空間10。非標準的 |
| 相対Poisson錐のschemeとしての構造 | 同節 `prop:relative-poisson-cubic-cone` | MayanskiyのSchouten式、相対勾配の分裂単射。任意底変更と両立。非零部分は滑らかで相対次元7 |
| 実際の開上の非零Poisson持上げ | 同節 `thm:noncanonical-poisson-cubic-lift` | ρ上の相対超越基底による非標準的な支配射。scheme atlas合成は縮小後étale。双有理性は未証明 |
| 単純な対称化逆像の障害 | 同節 `prop:poisson-naive-symmetrization-fails` | 中心Fermat三次の明示式からPoisson idealでないことを代数的に証明。射影chartでも確認 |
| 点加群の一次持上げと零点scheme | `point_scheme_poisson.tex`, `prop:first-order-point-poisson-zero` | 平坦な二次一次変形・Poisson括弧・滑らかな中心三次。任意非被約T上で局所的な存在と同値。高次・一意性は含めない |
| Poisson零点のE⊔D分解 | 同節 `prop:poisson-zero-elliptic-polar` | Xと基底平面三次Eが滑らか。D=(F,Fx,Fy,Fz)は長さ24の完全交叉。一般に被約、特殊例では非被約 |
| 有限係数の点対応と長さ24 | 同節 `prop:central-two-point-scheme`, `prop:fermat-point-scheme` | u,v中心、境界は固定点なしの楕円graph、wが境界点加群を消す。D_wが真の三次切断 |
| 点対応からの二次包絡・尺度込みPoisson復元 | `point_scheme_poisson.tex`, `prop:point-correspondence-quadratic-recovery` | 境界smooth graph、D_wがCI。H⁰(I_Γ(1,1))=R_B。graph開でΠ_fin=hΠ_Fを復元。有限σのlogは不要 |
| 点schemeからPoisson直線とCasimir空間を復元 | 同節 `prop:point-gradient-reconstruction`, `cor:point-full-casimir-space` | 埋込みschemeを使用。非ST境界、Hesseではλ(λ³−8)≠0。R_Q=kF⊕Sym³U、dim5。特定三次・尺度は未選択 |
| 相対復元と全O保存同値への自然性 | 同節 `prop:point-recovery-relative-descent` | 既存Jacobian locusの開。任意底変更、GL同変、全Hom比較を使用。中心重みのある束自体のPGL降下は主張しない |
| Hesse族の埋込み零点非実現性 | 同節 `prop:hesse-point-zero-nonrealization` | h≠0、古典・量子境界smooth、有限成分CI。どのsmooth cubicへ替えても同じ埋込み零点にはならない |
| 半古典極限とshift速度 | 同節 `cor:fermat-point-flat-closure`, `prop:jacobian-modular-shift-comparison` | Fermat平坦閉包の特殊fiber=Z(π₀)だがPt(A₀)=X₀。指定経路でσ′₀=Res_mod/2。有限σの対数は扱わない |

現在の点検はpoint schemeの一次持上げ、E⊔Dのscheme分解、偏微分空間からの復元、Hesse非実現性、modular residueとの比較に集中した。別々の読み合わせで、非被約基底の持上げ・中心chartの単元・nilpotentの消去・未知の基底平面の強制・Casimirの分母消去を確認した。Hesse行列式と補正式等の9項目は、新しい厳密記号計算で全て確認した。二次包絡復元は楕円曲線上の線束乗法の全射性による証明を点検した。既知Jacobian Torelliとmodular residue自体は新規成果としない。外部査読・旧全証明の独立再証明・新規性の網羅調査は未完了である。

一般の係数perfect dg代数について「特殊ファイバーsmoothなら一般ファイバーsmooth」という命題(FS)は偽である。反例と、形式compact性・generator開性の別の障害をノート§1.8.2に保存する。上の定理は(FS)に依存せず、相対Serreと三次三様体固有の生成性で証明する。

## 4. 現在の方針を採る理由

Abel圏を直接扱うための相対Serre、全O保存同値、有限表示Isomと代数的部分stackは完成した。一般族の個々の圏のdg smooth性については、有限位数境界の稠密性だけでは一般点に進めない。そこで可換三次への量子化退化を用い、残余圏を通じて幾何性を回復する。形式的に幾何的なKuを認識し、係数perfect複体として同値核を効果化すると完全忠実な埋込みが得られる。相対Serreのtrace比較と、Serre安定な非零thick部分圏はKu全体になるという生成補題が全射性を与える。

この構成は17次元一般点へ函数体単射で届き、有限表示の降下により非空開へ広がる。Torelliにより三次の同型類が一意なので、核の選択に依存せずモジュライ射が降下する。したがって元の目標のうち、17次元の非空dg smooth proper開と可換三次モジュライへの射は解決した範囲である。全M内の開性・局所閉性・成分性、七次元fiberの具体的分類は残る。

可換点の全Abel模型には既存の比較定理から通常の中心商表示を選べる。残余操作には左mutation、compact generator、係数perfect Homがあれば足り、相対Serreを再構成する必要はない。この区別により全Abel形式近傍の残余射と、その射に両立する形式Poisson同型まで完成した。非周期的表示であること自体をこの構成の障害とはしない。

実際の開上のPoisson持上げは、相対有理座標の選択で存在するが、それだけでは量子化を記憶する幾何学的対応にならない。中心三次の完全対称化逆像には反例があり、point scheme全体を零点schemeとして一致させる方法にも一般Hesse族で障害がある。一方、埋込み点データからambient Poisson直線と五次元Casimir空間を復元できた。したがって点対応を入力にする方向を優先し、その空間の中の中心三次の補正と、Kuが復元する三次との一致を扱う。有限係数の尺度は点対応から復元でき、指定経路の半古典的規格化とは区別する。元のPoissonモジュライ射の存在は非標準的な意味で解決しており、内在的・量子化に両立する射は残る。

O(1)自体を商stack上へ降下させずとも、その基底直線束twistはmutationの評価で消える。これが全O-marked Abel同値に自然な残余圏を取れる理由である。targetの自己同型が自明な開へ制限すれば、粗モジュライへの射は通常の三次モジュライstackへの射ともなる。相対Morita核はétale局所で構成し、大域的な核の存在は結論に含めない。

## 5. 優先課題と達成基準

### P1：量子化としての意味を保つPoisson持上げ

まず `point_scheme_poisson.tex` の復元を使う。埋込みpoint schemeの唯一の曲線E_hと有限成分DからU=I(E_h)_1、Q=I(D)_2を取り、R_Q={G:∂_W G⊂Q}=kF⊕Sym³Uを復元した。この部分は証明済みであり、HesseでのHessian一意性はUeda–YoshinagaのJacobian Torelliの具体化である。

次は、量子中心直線と有限成分の三次イデアル I(D)_3/(V·Q) を、R_Qの特定の三次直線へ補正付きで対応させる。Fermat/Hesse中心の既存公式とHessian補正を使い、まず分離型で候補を定め、mixed係数・中心平行移動・binary cubic加算への変換則を調べる。I(D)_3の三次代表をそのまま古典Casimirにしてはならない。原点のない四次元torsorに標準的な切断が存在するかも別に確認する。

有限係数の尺度はpoint correspondenceから復元できる。H⁰(I_Γ(1,1))=R_Bと二次関係のskew/symmetric graphを使えば、Π_fin=hΠ_Fを得る。これはfinite σの対数を取る操作ではない。指定した量子化経路での半古典構造Π_Fとの比較は、σ′₀=Res_mod/2という一次の式で行う。達成基準は、復元したCasimir空間の中の三次直線を全O保存同値に自然に選び、その三次がρの出力と一致することを証明すること。ambient Πの復元だけをPoisson構造付きcubicへの射の完成と扱わない。

並行して固定Ku(X)と五矢Kronecker圏の接合双加群を調べ、七方向の内在的意味を探る。形式fiberはGr(2,5)錐と分かったが、一般の代数的fiberの双有理性、超越基底による有限拡大の次数1、既存の四次元torsor上でのρの挙動は未証明である。

### P2：Jacobian部分stackの全Abelモジュライ内での位置

滑らかな可換点の全Abel Artin比較、実際の残余射、rの形式fiberは完成した。一般非可換点では、全Abel変形群oidと有限関係窓の変形群oidを比較する。接空間一致だけを成分判定に用いず、小拡大の持上げと障害を扱う。全M内での開性・局所閉性・成分性の必要十分条件を得ることが達成基準である。有限stabilizer、対角の有限性、分離性も別々に調べる。

可換点で選んだPoisson形式同型の収束・代数化、有限Aut(X)作用との両立、frameを外したstack上の比較も独立に確認する。形式同型の存在と、一般点の代数的な同型を混同しない。

### P3：公表単位・先行研究・内在的復元

中心結果として、(a)全Abel三次変形の二次包絡とframed形式近傍、(b)相対双対とJacobian型代数的Abel部分モジュライ、(c)Kuznetsov成分による17→10射とPoisson持上げ・七次元fiber、(d)point schemeとPoisson零点・Jacobian復元を検討する。論理的なまとまりと新規性を調査して分割・統合を決める。正規超曲面対の周期、既存の有限中心結果など有効な証明は保持する。

Kuznetsov/JLLZ/Lurie/Bhatt/Stevenson/Orlov/Neeman/BMMSとPBW・CY・連続性の一次入力は、各定理の仮定と本研究の追加部分をIntroductionとノート§11で比較する。初出・新規性の網羅調査、第三者査読、旧PBW/CY・全Artin量子化入力の独立全面監査は未完了。Oを忘れた復元、特異三次への拡張は別課題である。

## 6. 再開時の具体的着手

1. 本方針の後、ノート§10.7、`point_scheme_poisson.tex`、§10.6と `poisson_cubic_lifts.tex` を読む。今回の主線は一次零点、E⊔24、Casimir復元、有限係数の障害、shift/residueの順である。
2. P1は五次元空間R_Qと量子中心三次の比較から始める。`central_pair_explicit_centers.tex` の公式を用いて、I(D)_3/(V·Q)からの補正候補を作る。Fermatでのsym⁻¹反例とHesseのB−3λA=h²(1+λ³)を再発防止の制約にする。
3. 論文に記載した一次持上げ・相対復元は再証明せず、特定のCasimir直線の選択とρとの一致を調べる。尺度込みambient復元には点対応の双線型イデアルを使う。接合による方法ではG_i=L_O L_O(1)(O(i))、i=2,3,4のHomから七方向の変形複体を作る。
4. P2は一般非可換点の全Abel変形を扱う。既存代数的atlasは§1.6–1.7、smooth性は§1.8。§1.8.2の反例により一般(FS)、compact核の無条件効果化、generator開性を使わない。
5. 新しい厳密式の再現は `python3 computations/verify_point_poisson.py --output build/point_poisson.json`。既存24計算資産は保持し、具体的なリスクがない限り再実行しない。

## 7. 主張の境界

一般族の結論は明示Δ開の標準模型と、その中のétale開 `T_B^e` からfpqc局所的に得られる族についてである。`C_J` 自体の有限型代数性・smooth性・次元17は証明したが、全Mの代数性やその中の開性・局所閉性・成分性は未証明である。全17係数空間の全点、任意のGrothendieck圏、Oを忘れた圏、裸の導来圏へ拡張しない。次数スカラー商はfpqc層商であり、大域点集合の単純な商ではない。Veroneseのμ2はGmに含まれ、追加2慣性ではない。

中心一次束Uと三次束Eの中心重みは1と3であり、それら自体をPGL商へ通常のベクトル束として降下させない。Hom(L,Sym³U)の重み0だけが必要である。source上のO(1)や無捩れなSerre式の大域降下も結論しない。targetの可換三次族のambientは、ω_B/V(2D)がfiberwise O(1)となるため射影束へ分裂する。このtarget上の結論とsourceの線対象の降下は区別する。周囲を同定まで固定した2-fiberはA4 torsorだが、周囲の同型類だけを固定すると有限自己同型の作用が残り得る。
Serre自体はcompact圏上の主張であり、全Db(coh)の有限大域次元やdg smoothnessは含まない。dg smooth性は有限位数境界上の相対開に加え、残余射の定理により17次元の非空開でも別に証明した。16次元族はatlasの局所閉部分スキームであり、独立の閉部分stackや17次元開と同一視しない。相対CY/AS性と非正則基底を含む絶対的大域次元を混同しない。有限中心模型では中心準同型の単射性や全中心の底変更可換性を仮定しない。

Abel圏側の可換点の全形式比較は、滑らかな複素三次Xを固定したframed Artin近傍である。frameを忘れた有限Aut(X)作用、未切断2群oid、一般の圏2降下、代数化へは広げない。四係数空間のmonomorphismも開埋込み・成分・atlasを意味しない。

point schemeの比較は埋込みデータと指定Jacobian模型に関する。抽象point schemeだけの復元、全NC圏での内在的な点対象の認識、finite hからのcanonical semiclassical parameterは結論しない。FermatのD_hは24個の被約点ではなく3個の台に局所長8を持つ。

## 8. 再現と検証範囲

`python3 scripts/verify.py` で参照・引用・TeX入力の閉包を検査する。既存のatlas点の小証明書は `python3 computations/verify_jacobian_etale_point.py --output build/jacobian_etale_point.json` で再現し、`computations/jacobian_etale_point_certificate.json` と比較する。2026-11-19の既存検証で実行し、Dの37次minor=127524、Mの113次minor=844194（ともにmod1000003）、整数上のMD=0、唯一のGLスカラー核、全Δ因子の非零を確認した。小証明書には入力・helper・sourceのhashを含める。M113の再計算は新script内で行い、旧scriptの全再実行とは区別する。

同日の `verify_general17_open.py` の九項目と2026-11-16の既存八計算は有効な検証として保持し、今回の再実行とは扱わない。圏論的な降下・中心束・全Hom比較には書かれた証明と読み合わせがあり、数値検算による証明とはしない。既存の残余射の証明には文献の仮定確認と別々の読み合わせがある。同日の先行検証では `python3 computations/verify_commutative_dominance.py --output build/commutative_dominance.json` を実行し、35×42微分行列の35次minorが752849 mod1000003であることとEuler関係を確認した。証明書は入力・source・helperのhashを含む。これは支配性の計算であり、圏の同値を数値計算で証明したものではない。既存の計算は今回再実行していない。新しい `verify_point_poisson.py` はSymPyの厳密式で行列式・Hessian補正・非実現性係数・rank8 minor・shift速度等を検算する。小証明書 `point_poisson_certificate.json` にsource hashと入力式を残し、scheme論的・圏論的証明とは区別する。

組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォント、既存計算にはPython3・SymPyが必要。atlas検算と新しい支配性検算はPython3標準ライブラリと同梱helperを使う。同日の先行組版試行は `lualatex.fmt` 不在で本文処理前に停止した。現行v19の組版は実行しておらず、現行PDF生成・視覚確認は未完了である。実施した範囲と未解決点は `validation.json` に記す。
