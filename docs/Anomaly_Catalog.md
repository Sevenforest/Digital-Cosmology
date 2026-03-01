
# Observational Anomalies: Feature List

## Status Legend
- 🔴 **Critical**: 標準理論と直接矛盾 / 未解決
- 🟡 **Significant**: 諸説あるが決定打に欠ける / 説明が不自然
- 🟢 **Resolved**: 標準理論で一応の解決を見たが、再考の余地あり

## デジタル宇宙論による解釈の信頼度
- ⭐⭐⭐⭐⭐ 理論の核心的予言と一致（仕様）
- ⭐⭐⭐⭐ 自然な帰結として説明可能（バグ/副作用）
- ⭐⭐⭐ 概念的に整合（参考）
- ⭐⭐ 今後の精緻化が必要
- ⭐ 推測レベル

---

## 1. Redshift Quantization (Tifft Effect)
**発見者:** William Tifft (1976)  
**観測:** 銀河の赤方偏移が 72 km/s の周期で量子化  
**標準理論のステータス:** 🔴 観測誤差として棄却（説明不能）  
**デジタル解釈:** ⭐⭐⭐⭐⭐

### Digital Cosmology Explanation

```

Kernel_03: Bit Depth & Quantization
Kernel_04: Global System Clock (T_sys ≈ 3.26 Myr)

宇宙の空間管理ブロック = 1 Mpc
→ 赤方偏移の最小更新単位 = 72 km/s
→ これはシステムのアロケーションユニット（仕様）

```

**関連文書:**
- `04_Future_Experiments/Experiment_Proposal.md`
- `01_Theory_Core/_Advanced_Mathematical_Kernel/Kernel_04_System_Clock.md`

**実装例:**
- `02_Implementation_Code/Simulation_Redshift.ipynb`

---

## 2. Arp's Anomalous Redshift
**発見者:** Halton Arp (1966-)  
**観測:** 物理的に接続された天体間で異なる赤方偏移  
**標準理論のステータス:** 🔴 投影効果として棄却（統計的に不自然）  
**デジタル解釈:** ⭐⭐⭐⭐⭐

### Digital Cosmology Explanation

```

Kernel_02: Processing Lag (Z_load)
Kernel_03: Unified Shift Equation

Z_total = Z_base(d) + Z_load(T_μν)

親銀河とクエーサー = 同一距離 (Z_base固定)
クエーサーの高エネルギー密度 → 高い Z_load
→ 距離ではなく演算負荷による赤方偏移の加算

```

**関連文書:**
- `01_Theory_Core/Vol3_System_Architecture.md`
- `01_Theory_Core/_Advanced_Mathematical_Kernel/Kernel_02_Discrete_Gravity.md`

**実装例:**
- `02_Implementation_Code/Arp_Effect_PoC.ipynb`

---

## 3. Flyby Anomaly
**発見:** NASA (1990-)  
**観測:** 地球フライバイ後の探査機速度異常（mm/s オーダー）  
**標準理論のステータス:** 🟡 諸説あり（決定打なし）  
**デジタル解釈:** ⭐⭐⭐⭐⭐

### Digital Cosmology Explanation

```

Kernel_02: Processing Lag
Kernel_03: Quantization Error

高速移動 (Z_move) + 重力井戸 (Z_load)
→ 同期タイミングのズレ
→ 速度ベクトルの「丸め誤差」

これは「計算の丸め誤差が物理現象として現れる」証拠。
標準モデルが想定する「無限精度の軌道計算」との乖離。

```

**影響を受けたミッション:**
- Galileo (1990)
- NEAR (1998)
- Cassini (1999)
- Rosetta (2005)

---

## 4. CMB Cold Spot
**発見:** WMAP (2003)  
**観測:** エリダヌス・スーパーボイド（超空洞）と一致する位置にある巨大な低温領域  
**標準理論のステータス:** 🔴 偶然、またはISW効果（ただし温度低下の振幅が合わない）  
**デジタル解釈:** ⭐⭐⭐⭐⭐

### Digital Cosmology Explanation

```

Vol.3: Thermal Management

巨大なボイド（物質の欠損）が存在する
→ その座標領域には計算対象（オブジェクト）が存在しない
→ システムはリソース節約のため、その領域の処理をスキップまたは簡易化する（Sparse Optimization）
→ 結果として「情報密度（温度）」が低下する

Cold Spotは、宇宙における「計算の空白地帯（Null Zone）」の可視化である。

```

**重要性:**
物質分布（ボイド）と温度分布（Cold Spot）の相関を、
「演算密度」という単一のパラメータで説明可能にする。

> Note: 統計的な裏付け：標準的なスタッキング解析（Granett et al. 2008等）により、ボイド領域のCMB温度が統計的に低いことは確認されている。 興味深いことに、その温度低下の幅は標準理論（ISW効果）の予測値よりも大きく観測される傾向があり、デジタル宇宙論における「演算密度の低下＝排熱の消失」というモデルの方が、この現象をより適切に記述できる可能性がある。

