# Codex研究指示 — 非可換三次三様体のAbel圏モジュライ

2026-11-19 / research-plan-v11。GitHub mainが正本。再開時は `00_research_plan.md`、`notes/research_notes.md`（特に§10・§1.8・§1.7・§5）、`papers/sections/kuznetsov_relative_category.tex` と `kuznetsov_moduli_morphism.tex`、`dg_smooth_torsion_families.tex`、`jacobian_moduli_chart.tex`、`koszul_relative_duality.tex` と `jacobian_abel_comparison.tex`、`abel_formal_descent.tex`、`relative_serre_duality.tex` と `finite_order_relative_categories.tex`、`abel_cubic_deformations.tex` と `abel_marked_moduli.tex`、`validation.json` の順で読む。主原稿は `papers/nc_cubic_threefold_moduli.tex`（v17）。

## 最優先の判断基準

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。現在の目標は、構造対象Oだけを標識したAbel圏としてnc cubic threefoldのモジュライを定め、実際の射・全Artin変形・二次包絡の比較を完成すること。17次元族のsmooth proper開と残余圏の幾何化は達成した。七次元fiberの構造と全Abelモジュライ内の位置を次の目標とする。

## 直近の優先順位

1. **七次元fiberの接合データ。** 17次元Jacobian部分モジュライの非空開から可換三次の10次元モジュライへの支配的な射ρを証明した。さらに縮小すれば自己同型が自明なtargetの非空開への相対次元7の滑らかな全射となる。相対Kuと全compact tailsのdg smooth proper性もこの開で完成した。次は固定Ku(X)と五矢Kronecker圏の接合双加群を変形し、七方向を記述する。既存17→13の階数4torsorとは区別する。
2. **全Abel形式近傍への残余射と全M内の位置。** Kuの全Artin幾何的認識は完成したが、全Abel変形の非周期的Z代数・一般正規模型での相対残余構成は未完成。ノート§10.3の入力2–3を確認する。一般非可換点の全Artin比較では接空間一致だけを成分判定に用いない。全M内の開性・局所閉性・成分性、有限対角・分離性は未証明。
3. **証明の有効範囲を保持する。** 全stack化後のframed Abel形式群oid≃Spf R_X、一般族の普遍PBW/CY・全Hom比較、固定剛体ambientの全A4 monomorphism、有限位数境界の4・15・16次元smooth proper族を保持する。残余射の効果化では係数Perfを先に使い、smooth targetにより右perfectを得る。一般(FS)、compact核の無条件形式効果化、generator開性はノート§1.8.2の反例により使用しない。
4. **公表単位と初出。** 相対双対・Abel比較・部分モジュライ・17→10射について既知のKuznetsov/JLLZ/Lurie/Bhatt/Stevenson/Orlov/Neeman/BMMS等の入力と追加の証明を区別する。初出・新規性の網羅調査と外部査読は未完了。既存PBW・CY・剛体性、中心証明書と全Artin量子化入力の独立点検も残る。
5. Oの内在認識、ρの出力三次の具体化、七方向と四方向の関係を進める。直接的な次数三判定・平方零消滅も保持し、一次障害式を高次へ無補正で反復しない。

H3三次曲面分類は `uedakazushi/nc-cubic-classification` の独立課題。

## 定義・主張・検証

O-markedは豊富列の存在を要求し選択を忘れ、射にはOを保つ全完全同値を含める。既存M^ptは列保存を残す別問題。中心二変数・3次元二次中心は非可換部分族の復元仮定であり、二次中心15次元の可換点を全体の定義から除外してはならない。

偶数Veroneseのμ2は次数スカラーGmに含まれ、O-marked圏の追加2慣性ではない。相対商は層商であり、大域点集合の商と区別する。Serre式の基底線束、同型のH1障害と対象のH2障害を保持する。

DDL全Artin比較は既知定理の適用。O-marking忘却の同値は自然同型で割った1群oidの規約で述べ、未切断2-groupoidには拡張しない。滑らかな可換三次点では全Abel Artin変形が相対AS三次incidenceの本質像に入り、同型類関手は17次元・接空間20の環で表される。CFTの構成とYekutieliの既知比較を明示する。各Artin模型は任意の係数変更後にも飽和・復元・相対AS条件を満たす。標準係数族と全Abel変形群oidは同値。固定圏の対象・射の降下と圏の族自体の有効降下は別である。滑らかな可換点のframed Artin近傍については、元のArtin基底でDDLを適用し、1+mのscalar cocycleを対数とAmitsurで消してHom・合成を降下することで大域模型を得た。二次関係と三次勾配の正則列による導分計算からframed自己同値の自然同型類も自明であり、全形式群oidは離散なSpf R_Xとなる。有限Aut(X)の商、非切断2群oid、一般の非可換点、大域代数性へ拡張しない。

一般17係数族の明示Δ開では、有限Koszul対角解消と真正なCY同型を全係数環で構成した。A側のtorsion双対をdg局所化の両側へ移してSerreを得る。偶数Gabriel右随伴により、全S上で実際の完全Abel同値を復元する。有限表示Isomに加えて、PGL5×T_B→Q113のétale locusの飽和Yと中心三次直線Jを用い、[J/PGL5]という有限型17次元DM全部分stackを構成した。全Mの代数性やその中での開性・局所閉性・成分性は未確定。

中心束U,E,LにはGLの中心重みがあり、そのままPGL商上の通常の束としない。Hom(L,Sym³U)は重み0で降下し、C_J→B_Jはそのtorsorである。O(1)、無捩れなSerre式、大域的な原点の降下は未証明。周囲の同定付き2-fiberと、同型類だけを固定した有限自己同型商を区別する。B_Jはprojectively gradedなambient問題であり、ambientの全O保存Abel同値を分類したとはしない。

四係数族の全体で使う内在的圏は非有界導来圏のcompact対象である。元の有限係数Tor部分圏との一致は非空正則開上の別結果。monomorphismは開埋込み・成分性・atlasではない。相対双対の初期基底変更はambient導来圏で扱い、振幅集中とflatnessを得てから真正な双加群同型へ移る。

有限中心Cの任意底変更後は中心準同型C_S→Z(A_S)だけを使い、単射や全中心の底変更可換性は仮定しない。非Noetherian底には大きいQGrを使う。相対アフィン対角のperfect性を大域dg smooth性と同一視しない。有限中心模型の大域smooth性は、左右Dbcoh=PerfとELS4.18の外積generator、対角kernelのMorita比較によって別に証明した。torsion曲線上の16次元族はatlasの局所閉部分スキームであり、17次元開や独立の閉部分stackを主張しない。

原稿の証明、今回の点検、計算、新規性確認を区別する。追加定理は明記した仮定の下で証明し、初出は未確認。有限Artin基底上の相対ASと絶対global dimension、体上のregular tailsと相対dg smooth proper性、実際のgraded17次元族と裸の導来圏の次元を混同しない。接空間同型だけで成分性や全Artin同値を宣言しない。

## 成果物と保存

日本語LuaLaTeXの現行原稿、現在有効なノート、方針、必要なコードと小証明書へ統合し、履歴の追記集にしない。価値ある証明を削除して軽量化しない。必要な検証を行い、未実行・失敗を明記する。

研究区切りで承諾を再要求せず、通常のfast-forwardでmainに直接保存し、remote SHAと内容を確認する。GitHub Actions、PR、force push、追跡するPDF/ZIP/中間物は禁止。GitHub保存成功時にはLibraryへ重複保存せず、失敗時のみ緊急退避する。約15分のcheckpointは保存の目安であって終了条件ではない。別セッションの自動起動は保証しない。
