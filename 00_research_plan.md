# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v11。研究再開時は最初に本書を読む。GitHub mainを正本とする。今回の変更前の確認済み基点は `8c037c64f686fc825a1c12c8182c40b208556c3b`。証明は `papers/nc_cubic_threefold_moduli.tex`（v17）と入力節、補助的知識は `notes/research_notes.md`、検証範囲は `validation.json` に置く。

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

現在の核心は、七次元fiberの接合データによる記述、全Abelモジュライ内でのJacobian部分stackの位置、可換点の全Abel形式近傍上への残余射の拡張である。実際の17係数族の結果を、非周期的Z代数や一般の正規三次模型へ無条件に延長しない。

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

新しい二節の証明について、相対射影・Serre・Euler・PBW/CY橋渡し、全Artin認識・効果化、graded生成性・有限表示降下・Torelli降下を分けて読み合わせた。支配性の35次minorを実行検算した。これは外部査読でも、既存全証明の独立再証明でもない。既知入力と本研究の具体的な組合せを区別し、初出・新規性の網羅調査は未完了とする。

一般の係数perfect dg代数について「特殊ファイバーsmoothなら一般ファイバーsmooth」という命題(FS)は偽である。反例と、形式compact性・generator開性の別の障害をノート§1.8.2に保存する。上の定理は(FS)に依存せず、相対Serreと三次三様体固有の生成性で証明する。

## 4. 現在の方針を採る理由

Abel圏を直接扱うための相対Serre、全O保存同値、有限表示Isomと代数的部分stackは完成した。一般族の個々の圏のdg smooth性については、有限位数境界の稠密性だけでは一般点に進めない。そこで可換三次への量子化退化を用い、残余圏を通じて幾何性を回復する。形式的に幾何的なKuを認識し、係数perfect複体として同値核を効果化すると完全忠実な埋込みが得られる。相対Serreのtrace比較と、Serre安定な非零thick部分圏はKu全体になるという生成補題が全射性を与える。

この構成は17次元一般点へ函数体単射で届き、有限表示の降下により非空開へ広がる。Torelliにより三次の同型類が一意なので、核の選択に依存せずモジュライ射が降下する。したがって元の目標のうち、17次元の非空dg smooth proper開と可換三次モジュライへの射は解決した範囲である。全M内の開性・局所閉性・成分性、七次元fiberの具体的分類は残る。

O(1)自体を商stack上へ降下させずとも、その基底直線束twistはmutationの評価で消える。これが全O-marked Abel同値に自然な残余圏を取れる理由である。targetの自己同型が自明な開へ制限すれば、粗モジュライへの射は通常の三次モジュライstackへの射ともなる。相対Morita核はétale局所で構成し、大域的な核の存在は結論に含めない。

## 5. 優先課題と達成基準

### P1：七次元fiberの幾何と接合

`ρ:U→V` は相対次元7の滑らかな全射である。固定した可換三次Xに対し、Ku(X)と五矢Kronecker圏を接合して得るO-marked tailsの変形を、接合双加群と二例外対象の配置から記述する。まず `G_i=L_O L_O(1)(O(i))`、i=2,3,4のHomと、例外pairへの接合加群を計算し、ρの接写像の核がどの変形を表すかを確定する。Feyzbakhsh–Liu–Zhangのgluing objectとの比較を入口とするが、一対象だけで七方向を尽くすとは仮定しない。

達成基準は、一般fiberの局所モジュライ解釈と七次元という次元の構造的説明、可能なら固定Ku上の接合データによる代数的表示である。既存17→13の四次元torsorとの関係、ρがそのtorsor上で定数かどうかも別途調べる。入力三次形式Fをρの出力と同一視せず、高次補正の有無を計算する。

### P2：全Abel形式近傍とJacobian部分stackの位置

可換点の全Abel形式環は確定しており、Kuの全Artin形式認識も証明した。ただし全Abel模型は非周期的Z代数・正規三次商を含み、中央CY模型用の相対残余構成をそのまま適用できるとは未証明である。ノート§10.3の条件付き積分解では、全Artin基底上の自然な残余射と幾何的部分での一致を完成させる。対象の持上げ・compact性・例外性・admissibility・相対dg Serreを、一般の全Abel模型について確認する。

一般非可換点では全Abel変形群oidと有限関係窓の変形群oidを比較する。接空間一致だけを成分判定に用いず、小拡大の持上げと障害を扱う。全M内での開性・局所閉性・成分性の必要十分条件を得ることが達成基準である。有限stabilizer、対角の有限性、分離性も別々に調べる。

### P3：公表単位・先行研究・内在的復元

中心結果として、(a)全Abel三次変形の二次包絡とframed形式近傍、(b)相対双対とJacobian型代数的Abel部分モジュライ、(c)Kuznetsov成分による17→10射と七次元fiberを検討する。論理的なまとまりと新規性を調査して分割・統合を決める。正規超曲面対の周期、既存の有限中心結果など有効な証明は保持する。

