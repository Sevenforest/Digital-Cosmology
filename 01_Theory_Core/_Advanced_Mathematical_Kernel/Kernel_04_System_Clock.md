# Mathematical Kernel Specification v2.0: Dual Clock Architecture
## Asynchronous Processing, Quantized Sync Steps, and Index Re-indexing Lag

**Date:** 2026-11-25
**Author:** Sevenforest (Concept Architect)
**Dependency:** Kernel_01 (v2.0), Kernel_02, Kernel_03 (v2.0), Vol.3 (v2.0)

---

### 概要 (Abstract)
本仕様書は、デジタル宇宙における「時間の二重性（非同期デュアル・クロック構造）」を定義する。
観測事実である「Tifftの赤方偏移の量子化（約 $72\text{ km/s}$ 周期）」と、日常的な「ミクロ時間の連続性」のギャップは、宇宙が単一のクロックではなく、**「ローカル処理（User Space）」**と**「グローバル同期（Kernel Space）」**に分離された**「非同期I/Oアーキテクチャ」**で稼働していることから生じる。
また、`Kernel_03` (v2.0) で定義された空間分割インデックス（ダークマター）がグローバル同期を待つ際に生じる更新遅延を、**「Dirty Cache（未反映の空間インデックス）」**として定式化する。

---

### 1. The Clock Rate Paradox (クロックのパラドクスと同期刻み)

#### 1.1 Primary Quantized Step ($\delta Z_{\text{global}}$)
`Kernel_03` (3章) の通り、赤方偏移の本質は物理的な後退速度ではなく同期レイテンシである。Tifftの赤方偏移量子化（速度換算 $\Delta v \approx 72\text{ km/s}$）が示す一次の仕様量は、**無次元のグローバル同期刻み $\delta Z_{\text{global}}$** である。

$$\delta Z_{\text{global}} = \frac{\Delta v}{c} \approx 2.4 \times 10^{-4}$$

広域の基底同期ラグ $Z_{\text{base}}$ は、ネットワーク上の空間管理ブロックのホップ数 $m \in \mathbb{Z}_{\ge 0}$ に応じた離散ステップとして累積する。

$$Z_{\text{base}}(m) = m \cdot \delta Z_{\text{global}}$$

#### 1.2 Approximate Scale Mapping (既存観測スケールへの近似換算)
`Kernel_01` (0章) の方針に基づき、この無次元刻み $\delta Z_{\text{global}}$ を標準宇宙論の距離・速度換算ツール（ハッブル定数の近似値 $H_0 \approx 72\text{ km/s/Mpc}$）へ便宜的に射影すると、空間管理の最小ブロックサイズおよびグローバル同期周期 $T_{\text{sys}}$ のオーダーは以下に見積もられる（※ $T_{\text{sys}}$ は同期周期を表すスカラーであり、`Kernel_02`/`05` の演算密度テンソル $T_{\mu\nu}$ とは別記号である）。

* **Block Size (近似空間単位 $L_{\text{block}}$):**
  $$L_{\text{block}} \approx \frac{\Delta v}{H_0} \approx 1\text{ Mpc} \approx 3.26 \times 10^6\text{ 光年}$$
* **Global System Tick (近似同期周期 $T_{\text{sys}}$):**
  $$T_{\text{sys}} = \frac{L_{\text{block}}}{c} \approx 3.26 \times 10^6\text{ 年} \approx 1.03 \times 10^{14}\text{ 秒}$$
* **Global Clock Frequency ($\nu_{\text{global}}$):**
  $$\nu_{\text{global}} = \frac{1}{T_{\text{sys}}} \approx 9.7 \times 10^{-15}\text{ Hz}$$

#### 1.3 Two-Tier Quantization Link to `Kernel_03`
本仕様書（v2.0）では、旧版の波長依存式（$\delta Z \propto E_{\text{bit}} / \hbar\nu_0$）を廃止し、`Kernel_03` (v2.0) と一貫する**2階層の無次元離散刻み**として統合する。

* **Local Step ($\delta Z_{\text{local}}$):** 局所空間ドメインのCPUスロットリング段数 $k(x)$ の最小刻み（`Kernel_03` 2章）。重力赤方偏移の不感帯を生む。
* **Global Step ($\delta Z_{\text{global}}$):** アドレス空間拡張および広域ブロック整合に伴う最小同期刻み。Tifftの赤方偏移量子化（$Z_{\text{base}}$ の階段構造）を生む。

いずれも空間ドメイン・同期プロトコル側の離散仕様であるため、観測する電磁波の波長帯（21cm線・可視光等）に依存せず一様に作用する。

#### 1.4 The Conflict
広域のシステム同期周期（$T_{\text{sys}}$）は、近似換算で約326万年に1回という極めて低い頻度でしか完了しない。一方、我々生命体や原子プロセスはナノ秒以下のスケールで連続的に動作している。単一クロックでは成立し得ないこのギャップを解消するのが、以下の二重時計構造である。

---

### 2. Dual Clock Architecture (二重時計構造)

宇宙システムは、処理効率と因果律の維持を両立するため、異なる更新周波数で動作する2つのクロックドメインを分離している。

