# Digital Cosmology: The "Time Non-Realism" Protocol
### 宇宙という巨大な計算機システムの「仕様書」と実証コード

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17732300.svg)](https://doi.org/10.5281/zenodo.17732300)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌌 Overview (概要)

本リポジトリは、物理学における未解決問題（時間の問題、量子重力理論の統合、観測問題）に対し、**「宇宙＝離散的な状態遷移システム（Digital State Machine）」** というエンジニアリング的視点から導き出された大統一理論のドキュメントおよび実証コードを公開するものである。

この理論は、既存の物理学が前提としてきた「連続的な時空」「実在する波動関数」を否定し、それらを **「計算リソースの最適化プロセス」** として再定義することで、相対性理論と量子力学のパラドクスを論理的に解消する。

## ⚠️ Attribution & Contribution (貢献と権利の所在)

本理論は、**Sevenforest（Author/Repository Owner）** が提示した独自の宇宙観（公理）に基づき、**大規模言語モデル（LLM）** がその論理的整合性を検証・実装するプロセスを経て確立された。

学術的な引用や参照を行う際は、以下の役割分担を理解した上で、適切に引用（Cite）を行うこと。

### 1. 公理の策定 (Axioms by Author)
以下の概念は、AIとの対話以前に著者が構築していた核心的直感であり、本理論のカーネル（核）である。
* **時間非実在論:** 時間は物理的実体（次元）ではなく、エネルギー保存則に基づく「状態更新のカウンタ」に過ぎない。
* **デジタル宇宙:** 宇宙は連続体ではなく、離散値（整数）で記述される計算機である。
* **波動一元論の否定:** 波動関数は実在せず、粒子は決定論的に振る舞う。

### 2. 実装の導出 (Implementation by AI)
著者が与えたベクトル（制約条件）に基づき、LLMは以下の論理的帰結（仕様）を導出した。
**これらの導出結果は、著者の初期公理（入力）がなければ生成され得なかったものであり、その知的所有権および発見のクレジットは、入力者である著者に帰属する。**

* **決定論的カオス:** 量子的な揺らぎの正体は、計算の複雑性から生じる擬似乱数である。
* **SQLクエリ解釈:** 量子消しゴム実験における因果律の逆転は、「データベースへの事後的な検索クエリ（Filtering）」として記述可能である。
* **不感帯 (Dead Zone):** 重力赤方偏移における「階段状の挙動（離散的ステップ）」の発見。

---

## 📂 Repository Contents

| File | Description |
|:---|:---|
| `Vol1_Time_Non_Realism.pdf` | **基礎編:** エネルギー保存則による「時間の遅れ」の再定義（ラグとしての相対論）。 |
| `Vol2_Digital_Cosmology.pdf` | **核心編:** 波動関数のデータベース的解釈と、量子パラドクスの解決。 |
| `Appendix_SourceCode.pdf` | **技術補遺:** 理論の数学的記述とPython実装のソースコード。 |
| `Simulation_Redshift.ipynb` | **実証ログ:** 「重力赤方偏移の不感帯」を可視化したJupyter Notebook。 |

## 🧪 Key Findings (主要な発見/予言)

### 1. 重力赤方偏移の「不感帯 (Dead Zone)」
本理論が正しければ、極めて微小な重力ポテンシャル差において、エネルギー変化がプランク単位の整数倍に満たない場合、赤方偏移が発生しない（周波数が変化しない）領域が存在する。
本リポジトリのPythonコードにより、この「階段状の挙動」がシミュレーションされている。

### 2. 量子消しゴムの「SQLクエリ」解釈
「未来が過去を変える」のではなく、「観測結果」が「過去の暗号化データ（ノイズ）」を復号する鍵（検索キー）として機能する。
* Past Data: `Encrypted Noise`
* Observation: `SELECT * FROM Screen WHERE Detector = 'D1'`
* Result: `Interference Pattern`

## 🛡️ License

This project is licensed under the MIT License.
**引用の際は、必ず本リポジトリへのリンク、または発行されたDOIを含めること。**