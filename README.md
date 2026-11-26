# 非可換三次三様体：Abel圏の変形・モジュライ・Kuznetsov比較

**共同研究：** 本リポジトリは大川新之介・植田一石の共同研究プロジェクトです。この表示は個々の論文の著者を確定するものではありません。

2026-11-21 / research-plan-v18・主稿v23＋点スキーム独立二稿v2。

構造対象Oを保つ全ての完全Abel圏同値を射として、非可換三次三様体のモジュライと、二次包絡・Kuznetsov残余圏による二つの射を研究する。

**研究再開は[研究方針](00_research_plan.md)から。** [主論文](papers/nc-cubic-threefold.tex) ／ [研究ノート](notes/research_notes.md) ／ [検証状態](validation.json) ／ [作業指示](AGENTS.md)。

## 三次三様体の現行公表論文

本repoには本文のある主原稿 [nc-cubic-threefold.tex](papers/nc-cubic-threefold.tex) と、点スキームに特化した独立論文 [mixed-cubic-point-schemes.tex](papers/mixed-cubic-point-schemes.tex)・[diagonal-cubic-point-geometry.tex](papers/diagonal-cubic-point-geometry.tex) を保持する。後者二稿は以前 `nc-cubic-point` の正本であった内容を引き継ぐ。特別な非可換三次三様体の点加群、楕円成分・長さ24の有限部分、零変形への平坦極限、次数56の衝突判別式、shift付き復元を扱う。主論文の点復元と補題の重複証明は避けるが、未照合の数学的結果は削らない。

点スキームの現行知識は [notes/point_schemes.md](notes/point_schemes.md)、検算コードは `computations/point/`、移管後の確認状態は [validation_point_schemes.json](validation_point_schemes.json) を参照する。

## 担当範囲と他研究との関係

このリポジトリを**非可換三次三様体（dimension 3）に固有の成果の入口**とする。最も重要な独立成果は、可換三次三様体点における全O-marked Abel圏のframed Artin形式近傍（主定理C）である。17次元Jacobian部分stack（A）、実際の残余Ku射と相対dg smooth proper性（B）、特殊な点データと尺度（D）を組み合わせる。

