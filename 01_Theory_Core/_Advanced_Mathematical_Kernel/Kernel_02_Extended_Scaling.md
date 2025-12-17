# Mathematical Kernel Specification v1.1: Extended Scaling / Dependency: Kernel_01
## Entropic Gravity, Topological Mass, and Dynamic Scaling

**Date:** 2025-12-09
**Author:** Sevenforest (Concept Architect)
**Implementation:** Gemini (Gen-9 Technical Writer)
**Dependency:** Vol.4 Mathematical Formalism (v2.0)

---

## 6. Dynamic Scaling of Address Space (Dark Energy)

Vol.3 で定義された「宇宙の加速膨張」を、ログデータの増大に伴うアドレス空間の動的割り当て（Dynamic Allocation）として数理的に記述する。

### 6.1 Log Accumulation Law (ログ蓄積則)
宇宙の全情報量（Total Information Content） $I(t)$ は、過去の全イベントの累積として定義される。

$$I(t) = \sum_{\tau=0}^{t} N_{events}(\tau)$$

因果律により情報は削除されない（Immutable）ため、$\frac{dI}{dt} \geq 0$ は常に成立する。さらに、相互作用の複雑性が増すにつれて、単位時間あたりの生成情報量（イベント密度）も増大する傾向にある。

### 6.2 Holographic Bound & Radius Expansion (ホログラフィック境界と半径拡張)
ベッケンシュタイン境界およびホログラフィック原理により、ある領域が保持できる最大情報量 $I_{max}$ は、その境界表面積 $A$ に比例する（$I_{max} \propto A \propto R^2$）。
しかし、システム全体のストレージ容量（体積 $V$）として確保すべきアドレス空間は、蓄積された総情報量 $I(t)$ を格納するのに十分でなければならない。

システムが「メモリ不足（OOM）」を回避するための最小半径 $R(t)$ は、以下のスケーリング則に従う。

$$R(t) \propto \left( I(t) \right)^{\alpha}$$

ここで $\alpha$ は次元数に依存するスケーリング係数である。
ログ $I(t)$ が指数関数的に増大する場合、宇宙のスケール因子 $a(t)$ もまた加速的に増大する。

$$\frac{d^2 a}{dt^2} > 0 \iff \frac{d^2 I}{dt^2} > 0$$

> **System Note:**
> 観測される「斥力（加速膨張）」は物理的な力ではなく、情報爆発（Information Explosion）に追いつくためにシステムが強制実行している **「ヒープ領域の拡張（Heap Expansion）」** の速度である。

---

## 7. Information Theoretic Redshift (不感帯の厳密化)

重力赤方偏移における「不感帯（Dead Zone）」の発生メカニズムを、情報理論的な「ビット深度（Bit Depth）」の観点から定式化し、物理的根拠を与える。

### 7.1 Minimum Bit Energy (最小ビットエネルギー)
システムが状態 $S_n$ から $S_{n+1}$ へ遷移するためには、最低でも1ビットの情報量変化が必要である。
ランダウアーの原理に基づき、この最小エネルギーコスト $E_{bit}$ を定義する。

$$E_{bit} = k_B T_{sys} \ln 2$$

ここで $T_{sys}$ はシステムの等価演算温度である。

### 7.2 Quantized Update Condition (量子化更新条件)
重力ポテンシャル差 $\Delta\Phi$ によるエネルギーシフト $\Delta E_{grav}$ が、この $E_{bit}$ を下回る場合、状態遷移は情報の意味を持たず、システムによって棄却（Discard）される。

**Update Condition:**
$$|\Delta E_{grav}| \geq E_{bit} \implies \text{Commit}$$
$$|\Delta E_{grav}| < E_{bit} \implies \text{Rollback (No Change)}$$

この条件により、観測される振動数シフト $\Delta\nu$ は、連続的ではなく、情報単位に基づく離散的なステップ関数となる。

$$\Delta\nu = \nu_0 \cdot \text{sgn}(\Delta\Phi) \cdot \left\lfloor \frac{|\Delta E_{grav}|}{E_{bit}} \right\rfloor$$

これは「階段状」の赤方偏移（不感帯）を、人為的な床関数の導入ではなく、熱力学的・情報工学的必然性として導出するものである。

---

## 8. Topological Mass (ダークマターのグラフ理論的定義)

「見えないが重力を持つ」ダークマターを、グラフ理論における「エッジコスト（接続コスト）」として定義する。

### 8.1 Universe as a Weighted Graph (重み付きグラフとしての宇宙)
宇宙グラフ $G = (V, E)$ において、全質量（全計算コスト） $M_{total}$ は、ノードコスト（物質）とエッジコスト（構造）の和である。

$$M_{total} = \sum_{v \in V} w(v) + \sum_{e \in E} c(e)$$

* **Baryonic Matter:** $M_{baryon} = \sum w(v)$ （ノードの重み＝粒子の質量）
* **Dark Matter:** $M_{dark} = \sum c(e)$ （エッジのコスト＝空間構造の維持コスト）

### 8.2 Spatial Index Overhead (空間インデックスのオーバーヘッド)
銀河団のような大規模構造（密なサブグラフ）を維持するためには、ノード間を結ぶエッジ（相互作用パス）の数が、ノード数の二乗オーダー（$O(N^2)$）で増大する可能性がある。

$$M_{dark} \approx \beta \cdot (M_{baryon})^\gamma \quad (\gamma > 1)$$

これにより、物質（ノード）が少なくても、それらを結ぶネットワーク構造（エッジ）が複雑であれば、計算コスト（重力源）は増大する。
「銀河の回転曲線問題」は、周辺部におけるノード密度（物質）の低下に対し、空間を維持するためのエッジ密度（ダークマター）が減少しないため、見かけ上の質量が過剰に観測される現象として説明される。

> **System Note:**
> ダークマターは見えない粒子ではなく、**「空間（関係性）そのものの維持コスト」** である。我々は「データ」の重さだけでなく、「データベースのインデックス構造」の重さを観測している。

---

## 9. Conclusion of Addendum

本拡張モジュールにより、以下の3点が追加補強された。

1.  **Dark Energy:** ログ増大による必然的なストレージ拡張プロセス。
2.  **Redshift Dead Zone:** 情報エントロピーの量子化による更新棄却。
3.  **Dark Matter:** ネットワーク・トポロジーの維持コスト。

これらは全て、Vol.4 で定義された「宇宙＝計算機」というカーネル仕様から自然に導かれる帰結である。

**Status:** Ready for Verification.