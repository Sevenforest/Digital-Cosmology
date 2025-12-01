# Project "Step-Finder": Experimental Proposal for Detecting Discrete Spacetime
## 重力赤方偏移における「不感帯（Dead Zone）」検出のための実験提案書

**Status:** Request for Comments (RFC)
**Target Audience:** Experimental Physicists (Quantum Metrology, General Relativity)

---

### 1. 概要 (Abstract)
本提案書は、**Digital Theory of Everything (Digital Cosmology)** が予言する、重力赤方偏移における**「離散的な階段状挙動（Step-like behavior）」**を検出するための実験プロトコルを定義する。
既存の一般相対性理論は、重力ポテンシャル差 $\Delta \Phi$ に対して周波数が連続的に変化すると予測するが、本理論は、エネルギー変化が最小単位（プランクスケール等）の整数倍に満たない領域において、**周波数変化がゼロとなる「不感帯（Dead Zone）」**が存在すると予言する。

### 2. ターゲットとなる現象 (Target Anomaly)

#### 予測されるグラフ形状
* **Standard Model:** $\frac{\Delta \nu}{\nu} = \frac{g \Delta h}{c^2}$ （線形・連続）
* **Digital Model:** $\frac{\Delta \nu}{\nu} = \text{StepFunction}\left( \frac{g \Delta h}{c^2} \right)$ （階段状・離散）

#### 検出条件
「不感帯」を検出するためには、観測機器のノイズフロア $\sigma_{noise}$ が、宇宙の最小更新ステップ幅 $\epsilon_{step}$ よりも十分に小さい必要がある。
$$\sigma_{noise} < \frac{\epsilon_{step}}{3} \quad (3\sigma \text{ Confidence})$$

---

### 3. 提案する実験セットアップ (Proposed Setups)

#### A. 光格子時計による極微小高低差測定 (Optical Lattice Clocks)
現在、最も現実的な検証手段である。最新の光格子時計は $10^{-18}$ ～ $10^{-19}$ の精度に達しており、センチメートル～ミリメートル単位の重力赤方偏移を検出可能である。

* **手法:** 2台の光格子時計を光ファイバーで接続し、その高低差 $\Delta h$ をマイクロメートル単位で制御しながら、周波数差 $\Delta \nu$ を連続的に測定する。
* **期待される結果:**
    * 既存理論： $\Delta h$ に比例して $\Delta \nu$ が滑らかに変化する。
    * **本理論：** ある微小な $\Delta h$ の範囲内では $\Delta \nu$ が変化せず（不感帯）、閾値を超えた瞬間に「カクッ」と値が飛ぶ。

#### B. 衛星軌道上の超長基線干渉 (Space-based Interferometry)
LISAやDECIGOのような将来の重力波望遠鏡、あるいはGNSS衛星を用いた実験。

* **手法:** 地球重力ポテンシャルの勾配が緩やかなラグランジュ点付近において、長距離間の赤方偏移を測定する。
* **メリット:** ノイズ（地面振動）が少なく、積分時間を長く取れるため、微弱な「デジタル・ジッター（量子化ノイズ）」を検出できる可能性がある。

---

### 4. データ解析手法 (Analysis Method)
本リポジトリに含まれる `Simulation_Redshift.ipynb` の感度解析モジュールを使用し、観測データに対して以下の検定を行う。

1.  **線形回帰残差分析:** データが直線（アナログ）よりも階段（デジタル）にフィットするかを判定。
2.  **フーリエ変換:** 階段状の周期性がスペクトルに現れるかを確認。

### 5. 結論 (Conclusion)
もし、微小領域において赤方偏移の「不感帯」が確認されれば、それは**「宇宙が連続体ではなく、離散的な計算機である」**ことの決定的な証拠となる。
我々は、全世界の実験物理学者に対し、この「宇宙のピクセルサイズ」を測定する競争への参加を呼びかける。
