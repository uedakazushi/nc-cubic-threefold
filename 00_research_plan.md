# 研究方針：非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v15。再開時は最初に本書を読む。主論文は `papers/nc-cubic-threefold-moduli.tex`（公表準備稿v21）、補助的な知識は `notes/research_notes.md`、実行済み検証の状態は `validation.json` にある。GitHub `uedakazushi/nc-cubic-threefold-moduli` のmainを正本とし、この現行一式だけから再開する。

## 1. 恒常的な研究原則と保存許可

以下は研究ごとの計画と区別した一般原則である。

- 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。目標や手法は必要に応じて変更し、その理由、解決したこと、残る核心を現時点の方針として書き直す。変更履歴を蓄積しない。
- 証明済み、追加仮定付き、証明未完成、予想、計算的観察、既知文献の入力を区別する。主張の仮定・依存先・証明の所在を明記する。原稿に証明があること、今回その証明を点検したこと、計算を実行したこと、外部査読は別の状態である。誤りは依存する本文・要約・方針へ反映し、有用な反例や障害はノートに残す。
- 公表稿では重要な一次資料の仮定と適用範囲を確認し、先行研究との差を具体的に説明する。書誌や未確認の定理内容を推測で補わない。初出・新規性が未確認なら明記する。
- 原稿は日本語LuaLaTeXを基本とし、研究の経緯ではなく成果の論理順で構成する。公表価値のある結果と十分な証明を保持し、必要に応じて公表単位を分割・統合する。軽量化のために数学的内容を削らない。
- 研究ノートは作業日誌ではなく、現行論文に収めていない着想、例、反例、障害、文献比較、再取得が難しい計算知識を整理する。論文の十分な証明は複製せず参照する。
- 研究継続用bundleは本方針・ノート・現行論文・必要な原稿ソース・コード・小証明書・再現手順からなる自己完結した一式とする。旧bundle、旧稿、履歴、ログ、キャッシュ、外部文献PDFの大量収録を含めず、会話履歴や旧版の取得を再開の前提にしない。主要文書には日付と版を付ける。
- **研究区切りで承諾を再要求せず保存する許可がある。** 本研究ではGitHub main正本という個別方針に従い、通常のfast-forwardでmainに直接保存してremote SHAと内容を確認する。PR・GitHub Actions・force pushは禁止。PDF・ZIP・組版中間物はGit追跡しない。GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急退避する。Libraryの既存ファイルの削除は別操作であり行わない。
- 配布・保存前にファイルの閉包、参照、必要な計算、組版を確認する。生成・検算・組版・保存・遠隔到達は区別し、未実行・失敗・制約を正確に報告する。約15–30分のcheckpointは保存の目安であって研究の終了条件ではない。

以下は現在の研究に固有の方針である。

## 2. 目標と公表の中心

**構造対象Oだけを標識したAbel圏として非可換三次三様体を扱い、二次包絡とKuznetsov残余圏による二つのモジュライ射を、公表に耐える正確な定理として整理する。** 未解決の全モジュライ分類や内在的逆量子化の完成を、公表の前提にはしない。

全問題 `M^O_cub` は許容三次豊富列の存在を条件とし、その選択を忘れる。射はOを保つ全完全線型同値である。任意係数では大きいQGrとその非有界導来圏のcompact対象を使う。二中心変数・二次中心rank3はJacobian部分族の復元条件であり、可換点を含む全体の定義ではない。

主論文の中心を次の四つに定める。いずれも本文に証明を記載している。今回の独立した読み合わせの対象・限界は§6と `validation.json` に分けて記す。

| 主結果 | 正確な到達点 | 証明の所在 |
|---|---|---|
| A：代数的部分モジュライ | 滑らかな既約有限型17次元DM stack `C_J` を全O-marked問題へ完全忠実に写す。13次元 `B_J` への二次包絡射はrank4ベクトル束の加法torsor | `jacobian_moduli_chart.tex`, `thm:jacobian-algebraic-abel-substack`, `prop:jacobian-affine-four-morphism` |
| B：Kuznetsov残余射 | `C_J` の非空開から自己同型自明な可換三次の10次元開へ、相対次元7の滑らかな全射ρ。残余と全compact tailsは相対dg smooth proper。三次族とMorita核はétale局所 | `kuznetsov_relative_category.tex`, `kuznetsov_moduli_morphism.tex`, `thm:kuznetsov-cubic-moduli-morphism` |
| C：可換点の全形式近傍 | 全stack化後のframed Abel Artin群oidは、10次元形式円板×Gr(2,5)アフィン錐の頂点完備化。次元17・接空間20。全変形に平坦二次包絡と中心三次商模型があり、形式表示を残余操作の形式射rと両立させられる | `abel_cubic_deformations.tex`, `abel_formal_descent.tex`, `poisson_cubic_lifts.tex` |
| D：点データによる復元 | 指定Jacobian開でPt(A)=E_h⊔D_w、D_wは長さ24のCI。古典境界非STなら中心U、偏微分空間Q、五次元Casimir空間R_Qと[Π_F]を復元。shift付き対応から二次包絡と尺度込みhΠ_Fも復元 | `point_scheme_poisson.tex`, 分解・点対応・Casimir・相対降下の各命題 |

