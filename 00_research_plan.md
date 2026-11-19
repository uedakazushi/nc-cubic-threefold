# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v7。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回の変更前の確認済み基点は `58ce4963c64383e9dfc1b6f19b82f6413abec774`。証明は `papers/nc_cubic_threefold_moduli.tex`（v13）と入力節、補助的知識は `notes/research_notes.md`、検証範囲は `validation.json` に置く。

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究全体の価値を最大化することを最優先する。特定の方法・定理名・当初の完成像を守ること自体を目的にしない。重要な変更は、現在有効な理由、解決したこと、残った核心を整理して方針を書き直す。時系列の方針変更履歴は蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算観察、既知文献の入力を区別する。原稿に証明があること、今回読んだ範囲、計算を再実行したこと、第三者査読を同一視しない。仮定・依存結果・証明の所在を明示し、誤りは依存する本文・要約・方針に反映する。将来役立つ反例や障害は研究ノートに残す。一次資料で重要な引用の仮定を確かめ、既存結果との差をIntroductionに書く。初出・新規性が未確認ならその旨を明記する。

論文は日本語LuaLaTeXを基本とし、研究経緯ではなく現在の論理順で構成する。公表価値のある結果と証明を削除・要約して軽量化しない。研究ノートは現在有効な補題、例、計算、文献比較、障害を記す。研究継続用bundleは本方針、ノート、現行論文、必要なコード・小証明書・再現手順の自己完結的な一式とする。旧ZIP、旧稿、バックアップ、編集履歴、外部文献PDFの大量収録は不要。

研究区切りでの承諾不要の保存は許可済み。本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存し、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・中間物・キャッシュはGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Library上の既存ファイルの削除は許可された保存と別の操作であり、行わない。生成・検算・組版・commit・remote到達確認は別の状態として報告する。

以下はこの一般原則と区別した、現在の具体的な研究計画である。

## 2. 現在の目標と定義

**構造対象だけを標識したAbel圏 `(C,O)` のモジュライとして、可換三次三様体と非可換Jacobian族を統一し、実際の射・変形・二次包絡を比較する。** 可換点では、全fpqc stack化後のframed形式変形群oidを、既存の全Abel変形と同定した。還元上恒等な自己同値もmarked自然同型を除き恒等なので、この群oid自体が17次元・接空間20次元のPfaffian形式環で表される。非可換側では固定剛体ambientの全四係数族について相対Serre双対、全O保存同値の比較、有限型C基底上のmonomorphismを得ている。次は有限中心性への依存を分離し、一般17係数族と13係数ambientの相対比較へ進む。

対象には許容三次豊富列の存在を要求し、その選択は記憶しない。射はOを保つ全ての完全線型同値であり、列保存 `M^pt` と区別する。標準模型の底変更は係数作用付き対象の圏で定義し、非Noetherian底では大きいQGrを用いる。特殊ファイバーとの同一視を保つ形式近傍と、それを忘れた有限Aut(X)を含む近傍も区別する。

四係数族の相対比較では内在的部分圏 `D(QGr A)^c` を用いる。これは有限中心模型の局所Perfに一致する。「有界coherentかつ有限係数Tor振幅」の部分圏との一致は、一般正則性入力の下で非空開上に成立する別結果であり、全四係数族の比較には不要である。中心二変数と二次中心rank3も非可換部分族の復元条件であり、二次中心15次元の可換点を全体の定義から除外しない。

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

新しい局所復元・cocycle補正・framed自己同型の証明を原稿に統合し、別々に読み合わせた。既存の量子化・形式環・PBW・AS・CY・剛体性の証明を今回全て独立に再証明したとはしない。初出・新規性の網羅調査と第三者査読は未完了である。

## 4. 現在の方針を採る理由

可換点では、全Abel Artin変形の二次包絡平坦性、任意係数の飽和・復元、stack化後の大域模型とframed自己同型の消滅まで解決した。これらを未解決課題として繰り返さない。全形式近傍が具体的な特異形式スキームになったので、今後はこの結論を基準に、一般非可換族での射・代数化・残余射を別々に検討できる。

大域模型の構成では、被覆環S自体をArtinと仮定しないことが核心である。元のR→Cを使って局所線対象を持ち上げ、還元frameにより降下のbandをGm全体から1+mへ小さくする。対数とAmitsur完全性でcocycleを消し、圏全体を降下させる前にHomと合成を降下する。詳細は研究ノート§5.6と現行論文に置く。

