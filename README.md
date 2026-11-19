# 非可換三次三様体と非可換P^4のモジュライ

2026-11-19 / research-plan-v9。研究再開は最初に[研究方針](00_research_plan.md)を読む。

**現在は、構造対象Oだけを標識したAbel圏のモジュライとして、非可換三次三様体の射・変形・二次包絡を比較している。** 許容豊富列の存在を条件とし、列の選択を忘れる。数学的重要性、新規性、理解の深化、応用可能性、正確性と実現可能性を総合して研究全体の価値を最大化する。

[主原稿 v15](papers/nc_cubic_threefold_moduli.tex) ／ [研究ノート](notes/research_notes.md) ／ [検証状態](validation.json) ／ [Codex指示](AGENTS.md)。

## 現在の到達点

- **[Jacobian型Abel圏の代数的部分モジュライ](papers/sections/jacobian_moduli_chart.tex)**：滑らかな有限型17次元Deligne–Mumford stack C_J=[J/PGL5] を構成し、全O-marked問題M^Oへ任意係数で完全忠実に写した。本質像は指定したatlasの模型へfpqc局所的に戻る族である。13係数開T_B^eとT_B^e×A4がambientと三次側の実際のétale atlasを与える。
- **同節の二次包絡射 C_J→B_J は階数4ベクトル束のtorsor。** B_Jは滑らかな13次元DM stack。射はスキームで表現可能・アフィン・滑らか・全射で、中心三次完全列の分裂として記述される。一次・三次中心は任意底変更と可換する。具体的な有理点で作用とsliceの微分rank37とΔの非消滅を[小証明書](computations/jacobian_etale_point_certificate.json)で確認した。
- **[有限中心に依存しない相対Serre双対](papers/sections/koszul_relative_duality.tex)**：有限射影Koszul対角解消と相対CY5同型、中心正則三次商の下で、任意の可換係数環に対しcompact tailsはproperでSerre関手(−2)[3]を持つ。真正な双加群局所双対とdg局所化から自然なpairing・traceを構成し、非平坦・非Noetherianな底変更も含める。
- **[実際の一般17係数族への適用](papers/sections/jacobian_abel_comparison.tex)**：明示した非空開Δ≠0上で、普遍PBW、相対CY/Koszul、二次中心、飽和・偶数Gabriel復元、Noetherian係数での許容性を証明した。全O保存同値はfpqc層としてIsom_gr/Gmであり、二次・三次関係を保つPGL5の有限表示閉部分スキームにより表される。
- **この開集合ではO-marked Abel圏の同型類も一般に17次元分変動する。** 既存のgraded Rosenlicht商との比較による。二次包絡への17→13射も全O保存同値と両立する。この同型類比較は上記の部分stack構成に使う。全モジュライのatlas・成分性、Oを忘れた圏の次元、各圏のdg smoothnessは未証明。
- [構造対象付きAbel圏](papers/sections/abel_marked_moduli.tex)：相対偶数Veronese復元、Isomのμ2-torsor、次数スカラー商、Oを保つ全Abel同値のHom群oidを、明示した仮定の下で証明する。相対圏の比較にはC1–C4、またはcompact版C3を用いる。二次中心rank3は非可換部分族の条件で、可換三次点を含む全体の定義ではない。
- [可換点の全Artin変形](papers/sections/abel_cubic_deformations.tex)：De Deken–Lowenの既知定理を適用し、全Abel変形とsection Z-algebra変形を比較する。自然同型で割った1群oidではO-marking忘却も同値。二次・三次提示、次数3の有限行列による障害、平坦二次包絡からの正規三次核と相対Koszul–AS性を証明する。
- **滑らかな可換三次点の全Abel Artin変形について、Q(b)の全次数平坦性と正規三次表示を証明した。** CFTの中心量子化を実際に構成し、Yekutieliの比較とsection復元によって全変形を尽くすことを示す。同型類関手の形式環は十次元形式円板とGr(2,5)アフィン錐の積で、次元17・接空間20。未知の同次変形分類は仮定しない。
- 次数三の平坦性から全次数へ進む非周期的Z代数の直接証明と、滑らかさを要しない平方零基底の障害消滅も収録する。前者の一般原理は既知のKoszul変形原理である。
- **任意の係数環への変更後の飽和・復元も証明した。** Artin模型から任意の可換R代数Sへの変更を、大きなGrothendieck圏の係数作用として扱う。固定模型の対象・射のfpqc降下と相対同値の一意的延長も成立する。さらに全stack化後の大域Artin模型も、次項の降下定理で構成した。
- **[全stackのframed形式近傍](papers/sections/abel_formal_descent.tex)**：非Noetherianなfpqc被覆でも元のArtin基底上で線対象を持ち上げ、1+mのscalar cocycleをAmitsur完全性で消す。Homと合成の降下から大域模型を構成し、全stack化後の形式群oidを全Abel変形と同定する。さらにsection導分の直接計算でframed自己同型が消えるため、群oid自体が17次元・接空間20次元のPfaffian形式環で表される。この形式近傍は完全交叉でない。
- 全twistの線対象コホモロジーを任意底変更について計算した。n≥0はH0、n=−1は零、n≤−2はH3だけで、線対象間RHomは普遍的にperfectである。
- [有限位数境界の相対圏](papers/sections/finite_order_relative_categories.tex)：全四係数族に有限な次数付き中心模型を構成し、任意係数の全shift飽和とNoetherian底変更のC1–C2を証明する。既存の一般正則性入力の下で、非空開上の有限係数Tor部分圏=局所Perfも得る。
- **[全四係数族の相対Serre双対](papers/sections/relative_serre_duality.tex)**：既存PBW・AS・CY入力の下で、局所Perf上のS≅(−2)[3]を両側加群の双対から構成し、任意Noetherian底変更との両立を証明する。特異ファイバーを含み、正則開への制限は不要。
- **同じ節で、全O保存相対同値の比較とA4→M^Oのmonomorphismを得る。** Compact対象の内在性、普遍的二次中心、既存B_*の剛体性入力とCartierの定理を使う。非被約な有限型C基底も含め、異なる係数はO-marked圏同値で同一視されない。開埋込み・4次元成分・atlasは主張しない。
- 既存の41→37、17→13、一般fiber4の有限係数族と、正規超曲面対のgcd周期性の証明を保持する。全AS/Zモジュライの大域成分性とは区別する。

