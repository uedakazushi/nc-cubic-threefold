# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v5。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回確認した基点は `d31ac3530a37dc6e04422860b5d6565060cf87ab`。証明は `papers/nc_cubic_threefold_moduli.tex`（v11）とその入力節、補助的な知識は `notes/research_notes.md`、検証状態は `validation.json` に置く。

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究全体の価値を最大化することを最優先する。特定の方法・定理名・当初の完成像を守ること自体を目的にしない。重要な変更は、現在有効な理由、解決したこと、残った核心を整理して方針を書き直す。時系列の方針変更履歴は蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算観察、既知文献の入力を区別する。原稿に証明があること、今回読んだ範囲、計算を再実行したこと、第三者査読を同一視しない。仮定・依存結果・証明の所在を明示し、誤りは依存する本文・要約・方針に反映する。将来役立つ反例や障害は研究ノートに残す。一次資料で重要な引用の仮定を確かめ、既存結果との差をIntroductionに書く。初出・新規性が未確認ならその旨を明記する。

論文は日本語LuaLaTeXを基本とし、研究経緯ではなく現在の論理順で構成する。公表価値のある結果と証明を削除・要約して軽量化しない。研究ノートは現在有効な補題、例、計算、文献比較、障害を記す。研究継続用bundleは本方針、ノート、現行論文、必要なコード・小証明書・再現手順の自己完結的な一式とする。旧ZIP、旧稿、バックアップ、編集履歴、外部文献PDFの大量収録は不要。

研究区切りでの承諾不要の保存は許可済み。本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存し、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・中間物・キャッシュはGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Library上の既存ファイルの削除は許可された保存と別の操作であり、行わない。生成・検算・組版・commit・remote到達確認は別の状態として報告する。

以下はこの一般原則と区別した、現在の具体的な研究計画である。

## 2. 現在の目標と定義

**構造対象だけを標識したAbel圏 `(C,O)` のモジュライとして、可換三次三様体と非可換Jacobian族を統一し、実際の射・変形・相対双対を比較する。** 可換三次点では全Abel Artin変形の二次包絡平坦性に加え、各模型から任意の係数環への変更後のsection飽和・復元・対象の降下を得た。具体的な有限位数楕円境界の四係数族では、相対Hom定理のC1–C2を全係数基底上で、C3とperfect RHom・底変更を非空基底開上で供給した。現在の最優先は、この開集合上の相対Serre公式である。

対象には許容三次豊富列の存在を要求し、その選択は記憶しない。射はOを保つ全ての完全線型同値であり、既存の列保存 `M^pt` と区別する。相対標準模型のアフィン底変更は係数環の作用付き対象の圏で定義する。非Noetherianな底では大きいQGrを使い、小さいqgrはAbel性が保証される場合に使う。

標準係数族の対象・射のfpqc降下と、圏の族そのものの任意の降下データの有効性を区別する。全平坦Abel Artin変形が普遍的な相対三次模型を持つことは証明済みである。一方、fpqc stack化がArtin基底上で新しい大域模型を持たない形式を加えないことは未証明であり、stack化後の全形式完備化との同定にはこの点が残る。

中心二変数と二次中心rank3は非可換chartの復元仮定である。可換点の二次中心は15次元なので、この条件を全体の定義に課さない。17次元全混合族の非空smooth proper開部分、13次元ambientへの一般4次元fiber、実際の残余圏への射と7方向の接合データ、Oの内在認識は上位目標として保持する。

## 3. 到達点・仮定・証明所在

