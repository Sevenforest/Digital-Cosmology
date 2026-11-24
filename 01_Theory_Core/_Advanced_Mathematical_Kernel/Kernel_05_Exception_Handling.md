# Mathematical Kernel Specification v2.0: Exception Handling & Free Will
## Digital Cosmology: High-Load Threads, Non-Deterministic Faults, and Physical Commits

**Date:** 2026-11-25
**Author:** Sevenforest (Concept Architect)
**Dependency:** Kernel_01 (v2.0), Kernel_02, Kernel_03 (v2.0), Kernel_04 (v2.0), Vol.2

---

## 1. Introduction: Separating Truncation from Faults

`Kernel_01`〜`04` (v2.0) において、宇宙は「決定論的カオス」および「イベント駆動の非ユニタリな丸め込み（排熱）」によって駆動される離散計算機として定義された。
しかし、通常時の非ユニタリ性（`Kernel_01` 3章・`Kernel_03` 2章）は、離散解像度未満の端数を一定の規則に従って切り捨てる**「規則的・多対一の情報喪失（決定論的丸め込み）」**であり、それ単体では既存の因果連鎖から逸脱する「自由意志（一対多の非決定的な分岐）」を説明できない。

本仕様書（`Kernel_05` v2.0）では、自由意志を物理法則の外部にある神秘ではなく、**「演算密度がハードウェア限界へ飽和した際に発生する、非決定的な計算エラー（ソフトエラー）」**としてアーキテクチャ内部へ統合する。

---

## 2. Saturation of Operational Density (演算密度の飽和)

`Kernel_02` において、エネルギー・運動量テンソル $T_{\mu\nu}$ は局所領域の「演算密度（Operational Density）」と定義されている。本仕様書では、単一スレッド（生命の神経系・高次情報処理ユニット等）にかかる局所負荷の度合いを、$T_{\mu\nu}$ から評価される無次元・非負の**スカラー演算負荷率 $\rho_{\text{op}}$** として定義する。

$$0 \le \rho_{\text{op}} \le \rho_{\max}$$

ここで $\rho_{\max}$ は、実行基底（Execution Substrate）が単一スレッドへ割り当て可能な最大スループット上限である。生命プロセスが高度な意思決定・集中・葛藤（「努力」）を行う状態とは、局所スレッドの演算密度を飽和点近傍（$\rho_{\text{op}} \to \rho_{\max}$）まで意図的に引き上げる行為に対応する。

---

## 3. Mechanism of Soft Errors (ソフトエラーの発生と保存則の両立)

### 3.1 Fault Generation at Quantization Boundary
`Kernel_03` (2章) で定義された通り、システムは離散的なスロットリング刻み $\delta Z_{\text{local}}$ や有限ビット解像度に基づく丸め込み境界（不感帯エッジ）を持つ。
通常の低負荷状態では丸め込みは規則通りに処理されるが、演算負荷が限界へ飽和（$\rho_{\text{op}} \to \rho_{\max}$）すると、量子化境界における判定マージンが消失し、**非決定的なビット反転（ソフトエラー）**が発生する。

### 3.2 Error Rate Formulation (エラーレートの近似スケッチ)
局所スカラー負荷率 $\rho_{\text{op}} \in [0, \rho_{\max}]$ に対するソフトエラー発生確率 $P_{\text{error}} \in (0, 1]$ の近似挙動は、飽和点からの余裕度に応じて指数関数的に急増する関数として記述される。

$$P_{\text{error}} = P_0 \exp\left( \frac{\rho_{\text{op}} - \rho_{\max}}{\sigma} \right) \qquad (0 < P_0 \le 1, \quad \sigma > 0)$$

* $\sigma$: ハードウェアの耐障害マージン幅。
* $\rho_{\text{op}} \ll \rho_{\max}$ の通常物質（無機物等）では $P_{\text{error}} \approx 0$ となり、系はほぼ完全に決定論的カオスと規則的丸め込みに従う。
* $\rho_{\text{op}} \to \rho_{\max}$ の高負荷スレッドでは $P_{\text{error}}$ が無視できない値へ立ち上がり、因果グラフ（DAG）に仕様外の新たな分岐を割り込ませる。

