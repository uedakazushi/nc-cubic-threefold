# 非可換三次三様体と非可換P^4のモジュライ

2026-11-19 / research-plan-v4。研究再開は最初に[研究方針](00_research_plan.md)を読む。

**現在は、構造対象Oだけを標識したAbel圏のモジュライとして、非可換三次三様体の射・変形・二次包絡を比較している。** 許容豊富列の存在を条件とし、列の選択を忘れる。数学的重要性、新規性、理解の深化、応用可能性、正確性と実現可能性を総合して研究全体の価値を最大化する。

[主原稿 v10](papers/nc_cubic_threefold_moduli.tex) ／ [研究ノート](notes/research_notes.md) ／ [検証状態](validation.json) ／ [Codex指示](AGENTS.md)。

## 現在の到達点

- [構造対象付きAbel圏](papers/sections/abel_marked_moduli.tex)：相対偶数Veronese復元、Isomのμ2-torsor、次数スカラー商、Oを保つ全Abel同値のHom群oidを、明示した仮定の下で証明する。相対圏の比較にはC1–C4を追加する。二次中心rank3は非可換部分族の条件で、可換三次点を含む全体の定義ではない。
- [可換点の全Artin変形](papers/sections/abel_cubic_deformations.tex)：De Deken–Lowenの既知定理を適用し、全Abel変形とsection Z-algebra変形を比較する。自然同型で割った1群oidではO-marking忘却も同値。二次・三次提示、次数3の有限行列による障害、平坦二次包絡からの正規三次核と相対Koszul–AS性を証明する。
- **滑らかな可換三次点の全Abel Artin変形について、Q(b)の全次数平坦性と正規三次表示を証明した。** CFTの中心量子化を実際に構成し、Yekutieliの比較とsection復元によって全変形を尽くすことを示す。同型類関手の形式環は十次元形式円板とGr(2,5)アフィン錐の積で、次元17・接空間20。未知の同次変形分類は仮定しない。
- 次数三の平坦性から全次数へ進む非周期的Z代数の直接証明と、滑らかさを要しない平方零基底の障害消滅も収録する。前者の一般原理は既知のKoszul変形原理である。
- 上の局所完全性はArtin試験環での結論である。全スキーム底変更を要求する相対stackの形式完備化との同定には、普遍的saturationと復元をさらに示す。
- 既存の剛体ambientの4係数regular tails開部分では、指定された入力の下でO-marked圏が相異なり、その自己同型は自明となる。モジュライへの開埋込みや相対smooth proper性は未証明。
- 既存の41→37、17→13、一般fiber4の有限係数族と、正規超曲面対のgcd周期性の証明を保持する。全AS/Zモジュライの大域成分性とは区別する。

最優先は具体的な非可換chartで相対Hom定理のC1–C4を供給することである。17次元族の非空smooth proper開集合、全Artin残余射、7方向の接合データ、Oも忘れた復元は上位目標として保持する。全AS許容potential locusの有限型性を先に全面解決することは要求しない。

## 再現

```sh
python3 scripts/verify.py
latexmk papers/nc_cubic_threefold_moduli.tex
python3 computations/independent/verify_generic17_slice.py
python3 computations/independent/verify_generic17_center.py
python3 computations/verify_split_codimension.py
python3 computations/verify_rat113_tangent.py
python3 computations/verify_two_factor_stabilizer.py
python3 computations/verify_central_pair_centers.py
python3 computations/verify_central_pair_orbits.py
python3 computations/verify_central_symmetry.py --output build/central_symmetry.json
```

LuaLaTeX・latexmk・luatexja・日本語フォント、Python3・SymPyを使用。PDF・中間物はGit追跡しない。既存8計算の実行日・hashは検証記録に保持し、今回の再実行とは区別する。新しい主張は証明の読み合わせと参照検査を行った。組版は実行環境の `lualatex.fmt` 不在で停止し、今回のPDF生成・視覚確認は未完了。詳細は[検証状態](validation.json)。

## 関連する独立研究

- [H3非可換三次曲面分類](https://github.com/uedakazushi/nc-cubic-classification)
- [四次元AS正則Z-algebra](https://github.com/uedakazushi/asz4)
- [非可換三次曲面・中心三次商の研究](https://github.com/uedakazushi/nc-cubic)
- [P^4のPoisson構造](https://github.com/uedakazushi/poisson-p4)

GitHub mainを正本とし、現行方針・ノート・論文・必要なコードと証明書から再開できる構成を保つ。新しい定式化・組合せの初出や新規性の網羅的確認は未完了。