四係数族の相対Serre公式は有限中心模型により完成したが、その有限中心性には有限位数の楕円境界を使う。一般17係数族へそのまま適用できるとは限らない。次の課題では、有限中心に依存する射影埋込みを、相対graded局所双対・Koszul解消・局所コホモロジーに置き換える範囲を明確にする。形式環やmonomorphismだけから大域代数性や成分性を先取りしない。

## 5. 優先課題と達成基準

### P1：一般17係数族の相対Serre・全同値比較

全17係数Jacobian族と13係数ambientの実際の射を、O-marked圏の族として比較する。

- `relative_serre_duality.tex` の有限中心を使う段階を列挙し、一般族で使える相対AS解消と双対複体の入力を分離する。
- 最初に、標準線対象間のRHomのperfect性と底変更、compact対象の生成、traceの構成を確認する。非Noetherian底では大きい圏を保持する。
- 無限位数の楕円境界に有限中心性を仮定しない。graded局所コホモロジーや相対balanced dualizing complexで代替する場合、その存在・底変更・Nakayama作用を明記する。
- 達成基準は、明示した非空基底上で全O保存同値の相対比較を得て、17→13射へ適用すること。大域dg smooth性、開埋込み、成分性は別途判定する。

### P2：公表単位の確定と独立点検

(a)全Abel三次変形の二次包絡と全stackのframed形式近傍、(b)正規超曲面対の周期と内在復元、(c)有限中心族の相対Serre双対とO-marked比較、を中心結果のまとまりとして扱う。現行の価値ある証明は保持し、公表単位に分ける場合も重複を増やさない。

DDL・Lowen・Yekutieli・CFT・通常の降下理論と本研究の適用の関係をIntroductionに具体的に記す。新しい一般変形理論や一般圏2降下とは主張しない。既存B_*のPBW・CY・剛体性の入力、全Artin量子化比較、初出を公表前に独立点検する。

### P3：残余射とOの内在認識

全Artin dg残余射を実際に構成し、可換cubicの10次元変形と忘れられる7方向を接合対象等で記述する。研究ノート§10の条件付き積分解は、実際の射と対象の変形擬関手を確立してから適用する。framed源の形式群oidは今回確定したので、その側の降下を再び仮定として残す必要はない。

Oを忘れた復元、任意の非可換点への形式比較、代数化と有限型atlasは別課題である。特異三次への全Artin拡張と、量子化を使わない高次障害消滅も補助課題として保持する。

## 6. 再開時の具体的着手

1. `abel_formal_descent.tex` の全stack比較・framed自己同型・離散形式近傍の三結果と、研究ノート§5.6を読む。可換点で解決した範囲を確認する。
2. `relative_serre_duality.tex` のambient双対構成と局所PerfのSerre公式を読み、どこで有限中心性を使ったか確認する。四係数族の完了範囲はノート§1.4–1.5。
3. 一般17係数族について、標準線対象の局所コホモロジー・相対AS双対と底変更を具体的に比較する。成立が未確認な仮定を先に明記し、一つずつ閉じる。
4. 新しい計算は具体的な未解決点に結び付ける。変更のない低次数中心や横断行列を目的なく再計算しない。

## 7. 主張の境界

全形式比較は滑らかな複素三次Xを固定したframed Artin近傍である。frameを忘れたAut(X)作用、全ての基底上の任意のGrothendieck圏の2降下、一般非可換点での局所完全性には広げない。形式環は代数化・有限型atlas・対角の代数性を自動的に与えない。

四係数空間のmonomorphismは有限型Cスキーム上での完全忠実性であり、開埋込み・4次元成分・atlasではない。有限係数Tor圏とcompact圏を全基底で同一視しない。相対ASは非正則基底を含む絶対的大域次元ではない。中心の底変更後は中心準同型だけを用い、その単射性や全中心の底変更可換性を仮定しない。

Veroneseのμ2は次数スカラーGmに吸収され、O-marked圏の追加2慣性ではない。層商と大域点集合の商を区別する。線対象のframed持上げの自己同型1+mと、圏のframed自己同値の自然同型類が自明であることは異なる主張である。

## 8. 再現と検証範囲

`python3 scripts/verify.py` で参照・引用・TeX入力の閉包を検査する。組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォントが必要。既存の計算はPython3・SymPyを用いる。

今回の形式降下と自己同型消滅は証明の点検による結果であり、数値実験ではない。既存8計算の実行日とsource hashは保持し、今回の再実行とは区別する。現環境の先行する組版試行は `lualatex.fmt` 不在で本文処理前に停止した。環境が同じなのでv13では再試行せず、現行PDF生成・視覚確認は未完了である。実施した検証範囲は `validation.json` に記す。