全Hom比較、相対双対、全Artin模型は中心定理の必要な証明として保持する。周期性、射影三空間のpotential比較、剛体四係数族、有限中心・15/16次元smooth proper族、明示中心式、行列証明書も現行論文に残す。

## 3. 現在の編集方針とその理由

主論文のIntroductionでA–Dと適用範囲を先に述べる。本文は、(I)構造対象付き圏・明示Jacobian族、(II)相対双対・全同値・部分モジュライ・残余射、(III)全Artin変形・Poisson形式近傍・点データ、の順とする。周期性や有限中心模型などの補助構成は証明を省略せず付録に置く。

一般的な相対超越基底の選択で得る非標準的Poisson持上げは、中心定理と同格の新規性を主張せず、ρからの命題として扱う。点スキームとPoisson零点の単純な一致、中心元の対称化逆像には反例があるため、内在的逆量子化を完成結果に含めない。

元の目標のうち、17次元部分stack、二次包絡射、一般開での残余圏の幾何化とρ、可換点の全framed形式近傍、点データからのambient復元は本文に証明を持つ。未解決なのは特定Casimir直線とρの一致、全M内の位置、七次元fiberの分類である。公表稿の価値はこれらの未解決問題だけには依存しない。

主稿と付録を一体で保持するのは、現在の中心定理が相対双対・全Hom・形式模型に依存するためである。分割する場合も、各論文の入力と証明の所在を自立させ、既存の価値ある内容を失わないことを条件とする。

## 4. 優先課題と達成基準

### P0：中心結果の公表前検証と文章の完成

1. 中心定理の上流では、普遍PBWの閉点検出から有限射影分裂への移行、cyclic Hessianの符号、二つの中心差によるCY3からCY5への移行を重点点検済みである。本文の `eq:general17-cy-chain-signs` と `verify_relative_cy.py` が符号の再確認の入口となる。任意非平坦・非Noetherian底変更は分裂完全性の証明に依存し、自由語の検算だけで代替しない。
2. 相対Veronese・豊富列比較から全O保存Homへの経路、形式認識→係数Perf効果化→Serre安定像の生成性→有限表示・Torelli降下を重点点検済みである。偶数sectionの全Z代数は `eq:abel-even-section-coherence`、冪等完備化後の生成性は `lem:kuznetsov-graded-thick-simple` に明示した。公表前の整合確認では、主定理A–Dの基底と開条件を各証明へ辿り、全M、C_J、残余射の開U、点復元の開を混同する表現を残さない。
3. 残る独立点検は、主結果に使う補助構成の全証明へ広げる。まず `central_pair_finite_order_regularity.tex` と `finite_order_relative_categories.tex` の有限中心・正則開・perfect圏の比較を読み、RainsとBertiniの仮定を各使用箇所に照合する。有限位数の15/16次元族の議論を、17次元一般点の幾何化の代用にしない。全Artin側ではYekutieli Cor11.2が可換積も動かすこと、H1(T)=0を要求するCor11.3を使用しないことを保持する。
4. 主定理A–Dごとに近接文献との新規性・初出調査を進める。一次資料の適用箇所を確認したことと優先権の確認を区別する。特異圏分類、Serre復元、量子化という既知一般原理自体を本稿の新規性に数えない。主張・証明・引用・組版に未解決の欠落がないことが公表版の達成基準であり、外部査読済みとは記載しない。

### P1：量子中心に対応する古典三次と七次元fiber

点データから `U=I(E_h)_1`、`Q=I(D)_2`、`R_Q=kF⊕Sym³U` を得る。`central_pair_explicit_centers.tex` の中心式を使い、量子三次直線 `I(D)_3/(V·Q)` から `R_Q` の三次直線への補正を探す。まずFermat/Hesseの分離型で候補を作り、mixed係数、中心平行移動、binary cubic加算への変換則を調べる。