| 内容 | 状態と証明所在 | 適用範囲 |
|---|---|---|
| Oだけを標識した定義、全Hom比較 | `abel_marked_moduli.tex`, `def:abel-cubic-pointed`, `thm:abel-relative-pointed-hom` | 全O保存完全同値。相対Hom定理はC1–C4付き |
| 全Artin Abel／section比較 | `abel_cubic_deformations.tex`, `thm:abel-cubic-all-artin` | DDL Thm4.5の適用。既知一般論の帰結 |
| 全Abel変形の平坦二次包絡 | 同節 `thm:abel-cubic-flat-envelope` | 滑らかな可換三次点の全Artin変形。CFT量子化・実際の局所化写像・Yekutieli比較を使用 |
| 任意係数の飽和・復元 | 同節 `prop:abel-universal-line-hom`, `cor:abel-universal-artin-model` | Artin模型から任意の可換R代数Sへ。非平坦・非Noetherianも含む |
| 係数族のfpqc降下、相対同値 | 同節 `prop:abel-coefficient-fpqc-descent`, `lem:abel-canonical-family-equivalences` | 固定Grothendieck圏の係数族。全圏の2降下とは別 |
| 標準相対模型のArtin群oid | 同節 `thm:abel-canonical-relative-formal` | 全O-marked Abel変形群oidと同値。全stack化後の形式完備化とは未同定 |
| 全twistのコホモロジー | `central_pair_artin_formal_moduli.tex`, `prop:artin-ore-universal-cohomology` | 任意底変更。n≥0はH0、n=−1は零、n≤−2はH3のみ。線対象間RHomもperfect |
| 四係数族の有限中心模型 | `finite_order_relative_categories.tex`, `thm:central-model-finite` | 既存PBW・有限位数THCR入力。全中心の底変更可換性は不要 |
| 普遍的二次中心rank3 | 同節 `cor:central-model-universal-center-two` | B_*族、任意可換底変更。全中心の底変更可換性とは別 |
| C1–C2の具体的供給 | 同節 `prop:central-model-qgr`, `thm:central-model-universal-sections`, `prop:central-model-even-sequence` | 全四係数族、任意Noetherian底変更。大域有限中心模型・偶数豊富列・全射の決定 |
| 非空開上のC3とproper RHom | 同節 `prop:central-model-intrinsic-perfect-open` | 一般幾何学的tailsの有限大域次元を入力。既存B_*の入力下で非空開が存在。相対Serreは未証明 |
| 形式局所環 | `cor:abel-cubic-formal-ring` | `C[[t_1,…,t_10,a_ij]]/(Pfaffian_4(a))`、次元17・接空間20。特殊ファイバー固定、Aut(X)未商 |
| 直接的な平坦性判定・平方零消滅 | `thm:abel-degree-three-propagation`, `thm:abel-square-zero-degree-three` | 非周期的Z代数、平方零基底ではF≠0だけ。全Artin結果と独立した証明を保持 |
| 既存の有限係数族・周期性 | 主原稿 `thm:17`, `thm:pair-route-gcd` 等 | 41→37、17→13、一般fiber4、gcd周期性、剛体4係数族の証明を保持 |

今回の証明は原稿へ統合し、主要な論理を別々に点検した。第三者査読、初出確認、全旧定理の独立再証明の完了は意味しない。Rainsの有限位数楕円代数の中心持上げ、RSVの有限中心代数の一般smoothness／射影性拡張、Stacksのproper pushforwardは既知入力である。

相対ASは非正則基底を含む絶対的大域次元ではない。相対アフィン対角のperfect性から大域dg圏のsmooth性を、Morita比較なしに追加結論としない。Veroneseのμ2は次数スカラーGmに含まれ、O-marked圏の追加2慣性ではない。層商と大域点集合の商、H¹の同型障害とH²の対象障害を区別する。

## 4. 現在の方針を採る理由

可換点の包絡平坦性と、任意底変更後の飽和・復元は既に証明された。これらを未解決課題として繰り返さない。係数環の有限表示性が必要な小さいAbel圏の一般論を無理に拡張せず、大きいGrothendieck模型の直接証明で問題を分離した。

非可換側では、四係数族全体の有限中心模型を得たため、構造対象のsection復元と有限型の相対圏論を具体的に扱える。一般のtails正則性を中心アフィン片へ局所化し、対角の有限射影分解を開集合へ延長することで、内在的有限Tor部分圏と局所perfect圏の間の隔たりも非空開上で解消した。従って相対Hom定理に必要な未解決入力は、四係数族では主に相対Serre双対へ絞られた。

全17係数族へ一度に拡張するより、この具体的族で全O保存相対同値の比較を完成させることを優先する。ただし中心全体の計算、最大の正則開集合の決定、既知の数値の再計算はその前提にしない。

## 5. 優先課題と達成基準

### P1：四係数族の相対Serre双対

