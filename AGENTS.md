# Codex研究指示 — 非可換三次三様体と非可換P^4

2026-11-16 / research-plan-v2。GitHub mainが正本。再開時は `00_research_plan.md`、`notes/research_notes.md`（特に§10–11）、`papers/nc_cubic_threefold_moduli.tex`、`validation.json` の順で読む。

## 最優先の判断基準

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。現在の上位目標は、既存のJacobian型17次元非可換三次族を、smooth proper圏の幾何・ambientモジュライ成分・残余圏の幾何化へ結び付けること。

## 直近の優先順位

1. 既存の41→37、17→13、gcd周期性、固定ambientでのregular tailsの仮定・証明・新規性を固定する。
2. **並行する主課題**：
   - 全Artin基底で実際の残余圏への写像を構成する。既知の HH^1=HH^3=0、HH^2=10、幾何的接写像の同型を使い、可換cubic形式変形への幾何化を狙う。既存の条件付きproduct hullと形式逆写像定理による7次元cone fiberの議論はノート§10。
   - 全混合17係数族に非空smooth proper開集合を与える。固定位数6のregular tails例と、可換cubicを含む代数的量子化族を入口にする。gldim qgr、dg smoothness、properness、相対開性を別に確認する。
3. 必要なJacobian開部分で有限型potential/incidence chart、相対周期降下、局所完全性・成分性を証明する。
4. 実際の一般点での可換cubic対応と、例外pairとの接合データに残る7方向を調べる。

全AS5/Zモジュライの代数性・開性の全面解決、有限忘却次数の全計算、P3の全分類を上記の前提にしない。H3三次曲面の完全分類は `uedakazushi/nc-cubic-classification` の別課題。

## 主張と検証

有限係数の17次元graded族は既に原稿にある。形式存在からやり直さない。一方、17次元を無標識導来圏の同型類の次元と読まない。体上の1周期化から族の降下や中心性を推論しない。finite windowの逆極限を有限型stackと呼ばない。Poisson成分・規格化CY芽・全AS/Zモジュライの成分を分ける。接空間同型だけで成分性を宣言しない。

原稿の証明、今回の点検、計算、新規性の確認を区別する。formal residual mapの構成、hullのformality入力、scalar 2慣性を明示する。形式幾何化は代数化・固定非零パラメータの同値を含まない。重要な引用は一次資料と仮定を確認する。

## 成果物と保存

日本語LuaLaTeXの現行原稿、現在有効なノート、方針、必要なコードと小証明書へ内容を統合し、履歴の追記集にしない。価値ある証明を削除して軽量化しない。必要な範囲の検証を行い、未実行・失敗を明記する。

研究区切りで承諾を再要求せず通常のfast-forwardでmainに直接保存し、remote SHAを確認する。GitHub Actions、PR、force push、追跡するPDF/ZIP/中間物は禁止。GitHub保存成功時にはLibraryへ重複保存せず、失敗時のみ緊急避難する。約15分のcheckpointは保存の目安であって終了条件ではない。別セッションの自動起動は保証しない。