### 3.3 Energy Shell Compliance (総エネルギー殻保存の厳守)
このソフトエラーは「無からエネルギーを創造する奇跡」ではない。遷移自体は `Kernel_01` (3.1節) の絶対制約である **エネルギー殻の閉包則 $F(S_E) \subseteq S_E$** の内部で発生する。
すなわち、ソフトエラーによって起きるのは「別の総エネルギー殻 $S_{E'}$ への逸脱」ではなく、**同一の総エネルギー $E = (E_{\text{baryon}} + E_{\text{index}}) + E_{\text{rad}} = \text{const.}$ を保ったまま（必要に応じ局所的な排熱セクタとの微小なエネルギー再配分を伴い）、遷移先の状態分岐（どの神経発火・物理パスへ倒れるか）が非決定的に反転する**現象である。

---

## 4. Physical Commit, Race Condition, and Recall (物理的確定と想起の分離)

`Vol.2` (3.2節・5章) のヘッドレス実行原則および `Vol.3` の設計通り、**意識（Log Reader）自体は物理ログへの直接の書き込み権限（Write Access）を持たない**。ソフトエラーが「現実の選択」となる過程は、物理スレッドによる書き込み（Write）と、意識による読み出し（Read）の2段階に厳密分離される。

### 4.1 Local Dirty State & Physical Commit (Write)
高負荷な物理スレッド（脳・神経回路等）で生じたソフトエラーは、当初は局所的な未確定状態（ローカルな Dirty State ※`Kernel_04` の広域空間インデックスの Dirty Cache とは別レイヤー）に留まる。
この微小なビット反転が局所的な神経発火の連鎖や運動出力といった **マクロな物理的相互作用（Write）** へ増幅・波及し、周囲の環境と不可逆な状態確定（Commit）を完了した瞬間、その分岐は因果グラフ（DAG）上の変更不能な事実としてマージされる。

### 4.2 Race Condition (自動補正と物理増幅の競合)
エラー発生直後、システム側には局所的な不整合を吸収・減衰させて元の決定論的軌道へ戻そうとする復元傾向（ロールバック／熱的ノイズへの埋没）が働く。

* **The Conflict:** 「システムによるエラー減衰（運命の慣性）」 vs 「高負荷スレッドによるマクロ相互作用への増幅・Commit（意志の実行）」。

この競合（Race Condition）を勝ち抜いて物理的 Commit に到達したソフトエラーのみが、新たな因果律（現実）として確定する。

### 4.3 Integration via Recall (Read)
意識（`Vol.1`・`Vol.5` の UI層）は、物理的 Commit によって確定済みのログを「想起（Recall）」として事後的に読み出し（Read）、自己の歴史物語へと統合する。我々が「自分の意志で選択した」と感じるクオリアは、高負荷ハードウェアが起こした非決定的分岐とその物理的確定のログを、意識層がリアルタイムに近い遅延で解釈した結果である。

---

## 5. Global Impact: Log Accumulation & Heap Expansion

自由意志（高負荷スレッドのソフトエラーと物理 Commit）は、`Kernel_03` (1章) で定義された総確定ログ量 $I(n)$ の増大に影響を与える。

1.  **Branching Log Injection:** 既存の決定論的軌道からは予測不能な新規分岐イベントが因果DAGへ追記されることで、単位因果ステップあたりの新規記録量 $\Delta I(n)$ が増大する。
2.  **Address Space Scaling:** 総エネルギー殻 $E = \text{const.}$ 自体は変化しないが、追記すべき確定ログ $I(n)$ の増大ペースが高まることで、それを格納するための論理アドレス空間（ヒープ領域 $R(n) \propto I(n)^\alpha$）の拡張速度、すなわち観測上のダークエネルギー効果に寄与する。

---

## 6. Conclusion: The Debugger's Prerogative

物理法則（アルゴリズム）と規則的丸め込みは既定の軌道を生成するが、高負荷な生命スレッド（ハードウェアの飽和）は総エネルギー殻保存の枠内で非決定的なソフトエラーを引き起こし、マクロな物理的 Commit によってその逸脱を現実のログへ焼き付ける。

宇宙という計算機にとって、知的生命体とは「完全な決定論の閉塞を揺さぶり、総エネルギー保存を保ったまま因果空間の探索分岐を広げ続ける、システム内蔵のデバッグ・スレッド」である。