`finite_order_relative_categories.tex` の非空開上で、内在的有限Tor部分圏に相対Serre関手 `S≅(−2)[3]` を構成し、任意Noetherian底変更との両立を証明する。基底線束による捩れが現れれば明示してfppf局所で扱う。

- 固定CY／AS5 ambient B_*と中心正則三次商から、相対graded局所双対複体を計算する。
- 有限中心の射影模型の双対核と比較し、体上のbalanced dualizing formulaを単にファイバーごとに引用して済ませない。
- 達成基準はC1–C4が同じ非空基底開上で成立し、`Isom_gr/Gm ≅ Eq_O` が実際の相対族に適用できること。開集合の存在証明と具体的な判別多項式の計算は区別する。
- 大域dg smooth性を述べる場合は、中心アフィン対角から大域核・Morita模型への比較を別途示す。

### P2：Artin模型とstack化後の形式完備化

任意底変更の飽和・復元・固定模型間の射の降下は解決済み。残るのは圏自体の降下と、stack化後のArtin対象の大域的な標準模型の存在である。

- 特殊ファイバーの同定とOの標識を固定し、局所的なO(i)の持上げの降下障害を調べる。
- 固定圏内の対象の降下と、圏値降下データそのものの有効性を区別する。
- 達成基準は `M^O_cub` の指定点の形式完備化と、現在証明済みの標準模型のArtin群oidとの同値。有限型atlasの存在を同時に主張しない。

### P3：有限型incidenceと全混合族

四係数族の相対比較を得た後に、17係数Jacobian中心対の有限型chart、周期構造と三次イデアルの降下、実際の17→13射へ拡張する。形式局所環の同型だけで代数化・大域成分性を結論しない。有限窓の表示と全次数条件の一様性を明示する。

### P4：残余圏とOの内在認識

全Artin dg残余射を構成し、可換cubicの10次元変形との比較と、忘れられる7方向を接合対象・rotation等で記述する。`notes/research_notes.md` §10の条件付き積分解は実際の射の構成後に適用する。Oを忘れた復元は別の最終課題とする。

補助課題として、特異三次への全Artin拡張、量子化を使わない高次障害消滅を保持する。平方零のδ²=0を高次へ無補正で反復しない。

## 6. 再開時の具体的着手

1. `finite_order_relative_categories.tex` の最後の命題を読み、非空開上で既に得られた内在的perfect圏とRHomを確認する。
2. `abel_marked_moduli.tex` のC4を、既存の `central_pair_mixed_derived_rigid.tex` の体上のSerre式と比較し、相対双対複体の構成に着手する。
3. `abel_cubic_deformations.tex` の標準相対模型定理を読み、全係数変更に関する証明済み事項と、圏自体の降下という残りを確認する。
4. 新たな計算を行うなら、双対核・中心標準開・相対対角の具体化に結び付ける。変更のない低次中心や横断行列を目的なく再計算しない。

## 7. 公表方針と新規性

統合稿に価値ある証明を保持する。公表単位は、(a)全Abel三次変形の二次包絡・普遍的相対模型、(b)正規超曲面対の周期と内在復元、(c)有限係数族とO-markedモジュライの相対比較、を中心結果のまとまりで整理する。

DDL、Lowen、Yekutieli、CFT、Koszul変形原理、Rains、RSV、通常の降下とProj理論は既知入力である。Grassmannian Poisson錐と17/20の数値だけを新結果にしない。全Abel変形への二次包絡の適用、普遍的相対模型、有限中心模型を用いた具体的C1–C3比較の初出と近接文献の網羅照合は未完了。公表前の独立点検と文献比較を続ける。

## 8. 再現と検証範囲

`python3 scripts/verify.py` が参照・引用とTeX入力の閉包を検査する。組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォントが必要。計算はPython3・SymPyを用いる。

既存8計算の実行日・source hashを保持し、今回の再実行とは区別する。新しい結果は証明の点検であり数値実験による確認ではない。生成、証明点検、静的検査、組版、保存を分けて記録する。現在のTeX環境は `lualatex.fmt` が欠けており、組版成功・PDFの視覚確認は未完了。正確な実施範囲は `validation.json` に従う。
