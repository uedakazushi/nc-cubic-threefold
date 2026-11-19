# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v9。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回の変更前の確認済み基点は `a9baf7b836fd43205cf531e3df316ba9944e0e74`。証明は `papers/nc_cubic_threefold_moduli.tex`（v15）と入力節、補助的知識は `notes/research_notes.md`、検証範囲は `validation.json` に置く。

## 1. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、研究全体の価値を最大化することを最優先する。特定の方法・定理名・当初の完成像を守ること自体を目的にしない。重要な変更は、現在有効な理由、解決したこと、残った核心を整理して方針を書き直す。時系列の方針変更履歴は蓄積しない。

証明済み、追加仮定付き、証明未完成、予想、計算観察、既知文献の入力を区別する。原稿に証明があること、今回読んだ範囲、計算を再実行したこと、第三者査読を同一視しない。仮定・依存結果・証明の所在を明示し、誤りは依存する本文・要約・方針に反映する。将来役立つ反例や障害は研究ノートに残す。一次資料で重要な引用の仮定を確かめ、既存結果との差をIntroductionに書く。初出・新規性が未確認ならその旨を明記する。

論文は日本語LuaLaTeXを基本とし、研究経緯ではなく現在の論理順で構成する。公表価値のある結果と証明を削除・要約して軽量化しない。研究ノートは現在有効な補題、例、計算、文献比較、障害を記す。研究継続用bundleは本方針、ノート、現行論文、必要なコード・小証明書・再現手順の自己完結的な一式とする。旧ZIP、旧稿、バックアップ、編集履歴、外部文献PDFの大量収録は不要。

研究区切りでの承諾不要の保存は許可済み。本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存し、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・中間物・キャッシュはGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Library上の既存ファイルの削除は許可された保存と別の操作であり、行わない。生成・検算・組版・commit・remote到達確認は別の状態として報告する。

以下はこの一般原則と区別した、現在の具体的な研究計画である。

## 2. 現在の目標と定義

**構造対象だけを標識したAbel圏 `(C,O)` のモジュライとして、可換三次三様体と非可換Jacobian族を統一し、実際の射・変形・二次包絡を比較する。** 一般Jacobian族について、滑らかな有限型17次元Deligne–Mumford stack `C_J=[J/PGL5]` と全O-marked問題への完全忠実な射を構成した。全O保存同値を含む、そのfpqc局所模型からなる全部分stackである。さらに13次元の滑らかなDM stack `B_J=[Y/PGL5]` への二次包絡射は、階数4ベクトル束のtorsorであり、スキームで表現可能・アフィン・滑らか・全射となる。

可換三次点の全fpqc stack化後のframed形式群oidは、17次元・接空間20次元のPfaffian形式環で表される。固定剛体ambientの全四係数族のmonomorphism、一般族の任意係数上の相対Serreと全Hom比較も保持する。次の核心は、構成した部分モジュライ内のdg smoothな非空開、全Mの変形との局所比較、実際の残余射である。パラメータstackのsmooth性から個々の圏のdg smooth性は従わない。

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
| 代数的ambientのétale atlas | `jacobian_moduli_chart.tex`, `prop:jacobian-ambient-etale-chart` | `PGL5×T_B→Q113` のétale locus、非空不変開Y。13次元DM stack。指定有理点の微分同型を厳密検算 |
| 一次・三次中心の任意底変更 | 同節 `prop:general13-universal-centers` | Δ開の低次THCR中心、PBW分裂、交換子写像の局所分裂単射。非平坦底変更を含む |
| 実際の17→13射 | 同節 `prop:jacobian-affine-four-morphism` | 中心完全列の分裂torsor。中心重みの相殺により階数4ベクトル束がPGL商へ降下 |
| 17次元の代数的Abel部分モジュライ | 同節 `thm:jacobian-algebraic-abel-substack` | 有限関係窓と全Hom比較、PGL scalar coherence。任意係数で完全忠実、全M内の開性・局所閉性・成分性は未証明 |

