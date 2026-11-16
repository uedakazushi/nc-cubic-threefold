# 非可換三次三様体と非可換P^4のモジュライ

2026-11-16。元の `uedakazushi/nc-cubic-moduli` から非可換三次三様体・非可換射影四空間の研究を独立させた現行正本。研究の再開はまず [研究方針](00_research_plan.md) を読む。

## 研究内容
標準5次元二次Koszul AS正則Z-algebraの非可換P^4と、正規三次商としての非可換三次三様体を、豊富列・二次包絡・周期構造を介して比較する。相対fpqc stack、pointed potentials、正規三次incidence、形式変形と中心対を扱う。

[主原稿](papers/nc_cubic_threefold_moduli.tex) ／ [研究ノート](notes/research_notes.md) ／ [証明・計算の検証状態](validation.json) ／ [Codex指示](AGENTS.md)。

主原稿には41次元中心対、37次元形式ambient、17係数の横断族とモジュライ比較などがある。これらの形式的・相対的な結果を全大域stackの既約成分やsmooth proper locusの被覆とは同一視しない。

## 再現
```sh
latexmk papers/nc_cubic_threefold_moduli.tex
python3 scripts/verify.py
python3 computations/verify_p3_potentials.py
python3 computations/verify_rat113_tangent.py
python3 computations/verify_two_factor_stabilizer.py
python3 computations/verify_central_pair_centers.py
python3 computations/independent/verify_generic17_slice.py
```
LuaLaTeX・latexmk・luatexja、Python3と必要なSymPyを使用。PDF・ログ・キャッシュはGit追跡しない。移管元の `validation.json` の実行歴は当時の検証記録であり、移管後の再実行ではない。

## 関連する独立研究
- [H3非可換三次曲面分類](https://github.com/uedakazushi/nc-cubic-moduli)
- [四次元AS正則Z-algebra](https://github.com/uedakazushi/asz4)
- [非可換三次曲面](https://github.com/uedakazushi/nc-cubic)
- [P^4のPoisson構造](https://github.com/uedakazushi/poisson-p4)

外部入力は主原稿に必要な文献情報・コミットを記載し、本リポジトリには現行研究を再開・検証する最小限のソースを保持する。