[一般次元のnc-cubic](https://github.com/uedakazushi/nc-cubic) が全n≥3の一ブロック moduli・残余Poisson射の一般次数9／符号商18・比較核のPicard障害の正本である。これらを三様体で再証明せずn=3特殊化を引用する。**未証明：** 同repoの良い一ブロックstackと本稿のJacobian stackの共通開の厳密な同定、同repoの残余Poisson射の可換三次への忘却と本稿のρの一致、全O-markedモジュライの成分性。

[poisson-cubic](https://github.com/uedakazushi/poisson-cubic) は古典的Poisson正規形、[cubic-quantization](https://github.com/uedakazushi/cubic-quantization) はその代数的量子化、点スキーム・非被約退化の現行正本は本repo、[pfaffian-brill-noether](https://github.com/uedakazushi/pfaffian-brill-noether) は三次三様体のPfaffian/Brill--Noether研究、[nc-cubic2](https://github.com/uedakazushi/nc-cubic2) は相対復元の別研究の正本。独立した公表原稿をこのrepoへ機械的に合併しない。

## 論文の中心結果

| 結果 | 内容 | 主な証明 |
|---|---|---|
| A：代数的部分モジュライ | 全O-marked問題に完全忠実な、滑らかな既約有限型17次元DM stack。13次元の二次包絡stackへの射はrank4ベクトル束の加法torsor | [Jacobian部分モジュライ](papers/sections/jacobian_moduli_chart.tex) |
| B：17→10の残余射 | 非空開上で残余圏は滑らかな可換三次のKuとなり、相対次元7の滑らかな全射を得る。同じ開で残余と全compact tailsは相対dg smooth proper | [相対残余構成](papers/sections/kuznetsov_relative_category.tex)、[残余射](papers/sections/kuznetsov_moduli_morphism.tex) |
| C：可換点の全形式近傍 | framed Abel Artin群oidは10次元形式円板×Gr(2,5)アフィン錐の完備化。次元17・接空間20。全変形の平坦二次包絡・中心三次商模型と、残余形式射に両立する表示 | [全Artin模型](papers/sections/abel_cubic_deformations.tex)、[形式降下](papers/sections/abel_formal_descent.tex)、[Poisson比較](papers/sections/poisson_cubic_lifts.tex) |
| D：点データの復元 | 指定Jacobian開で楕円曲線と長さ24の完全交叉。古典境界非STなら点スキームから五次元Casimir空間とPoisson直線を復元。shift付き点対応から二次包絡と尺度も復元 | [点スキームとPoisson構造](papers/sections/point_scheme_poisson.tex) |

これらの主張には本文に証明がある。今回点検した範囲と、未完了の独立検証・新規性調査は[検証状態](validation.json)に分けて記載している。全モジュライの分類や成分性を完成したとは扱わない。

## 読み方

Introductionで主定理A–Dと先行研究との関係を述べる。第I部はモジュライの定義と明示的なJacobian中心三次族、第II部は相対双対・全同値・代数的部分モジュライ・残余射、第III部は全Artin変形とPoisson幾何である。周期性、非可換射影三空間との比較、有限中心模型、16次元smooth proper族、正確な行列証明書の補助結果は、証明を保ったまま付録に置く。

中心となる未解決問題は、量子中心に対応する古典Casimir直線を自然に選び、残余射ρの出力三次との一致を示すことである。相対有理座標による非標準的Poisson持上げは、内在的な逆量子化と区別する。中心元の単純な対称化や、有限点スキームをそのままPoisson零点にする方法には反例がある。

## 再現

リポジトリのルートで実行する。

```sh
python3 scripts/verify.py
latexmk papers/nc-cubic-threefold.tex
python3 scripts/check_point_schemes.py
python3 scripts/check_point_schemes.py --calculations
latexmk papers/mixed-cubic-point-schemes.tex
latexmk papers/diagonal-cubic-point-geometry.tex
python3 computations/verify_relative_cy.py --output build/relative_cy.json
python3 computations/verify_point_poisson.py --output build/point_poisson.json
python3 computations/verify_jacobian_etale_point.py --output build/jacobian_etale_point.json
python3 computations/verify_commutative_dominance.py --output build/commutative_dominance.json
```

LuaLaTeX、latexmk、luatexja、日本語フォント、Python3、SymPyを用いる。既定の日本語フォントはNoto Serif CJK、利用できない場合はHarano Aji Mincho。`.latexmkrc` とVS Codeの設定はルートからのLuaLaTeXビルドに対応する。出力は `build/nc-cubic-threefold.pdf`。

計算の出力は `computations/` の対応する小証明書と比較する。`verify_relative_cy.py` はPython標準ライブラリだけで全40自由語の恒等式とcochain符号を検算し、PBW・解消の完全性は本文で別に証明する。`scripts/verify.py` はTeX入力・参照・引用の静的検査であり、数学的証明の検証を代替しない。PDF・中間物・ZIP・キャッシュはGit追跡しない。GitHub mainに現行一式を保存し、旧版の取得なしに再開できる構成を保つ。

## 関連する独立研究

[非可換三次曲面分類](https://github.com/uedakazushi/nc-cubic-classification) ／ [四次元AS正則Z代数](https://github.com/uedakazushi/asz4) ／ [古典的Poisson幾何](https://github.com/uedakazushi/poisson-cubic) ／ [三次の代数的量子化](https://github.com/uedakazushi/cubic-quantization) ／ [全次元非可換三次](https://github.com/uedakazushi/nc-cubic) ／ [P4のPoisson構造](https://github.com/uedakazushi/poisson-p4)。これらの課題や全分類を本論文の結論と混同しない。

## 旧リポジトリの扱い

`nc-cubic-point` はこのrepoへの移管後の正本ではない。新リポジトリで必要なTeX・計算と参照を検証したうえで、GitHub管理画面から削除する予定。旧repoにある研究ノート・旧版ソースを研究再開時に取得する必要はない。削除前にリンク・引用・組版・コードの参照を確認する。
