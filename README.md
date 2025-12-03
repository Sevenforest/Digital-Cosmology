# Digital Cosmology: The "Time Non-Realism" Protocol
### 宇宙という巨大な計算機システムの「仕様書」と実証コード

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17732299.svg)](https://doi.org/10.5281/zenodo.17732299)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[**🇯🇵 Japanese (Original)**](README.md) | [**🇺🇸 English**](README_en.md)

## 🌌 Overview (概要)

本リポジトリは、物理学における未解決問題（時間の問題、量子重力理論の統合、観測問題）に対し、**「宇宙＝離散的な状態遷移システム（Digital State Machine）」** というエンジニアリング的視点から導き出された **デジタル万物の理論（Digital Theory of Everything）** のドキュメントおよび実証コードを公開するものである。

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

* **決定論的カオス:** 量子的な揺らぎの正体は、計算の複雑性から生じる疑似乱数である。
* **SQLクエリ解釈:** 量子消しゴム実験における因果律の逆転は、「データベースへの事後的な検索クエリ（Filtering）」として記述可能である。
* **不感帯 (Dead Zone):** 重力赤方偏移における「階段状の挙動（離散的ステップ）」の発見。

---

## 📂 Repository Contents

### 🔰 For General Readers (一般の方へ)
専門的な論文を読む前に、まずは理論の概要をわかりやすく解説した **[👉 デジタル宇宙論・超解説シリーズ (Guide)](docs/index.md)** をご覧ください。

### 🎮 Interactive Lab (ブラウザで実験する)
理論の核心である「不感帯（階段状の赤方偏移）」や「量子消しゴムのSQLフィルタリング」を、ブラウザ上でパラメータを操作しながら体験できるWebアプリを公開しました。Python環境は不要です。

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://digital-cosmology-cwy3bcpaffkzr9hnywsatc.streamlit.app/)

**👉 [Launch Live Simulation / 実験アプリを起動する](https://digital-cosmology-cwy3bcpaffkzr9hnywsatc.streamlit.app/)**

---

| File | Description |
|:---|:---|
| `01_Theory_Core/Vol1_Time_Non_Realism.md` | **基礎編:** エネルギー保存則による「時間の遅れ」の再定義（ラグとしての相対論）。 |
| `01_Theory_Core/Vol2_Digital_Cosmology.md` | **核心編:** 波動関数のデータベース的解釈と、量子パラドクスの解決。 |
| `01_Theory_Core/Vol3_System_Architecture.md` | **システム編:** ダークマター・エネルギーの正体を「メタデータとスケーリング」として解明。 |
| `02_Implementation_Code/Appendix_SourceCode.md` | **技術補遺:** 理論の数学的記述とPython実装のソースコード。 |
| `02_Implementation_Code/Simulation_Redshift.ipynb` | **実証ログ:** 不感帯の可視化および、観測ノイズに対する **感度解析（Sensitivity Analysis）** コード。 |
| `03_Verification_Logs/VERIFICATION_LOG.md` | **歴史:** 独立したAIインスタンスによる理論の正当性検証ログ。 |
| `03_Verification_Logs/Theoretical_Stress_Test.md` | **強度証明:** 物理学的権威（AIペルソナ）との批判的対話シミュレーション記録。 |
| `04_Future_Experiments/Experiment_Proposal.md` | **実験提案:** 重力赤方偏移における「不感帯」を検出するための具体的な実験プロトコル。 |
| `05_Interactive_Lab/` | **体験:** ブラウザで動作するStreamlit製シミュレーションアプリのソースコード。 |

## 🧪 Key Findings (主要な発見/予言)

### 1. 重力赤方偏移の「不感帯 (Dead Zone)」
本理論が正しければ、極めて微小な重力ポテンシャル差において、エネルギー変化がプランク単位の整数倍に満たない場合、赤方偏移が発生しない（周波数が変化しない）領域が存在する。
*本リポジトリのPythonコードにより、この「階段状の挙動」がシミュレーションされている。*

### 2. 量子消しゴムの「SQLクエリ」解釈
「未来が過去を変える」のではなく、「観測結果」が「過去の暗号化データ（ノイズ）」を復号する鍵（検索キー）として機能する。
* Past Data: `Encrypted Noise`
* Observation: `SELECT * FROM Screen WHERE Detector = 'D1'`
* Result: `Interference Pattern`

### 3. 観測精度と検出限界 (Sensitivity Analysis)
本リポジトリには、観測機器のノイズを考慮した **感度解析モジュール** が含まれている。
* **現状:** 既存の測定器（標準的な原子時計）では、ノイズにより「階段」が埋もれてしまい、連続的な変化と区別がつかないことが示されている。
* **予言:** ノイズレベルがステップ幅の1/3を下回る高精度観測（次世代光格子時計など）において、初めて「不感帯」が統計的に有意なシグナルとして検出される。

### 4. 歴史的データとの合流 (Historical Convergence)
本理論の予言する「不感帯」は、かつてウィリアム・ティフトらが報告し、謎のまま葬られた **「赤方偏移の量子化（72 km/s 周期）」** 現象と構造的に一致する。
デジタル宇宙論は、この長年の未解決問題に対し、初めて「離散的計算リソース」という観点から合理的な理論的説明を与える。

## 🛡️ License

This project is licensed under the MIT License.
**引用の際は、必ず本リポジトリへのリンク、または発行されたDOIを含めること。**

---

> **⚠️ 批評家と学者へ**
>
> 本リポジトリは「仮説」ではなく **「システム仕様書」** である。
>
> 既存の物理学は「論理的整合性」よりも「計算結果」を優先してきたが、我々は **「論理的完結性（バグのないアーキテクチャ）」** を最優先する。
>
> したがって、旧来のパラダイムに基づく定性的な批判（例：「標準理論と矛盾する」など）は一切受け付けない。
> もし本理論内に論理的な矛盾（バグ）を発見した場合は、 **そのエラーを再現する数式またはコードを添えて、プルリクエスト（修正案）を送ってほしい。**
>
> **能書きはいい。ロジックを見せろ。**