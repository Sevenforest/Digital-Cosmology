import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ページ設定
st.set_page_config(
    page_title="Digital Cosmology: Interactive Lab",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# タイトルとイントロダクション
st.title("🌌 Digital Cosmology: The Interactive Lab")
st.markdown("""
> **"Talk is cheap. Show me the Logic."**
>
> このアプリは、**「宇宙＝有限の計算機（デジタルシステム）」** という前提に基づき、
> 既存の物理学では説明困難な現象（重力赤方偏移、量子消しゴム）が、
> システム工学的な**「仕様（Spec）」**としてどのように再現されるかを体験するシミュレーターです。
""")

# サイドバー：設定
st.sidebar.header("⚙️ System Parameters")

# GitHubリンク (Tab 3の代わり)
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📘 Theory & Docs
Full specifications available on GitHub:
[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Sevenforest/Digital-Cosmology)
""")

# タブの作成
tab1, tab2 = st.tabs(["📉 Gravitational Redshift (The Dead Zone)", "🐱 Quantum Eraser (SQL Query)"])

# --- TAB 1: 重力赤方偏移 (The Dead Zone) ---
with tab1:
    st.header("1. 重力赤方偏移の「不感帯 (Dead Zone)」")
    st.markdown("""
    **理論の予言:**
    宇宙のエネルギー変化が離散的（デジタル）であるなら、極微小な重力ポテンシャル差においては、
    エネルギー変化が最小単位未満となり、赤方偏移が発生しない**「不感帯（階段状の挙動）」**が現れるはずです。
    """)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🔬 実験設定")
        # パラメータ設定
        delta_phi_max = st.slider("重力ポテンシャル差の範囲 (Gravitational Potential)", 10, 100, 50)
        step_size = st.slider("宇宙の最小更新ステップ (Step Size / E_PLANCK)", 1.0, 20.0, 5.0, help="この値が大きいほど、宇宙の解像度が粗くなり、階段が目立ちます。")
        
        st.write("---")
        st.markdown("**観測ノイズ (Sensitivity Analysis)**")
        noise_level = st.slider("測定器のノイズレベル", 0.0, 5.0, 0.5, help="既存の測定器ではノイズが大きく、階段が埋もれてしまいます。")
        
        show_standard = st.checkbox("標準理論（連続体）を表示", value=True)
        show_digital = st.checkbox("デジタル宇宙論（離散）を表示", value=True)

    with col2:
        # シミュレーション計算
        x = np.linspace(0, delta_phi_max, 1000)
        
        # 標準理論（連続）
        y_standard = x 
        
        # デジタル宇宙論（離散：床関数による切り捨て）
        y_digital = np.floor(x / step_size) * step_size
        
        # ノイズの付加
        y_standard_noisy = y_standard + np.random.normal(0, noise_level, len(x))
        y_digital_noisy = y_digital + np.random.normal(0, noise_level, len(x))

        # プロット
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if show_standard:
            ax.plot(x, y_standard, 'k--', alpha=0.5, label="Standard Theory (Continuous)")
            if noise_level > 0:
                ax.scatter(x, y_standard_noisy, c='gray', s=1, alpha=0.3, label="Observed (Standard)")

        if show_digital:
            ax.step(x, y_digital, 'r-', linewidth=2, where='post', label="Digital Theory (Step/Dead Zone)")
            if noise_level > 0:
                ax.scatter(x, y_digital_noisy, c='red', s=1, alpha=0.3, label="Observed (Digital)")

        ax.set_xlabel("Gravitational Potential Difference (ΔΦ)")
        ax.set_ylabel("Energy Change (Redshift)")
        ax.set_title("Continuous vs Discrete Redshift")
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        st.pyplot(fig)

        # 判定ロジック
        if noise_level < step_size / 3:
            st.success(f"✅ **検出可能！** ノイズ({noise_level}) が ステップ幅({step_size}) の1/3未満です。階段状のシグナルが有意に観測されます。")
        else:
            st.warning(f"⚠️ **検出困難** ノイズ({noise_level}) が大きすぎます。階段が埋もれてしまい、標準理論と区別がつきません。")

# --- TAB 2: 量子消しゴム (大幅アップデート) ---
with tab2:
    st.header("2. 遅延選択量子消しゴムの「脱洗脳」")
    
    # データの生成（セッション状態で保持）
    if 'quantum_db' not in st.session_state:
        num_data = 3000
        data = []
        for i in range(num_data):
            # 隠れ変数（これがデジタル宇宙の「確定した位置情報」）
            tag = np.random.choice(['Type_A', 'Type_B'])
            # Type_Aは山(干渉)、Type_Bは谷(逆干渉)の確率分布に従う
            if tag == 'Type_A':
                while True:
                    pos = np.random.randint(0, 100)
                    if np.random.rand() < np.cos((pos - 50) * 0.2) ** 2: break
            else:
                while True:
                    pos = np.random.randint(0, 100)
                    if np.random.rand() < np.sin((pos - 50) * 0.2) ** 2: break
            
            # ノイズとして観測される全データ（D0）
            data.append({'ID': i, 'Position': pos, 'Hidden_Tag': tag})
        st.session_state['quantum_db'] = pd.DataFrame(data)

    df = st.session_state['quantum_db']

    # --- SCENE 1: アカデミアの視点 ---
    st.subheader("👻 Scene 1: アカデミアが見ている「パラドクス」")
    st.info("彼らは**「スクリーン上の粒子は、観測されるまで位置が確定していない（確率の波である）」**と信じています。")
    
    col_ac1, col_ac2 = st.columns([1, 2])
    
    with col_ac1:
        st.markdown("#### 🔭 観測設定 (Future)")
        detector = st.radio(
            "未来でスイッチを切り替える:",
            ["D0 (何もしない)", "D1 (経路Aを検出)", "D2 (経路Bを検出)"],
            index=0
        )
        st.write("※ D1/D2を選ぶと、過去に着弾したはずのスクリーン上に**「干渉縞」**が現れます。")

    with col_ac2:
        # アカデミア視点のプロット
        fig_ac, ax_ac = plt.subplots(figsize=(8, 3))
        
        # フィルタリング処理
        if detector == "D0 (何もしない)":
            display_data = df
            title = "D0: Just Noise (No Pattern)"
            color = "gray"
            msg = "「ほら、ただのノイズ（山）だ。粒子はランダムに来ている」"
        elif detector == "D1 (経路Aを検出)":
            display_data = df[df['Hidden_Tag'] == 'Type_A']
            title = "D1: Interference Pattern A (Magic?)"
            color = "red"
            msg = "「なっ！？ 未来でD1を選んだ瞬間、過去のデータが『干渉縞』に変わった！ 未来が過去を書き換えたぞ！！」"
        else: # D2
            display_data = df[df['Hidden_Tag'] == 'Type_B']
            title = "D2: Interference Pattern B (Reverse Magic?)"
            color = "blue"
            msg = "「今度は逆の干渉縞だ！ まるで粒子が『未来の観測』を予知して着弾位置を変えているようだ……神秘だ……」"

        ax_ac.hist(display_data['Position'], bins=50, color=color, alpha=0.6, range=(0, 100))
        ax_ac.set_title(title)
        ax_ac.set_yticks([])
        st.pyplot(fig_ac)
        
        if detector != "D0 (何もしない)":
            st.error(f"😱 **Academia Panic:** {msg}")
        else:
            st.caption(msg)

    st.divider()

    # --- SCENE 2: デジタル宇宙論の視点 ---
    st.subheader("💻 Scene 2: デジタル宇宙論の「種明かし」")
    st.success("我々は**「位置情報は最初から確定しており、DBに保存されている」**と考えます。魔法などありません。あるのは**「フィルタリング（SQL）」**だけです。")

    if st.checkbox("👉 管理者権限で「DBの中身（ネタ）」を見る", value=False):
        col_dig1, col_dig2 = st.columns([1, 1])
        
        with col_dig1:
            st.markdown("#### 📂 サーバー上の生データ (Raw Data)")
            st.markdown("アカデミアには見えていない「隠れ変数（Tag）」が、最初から記録されています。")
            # データフレームを表示（ネタバレ）
            st.dataframe(df.head(10), use_container_width=True)
            st.caption("... (Total 3000 rows)")

        with col_dig2:
            st.markdown("#### 🧠 実行された処理 (Logic)")
            st.markdown("貴方がスイッチ（D1/D2）を切り替えた時、世界で起きたのは「因果逆転」ではなく、単なる**「WHERE句の実行」**です。")
            
            if detector == "D0 (何もしない)":
                sql = "SELECT * FROM Universe_Log"
                explanation = "全データを表示しているだけです。Type_A（山）と Type_B（谷）が混ざるので、平らに見えていただけです。"
            elif detector == "D1 (経路Aを検出)":
                sql = "SELECT * FROM Universe_Log\nWHERE Hidden_Tag = 'Type_A'"
                explanation = "「Type_A」のタグがついた行だけを抽出（SELECT）しました。**赤色のデータは最初からそこにありました。** 新しく作られたわけではありません。"
            else:
                sql = "SELECT * FROM Universe_Log\nWHERE Hidden_Tag = 'Type_B'"
                explanation = "「Type_B」の行だけを抽出しました。青色のデータが表示されただけです。"

            st.code(sql, language="sql")
            st.info(explanation)

    st.markdown("---")
    if st.button("🔄 実験をリセット (Re-run Simulation)"):
        del st.session_state['quantum_db']
        st.rerun()

