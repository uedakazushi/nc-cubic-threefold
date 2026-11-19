# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v6。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回の変更前の確認済み基点は `52eaff8b54cd8eeb7c0738ceb503a73d56ab91bb`。証明は `papers/nc_cubic_threefold_moduli.tex`（v12）と入力節、補助的知識は `notes/research_notes.md`、検証範囲は `validation.json` に置く。

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究全体の価値を最大化することを最優先する。特定の方法・定理名・当初の完成像を守ること自体を目的にしない。重要な変更は、現在有効な理由、解決したこと、残った核心を整理して方針を書き直す。時系列の方針変更履歴は蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算観察、既知文献の入力を区別する。原稿に証明があること、今回読んだ範囲、計算を再実行したこと、第三者査読を同一視しない。仮定・依存結果・証明の所在を明示し、誤りは依存する本文・要約・方針に反映する。将来役立つ反例や障害は研究ノートに残す。一次資料で重要な引用の仮定を確かめ、既存結果との差をIntroductionに書く。初出・新規性が未確認ならその旨を明記する。

論文は日本語LuaLaTeXを基本とし、研究経緯ではなく現在の論理順で構成する。公表価値のある結果と証明を削除・要約して軽量化しない。研究ノートは現在有効な補題、例、計算、文献比較、障害を記す。研究継続用bundleは本方針、ノート、現行論文、必要なコード・小証明書・再現手順の自己完結的な一式とする。旧ZIP、旧稿、バックアップ、編集履歴、外部文献PDFの大量収録は不要。

研究区切りでの承諾不要の保存は許可済み。本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存し、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・中間物・キャッシュはGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Library上の既存ファイルの削除は許可された保存と別の操作であり、行わない。生成・検算・組版・commit・remote到達確認は別の状態として報告する。

以下はこの一般原則と区別した、現在の具体的な研究計画である。

## 2. 現在の目標と定義

**構造対象だけを標識したAbel圏 `(C,O)` のモジュライとして、可換三次三様体と非可換Jacobian族を統一し、実際の射・変形・二次包絡を比較する。** 可換点では全Abel Artin変形の普遍的な三次模型を得た。非可換側では、固定剛体ambientの四係数族全体について相対Serre双対と全O保存同値の比較を完成し、有限型Cスキーム上でモジュライへのmonomorphismを得た。対象の定義と具体的な非自明族の射の理解が揃ったので、次はstack化後の可換点の形式完備化を確定し、一般族への拡張を進める。

対象には許容三次豊富列の存在を要求し、その選択は記憶しない。射はOを保つ全ての完全線型同値であり、既存の列保存 `M^pt` と区別する。標準模型のアフィン底変更は係数環の作用付き対象の圏で定義する。非Noetherianな底では大きいQGrを使い、小さいqgrはAbel性が保証される場合に使う。

四係数族の相対Hom比較では、内在的部分圏として `D(QGr A)^c`、すなわち非有界導来圏のcompact対象を用いる。これは有限中心模型の局所Perfに一致し、全Abel圏同値が保存する。元の「有界coherentかつ有限係数Tor振幅」の部分圏との一致は、一般正則性入力の下で非空開上に成立する別の結果である。全四係数族の相対比較にこの開条件は不要となった。

中心二変数と二次中心rank3は非可換部分族の復元仮定である。可換点の二次中心は15次元なので、全体の定義に課さない。固定模型の対象・射のfpqc降下と、圏の族自体の有効降下も区別する。全stack化後の形式完備化、有限型atlas、全17係数族のsmooth proper開部分、残余圏への実際の射は未完了である。

## 3. 到達点・仮定・証明所在

