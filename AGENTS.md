# Codex研究指示 — 非可換三次三様体のAbel圏変形・モジュライ・残余比較

2026-11-21 / research-plan-v18。GitHub mainが正本。再開時は `00_research_plan.md`、主稿Introduction、`notes/research_notes.md` §12、`validation.json` を読む。主稿は `papers/nc-cubic-threefold.tex`（v23）。各数学課題の入口は研究方針§4–5にある。

## 最優先の判断基準

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。現在の目標は、構造対象Oだけを標識したAbel圏としてnc cubic threefoldのモジュライを定め、実際の射・全Artin変形・二次包絡の比較を完成すること。17次元族のsmooth proper開と残余圏の幾何化は達成した。全Abel形式残余とPoisson形式fiberも達成し、実際の開上の非標準的なPoisson持上げも得た。公表前の証明点検・文章の完成を優先し、内在的Poisson持上げと全Abelモジュライ内の位置を次の数学的目標とする。

## 研究間の分担・正本

- 正本は改名後の `uedakazushi/nc-cubic-threefold` の `main`、主原稿は本文のある `papers/nc-cubic-threefold.tex`。日本語LuaLaTeX、著者欄空欄。全$n\ge3$の証明は `nc-cubic`、古典正規形は `poisson-cubic`、量子化存在は `cubic-quantization` を引用する。三様体に固有の**全Abel Artin形式変形と残余射の実際の代数化**を中心にする。
- `nc-cubic` の$n=3$の良い一ブロックstackが本repoの$\mathfrak C_J$とどの開で同一か、および$\rho$が$\operatorname{forget}\circ\Psi_{\mathrm{res}}^{\mathrm{sc}}$に一致するかは未確認。全次元の定理の$n=3$特殊化・最小次数や残余射の次数をこのrepo固有の新定理として再証明・再計上しない。
- 点スキームに固有の論文・ノート・計算・証明書は本repo内の `papers/mixed-cubic-point-schemes.tex` と `papers/diagonal-cubic-point-geometry.tex`、`papers/point/`、`notes/point_schemes.md`、`computations/point/` を正本とする。`nc-cubic-point` は旧リポジトリで削除予定、研究再開時に依存しない。`pfaffian-brill-noether` のTorelli/Pfaffian、`nc-cubic2` の相対復元は独立研究の正本として保持し、内容の重複が立証できない限り削除・移管しない。ここには要点と正確な定理の出典を記す。
- 再開時は [research-hub](https://github.com/uedakazushi/research-hub) の研究間分担を確認し、本repoの `00_research_plan.md` を最初に読む。研究区切りには本repoの原稿・方針・ノート・READMEを先にmainへ保存し、次にhubの到達点・確実性・核心・次の一手・依存・再開先・実確認日を更新する。他の研究の変更を保持し、双方の反映を別に確認する。

## 点スキーム論文と旧リポジトリ削除の運用

- 主原稿は `papers/nc-cubic-threefold.tex` のまま。独立した点スキーム二稿は `papers/mixed-cubic-point-schemes.tex` と `papers/diagonal-cubic-point-geometry.tex`。必要な証明を保持し、一つの主原稿へ無理に結合しない。別論文としての役割を方針・README・引用に明示する。
- `python3 scripts/check_point_schemes.py` は二稿の入力・参照・引用を検査し、`--calculations` は有限検算、`--build` は両稿のLuaLaTeX組版を実行する。移管前の検証を移管後の成功と誤記しない。
- `nc-cubic-point` リポジトリの内容を旧正本としない。旧repoの削除は新repoの現行内容・必要な証明書と参照を確認してから。GitHubの接続でリポジトリ自体を削除できない場合は、旧repoを案内専用にして残し、管理画面での削除が必要と正確に報告する。既存研究の全ファイルを衝動的に削除しない。

## 直近の優先順位

1. **公表前検証と推敲。** 主稿 `papers/nc-cubic-threefold.tex` のIntroductionにA–Dを集約する。相対Koszul/CYからSerre trace、全O保存同値、atlas、残余射という依存鎖、全Artin模型、および有限中心・相対圏・大域smoothness三節の重点点検範囲を保持する。次は ambient_periodicity.tex と period_forgetting_moduli.tex の周期選択、正規族との可換性、相対降下を点検する。一般の未解決分類や内在的逆量子化の完成を公表の前提にしない。主稿の3部と証明を保持した付録という構成を尊重する。
2. **量子中心に対応する古典三次。** 点schemeからU,Q,R_Qと[Π]、shift付き対応から二次包絡とhΠ_Fを復元した。次は量子中心直線をR_Q内へ補正し、ρの出力三次との一致を示す。Hesseの有限点schemeの零点非実現性とsym⁻¹反例を制約とする。有限σのlogは使わない。相対超越基底による非標準的持上げは一般論の命題として扱う。
3. **七次元fiberと全M内の位置。** 接合双加群と既存17→13 torsorの関係を調べる。一般非可換点の全変形は小拡大・障害を含めて比較する。C_Jは可換点を含まず、次元17の一致だけで成分性を宣言しない。全Mの代数性、開性・局所閉性、有限対角、分離性は未解決。
4. **入力と検証の状態。** 一般(FS)、compact核の無条件形式効果化、generator開性はノート§1.8.2の反例により使わない。係数Perfを先に効果化しsmooth targetと相対Serreを使う。主要節の読み合わせ、引用仮定確認、計算実行、組版、外部査読を区別する。初出・新規性の網羅調査と全証明の独立監査は未完了。

H3三次曲面分類は `uedakazushi/nc-cubic-classification` の独立課題。

## 定義・主張・検証

O-markedは豊富列の存在を要求し選択を忘れ、射にはOを保つ全完全同値を含める。既存M^ptは列保存を残す別問題。中心二変数・3次元二次中心は非可換部分族の復元仮定であり、二次中心15次元の可換点を全体の定義から除外してはならない。

偶数Veroneseのμ2は次数スカラーGmに含まれ、O-marked圏の追加2慣性ではない。相対商は層商であり、大域点集合の商と区別する。Serre式の基底線束、同型のH1障害と対象のH2障害を保持する。

DDL全Artin比較は既知定理の適用。O-marking忘却の同値は自然同型で割った1群oidの規約で述べ、未切断2-groupoidには拡張しない。滑らかな可換三次点では全Abel Artin変形が相対AS三次incidenceの本質像に入り、同型類関手は17次元・接空間20の環で表される。CFTの構成とYekutieliの既知比較を明示する。各Artin模型は任意の係数変更後にも飽和・復元・相対AS条件を満たす。標準係数族と全Abel変形群oidは同値。固定圏の対象・射の降下と圏の族自体の有効降下は別である。滑らかな可換点のframed Artin近傍については、元のArtin基底でDDLを適用し、1+mのscalar cocycleを対数とAmitsurで消してHom・合成を降下することで大域模型を得た。二次関係と三次勾配の正則列による導分計算からframed自己同値の自然同型類も自明であり、全形式群oidは離散なSpf R_Xとなる。有限Aut(X)の商、非切断2群oid、一般の非可換点、大域代数性へ拡張しない。

一般17係数族の明示Δ開では、有限Koszul対角解消と真正なCY同型を全係数環で構成した。A側のtorsion双対をdg局所化の両側へ移してSerreを得る。偶数Gabriel右随伴により、全S上で実際の完全Abel同値を復元する。有限表示Isomに加えて、PGL5×T_B→Q113のétale locusの飽和Yと中心三次直線Jを用い、[J/PGL5]という有限型17次元DM全部分stackを構成した。全Mの代数性やその中での開性・局所閉性・成分性は未確定。普遍PBWの閉点検出は被約な有限型の普遍基底で行い、そこで得た分裂を任意底変更する。CYの符号は `eq:general17-cy-chain-signs`、全偶数section Z代数の整合は `eq:abel-even-section-coherence` を参照する。

中心束U,E,LにはGLの中心重みがあり、そのままPGL商上の通常の束としない。Hom(L,Sym³U)は重み0で降下し、C_J→B_Jはそのtorsorである。O(1)、無捩れなSerre式、大域的な原点の降下は未証明。周囲の同定付き2-fiberと、同型類だけを固定した有限自己同型商を区別する。B_Jはprojectively gradedなambient問題であり、ambientの全O保存Abel同値を分類したとはしない。

四係数族の全体で使う内在的圏は非有界導来圏のcompact対象である。元の有限係数Tor部分圏との一致は非空正則開上の別結果。monomorphismは開埋込み・成分性・atlasではない。相対双対の初期基底変更はambient導来圏で扱い、振幅集中とflatnessを得てから真正な双加群同型へ移る。

有限中心Cの任意底変更後は中心準同型C_S→Z(A_S)だけを使い、単射や全中心の底変更可換性は仮定しない。非Noetherian底には大きいQGrを使う。big QGr≃QCohとcompact=局所Perfは任意係数で成立し、coherent部分・locally Noetherian性・偶数豊富列による全射比較はNoetherian底で述べる。相対アフィン対角のperfect性を大域dg smooth性と同一視しない。有限中心模型の大域smooth性は、左右Dbcoh=PerfとELS4.18の外積generator、対角kernelのMorita比較によって別に証明した。torsion曲線上の16次元族はatlasの局所閉部分スキームであり、17次元開や独立の閉部分stackを主張しない。

橋渡し族のh≠0上では17係数族の関係式に移るが、指定Δ開・étale chart開の逆像へさらに制限する。d(h)≠0だけでは量子楕円境界は滑らかとは限らず、a=1/6,b=0,h⁶=−1728が反例である。係数基底は通常の可換C代数で、導来底変更はその射に沿う導来テンソルを指す。主定理Cの可換点は全Mに属し、C_Jには属さない。点復元の開C_J,ptと残余射の開Uは既約性により非空に交わる。

Poisson持上げは、尺度を記憶する17次元の標的を用いる。射影化した標的は16次元である。相対Poisson錐のscheme方程式はSchouten–Plücker式と勾配の局所分裂単射から得る。可換targetのambientはω_B/V(2D)により射影束へ分裂するが、source上のO(1)降下とは区別する。実際の持上げは選択後には全O保存同値と底変更に両立する。選択独立性、NC交換子との半古典的意味、ΘQ⁻¹との一致は別の課題である。Pymの解析芽同型、Yekutieliの完備局所parameter上の比較を、この特定の大域代数的射と同一視しない。

point schemeの復元には埋込みとscheme構造を使う。Fermat有限部分は3個の台×長さ8で、24個の被約点ではない。R_Qのrank5はJacobian locusの開で述べ、全Grassmannianの開性としない。Ueda–Yoshinaga/HwangのJacobian復元原理、Vancliffの一定point scheme仮定、Gualtieri–Pymのmodular residueを既知結果として明記する。相対CYの40自由語・6項目、中心式、17係数開、点Poisson・étale点・Eulerの検証情報を保持し、本版では再実行していない。今回実行したのはノート§1.8.1の橋渡し開条件の厳密計算である。正本を `validation.json` に置く。

原稿の証明、今回の点検、計算、新規性確認を区別する。追加定理は明記した仮定の下で証明し、初出は未確認。有限Artin基底上の相対ASと絶対global dimension、体上のregular tailsと相対dg smooth proper性、実際のgraded17次元族と裸の導来圏の次元を混同しない。接空間同型だけで成分性や全Artin同値を宣言しない。

## 成果物と保存

日本語LuaLaTeXの現行原稿、現在有効なノート、方針、必要なコードと小証明書へ統合し、履歴の追記集にしない。価値ある証明を削除して軽量化しない。必要な検証を行い、未実行・失敗を明記する。

研究区切りで承諾を再要求せず、通常のfast-forwardでmainに直接保存し、remote SHAと内容を確認する。GitHub Actions、PR、force push、追跡するPDF/ZIP/中間物は禁止。GitHub保存成功時にはLibraryへ重複保存せず、失敗時のみ緊急退避する。約15分のcheckpointは保存の目安であって終了条件ではない。別セッションの自動起動は保証しない。