Kuznetsov/JLLZ/Lurie/Bhatt/Stevenson/Orlov/Neeman/BMMSとPBW・CY・連続性の一次入力は、各定理の仮定と本研究の追加部分をIntroductionとノート§11で比較する。初出・新規性の網羅調査、第三者査読、旧PBW/CY・全Artin量子化入力の独立全面監査は未完了。Oを忘れた復元、特異三次への拡張は別課題である。

## 6. 再開時の具体的着手

1. 本方針の後、ノート§10と `kuznetsov_relative_category.tex`、`kuznetsov_moduli_morphism.tex` を読む。主定理は `thm:kuznetsov-cubic-moduli-morphism`。形式認識、係数perfect効果化、Serre安定生成性、有限表示降下の順序を維持する。
2. P1では相対残余generatorと例外pairの接合双加群から始める。全tailsのsmooth性は既に得ているので、その証明を反復せず、七次元fiberを記述する変形複体を作る。
3. P2ではノート§10.3の入力2–3を確認する。全Artinの幾何的Ku認識は完成済みだが、全Abel族からの残余射とは別の結果である。
4. 代数的atlasと全Abel同値はノート§1.6–1.7、有限中心と一般点からのsmooth性拡張は§1.8。ノート§1.8.2の反例により、一般(FS)、形式compact性からの無条件効果化、generatorの開性を使わない。
5. 支配性の入力は `commutative_dominance_certificate.json`。既存atlasの横断性証明書と役割を区別し、変更のない計算は具体的なリスクがなければ再実行しない。

## 7. 主張の境界

一般族の結論は明示Δ開の標準模型と、その中のétale開 `T_B^e` からfpqc局所的に得られる族についてである。`C_J` 自体の有限型代数性・smooth性・次元17は証明したが、全Mの代数性やその中の開性・局所閉性・成分性は未証明である。全17係数空間の全点、任意のGrothendieck圏、Oを忘れた圏、裸の導来圏へ拡張しない。次数スカラー商はfpqc層商であり、大域点集合の単純な商ではない。Veroneseのμ2はGmに含まれ、追加2慣性ではない。

中心一次束Uと三次束Eの中心重みは1と3であり、それら自体をPGL商へ通常のベクトル束として降下させない。Hom(L,Sym³U)の重み0だけが必要である。O(1)や無捩れなSerre式の大域降下も結論しない。周囲を同定まで固定した2-fiberはA4 torsorだが、周囲の同型類だけを固定すると有限自己同型の作用が残り得る。
Serre自体はcompact圏上の主張であり、全Db(coh)の有限大域次元やdg smoothnessは含まない。dg smooth性は有限位数境界上の相対開に加え、残余射の定理により17次元の非空開でも別に証明した。16次元族はatlasの局所閉部分スキームであり、独立の閉部分stackや17次元開と同一視しない。相対CY/AS性と非正則基底を含む絶対的大域次元を混同しない。有限中心模型では中心準同型の単射性や全中心の底変更可換性を仮定しない。

Abel圏側の可換点の全形式比較は、滑らかな複素三次Xを固定したframed Artin近傍である。frameを忘れた有限Aut(X)作用、未切断2群oid、一般の圏2降下、代数化へは広げない。四係数空間のmonomorphismも開埋込み・成分・atlasを意味しない。

## 8. 再現と検証範囲

`python3 scripts/verify.py` で参照・引用・TeX入力の閉包を検査する。既存のatlas点の小証明書は `python3 computations/verify_jacobian_etale_point.py --output build/jacobian_etale_point.json` で再現し、`computations/jacobian_etale_point_certificate.json` と比較する。2026-11-19の既存検証で実行し、Dの37次minor=127524、Mの113次minor=844194（ともにmod1000003）、整数上のMD=0、唯一のGLスカラー核、全Δ因子の非零を確認した。小証明書には入力・helper・sourceのhashを含める。M113の再計算は新script内で行い、旧scriptの全再実行とは区別する。

同日の `verify_general17_open.py` の九項目と2026-11-16の既存八計算は有効な検証として保持し、今回の再実行とは扱わない。圏論的な降下・中心束・全Hom比較には書かれた証明と読み合わせがあり、数値検算による証明とはしない。今回の残余射の証明には文献の仮定確認と別々の読み合わせがある。新しく `python3 computations/verify_commutative_dominance.py --output build/commutative_dominance.json` を実行し、35×42微分行列の35次minorが752849 mod1000003であることとEuler関係を確認した。証明書は入力・source・helperのhashを含む。これは支配性の計算であり、圏の同値を数値計算で証明したものではない。

組版は `latexmk papers/nc_cubic_threefold_moduli.tex`。LuaLaTeX・latexmk・luatexja・日本語フォント、既存計算にはPython3・SymPyが必要。atlas検算と新しい支配性検算はPython3標準ライブラリと同梱helperを使う。同日の先行組版試行は `lualatex.fmt` 不在で本文処理前に停止した。現行v17の組版は実行しておらず、現行PDF生成・視覚確認は未完了である。実施した範囲と未解決点は `validation.json` に記す。
