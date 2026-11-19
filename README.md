# 非可換三次三様体と非可換P^4のモジュライ

2026-11-19 / research-plan-v13。研究再開は最初に[研究方針](00_research_plan.md)を読む。

**現在は、構造対象Oだけを標識したAbel圏のモジュライとして、非可換三次三様体の射・変形・二次包絡を比較している。** 許容豊富列の存在を条件とし、列の選択を忘れる。数学的重要性、新規性、理解の深化、応用可能性、正確性と実現可能性を総合して研究全体の価値を最大化する。

[主原稿 v19](papers/nc_cubic_threefold_moduli.tex) ／ [研究ノート](notes/research_notes.md) ／ [検証状態](validation.json) ／ [Codex指示](AGENTS.md)。

## 現在の到達点

- **[Point schemeからのPoisson復元](papers/sections/point_scheme_poisson.tex)**：一般のJacobian模型で、埋込みpoint schemeの曲線成分と長さ24の有限成分から、ambient Poisson構造の射影類と五次元三次Casimir空間を復元した。shiftを付ければ二次包絡も復元でき、有限係数のambient Poisson構造を尺度込みで得る。特定のCasimir直線とKuznetsov残余射ρとの一致は残る。
- **点加群の一次持上げ可能点はPoisson零点scheme。** smoothな中心三次とPoisson一次括弧の仮定の下で、任意非被約基底上の局所的持上げについて証明した。有限係数のpoint schemeは楕円曲線と長さ24の完全交叉に分かれる。
- **有限Hesse族では埋込み零点への単純な一致が不可能。** 古典・量子境界smooth、h≠0、有限成分がCIという開で、どのsmooth cubicに替えてもpoint scheme全体をPoisson零点にできない。Fermat族の平坦閉包は半古典零点へ退化し、shift速度はmodular residueの半分である。

- **[Poisson構造付き三次への持上げ](papers/sections/poisson_cubic_lifts.tex)**：17次元非空開上で、Kuznetsov残余射ρに両立する非零Poisson構造付き三次への支配的な射を構成した。相対有理座標の選択を含む。scheme atlasからの合成は縮小後étaleだが、双有理性や選択を不要とする逆量子化は未証明。
- **可換点の全Abel形式近傍では、残余射rに両立するPoisson形式近傍との同型まで得た。** 既存の全Artin中心商表示、CY orientationを使わないcompact/proper模型とO(1)持上げの一意性によりrを構成する。量子化比較と形式座標補正を選ぶため非標準的。形式fiberはGr(2,5)アフィン錐の頂点完備化で、次元7・接空間10。
- **中心三次の単純な対称化逆像には反例がある。** Fermat中心式から得る滑らかな三次が、対応するambient Poisson括弧のPoisson超曲面にならないことを射影chart上でも証明した。量子補正を含む内在的持上げの不存在は主張しない。

- **[Kuznetsov成分による17→10のモジュライ射](papers/sections/kuznetsov_moduli_morphism.tex)**：17次元Jacobian型Abel圏モジュライC_Jの非空開Uから滑らかな可換三次の10次元モジュライへの支配的な射ρを構成した。ρ(c)は残余圏がKu(X_c)とdg Morita同値になる唯一の三次の同型類である。さらに縮小すれば、自己同型が自明なtargetの非空開Vへの相対次元7の滑らかな全射U→Vとなる。
- **同じ開で残余圏と全compact tailsは相対dg smooth proper。** [相対残余構成](papers/sections/kuznetsov_relative_category.tex)は任意導来底変更と全O-marked Abel同値に自然である。形式的な幾何的認識、係数perfectな核の効果化、Serre安定な像の生成性、有限表示降下とcategorical Torelliを使う。étale局所で三次族と相対同値を得る。
- **支配性を[小証明書](computations/commutative_dominance_certificate.json)で補強した。** 古典三次形式へのGL5作用と17係数族の微分のrank35を、35次minor=752849 mod1000003により確認した。ρの出力三次が入力形式Fそのものであるとは主張しない。
- **[相対dg smooth properな16次元族と稠密性](papers/sections/dg_smooth_torsion_families.tex)**：17次元Jacobian atlasの任意の非空開Wの中に、Hesse楕円族のtorsion曲線Z上のZ×A15の非空開Vを取り、V上のcompact tailsが任意係数変更と両立する相対dg smooth proper族となることを証明した。固定境界では15次元、固定ambientでは4次元の相対開も得る。smooth proper複素点はatlasとC_Jで稠密。17次元一般点とその非空開のsmooth性は上記の残余射で別に証明した。
- **同節で大域対角と一般点からの拡張を証明した。** 有限中心射影模型の左右Dbcoh=PerfとELSの外積generatorから、大域dg対角のperfect性を得る。係数-perfectなdg代数の一般点がsmoothなら、TVのperfect加群の連続性とconeの消滅から非空主開へ広がる。未知のhfpやclosedpointからのopennessは仮定しない。

