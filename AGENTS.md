# Codex研究指示 — 非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v5。GitHub mainが正本。再開時は `00_research_plan.md`、`notes/research_notes.md`（特に§1・§5）、`papers/sections/finite_order_relative_categories.tex`、`abel_cubic_deformations.tex` と `abel_marked_moduli.tex`、`validation.json` の順で読む。主原稿は `papers/nc_cubic_threefold_moduli.tex`（v11）。

## 最優先の判断基準

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。現在の目標は、構造対象Oだけを標識したAbel圏としてnc cubic threefoldのモジュライを定め、実際の射・全Artin変形・二次包絡の比較を完成すること。17次元混合族のsmooth proper開部分、13次元ambient、残余圏の幾何化は上位目標として保持する。

## 直近の優先順位

1. **四係数族の相対Serre公式が最優先。** `finite_order_relative_categories.tex` は既存PBW・有限位数THCR入力の下でC1–C2を全係数基底上、C3とperfect RHom・底変更を非空開上で証明する。残るC4の双対・S≅(−2)[3]を固定CY ambientの相対局所双対と比較する。
2. **可換点の全Abel Artin変形と任意係数変更の飽和・復元は解決済み。** `thm:abel-cubic-flat-envelope`, `cor:abel-universal-artin-model`, `thm:abel-canonical-relative-formal` を読む。全stack化後の形式完備化との同定には圏自体の有効降下・Artin大域模型が残る。
3. 17係数族、相対周期降下、有限型incidence、実際のambient射へ拡張する。形式環や有限係数の次元から大域代数性・成分性を先取りしない。
4. actual residual map、7方向の接合データ、Oの内在認識を進める。
5. 次数三から全次数への平坦性伝播と平方零消滅は独立に保持する。一般Artinに一次障害式を無補正で反復しない。

H3三次曲面分類は `uedakazushi/nc-cubic-classification` の独立課題。

## 定義・主張・検証

O-markedは豊富列の存在を要求し選択を忘れ、射にはOを保つ全完全同値を含める。既存M^ptは列保存を残す別問題。中心二変数・3次元二次中心は非可換部分族の復元仮定であり、二次中心15次元の可換点を全体の定義から除外してはならない。

偶数Veroneseのμ2は次数スカラーGmに含まれ、O-marked圏の追加2慣性ではない。相対商は層商であり、大域点集合の商と区別する。Serre式の基底線束、同型のH1障害と対象のH2障害を保持する。

DDL全Artin比較は既知定理の適用。O-marking忘却の同値は自然同型で割った1群oidの規約で述べ、未切断2-groupoidには拡張しない。滑らかな可換三次点では全Abel Artin変形が相対AS三次incidenceの本質像に入り、同型類関手は17次元・接空間20の環で表される。CFTの構成とYekutieliの既知比較を明示する。各Artin模型は任意の係数変更後にも飽和・復元・相対AS条件を満たす。標準係数族と全Abel変形群oidは同値。固定圏の対象・射の降下と、圏の族自体の有効降下は別であり、全stack化後の形式完備化には後者が残る。有限Aut(X)の商、非切断2群oid、一般の非可換点、大域代数性へ拡張しない。

有限中心Cの任意底変更後は中心準同型C_S→Z(A_S)だけを使い、単射や全中心の底変更可換性は仮定しない。非Noetherian底には大きいQGrを使う。相対アフィン対角のperfect性を大域dg smooth性と同一視しない。

原稿の証明、今回の点検、計算、新規性確認を区別する。追加定理は明記した仮定の下で証明し、初出は未確認。有限Artin基底上の相対ASと絶対global dimension、体上のregular tailsと相対dg smooth proper性、実際のgraded17次元族と裸の導来圏の次元を混同しない。接空間同型だけで成分性や全Artin同値を宣言しない。

## 成果物と保存

日本語LuaLaTeXの現行原稿、現在有効なノート、方針、必要なコードと小証明書へ統合し、履歴の追記集にしない。価値ある証明を削除して軽量化しない。必要な検証を行い、未実行・失敗を明記する。

研究区切りで承諾を再要求せず、通常のfast-forwardでmainに直接保存し、remote SHAと内容を確認する。GitHub Actions、PR、force push、追跡するPDF/ZIP/中間物は禁止。GitHub保存成功時にはLibraryへ重複保存せず、失敗時のみ緊急退避する。約15分のcheckpointは保存の目安であって終了条件ではない。別セッションの自動起動は保証しない。