#### 2.1 Local Clock (User Space / High Frequency)
* **対象:** バリオン物質（原子・恒星・生命）、局所的な相互作用および局所スロットリング（$\delta Z_{\text{local}}$）。
* **更新レート:** 観測分解能を遥かに上回る超高周波ドメイン（既存物理のプランク周波数オーダー等で近似される高解像度ステップ）。
* **機能:** **Client-Side Execution（局所先行実行）**。
* **定義:** 物質は近傍の因果関係に基づいて超高速で状態遷移を実行・確定（Local Commit）し、上位レイヤーで生じる極微小な端数負荷（$10^{-5}$ オーダー）はイベント駆動で背景セクタ $E_{\text{rad}}$ へ排熱される（`Kernel_01` 3.2節。なおCMBの基底99.99%超は下位レイヤーの定常リフレッシュにより全天均一に維持される）。この超高周波な局所更新をUI層がダウンサンプリングすることで、日常の「滑らかな連続時間」が知覚される（`Vol.5`）。

#### 2.2 Global Clock (Kernel Space / Low Frequency)
* **対象:** 広域のアドレス空間拡張（ヒープ領域）、疎な空間分割インデックス（Octree / BVH）の大域的再構築、および広域ブロック同期（$\delta Z_{\text{global}}$）。
* **更新レート:** $\nu_{\text{global}} \approx 9.7 \times 10^{-15}\text{ Hz}$（周期 $T_{\text{sys}} \approx 3.26 \times 10^6\text{ 年}$ 相当）。
* **機能:** **Global Reconciliation & Spatial Re-indexing（大域整合と空間インデックス再構築）**。
* **定義:** 1 Mpc 規模の空間ブロック間で大域的な整合性をとる同期サイクル。因果伝播の上限速度（光速 $c$）による帯域制約のため、ブロック横断的な再構築は $T_{\text{sys}}$ より高速には完了できない。

---

### 3. Asynchronous Re-indexing & Dirty Cache (非同期更新と空間インデックス遅延)

ローカルでの高速な物質移動と、グローバルでの低速な空間インデックス再構築の間に生じるタイムラグ（最大 $T_{\text{sys}}$ 相当）は、分散データベースの **結果整合性（Eventual Consistency）** モデルによって処理される。

#### 3.1 Eventual Consistency Workflow
1.  **Local Execution:** バリオン物質（$M_{\text{baryon}}$）はローカルクロックに従って移動・相互作用する。
2.  **Dirty State Accumulation:** 物質の配置が変わっても、広域の空間分割インデックス（$M_{\text{index}}$：`Kernel_03` 4章）は即座には再構築されない。変更差分は「未反映の更新キュー」として保留され、旧配置のままの空間インデックスが一時的に **Dirty Cache（更新待ち状態）** となる。
3.  **Global Re-indexing:** グローバルクロックの同期タイミング（$T_{\text{sys}}$）において、空間分割ツリーの再構築（Re-indexing）が実行され、実体配置と空間インデックスが再整合する。なお、オブジェクトが存在しない空洞領域（ボイド）は Sparse Optimization により上位レイヤーの空間インデックスが未分割（Null）のまま維持されるため、不要な再構築コストは発生しない。

#### 3.2 Role of "Dirty Cache" in Dark Matter Architecture
本仕様書（v2.0）では、ダークマターを「Dirty Cache 単体」と誤読させる旧定義を修正し、`Kernel_03` (4章) との親子関係を明確化する。

* **実体（主因）：** ダークマターの正体は、疎な空間分割インデックス（Sparse Octree / BVH）の維持オーバーヘッド $M_{\text{index}}$ である。
* **挙動（Dirty Cache）：** Dirty Cache とは「別種の第2のダークマター」ではなく、**空間インデックス $M_{\text{index}}$ がグローバル同期待ちのために実体移動へ追従しきれずにいる状態**を指す。
* **観測上の帰結:** 定常状態にある銀河では $M_{\text{index}}$ の静的構造（低密度外縁部での比率増大）が支配的となる。一方、銀河・銀河団の高速衝突や急激な大規模質量移動が発生した直後の **$T_{\text{sys}}$（近似換算約326万年）以内の過渡的フェーズ** においては、バリオンの移動に対して空間インデックスの再配置が遅延し、実体分布からズレた位置に Dirty 状態の重力源（空間インデックス）が一時的に取り残される過渡的オフセット現象が生じる（※衝突から数千万〜1億年以上が経過し、すでに複数回のグローバル再構築を完了した系は Dirty Cache の適用範囲外であり、定常的な空間インデックス分布およびバリオン配置の問題として扱う）。

---

### 4. Conclusion: The Frame Rate of Universe

我々は、$T_{\text{sys}}$（近似換算約326万年）周期で大域インデックスが再構築される広域空間の上で、超高周波なローカルクロックにより駆動される物質プロセスとして存在している。

* **Tifftの赤方偏移量子化：** グローバル同期の離散刻み $\delta Z_{\text{global}}$（広域ブロックのホップ数）が観測上に露出した仕様。
* **日常の連続時間：** ローカルクロックの超高周波更新がUI層で平滑化された UX。
* **過渡的衝突系におけるDMオフセット:** 質量再配置直後（$T_{\text{sys}}$ 以内）に空間分割インデックス（$M_{\text{index}}$）の非同期再構築待ち（Dirty Cache）が露出した過渡現象。