新しい部分モジュライの構成、任意底変更の中心、torsorの降下、全Abel同値との比較を別々に読み合わせた。今回の計算は同一の指定点におけるΔの非消滅、作用とsliceの微分rank37、全Poisson微分rank113と整数上の積零である。原稿の証明、今回の点検、計算を区別する。既存の全相対双対・量子化・形式環・PBW・剛体性を今回一から再証明したとはしない。一般的な商stack・étale・降下の原理は既知であり、この具体的適用の初出・新規性の網羅調査と第三者査読は未完了である。

## 4. 現在の方針を採る理由

一般族への拡張は、有限中心性に代えて有限Koszul対角解消と相対CY同型を使うことで成立した。任意係数の相対Serreと全O保存同値比較、有限なIsom方程式は解決した範囲として扱う。詳細はノート§1.6と現行論文に保持する。

代数的部分モジュライは、13係数ambientを先に商にする方法で構成した。37次元の関係graph成分に対する作用とsliceの射が等次元・支配的なので、標数零で非空étale locusを持つ。同変性によりこの開は `PGL5×T_B^e` となり、飽和像Yの商に実際のétale atlasを与える。中心三次直線の相対A4 torsorをその上に載せることで、17次元stackと17→13射が同時に得られる。17係数slice自体が大域正規形であるという仮定は不要である。

元の目標のうち、実際のJacobian族をAbel圏の代数的モジュライとして扱うことは、この全部分stackについて解決した。全Mの局所変形を尽くすこと、成分性、dg smooth性は未解決である。有限関係窓での局所閉性と、全Abel問題内での局所閉性を混同しない。以後は同じ商構成を反復せず、個々の圏の幾何的正則性と全Mとの関係に進む。

有限中心の四係数族における局所対角・有限係数Tor振幅の比較は、別の幾何的情報を持つので保持する。Δ開が固定B_*を含むとは限らず、既存の四係数結果を削除しない。可換点の形式降下・framed自己同型消滅も保持する。

## 5. 優先課題と達成基準

### P1：Jacobian部分モジュライのdg smooth開

compact圏のproper性と相対SerreはΔ開上で完成し、パラメータstackもsmoothである。次は各圏のdg対角のperfect性を扱う。

- `T_B^e×A4` 上の五線対象のcompact generatorと、その有限係数dg自己準同型代数から始める。dg対角が有限セルで分解される一点または非空開を探し、相対的な分解の延長で開性を示す。
- 既存の有限中心族のregular点を利用する場合は、まず新atlasとの交わりを実証する。有限位数・有限中心の一般正則性を無限位数の一般族へ無条件に転用しない。
- 達成基準は、具体的な非空開上の相対dg smooth proper性と任意底変更の証明。特異ファイバーを含む既存Serre公式は保持する。

### P2：全Mとの局所比較、有限自己同型、公表単位

`C_J→M^O` は完全忠実だが、形式的にすべての変形を尽くすとは未証明である。一般の一点のAbel変形群oidと、関係窓の変形群oidを比較する。接空間一致だけを成分判定に使わず、持上げの存在・障害と全Artin比較を明示する。到達点はこの部分が全M内で開、局所閉、または成分となるための必要条件と十分条件の確定である。

一般の有限stabilizerと有限残余正規形も具体化する。幾何学的stabilizerの有限性だけから対角の有限性・商の分離性・大域coarse moduliを宣言しない。周囲の分類はprojectively gradedの範囲であり、ambientの全O保存Abel同値との比較は別課題である。

公表単位は、(a)全Abel三次変形の二次包絡とframed形式近傍、(b)正規超曲面対の周期・内在復元、(c)有限Koszul解消の相対双対とJacobian型Abel圏の代数的部分モジュライ、を中心結果として検討する。分割を目的化せず、価値ある証明を保持する。Mori–Smith/BT/EG/Keller/KeelerとStacks Projectの既知入力、近年の双対論との仮定の差をIntroductionに記した。具体的な相対構成・応用の初出は未確認であり、公表前の独立点検を要する。

### P3：残余射とOの内在認識

全Artin dg残余射を実際に構成し、可換cubicの10次元変形と忘れられる7方向を接合対象等で記述する。ノート§10の条件付き積分解は、実際の射と対象の変形擬関手を確立してから適用する。源のframed形式群oidは確定済みである。