| 内容 | 現行の証明所在 | 適用範囲と依存 |
|---|---|---|
| Oだけを標識した定義と一般相対Hom比較 | `abel_marked_moduli.tex` | 全O保存完全同値。C1–C4の条件付き定理と、後述のcompact版 |
| 全Artin Abel／section比較 | `abel_cubic_deformations.tex`, `thm:abel-cubic-all-artin` | DDL Thm4.5の既知一般論の適用 |
| 全Abel変形の平坦二次包絡 | 同節 `thm:abel-cubic-flat-envelope` | 滑らかな可換三次点。CFTの構成、実際の局所化写像、Yekutieli比較 |
| 任意係数の飽和・復元・相対AS | 同節 `cor:abel-universal-artin-model`, `cor:abel-universal-relative-cubic` | 任意可換係数への変更。非平坦・非Noetherianも含む |
| 標準相対模型のArtin群oid | 同節 `thm:abel-canonical-relative-formal` | 全O-marked Abel変形群oidと同値。全stack化後の形式完備化は未同定 |
| 線対象の全twistコホモロジー | `central_pair_artin_formal_moduli.tex`, `prop:artin-ore-universal-cohomology` | 任意底変更、perfect RHom、n≥0はH0、n=−1は零、n≤−2はH3のみ |
| 四係数族の有限中心模型 | `finite_order_relative_categories.tex`, `thm:central-model-finite` | PBW・中心正則三次元・有限位数THCR境界を入力 |
| 普遍的二次中心・全shift飽和 | 同節 `cor:central-model-universal-center-two`, `thm:central-model-universal-sections` | B_*族、任意可換底変更。全中心の底変更可換性は要求しない |
| 全係数基底のC1–C2 | 同節 `prop:central-model-qgr`, `prop:central-model-even-sequence` | Noetherian底変更の相対圏、偶数豊富列、全射の決定 |
| 全四係数族の相対Serre公式 | `relative_serre_duality.tex`, `thm:relative-serre-projective` | 局所Perf上でS≅(−2)[3]、任意Noetherian底変更。特異ファイバーも含む。既存PBW・AS・CY入力を明示 |
| 全O保存相対同値の比較 | 同節 `cor:central-model-relative-hom` | compact版C3を用い、有限型CサイトでIsom_gr/Gm≅Eq_O |
| 四係数空間のmonomorphism | 同節 `prop:rigid-four-family-monomorphism` | 全A4、非被約な有限型基底を含む。既存Aut_gr(B_*)(C)=C×入力とCartierの定理 |
| 非空開上の元のC3 | `finite_order_relative_categories.tex`, `prop:central-model-intrinsic-perfect-open` | 一般幾何tailsの有限大域次元の入力下で、有限係数Tor圏=局所Perf |
| 可換点の形式局所環 | `cor:abel-cubic-formal-ring` | `C[[t_1,…,t_10,a_ij]]/(Pfaffian_4(a))`。次元17・接空間20。特殊ファイバー固定、Aut(X)未商 |
| 平坦性判定・平方零消滅 | `thm:abel-degree-three-propagation`, `thm:abel-square-zero-degree-three` | 非周期的Z代数、平方零ではF≠0だけ。全Artin定理と独立の証明を保持 |
| 有限係数族・周期性 | 主原稿 `thm:17`, `thm:pair-route-gcd` 等 | 41→37、17→13、一般fiber4、gcd周期性の有効な証明を保持 |

今回の新しい証明は原稿に統合し、主要段階を別々に点検した。既存B_*のPBW・AS・CY・剛体性の入力は引用箇所を明示し、その全てを今回独立に再証明したとはしない。第三者査読・初出確認は未完了である。

## 4. 現在の方針を採る理由

可換点の全Artin二次包絡平坦性、任意係数変更後の飽和・復元、および四係数族の相対Serre公式は解決した課題であり、次の未解決課題として繰り返さない。

相対Serre公式には有限中心模型を通常の射影空間へ埋め込む方法が有効だった。体上で双対複体を両側加群として同定した後、係数平坦性とGrothendieck双対により底変更を含む相対公式を作った。局所Perfをcompact対象として特徴付けることで、Hom比較に有限大域次元を要求する必要もなくなった。この結果、固定ambientの全四係数が、Abel圏の実際の族として区別される。

一方、有限中心性には有限位数の楕円境界を使っている。一般の17係数族へこの方法をそのまま適用できるとは限らない。全族への拡張では、まず有限中心入力に依存しない相対局所双対・proper RHomの構成を分離する。大域代数性や成分性は、今回のmonomorphismや形式環から先取りしない。

## 5. 優先課題と達成基準

### P1：stack化後の可換点の形式完備化

標準係数族と全平坦Abel Artin変形の群oidは既に同値である。任意係数の飽和・復元と固定模型間のHomの任意fpqc降下も証明済みである。残るのは、stack化によって加わり得るArtin基底上の対象が大域的標準模型を持つかという点である。

