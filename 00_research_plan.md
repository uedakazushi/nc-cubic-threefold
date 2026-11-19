# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v8。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回の変更前の確認済み基点は `48a1e3ecafa491a0cf93a69f973eeb88863bc681`。証明は `papers/nc_cubic_threefold_moduli.tex`（v14）と入力節、補助的知識は `notes/research_notes.md`、検証範囲は `validation.json` に置く。

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究全体の価値を最大化することを最優先する。特定の方法・定理名・当初の完成像を守ること自体を目的にしない。重要な変更は、現在有効な理由、解決したこと、残った核心を整理して方針を書き直す。時系列の方針変更履歴は蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算観察、既知文献の入力を区別する。原稿に証明があること、今回読んだ範囲、計算を再実行したこと、第三者査読を同一視しない。仮定・依存結果・証明の所在を明示し、誤りは依存する本文・要約・方針に反映する。将来役立つ反例や障害は研究ノートに残す。一次資料で重要な引用の仮定を確かめ、既存結果との差をIntroductionに書く。初出・新規性が未確認ならその旨を明記する。

論文は日本語LuaLaTeXを基本とし、研究経緯ではなく現在の論理順で構成する。公表価値のある結果と証明を削除・要約して軽量化しない。研究ノートは現在有効な補題、例、計算、文献比較、障害を記す。研究継続用bundleは本方針、ノート、現行論文、必要なコード・小証明書・再現手順の自己完結的な一式とする。旧ZIP、旧稿、バックアップ、編集履歴、外部文献PDFの大量収録は不要。

研究区切りでの承諾不要の保存は許可済み。本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存し、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・中間物・キャッシュはGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Library上の既存ファイルの削除は許可された保存と別の操作であり、行わない。生成・検算・組版・commit・remote到達確認は別の状態として報告する。

以下はこの一般原則と区別した、現在の具体的な研究計画である。

## 2. 現在の目標と定義

**構造対象だけを標識したAbel圏 `(C,O)` のモジュライとして、可換三次三様体と非可換Jacobian族を統一し、実際の射・変形・二次包絡を比較する。** 一般17係数族の明示した非空開集合上で、任意の係数変更に両立する相対Serre双対と、全O保存Abel同値の比較を証明した。従って既存の17次元graded同型類の変動は、O-marked Abel圏同型類でも17次元であり、二次包絡への17→13射もこの同値関係と両立する。

可換三次点の全fpqc stack化後のframed形式群oidは、17次元・接空間20次元のPfaffian形式環で表される。固定剛体ambientの全四係数族のmonomorphismも保持する。次の核心は、有限表示された相対Isomを使った一般族の代数的部分モジュライの構成、dg smoothな非空開の判定、実際の残余射である。

対象には許容三次豊富列の存在を要求し、その選択は記憶しない。射はOを保つ全完全線型同値であり、列保存の問題と区別する。標準模型の底変更は係数作用付き対象の圏で定義し、非Noetherian底では大きいQGrを用いる。比較に使う内在的部分圏は `D(QGr A)^c` である。中心二変数と二次中心rank3は非可換部分族の復元条件であり、二次中心15次元の可換点を全体の定義から除外しない。

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

新しい二節の局所コホモロジー、真正な双加群双対、dg局所化、実際の相対CY/PBW入力、全Hom比較を別々に読み合わせた。原稿にある証明と今回の点検を区別する。既存の量子化・形式環・全PBW証明書・剛体性の全証明を今回再実行・再証明したとはしない。初出・新規性の網羅調査と第三者査読は未完了である。

## 4. 現在の方針を採る理由

一般族への拡張を阻んでいた有限中心性は、有限Koszul対角解消によるtorsionの有界模型で置き換えた。中心三次商の局所双対をA双加群として作り、dg局所化A→Qの両側へ移すと、compact全体のSerre pairingとtraceが得られる。実際の17係数族には、三変数potential複体の自己双対と中心二変数のKoszul双対がこの入力を供給する。体値のCY性だけから相対同型を推測していない。詳細はノート§1.6と現行論文に置く。

このため、一般族の全同値比較は解決した範囲として扱う。相対IsomがPGL5内の有限表示閉部分スキームになったことを、代数的部分モジュライを作る次の入口とする。ただし、二つの既知模型間の射が表現可能なことから、全モジュライのatlas・代数性・成分性は従わない。

有限中心の四係数族では、局所アフィン対角や有限係数Tor振幅との比較も得られる。その幾何的内容は新しい双対証明とは異なるので保持する。明示Δ開は固定B_*を含むとは限らず、既存の四係数結果を削除しない。可換点の形式降下・framed自己同型消滅も解決済みとして保持する。

## 5. 優先課題と達成基準

### P1：一般17係数族の代数的部分モジュライとambient射

全同値比較を基礎に、実際に構成された模型の範囲を代数的に表す。