Oを忘れた復元、任意の非可換点の形式比較、特異三次への全Artin拡張、量子化を使わない高次障害消滅は別課題として保持する。

## 6. 再開時の具体的着手

1. ノート§1.7と `jacobian_moduli_chart.tex` を読む。`C_J=[J/PGL5]→B_J=[Y/PGL5]`、étale atlas、完全忠実性と主張の境界を確認する。中心の重み1/3とHom(L,W)の重み0、大域的な原点・O(1)の未選択を保持する。
2. P1では `koszul_relative_duality.tex` の五線compact generatorと `jacobian_abel_comparison.tex` の具体的PBW/CY入力から、有限係数dg代数の対角を調べる。相対Serreとdg smoothnessの区別はノート§1.6–1.7を参照する。
3. 明示点 `(a,b,α,β)=(3,5,2,3)`、`m=[[1,1,2],[2,3,1],[1,4,5]]` は新atlasの定義域に入る。`verify_jacobian_etale_point.py` と小証明書が再開用の有限入力であり、この点の個々のcubic圏のdg smooth性まで証明したものではない。
4. 可換点の全Artin比較を使う場合はノート§5.6、有限中心幾何は§1.4–1.5へ進む。必要な新しいリスクがない限り、変更のない中心式・横断行列を再計算しない。

## 7. 主張の境界

一般族の結論は明示Δ開の標準模型と、その中のétale開 `T_B^e` からfpqc局所的に得られる族についてである。`C_J` 自体の有限型代数性・smooth性・次元17は証明したが、全Mの代数性やその中の開性・局所閉性・成分性は未証明である。全17係数空間の全点、任意のGrothendieck圏、Oを忘れた圏、裸の導来圏へ拡張しない。次数スカラー商はfpqc層商であり、大域点集合の単純な商ではない。Veroneseのμ2はGmに含まれ、追加2慣性ではない。

中心一次束Uと三次束Eの中心重みは1と3であり、それら自体をPGL商へ通常のベクトル束として降下させない。Hom(L,Sym³U)の重み0だけが必要である。O(1)や無捩れなSerre式の大域降下も結論しない。周囲を同定まで固定した2-fiberはA4 torsorだが、周囲の同型類だけを固定すると有限自己同型の作用が残り得る。
Serreはcompact圏上の主張であり、全Db(coh)の有限大域次元やdg smoothnessは含まない。相対CY/AS性と非正則基底を含む絶対的大域次元を混同しない。有限中心模型では中心準同型の単射性や全中心の底変更可換性を仮定しない。

可換点の全形式比較は、滑らかな複素三次Xを固定したframed Artin近傍である。frameを忘れた有限Aut(X)作用、未切断2群oid、一般の圏2降下、代数化へは広げない。四係数空間のmonomorphismも開埋込み・成分・atlasを意味しない。

## 8. 再現と検証範囲

`python3 scripts/verify.py` で参照・引用・TeX入力の閉包を検査する。新しいatlas点の小証明書は `python3 computations/verify_jacobian_etale_point.py --output build/jacobian_etale_point.json` で再現し、`computations/jacobian_etale_point_certificate.json` と比較する。2026-11-19に実行し、Dの37次minor=127524、Mの113次minor=844194（ともにmod1000003）、整数上のMD=0、唯一のGLスカラー核、全Δ因子の非零を確認した。小証明書には入力・helper・sourceのhashを含める。M113の再計算は新script内で行い、旧scriptの全再実行とは区別する。

同日の `verify_general17_open.py` の九項目と2026-11-16の既存八計算は有効な検証として保持し、今回の再実行とは扱わない。圏論的な降下・中心束・全Hom比較には書かれた証明と読み合わせがあり、数値検算による証明とはしない。

組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォント、既存計算にはPython3・SymPyが必要。新atlas検算はPython3標準ライブラリと同梱helperを使う。同日の先行組版試行は `lualatex.fmt` 不在で本文処理前に停止した。環境が同じなのでv15では再試行せず、現行PDF生成・視覚確認は未完了である。実施した範囲と未解決点は `validation.json` に記す。