- `thm:abel-canonical-relative-formal` から出発し、特殊ファイバーとOの標識を固定する。
- fpqc局所の線対象O(i)の持上げについて、存在・同型・三重交叉の整合性を分けて降下障害を計算する。固定圏内の対象降下だけで圏の2降下を済ませない。
- Artin局所基底上のBrauer型障害の消滅を使う場合は、実際の係数層と位相を同定してから適用する。
- 達成基準は、定義した `M^O_cub` の指定点の形式完備化と既証明の標準模型群oidの同値。有限型atlasの構成は別に扱う。

### P2：一般の有限係数族への相対比較

全17係数Jacobian族と13係数ambientの実際の射を、O-marked圏の族として比較する。

- 有限位数境界の有限中心手法が使える範囲を明示する。一般の無限位数境界まで同じ仮定を暗黙に広げない。
- `relative_serre_duality.tex` のどの段階が有限中心を要するかを分離し、相対graded局所双対・標準AS解消・共通の局所模型で置き換える。
- まずcompact圏上のproper RHom、底変更、Serre双対を完成させる。大域dg smooth性には相対対角と大域Morita模型の比較を追加する。
- 達成基準は明示した非空基底上で全O保存同値の比較が成立し、既存17→13射に適用できること。開埋込み・成分性は追加の変形論で判定する。

### P3：公表単位の確定と独立点検

統合稿に価値ある証明を保持しつつ、(a)全Abel三次変形の二次包絡と普遍的模型、(b)正規超曲面対の周期と内在復元、(c)有限中心族の相対Serre双対とO-marked比較、を中心定理のまとまりとして整理する。

新しい具体的適用の初出を網羅照合し、既存B_*のPBW・CY・自己同型計算の依存箇所を公表前に独立に再点検する。新しい一般双対理論を作ったとは主張せず、Yekutieli、Burban–Drozd–Gavran、通常のGrothendieck双対との関係をIntroductionに残す。

### P4：残余圏とOの内在認識

全Artin dg残余射を実際に構成し、可換cubicの10次元変形と忘れられる7方向を接合対象等で記述する。`notes/research_notes.md` §10の条件付き積分解は射の構成後に適用する。Oを忘れた復元は別の課題である。特異三次への全Artin拡張と量子化を使わない高次障害消滅も補助課題として保持する。

## 6. 再開時の具体的着手

1. `relative_serre_duality.tex` の主要定理・相対Hom系・最後のmonomorphism命題を読み、四係数族の完了範囲を確認する。詳細な依存は `notes/research_notes.md` §1.4–1.5。
2. `abel_cubic_deformations.tex` の最後の標準相対模型定理と、その直後の残る降下問題を読む。
3. Artin基底上のfpqc降下データに対する線対象の持上げを、現行ノートのExt消滅・係数作用と接続する。定理を拡張する前に障害の所在を記す。
4. 新たな計算を行う場合は具体的な未解決点に結び付ける。変更のない低次数中心や横断行列を目的なく再計算しない。

## 7. 主張の境界

四係数空間のmonomorphismは、有限型Cスキーム上のstackの完全忠実性である。開埋込み、étale chart、4次元成分、対角の代数性、全モジュライの有限型性を意味しない。全stack化後の射については固定模型の任意fpqc Hom降下を使うが、対象の有効降下まで解決してはいない。

相対ASは非正則基底を含む絶対的大域次元ではない。有限係数Tor圏とcompact圏を全基底で同一視しない。有限中心の任意底変更後は中心準同型だけを用い、中心部分環の単射性や全中心の形成の底変更可換性を仮定しない。Veroneseのμ2は次数スカラーGmに吸収され、O-marked圏の追加2慣性ではない。層商と大域点集合の商、H1とH2の降下障害を区別する。

## 8. 再現と検証範囲

`python3 scripts/verify.py` が参照・引用・TeX入力の閉包を検査する。組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォントが必要。計算はPython3・SymPyを用いる。

既存8計算の実行日・source hashは保持し、今回の再実行とは区別する。新しい双対性・群スキーム・monomorphismは証明の点検であり、数値実験による確認ではない。現環境の組版試行は `lualatex.fmt` 不在で本文の処理前に停止した。現在の原稿の組版成功・PDF視覚確認は未完了である。実施範囲は `validation.json` に記録する。
