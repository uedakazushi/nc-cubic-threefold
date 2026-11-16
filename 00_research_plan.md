# 研究方針：非可換三次三様体と非可換P^4のモジュライ

2026-11-16 / research-plan-v1。研究再開時は最初に本書を読む。GitHub mainを研究の正本とする。

## 恒常的な研究原則と保存許可
数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性に基づいて目標と方針を柔軟に更新し、重要な変更は現在有効な研究方針として整理する。証明済み、追加仮定付き、未完成、予想、計算観察、先行研究の入力を区別し、原稿にある証明・今回の点検・有限計算・第三者査読を同一視しない。誤りは依存する主張に反映し、将来役立つ障害は研究ノートに残す。公表論文では一次資料を確認し、既存結果との相違をIntroductionで具体的に説明する。未確認の書誌は推測しない。

原稿は日本語LuaLaTeX、研究経緯ではなく現行の数学的論理順に記述する。価値ある結果・証明を削除・要約して軽量化しない。研究ノートには原稿にない現在有効な知識、障害、計算、例を収め、作業日誌・変更履歴・過去のZIPは残さない。研究継続用bundleは研究方針、研究ノート、論文、必要なソース・計算証明書・手順の自己完結的な最小一式とする。一般に研究区切りでの承諾不要Library保存は許可済みだが、本研究ではGitHub main正本の個別指示を優先し、GitHub保存成功時にはLibraryへ重複保存しない。保存に失敗した場合のみLibraryへ緊急避難する。GitHubの既存ファイル削除と現行bundleからの除外を区別する。

通常のfast-forwardでmainに直接pushし、remote SHAを確認する。PR、GitHub Actions、force pushは禁止。PDF・ZIP・コンパイル中間物・キャッシュはGitで追跡しない。生成・検算・組版・commit・push・remote到達確認は別の状態として報告する。

## 数学的目標・完成基準
豊富列付きの内在的非可換三次三様体のモジュライと、標準5次元二次Koszul AS-regular Z-algebraに対応する非可換P^4のモジュライを比較する。二次包絡、正規三次incidence、周期忘却、potential stack、形式変形から実際のsmooth proper圏と大域的既約成分へ進む。pointed/Z-algebra、周期付き、裸のアーベル圏、導来圏を混同しない。非可換P^3/H3三次曲面は別プロジェクトであり、その一般化を無条件に入力しない。

## 現行到達点
- 主原稿 `papers/nc_cubic_threefold_moduli.tex` と16個の証明節で相対fpqc stack、二次包絡、厳密2-fiber、有限窓、標準potential商、周期忘却と形式局所モデルを記述する。全逆極限の有限型性は未証明。
- Rat(1,1,3)の非射影化Poisson/形式ambient37、中心三次対41、一般PGL商13/17、忘却fiber4をそれぞれの限定条件で計算した。可換三次点の局所次元17、接空間20、ambientの接写像の核10・像10は一般fiber4と別の結果。
- 17係数slice、分離型余次元15、可換cubic忘却核7、混合中心とPicard、四/五頂点potential、相対正規三次の変形・復元を保持。形式的な次元計算のみからglobal componenthoodを推論しない。
- 既存の根拠と検証範囲は `validation.json`。移管前の計算実行を移管後の新規再検算と主張しない。

## 優先的な次の課題
1. 非可換P^4側のAS許容potential locusと正規三次incidenceの代数性・開性・既約成分を証明する。特に標準五頂点モデルのrank条件をscheme-theoreticに追う。
2. 相対periodizationがnormal cubic idealを保存する条件と、周期忘却の有限安定化群・次数を計算する。
3. 17次元Artinモデルの全次数の形式座標互換性と、smooth properな非可換三次圏の実変形への降下、一般繊維上の成分性を確定する。
4. 非可換P^4の既知成分との比較、裸の圏への忘却と構造対象の復元、非commutative cubicの残余/Kuznetsov成分への応用を検討する。

## 再開と再現
最初に本書、次に `notes/research_notes.md`、主原稿、必要な `papers/sections/*.tex`、`validation.json` と `computations/` を読む。外部依存は原稿中に識別子・コミットSHAを固定している。LuaLaTeX・latexmk・Python3（必要に応じてSymPy）で `latexmk papers/nc_cubic_threefold_moduli.tex`、`python3 scripts/verify.py`、`python3 computations/verify_p3_potentials.py` などを実行する。検証が実行不能ならその理由と未実行項目を明示する。