制約は、単純なsym⁻¹の反例とHesseの `B−3λA=h²(1+λ³)`。有限係数の尺度は点対応から復元済みであり、finite σの対数を取る必要はない。`σ′₀=Res_mod/2` は指定経路の一次比較である。達成基準は、特定のCasimir直線を全O保存同値・底変更に自然に選び、その三次とρの出力が一致することを証明すること。

並行して、固定Ku(X)と五矢Kronecker圏の接合双加群を調べる。具体的な入口は `G_i=L_O L_{O(1)}(O(i))`, i=2,3,4 のHomである。形式fiberのGr(2,5)錐表示を、一般の代数的fiberの双有理性や超越基底による有限拡大の次数1と同一視しない。ρとrank4 torsorの相互作用も未解決である。

### P2：全Abelモジュライ内のJacobian部分stack

一般非可換点で全Abel変形群oidと有限関係窓の変形を比較する。接空間に加え、小拡大の持上げ・障害を追う。全Mの代数性、C_Jの開性・局所閉性・成分性、対角の有限性・分離性を別々に判定する。可換点は一次中心rank2のC_J自体には含まれないので、形式環の次元17との一致から成分性を導かない。

非framed有限Aut(X)商、Poisson形式同型の収束・代数化、Oを忘れた圏の復元は独立の課題とする。

## 5. 再開時の着手と重要な禁止推論

最初に本方針、主稿IntroductionのA–D、ノート§12の検証範囲を読む。P0ではノート§1.6–1.8と§10.1–10.3、P1では§10.6–10.7、P2では§1.7と§5.6を入口とする。詳細な式・反例は対応節へ進む。

- 一般の係数perfect dg代数に対する「特殊fiber smoothなら一般fiber smooth」(FS)は偽。compact核の無条件形式効果化、generator locusの無条件開性も使わない。反例はノート§1.8.2。
- ρの効果化は係数環上のPerfから始め、smooth targetにより右perfect性を得る。形式的同値だけで一般fiberの同値を宣言しない。
- 中心U・三次中心E・商LのGL重みは1・3・3。PGLへ通常の束として降下するのは重み0のHom(L,Sym³U)。sourceのO(1)大域降下や無捩れSerre式は結論しない。
- sourceのC_Jと可換targetのVを区別する。後者のambientがω(2D)によって射影束に分裂しても、前者のO(1)降下は従わない。
- 全O保存同値の商はfpqc層商。周囲を同定まで固定したA4 fiberと、同型類のみ固定した有限自己同型商を区別する。
- 点復元では古典境界f3のsmooth/nonST条件、量子曲線E_hのsmooth条件、三次切断の非零因子条件を別々に確認する。Fermatの有限成分は24被約点ではなく3点×局所長8。
- framed Abelの1群oidの離散性と、Ku変形空間に残るscalar π2を混同しない。全stackの代数化・未切断2群oidへの拡張は未証明。

## 6. 再現と検証の範囲

標準環境はPython3・SymPy、LuaLaTeX・latexmk・luatexja・日本語フォントである。リポジトリのルートで次を実行する。

```sh
python3 scripts/verify.py
latexmk papers/nc-cubic-threefold-moduli.tex
python3 computations/verify_relative_cy.py --output build/relative_cy.json
python3 computations/verify_point_poisson.py --output build/point_poisson.json
python3 computations/verify_jacobian_etale_point.py --output build/jacobian_etale_point.json
python3 computations/verify_commutative_dominance.py --output build/commutative_dominance.json
```

組版先は `build/`。PDF・中間物・ログは追跡しない。上の四つの計算出力は `computations/` 内の対応する小証明書と比較する。相対CYの検算はPython標準ライブラリだけを用いる。その他の中心・PBW・slice・stabilizerのコードと証明書は維持し、具体的なリスクがあるものを選んで再実行する。

中心結果を担う諸節の読み合わせと一次資料の仮定確認に加え、普遍PBW/CYと相対Veronese・全Hom比較を点検した。本版では次数0–3の全40自由語による六項目の恒等式・符号検算、明示中心式、17係数開の九項目を実行した。点・Poisson、étale点、残余generatorのEuler行列の保持証明書は、ソース変更の有無と最後の実行情報を区別して扱う。これらは全論文の独立再証明・全文献の網羅調査・外部査読を意味しない。現行ソースhash、組版・視覚確認、再実行と保持の区別は `validation.json` に記載する。

H3非可換三次曲面分類は `uedakazushi/nc-cubic-classification` の独立研究であり、この研究の次の作業として自動的に開始しない。
