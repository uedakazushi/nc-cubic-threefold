# Codex研究指示 — 非可換三次三様体と非可換P^4
2026-11-16。GitHub mainが唯一の正本。再開時は `00_research_plan.md`、`notes/research_notes.md`、`papers/nc_cubic_threefold_moduli.tex`、`validation.json` の順で読む。三次曲面H3の完全分類は別リポジトリ `uedakazushi/nc-cubic-moduli` の仕事であり、本研究をそのタスクへ戻さない。

主課題は非可換P^4のAS/Z-algebra potential stack、三次正規incidence、period-forgetting、17次元Artin形式変形とsmooth proper/大域成分との比較。証明・仮定・依存結果・有限検算と未証明を正確に分ける。形式局所次元から大域成分性を宣言しない。重要な新規性は一次文献で確認する。主原稿は日本語LuaLaTeX、研究ノートは現在有効な数学のみを収める。

研究を逐次継続し、約15分のcheckpointは保存の目安（終了条件ではない）。数学的内容を現行原稿・研究方針・ノート・必要なコード/小証明書へ統合。利用可能なテストを実行し、未実行は明記してmainへfast-forward push、remote SHAを確認する。GitHub Actions、PR、force push、Git追跡するPDF/ZIP/中間物を用いない。GitHub保存成功時にはLibraryへの重複保存をせず、失敗時のみ緊急避難。変更履歴や古いバックアップをbundleに入れない。別セッションの自動起動は保証しない。