可換点の全framed形式近傍と、一般Jacobian族の代数的Abel部分モジュライを踏まえ、次は各圏のdg smoothな非空開と全Mの変形との局所比較へ進む。部分stack自体のsmooth性と個々の圏のsmooth性は区別する。全Artin残余射、7方向の接合データ、Oも忘れた復元は上位目標として保持する。詳細な達成基準と具体的着手は研究方針に記す。

## 再現

```sh
python3 scripts/verify.py
python3 computations/verify_jacobian_etale_point.py --output build/jacobian_etale_point.json
python3 computations/verify_general17_open.py
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

LuaLaTeX・latexmk・luatexja・日本語フォント、Python3・SymPyを使用。新atlas点の検算はPython3標準ライブラリと同梱の多項式helperのみで実行できる。PDF・中間物はGit追跡しない。既存計算の実行日・hashを保持し、今回の再実行とは区別する。

2026-11-19に新atlas点の150×38微分行列のrank37、全Poisson微分のrank113、整数上の積零・スカラー核、Δ非消滅を実行確認し、独立再実行の小証明書も一致した。これはstack降下・普遍中心・全Abel同値の計算証明ではなく、それらには書かれた証明と別々の読み合わせがある。参照・引用の静的検査も行う。先行組版試行は `lualatex.fmt` 不在で停止しており、環境が同じためv15は再試行していない。現行PDF生成・視覚確認は未完了。詳細は[検証状態](validation.json)。

## 関連する独立研究

- [H3非可換三次曲面分類](https://github.com/uedakazushi/nc-cubic-classification)
- [四次元AS正則Z-algebra](https://github.com/uedakazushi/asz4)
- [非可換三次曲面・中心三次商の研究](https://github.com/uedakazushi/nc-cubic)
- [P^4のPoisson構造](https://github.com/uedakazushi/poisson-p4)

GitHub mainを正本とし、現行方針・ノート・論文・必要なコードと証明書から再開できる構成を保つ。新しい定式化・組合せの初出や新規性の網羅的確認は未完了。
