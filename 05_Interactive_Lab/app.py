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

# タブの作成
tab1, tab2, tab3 = st.tabs(["📉 Gravitational Redshift (The Dead Zone)", "🐱 Quantum Eraser (SQL Query)", "📘 About Theory"])

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

# --- TAB 2: 量子消しゴム (Quantum Eraser) ---
with tab2:
    st.header("2. 遅延選択量子消しゴム: 「因果逆転」vs「DB検索」")
    
    st.markdown("""
    **既存のアカデミアの解釈（バグ？）:** 「未来の観測（D1/D2での検出）が、過去の粒子（スクリーン着弾）の振る舞いを変えた！ 因果律が逆転している！ 不思議だ！」

    **デジタル宇宙論の解釈（仕様！）:** 「未来も過去も関係ない。スクリーン上のデータは『暗号化されたノイズ』として既に保存されている。
    検出器の信号は、そのDBから意味のあるパターンを抽出するための**『検索キー（WHERE句）』**に過ぎない」
    """)

    col1, col2 = st.columns([1, 2])
    
    # シミュレーションの状態管理
    if 'quantum_data' not in st.session_state:
        # データ生成（過去の確定）
        num_data = 5000
        data = []
        for i in range(num_data):
            # 隠れ変数（経路タグ）
            tag = np.random.choice(['Path_A', 'Path_B'])
            
            # 位置の決定（タグに応じて確率分布を変える＝干渉の元）
            # Path_A: cos^2, Path_B: sin^2 -> 足すと1（ノイズ）になる
            if tag == 'Path_A':
                while True:
                    pos = np.random.randint(0, 100)
                    if np.random.rand() < np.cos((pos - 50) * 0.2) ** 2: break
            else:
                while True:
                    pos = np.random.randint(0, 100)
                    if np.random.rand() < np.sin((pos - 50) * 0.2) ** 2: break
            
            data.append({'ID': i, 'Position': pos, 'Tag': tag})
        st.session_state['quantum_data'] = pd.DataFrame(data)

    df = st.session_state['quantum_data']

    with col1:
        st.subheader("🎛️ 検出器（フィルタ）の選択")
        st.write("実験を開始しました。スクリーンには5000個の粒子が着弾済み（DB保存済み）です。")
        
        filter_mode = st.radio(
            "どの検出器のデータを見ますか？ (SELECT Query)",
            ["D0 (全データ/フィルタなし)", "D1 (経路Aの干渉縞)", "D2 (経路Bの干渉縞)", "D3/D4 (経路情報あり/干渉なし)"]
        )
        
        if st.button("データを再生成（実験リセット）"):
            del st.session_state['quantum_data']
            st.experimental_rerun()

    with col2:
        st.subheader("📊 スクリーン上の分布 (Query Result)")
        
        # フィルタリングロジック（これがSQLクエリの正体）
        filtered_df = df
        query_sql = "SELECT * FROM Screen_Data"
        color = 'gray'
        
        if filter_mode == "D1 (経路Aの干渉縞)":
            filtered_df = df[df['Tag'] == 'Path_A']
            query_sql = "SELECT * FROM Screen_Data WHERE Tag = 'Path_A' -- (Detector D1 Active)"
            color = 'red'
        elif filter_mode == "D2 (経路Bの干渉縞)":
            filtered_df = df[df['Tag'] == 'Path_B']
            query_sql = "SELECT * FROM Screen_Data WHERE Tag = 'Path_B' -- (Detector D2 Active)"
            color = 'blue'
        elif filter_mode == "D3/D4 (経路情報あり/干渉なし)":
            # D3/D4は経路が特定されるが、干渉はしない（単なるガウス分布の和などになるが、ここでは簡易的に全データの半分ずつとして表現）
            # ※厳密にはD3/D4は干渉項が消えるが、本デモでは「タグによる選別ができない（ランダム）」として表現
            filtered_df = df.sample(frac=0.5) 
            query_sql = "SELECT * FROM Screen_Data WHERE Detector IN ('D3', 'D4') -- (Path Known, No Interference)"
            color = 'green'

        # SQL表示
        st.code(query_sql, language="sql")

        # ヒストグラム描画
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(filtered_df['Position'], bins=50, color=color, alpha=0.7, range=(0, 100))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 250)
        ax.set_xlabel("Screen Position")
        ax.set_ylabel("Particle Count")
        
        if filter_mode == "D0 (全データ/フィルタなし)":
            ax.set_title("All Data: Just Noise (Interference Hidden)")
            st.info("全てのデータを足し合わせると、波の山と谷が打ち消し合って「ただのノイズ（山なり）」に見えます。物理学者はこれを「波動関数の収縮前」と呼びますが、エンジニアは「全件取得（SELECT ALL）」と呼びます。")
        elif filter_mode in ["D1 (経路Aの干渉縞)", "D2 (経路Bの干渉縞)"]:
            ax.set_title(f"Filtered by {filter_mode.split()[0]}: Interference Pattern Emerges!")
            st.success(f"特定のタグ（{filter_mode.split()[0]}）でフィルタリングすると、隠れていた干渉縞が浮かび上がりました！ データは最初からそこにありましたが、**クエリを投げるまで見えなかっただけ**です。")
        else:
            ax.set_title("D3/D4: No Interference Pattern")
            st.warning("経路情報が確定する（D3/D4）ということは、干渉の位相情報（タグ）が相殺される、あるいは意味をなさなくなるため、干渉縞は現れません。")

        st.pyplot(fig)

# --- TAB 3: 理論解説 ---
with tab3:
    st.markdown(open("README.md", encoding='utf-8').read())