- 17係数空間Tと二次・三次関係の有限なGrassmann空間への写像を使い、PGL5×Tの像と、そのG不変な局所閉部分を調べる。対応するIsom群oidは `cor:general-relative-isom-scheme` の閉条件で書く。
- 既存sliceの横断性と自己同型計算を使い、源・標的射のflatnessまたはsmoothness、一般の有限安定化群、正規形の有限残余同一視を確認する。有限表示群oidだけで代数stackやatlasと宣言しない。
- 達成基準は、明示した代数的部分stackとO-marked問題への完全忠実な射を構成し、二次包絡への17→13射を族として記述すること。全Mの成分・開部分であるかは別に調べる。

### P2：smooth proper開部分と公表単位

compact圏のproper性はΔ開上で完成した。次はdg対角のperfect性を扱い、smoothな非空開を得る。有限中心の一般正則性を無限位数の一般族へ無条件に転用しない。特異ファイバーを含むSerre公式とsmoothnessは別の主張である。

公表単位は、(a)全Abel三次変形の二次包絡とframed形式近傍、(b)正規超曲面対の周期・内在復元、(c)有限Koszul解消による相対双対と一般Jacobian族のO-marked比較、を中心結果のまとまりとして検討する。有限中心族の幾何的結果も価値を保つ形で収める。分割を先に目的化しない。

Mori–Smith、Berger–Taillefer、Etingof–Ginzburg、Reyes–Rogalski、Keller、Keeler、および近年のgraded/dg/Z-algebra双対論との仮定の差をIntroductionに記した。相対構成の初出は未確認である。公表前には既存B_*の剛体性、中心式証明書、全Artin量子化比較を含めて独立点検する。

### P3：残余射とOの内在認識

全Artin dg残余射を実際に構成し、可換cubicの10次元変形と忘れられる7方向を接合対象等で記述する。ノート§10の条件付き積分解は、実際の射と対象の変形擬関手を確立してから適用する。源のframed形式群oidは確定済みである。

Oを忘れた復元、任意の非可換点の形式比較、特異三次への全Artin拡張、量子化を使わない高次障害消滅は別課題として保持する。

## 6. 再開時の具体的着手

1. ノート§1.6と `koszul_relative_duality.tex` の四入力・最終Serre定理を読む。AとBのtorsion比較、A双加群からQ双加群への移行、任意底変更の証明を確認する。
2. `jacobian_abel_comparison.tex` のΔ、相対CY/Koszul命題、全Hom定理、PGL5有限表示、最後の17次元系を読む。数値点a=1/6,b=0はΔの非消滅例であり、slice横断性をその同じ点で検証したという意味ではない。
3. P1では二つの関係部分束 I2（rank10）とI3（rank91）から開始する。PGL5作用の飽和像と、既存17係数sliceの有限同一視を比較する。
4. 可換点を使う時は `abel_formal_descent.tex` とノート§5.6、有限中心幾何を使う時はノート§1.4–1.5を参照する。変更のない低次数中心や横断行列を目的なく再計算しない。

## 7. 主張の境界

一般族の結論は明示Δ開上の標準模型とその任意底変更についてである。全17係数空間の全点、全てのGrothendieck圏、Oを忘れた圏、裸の導来圏へ拡張しない。17という次元は同型類の一般変動のRosenlicht次元であり、全Mの成分・atlas・大域代数性を意味しない。次数スカラーを除いたIsomはfpqc層商であり、大域点集合の単純な商ではない。Veroneseのμ2はGmに含まれ、追加2慣性ではない。

Serreはcompact圏上の主張であり、全Db(coh)の有限大域次元やdg smoothnessは含まない。相対CY/AS性と非正則基底を含む絶対的大域次元を混同しない。有限中心模型では中心準同型の単射性や全中心の底変更可換性を仮定しない。

可換点の全形式比較は、滑らかな複素三次Xを固定したframed Artin近傍である。frameを忘れた有限Aut(X)作用、未切断2群oid、一般の圏2降下、代数化へは広げない。四係数空間のmonomorphismも開埋込み・成分・atlasを意味しない。

## 8. 再現と検証範囲

`python3 scripts/verify.py` で参照・引用・TeX入力の閉包を検査する。新しい小証明書は `python3 computations/verify_general17_open.py` で再現できる。2026-11-19に九つの厳密な多項式・有理数検算を実行し、全て一致した。これは圏論的定理の計算証明ではない。既存八計算は実行日2026-11-16とsource hashを保持し、今回の再実行とは区別する。

組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォント、計算にはPython3・SymPyが必要。同日の先行組版試行は `lualatex.fmt` 不在で本文処理前に停止した。環境が同じなのでv14では再試行せず、現行PDF生成・視覚確認は未完了である。実施した範囲と未解決点は `validation.json` に記す。
