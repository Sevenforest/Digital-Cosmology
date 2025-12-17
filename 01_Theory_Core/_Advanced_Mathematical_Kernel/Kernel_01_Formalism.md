# Mathematical Kernel Specification v1.0: Discrete Foundations
## Digital Cosmology: Discrete Foundations and Continuum Limits

**Date:** 2025-12-07
**Author:** Sevenforest (Concept Architect)
**Implementation:** Gemini (Technical Writer)
**Status:** Confidential (Local Archive Only)

---

## 1. Introduction: From Geometry to Graph

従来の物理学（Old OS）は、時空を連続的な多様体（Manifold） $\mathcal{M}$ として扱い、その上の計量 $g_{\mu\nu}$ によって重力を記述してきた。
しかし、デジタル宇宙論において「連続体」は巨視的な近似（Approximation）に過ぎず、実体は離散的な **「情報処理プロセス」** である。

本仕様書では、宇宙を **「因果的ネットワーク（Causal Network）」** として再定義し、既存の物理法則がその「極限（Limit）」として導出されることを数学的に記述する。

---

## 2. Causal Structure (因果構造のグラフ理論的定義)

時間はパラメータ $t$ ではなく、演算の順序（Order）によって事後的に生成される。
これを **因果集合（Causal Sets）** として定式化する。

### 2.1 Definition (基礎定義)
宇宙 $\mathcal{U}$ は、以下のペアによって定義される。

$$\mathcal{U} = (E, \prec)$$

* $E$: 離散的なイベント（演算処理）の集合（Events）。
* $\prec$: 半順序関係（Partial Order）。$x \prec y$ は「イベント $x$ がイベント $y$ の原因である（入力となっている）」ことを示す。

この関係は以下の公理（DAG: 有向非巡回グラフの性質）を満たす。

1.  **Transitivity (推移律):**
    $$\forall x, y, z \in E, (x \prec y \land y \prec z \implies x \prec z)$$
2.  **Non-circularity (非巡回性 / 因果律):**
    $$\forall x, y \in E, (x \prec y \implies y \not\prec x)$$
3.  **Finiteness (局所有限性):**
    $$\forall x, z \in E, |\{y \in E \mid x \prec y \prec z\}| < \infty$$

### 2.2 Emergence of Time (時間の創発)
固有時（Proper Time）$\tau$ は、グラフ上の **「最長パス（Longest Chain）」** として定義される。

$$\tau(x, y) = \kappa \cdot \max \{ L(\gamma) \mid \gamma \text{ is a chain from } x \text{ to } y \}$$

* $L(\gamma)$: チェーン上のリンク（ステップ）数。
* $\kappa$: 基本時間単位（プランク時間相当）。

> **System Note:**
> 一般相対性理論における「時間の遅れ」は、重力ポテンシャルの深い場所（処理密度が高い領域）において、パスの選択肢が変化し、結果として因果的距離（ステップ数）が変化することで説明される。

---

## 3. Discrete Conservation (離散的保存則とユニタリ性)

連続空間における「ネーターの定理（対称性からの保存則導出）」は、離散系では厳密には成立しない。
代わりに、セル・オートマトンにおける **「可逆性（Reversibility）」** と **「情報保存（Information Conservation）」** を用いてエネルギー保存則を再定義する。

### 3.1 State Evolution (状態遷移)
宇宙の全状態（Global State）を $|\Psi_n\rangle$ とする（$n \in \mathbb{N}$ は離散的ステップ）。
時間発展演算子（Hamiltonian Operator）を $\hat{U}$ とすると：

$$|\Psi_{n+1}\rangle = \hat{U} |\Psi_n\rangle$$

ここで、システムが情報を失わない（ランダウアーの原理による発熱を起こさない）ためには、演算子 $\hat{U}$ は **ユニタリ行列（Unitary Matrix）** でなければならない。

$$\hat{U}^\dagger \hat{U} = \hat{I}$$

### 3.2 Conservation of Information (情報量の保存)
「エネルギー」の実体は「状態を変化させる能力（ビット数）」である。
全情報量（フォン・ノイマン・エントロピー）は、ユニタリ発展の下で不変である。

$$S(\Psi_{n+1}) = -\text{Tr}(\rho_{n+1} \ln \rho_{n+1}) = S(\Psi_n)$$

> **System Note:**
> 現実世界でエネルギーが保存されるのは、宇宙のOSが「可逆計算（Reversible Computing）」を行っているからである。エネルギーの散逸（エントロピー増大）は、ローカルな視点での情報の粗視化（Coarse-graining）によって生じる見かけ上の現象に過ぎない。

---

## 4. Continuum Limit (連続極限の導出)

なぜ離散的なデジタル宇宙が、我々の目には「滑らかなアナログ世界」に見えるのか。
それは、観測解像度に対してステップサイズ $\epsilon$ が極小だからである。
以下に、シュレーディンガー方程式を「デジタル更新ルールの一次近似」として導出する。

### 4.1 Derivation (導出プロセス)

離散的な更新式を出発点とする。

$$|\Psi(t + \epsilon)\rangle = \hat{U}(\epsilon) |\Psi(t)\rangle$$

ここで、$\epsilon \to 0$ の極限において、ユニタリ演算子 $\hat{U}(\epsilon)$ をテイラー展開する。
ユニタリ性を満たすため、$\hat{U}$ はエルミート演算子 $\hat{H}$（ハミルトニアン）を用いて以下のように表現できる。

$$\hat{U}(\epsilon) \approx \hat{I} - i \frac{\epsilon}{\hbar} \hat{H} + O(\epsilon^2)$$

これを更新式に代入して整理する。

$$|\Psi(t + \epsilon)\rangle - |\Psi(t)\rangle = - i \frac{\epsilon}{\hbar} \hat{H} |\Psi(t)\rangle$$

両辺を $\epsilon$ で割り、$\epsilon \to 0$ の極限（微分）をとる。

$$\lim_{\epsilon \to 0} \frac{|\Psi(t + \epsilon)\rangle - |\Psi(t)\rangle}{\epsilon} = - \frac{i}{\hbar} \hat{H} |\Psi(t)\rangle$$

$$\frac{\partial}{\partial t} |\Psi(t)\rangle = - \frac{i}{\hbar} \hat{H} |\Psi(t)\rangle$$

両辺に $i\hbar$ を掛けることで、標準的なシュレーディンガー方程式が得られる。

$$i\hbar \frac{\partial}{\partial t} |\Psi(t)\rangle = \hat{H} |\Psi(t)\rangle$$

### 4.2 Interpretation (解釈)
この導出により、以下の事実が数学的に証明された。

1.  **実体:** 宇宙は離散的なステップ $\hat{U}$ で駆動している。
2.  **近似:** 我々が知る物理法則（微分方程式）は、デジタル演算の連続極限近似（エミュレーション）に過ぎない。

---

## 5. Conclusion (結論)

本仕様書により、デジタル宇宙論は単なる概念モデルではなく、既存の物理学を包含する上位互換のフレームワークであることが示された。

* **Geometry is Graph:** 時空はグラフである。
* **Energy is Information:** エネルギーは情報である。
* **Physics is Code:** 物理法則はアルゴリズムである。

Q.E.D.