- **[Jacobian型Abel圏の代数的部分モジュライ](papers/sections/jacobian_moduli_chart.tex)**：滑らかな有限型17次元Deligne–Mumford stack C_J=[J/PGL5] を構成し、全O-marked問題M^Oへ任意係数で完全忠実に写した。本質像は指定したatlasの模型へfpqc局所的に戻る族である。13係数開T_B^eとT_B^e×A4がambientと三次側の実際のétale atlasを与える。
- **同節の二次包絡射 C_J→B_J は階数4ベクトル束のtorsor。** B_Jは滑らかな13次元DM stack。射はスキームで表現可能・アフィン・滑らか・全射で、中心三次完全列の分裂として記述される。一次・三次中心は任意底変更と可換する。具体的な有理点で作用とsliceの微分rank37とΔの非消滅を[小証明書](computations/jacobian_etale_point_certificate.json)で確認した。
- **[有限中心に依存しない相対Serre双対](papers/sections/koszul_relative_duality.tex)**：有限射影Koszul対角解消と相対CY5同型、中心正則三次商の下で、任意の可換係数環に対しcompact tailsはproperでSerre関手(−2)[3]を持つ。真正な双加群局所双対とdg局所化から自然なpairing・traceを構成し、非平坦・非Noetherianな底変更も含める。
- **[実際の一般17係数族への適用](papers/sections/jacobian_abel_comparison.tex)**：明示した非空開Δ≠0上で、普遍PBW、相対CY/Koszul、二次中心、飽和・偶数Gabriel復元、Noetherian係数での許容性を証明した。全O保存同値はfpqc層としてIsom_gr/Gmであり、二次・三次関係を保つPGL5の有限表示閉部分スキームにより表される。
- **この開集合ではO-marked Abel圏の同型類も一般に17次元分変動する。** 既存のgraded Rosenlicht商との比較による。二次包絡への17→13射も全O保存同値と両立する。この同型類比較は上記の部分stack構成に使う。全モジュライのatlas・成分性と、Oを忘れた圏の次元は未証明。
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

現在の中心課題は、復元した三次Casimir空間から量子中心に対応する直線を選び、ρが復元する三次との一致を示すことである。有限係数の尺度はpoint correspondenceから復元できた。point schemeの一次零点と射影ambient復元は証明済みで、有限係数での文字通りの零点一致には障害がある。量子補正の同変性、七次元fiberの接合データ、全Abelモジュライ内のJacobian部分stackの位置は残る。詳細な達成基準は研究方針にある。

## 再現

新しい厳密恒等式の小証明書は、`python3 computations/verify_point_poisson.py --output build/point_poisson.json` で再生成し、`computations/point_poisson_certificate.json` と比較する。9項目の式とsource SHA256を記録する。

```sh
python3 scripts/verify.py
python3 computations/verify_commutative_dominance.py --output build/commutative_dominance.json
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

既存24計算資産は変更・再実行せず保持した。今回のpoint schemeの結果は記載した証明と別々の読み合わせを点検し、行列式・Hessian補正・可積分性minor等の9項目は新しいSymPyの厳密記号計算で全て通過した。既知のJacobian Torelli、point/Poisson比較、modular residueとの違いをIntroductionに記載した。参照・引用の静的検査と組版は区別する。先行組版試行は `lualatex.fmt` 不在で停止し、現行v19の組版は実行していない。現行PDF生成・視覚確認は未完了。詳細は[検証状態](validation.json)。

## 関連する独立研究

- [H3非可換三次曲面分類](https://github.com/uedakazushi/nc-cubic-classification)
- [四次元AS正則Z-algebra](https://github.com/uedakazushi/asz4)
- [非可換三次曲面・中心三次商の研究](https://github.com/uedakazushi/nc-cubic)
- [P^4のPoisson構造](https://github.com/uedakazushi/poisson-p4)

GitHub mainを正本とし、現行方針・ノート・論文・必要なコードと証明書から再開できる構成を保つ。新しい定式化・組合せの初出や新規性の網羅的確認は未完了。
