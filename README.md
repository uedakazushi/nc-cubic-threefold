# 非可換三次三様体と非可換P^4のモジュライ

2026-11-16 / research-plan-v2。研究再開は最初に[研究方針](00_research_plan.md)を読む。

**現在の最優先は、既存の17次元混合Jacobian族を、smooth properな三次圏の開部分・ambientのモジュライ成分・残余圏の幾何化へ結び付けること。** 数学的重要性、新規性、正確性と実現可能性を総合し、研究全体の価値を最大化する。

[主原稿](papers/nc_cubic_threefold_moduli.tex) ／ [研究ノート](notes/research_notes.md) ／ [検証状態](validation.json) ／ [Codex指示](AGENTS.md)。

## 到達点と未解決の核心

- 有限係数の41次元中心三次対・37次元ambient族、PGL商の17→13次元射、一般4次元fiberの構成と証明がある。17次元は形式的な数え上げだけでなく、実際のgraded同型類の変動を扱う。
- 正則正規超曲面対について、左右AS条件・uniform index Nと次数dの下でgcd(N,d)周期性を証明する。N=5,d=3では体上の対が1周期化する。相対降下・中心化は別問題。
- 有限位数の楕円境界を持つ固定ambientでは、非空開集合上のregular tailsを扱う。一般17係数族の相対dg smooth proper性は未完成。
- Rat(1,1,3) Poisson成分と可換点の形式局所比較を持つ。全AS/Z-algebra大域モジュライの成分性とは区別する。
- 残余圏の既知HH計算と幾何的接写像の同型を使い、全Artin基底のactual residual mapと形式的積分解を早期課題にする。形式的な17→10と二次包絡の17→13は異なる射である。

全AS許容potential locusの有限型性を先に全面解決することは要求せず、既存族に沿う有限chartから進める。裸の圏・導来圏のモジュライと、豊富列付きの比較も区別する。

## 再現

```sh
latexmk papers/nc_cubic_threefold_moduli.tex
python3 scripts/verify.py
python3 computations/independent/verify_generic17_slice.py
python3 computations/independent/verify_generic17_center.py
python3 computations/verify_split_codimension.py
python3 computations/verify_rat113_tangent.py
python3 computations/verify_two_factor_stabilizer.py
python3 computations/verify_central_pair_centers.py
python3 computations/verify_central_pair_orbits.py
python3 computations/verify_central_symmetry.py --output build/central_symmetry.json
```

LuaLaTeX・latexmk・luatexja・日本語フォント、Python3・SymPyを使用。PDF・中間物はGit追跡しない。今回の主要8計算と参照検査は成功し、3証明書も一致した。組版は実行環境の `lualatex.fmt` 不在で停止したため、今回のPDF生成・視覚確認は未完了。詳細は[検証状態](validation.json)。

## 関連する独立研究

- [H3非可換三次曲面分類](https://github.com/uedakazushi/nc-cubic-moduli)
- [四次元AS正則Z-algebra](https://github.com/uedakazushi/asz4)
- [非可換三次曲面・中心三次商の研究](https://github.com/uedakazushi/nc-cubic)
- [P^4のPoisson構造](https://github.com/uedakazushi/poisson-p4)

GitHub mainを正本とし、現行方針・ノート・論文・必要なコードと証明書から再開できる構成を保つ。