---

## 5. Axis of Evil
**発見:** WMAP (2003)  
**観測:** CMB温度揺らぎの異常な優先方向（宇宙論原理違反）  
**標準理論のステータス:** 🔴 観測装置の偏りとして否定傾向  
**デジタル解釈:** ⭐⭐⭐⭐⭐

### Digital Cosmology Explanation

```

Kernel_01: Causal Network (DAG) & Rendering Order

宇宙 = 有向非巡回グラフ (DAG)
→ 完全な等方性（無向グラフ）は計算コスト的に成立しない
→ グラフの生成順序（レンダリング走査線）が存在する

Axis of Evil = 空間生成の「優先軸」または「走査方向」

```

**影響:**
宇宙論原理（等方性・一様性）は近似に過ぎず、微細構造では破れていることを示唆。

---

## 6. Accelerating Expansion (Details)
**発見:** Ia型超新星観測 (1998)  
**観測:** 宇宙膨張の加速（z > 1で顕著）  
**標準理論のステータス:** 🟡 ダークエネルギー（正体不明）  
**デジタル解釈:** ⭐⭐⭐⭐⭐

### Digital Cosmology Explanation

```

Kernel_03: Dynamic Heap Expansion
Vol.3: Dark Energy as Storage Scaling

情報量 I(t) の指数関数的増大
→ ヒープ領域の動的拡張（スケーリング）
→ 空間自体の「増設」による加速

遠方（過去）= ログ蓄積少 → 膨張遅い
近傍（現在）= ログ膨大 → 膨張速い

```

**関連文書:**
- `01_Theory_Core/Vol3_System_Architecture.md`

---

## 7. Amaterasu Particle (UHECR Exception)

**発見:** Telescope Array Collaboration (2021/2023)  
**観測:** 244 EeV という絶大なエネルギーを持つ宇宙線が、発生源のない「ローカル・ボイド」から飛来  
**標準理論のステータス:** 🔴 GZK限界との矛盾 / 発生源不明  
**デジタル解釈:** ⭐⭐⭐ 

### Digital Cosmology Explanation

```

External_Logic: LIV (Lorentz Invariance Violation)
Internal_Ref: Vol.3 (Thermal Management / Sparse Optimization)

1. Environmental Trigger (Void/Cold Spot):
   対象セグメントの低演算負荷により、OSの「Sparse Optimization」が有効化。

2. External Mechanism (LIV / Modified Dispersion Relation):
   $E^2 \simeq p^2 + m^2 + \eta \frac{p^3}{M_{Pl}}$
   高エネルギー領域における演算精度の限界（離散性）を定義。
   この数理モデルに基づき、衝突反応の閾値が消失したと推測。

3. Observation (Amaterasu):
   ボイド領域特有の「演算の簡略化」と「LIVによる反応制限」が重なった結果、
   通常なら遮断されるはずのパケットが、衝突例外を発生させずに到達。

```
**参考文献 (External Resources):**
- *An extremely energetic cosmic ray observed by a surface detector array* (Science, 2023)
  - https://www.science.org/doi/10.1126/science.abo5095
- *New physics as a possible explanation for the Amaterasu particle* (Lang et al., 2024 / arXiv:2405.03528)

**関連文書:**
- `01_Theory_Core/Vol3_System_Architecture.md`

---


## Summary Table

| Anomaly | Standard Status | Digital Confidence | Core Kernel / Reference |
|:--------|:----------------|:-------------------|:------------|
| Tifft Quantization | 🔴 Rejected | ⭐⭐⭐⭐⭐ | Kernel_03, 04 |
| Arp Effect | 🔴 Rejected | ⭐⭐⭐⭐⭐ | Kernel_02, 03 |
| Flyby Anomaly | 🟡 Debated | ⭐⭐⭐⭐⭐ | Kernel_02, 03 |
| CMB Cold Spot | 🔴 Ignored | ⭐⭐⭐⭐⭐ | Vol.3 |
| Axis of Evil | 🔴 Denied | ⭐⭐⭐⭐⭐ | Kernel_01 |
| Dark Energy | 🟡 Unknown | ⭐⭐⭐⭐⭐ | Vol.3 |
| Amaterasu Particle | 🔴 Critical | ⭐⭐⭐ | Vol.3 |

---

## How to Contribute

もし他の「説明困難な観測」をご存知でしたら、Issueまたは Pull Request をお願いします。

**条件:**
- 査読済み論文で報告されていること
- 標準理論で説明が困難、または無視されていること
- 観測データが公開されていること

---

## Disclaimer

本カタログは、これらの観測が「デジタル宇宙論によって証明された」ことを主張するものではありません。
これは「標準理論で説明困難な現象が、デジタル宇宙論では自然な帰結として記述可能である」ことを示すリファレンスです。

