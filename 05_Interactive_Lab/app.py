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
> このアプリは、 **「宇宙＝有限の計算機（デジタルシステム）」** という前提に基づき、
> 既存の物理学では説明困難な現象（重力赤方偏移、量子消しゴム）が、
> システム工学的な **「仕様（Spec）」** としてどのように再現されるかを体験するシミュレーターです。
""")

# サイドバー
st.sidebar.header("⚙️ System Parameters")
st.sidebar.info("パラメータを操作して、宇宙の挙動（バグか仕様か）を確認してください。")
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📘 Theory & Docs
Full specifications available on GitHub:
[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Sevenforest/Digital-Cosmology)
""")

# タブの作成
tab1, tab2 = st.tabs(["📉 Gravitational Redshift (The Dead Zone)", "🐱 Quantum Eraser (SQL Query)"])

# ==========================================
# TAB 1: 重力赤方偏移 (不感帯の可視化)
# ==========================================
with tab1:
    st.header("1. 重力赤方偏移の「不感帯 (Dead Zone)」")
    st.markdown("""
    **理論の予言:**
    宇宙のエネルギー変化が離散的（デジタル）であるなら、極微小な重力ポテンシャル差においては、
    エネルギー変化が最小単位未満となり、赤方偏移が発生しない **「不感帯（階段状の挙動）」** が現れるはずです。
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

        ax.set_xlabel("Gravitational Potential Difference (Delta Phi)") # 英語に変更
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

        with st.expander("💡 ヒント： どうすれば「階段」が見える？"):
            st.markdown("""
            このシミュレーターで「デジタル宇宙の証拠」を見つけるには、以下の設定を試してみてください。
            
            1. **ノイズを消す:** `測定器のノイズレベル` を **0.0** （または小さく）にしてみてください。
            2. **解像度を下げる:** `宇宙の最小更新ステップ` を **大きめ (10.0以上)** にします。
            3. **ズームイン:** `重力ポテンシャル差の範囲` を **小さく (20以下)** にします。
            
            👉 **プロットされた「赤い点（観測データ）」が、階段状に並んで見えませんか？**
            ノイズが減ると、バラバラだった点が「宇宙のピクセル（不感帯）」の形に整列するのが分かります。
            逆に、ノイズを増やすと、階段が埋もれて「普通の坂道」に見えてしまうことも確認できます。
            これこそが、標準理論（連続的な黒い線）が見落としていた宇宙の姿です。
            """)

# ==========================================
# TAB 2: 量子消しゴム (SQLクエリ解釈)
# ==========================================
with tab2:
    st.header("2. 遅延選択量子消しゴムの「脱洗脳」")
    st.markdown("物理学者が「未来が過去を変えた！」と大騒ぎするパラドクスを、データベースの仕様として解き明かします。")
    
    # --- 0. データの生成（過去の確定） ---
    # セッション状態でデータを保持することで、「過去は変わっていない」ことを保証する
    if 'quantum_db' not in st.session_state:
        num_data_init = 3000
        data = []
        for i in range(num_data_init):
            # 隠れ変数（これがデジタル宇宙の「確定した位置情報」）
            # アカデミアには見えないが、DBには最初から書き込まれている
            tag = np.random.choice(['Type_A', 'Type_B'])
            
            # Type_Aは山(干渉)、Type_Bは谷(逆干渉)の確率分布に従う
            if tag == 'Type_A':
                while True:
                    pos = np.random.randint(0, 100)
                    # 山を作る確率分布
                    if np.random.rand() < np.cos((pos - 50) * 0.2) ** 2: break
            else:
                while True:
                    pos = np.random.randint(0, 100)
                    # 谷を作る確率分布
                    if np.random.rand() < np.sin((pos - 50) * 0.2) ** 2: break
            
            data.append({'ID': i, 'Position': pos, 'Hidden_Tag': tag})
        st.session_state['quantum_db'] = pd.DataFrame(data)

    df = st.session_state['quantum_db']

    st.divider()

    # --- SCENE 1: アカデミアの視点 (The Paradox) ---
    st.subheader("👻 Scene 1: アカデミアが見ている「パラドクス」")
    st.info("彼らは **「スクリーン上の粒子は、観測されるまで位置が確定していない（確率の波である）」** と信じています。")
    
    col_ac1, col_ac2 = st.columns([1, 2])
    
    with col_ac1:
        st.markdown("#### 🔭 未来の観測設定")
        st.write("過去にスクリーンに着弾した粒子の「ペア」を、今から観測します。")
        detector = st.radio(
            "検出器のスイッチ:",
            ["D0 (経路不明・放置)", "D1 (経路Aを検出)", "D2 (経路Bを検出)"],
            index=0
        )

    with col_ac2:
        # --- 厳密な描画ロジック (np.histogram + bar) ---
        fig_ac, ax_ac = plt.subplots(figsize=(8, 4))

        # 1. 共通設定
        BINS = 50
        RANGE = (0, 100)
        
        # ヒストグラムの数値を先に計算する（描画ズレを防ぐため）
        # 全体（ノイズ）
        counts_total, bin_edges = np.histogram(df['Position'], bins=BINS, range=RANGE)
        # D1成分（赤）
        counts_d1, _ = np.histogram(df[df['Hidden_Tag'] == 'Type_A']['Position'], bins=BINS, range=RANGE)
        # D2成分（青）
        counts_d2, _ = np.histogram(df[df['Hidden_Tag'] == 'Type_B']['Position'], bins=BINS, range=RANGE)
        
        # 棒グラフの中心位置
        bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
        # Y軸の最大値を固定
        Y_MAX = max(counts_total) * 1.1

        # 2. 背景（Total）を常にグレーで描画
        # これが「全データ」の枠になります
        ax_ac.bar(bin_centers, counts_total, width=(100/BINS), color='lightgray', label='Total Signal (Noise)', align='center')

        # 3. 選択された成分を「手前」に上書き描画
        if detector == "D0 (経路不明・放置)":
            # D0: 全体を少し濃いグレーで強調
            ax_ac.bar(bin_centers, counts_total, width=(100/BINS), color='gray', alpha=0.5, label='Observed', align='center')
            title = "D0: Just Noise (Total)"
            msg = "「ほら、ただのノイズ（山）だ。干渉縞なんてない。粒子はランダムだ」"
            count_text = f"Total Particles: {len(df)}"
        
        elif detector == "D1 (経路Aを検出)":
            # D1: 赤色で上書き。
            # グレーの「はみ出している部分」が D2 であることが明確になる。
            ax_ac.bar(bin_centers, counts_d1, width=(100/BINS), color='red', alpha=0.8, label='D1 (Path A)', align='center')
            title = "D1: Interference Pattern A"
            msg = "「なっ！？ 未来でD1を選んだ瞬間、過去のスクリーンに『干渉縞』が浮かび上がった！ 因果律が崩壊したぞ！！」"
            count_text = f"D1 Particles: {len(df[df['Hidden_Tag'] == 'Type_A'])} / Total: {len(df)}"
        
        else: # D2
            # D2: 青色で上書き。
            ax_ac.bar(bin_centers, counts_d2, width=(100/BINS), color='blue', alpha=0.8, label='D2 (Path B)', align='center')
            title = "D2: Interference Pattern B"
            msg = "「今度は逆の干渉縞だ！ まるで粒子が『未来の観測』を予知して着弾位置を変えているようだ……神秘だ……」"
            count_text = f"D2 Particles: {len(df[df['Hidden_Tag'] == 'Type_B'])} / Total: {len(df)}"

        # グラフ装飾
        ax_ac.set_title(title)
        ax_ac.set_ylim(0, Y_MAX)
        ax_ac.set_xlim(0, 100)
        ax_ac.set_xlabel("Screen Position")
        ax_ac.set_yticks([]) # 目盛りは消す
        ax_ac.legend(loc='upper right')
        
        # 数値の整合性を証明するテキスト
        ax_ac.text(0.02, 0.95, count_text, transform=ax_ac.transAxes, fontsize=9, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

        st.pyplot(fig_ac)
        
        if detector != "D0 (経路不明・放置)":
            st.error(f"😱 **Academia Panic:** {msg}")
        else:
            st.caption(msg)

        # --- グラフの見方ガイド ---
        st.info("""
        **📊 グラフの見方 (Visual Guide):**
        
        このヒストグラムは、以下の数式に基づいて描画されています。
        
        $$ \\text{Gray (Total)} = \\text{Red (D1)} + \\text{Blue (D2)} $$
        
        * **D1 (赤) を選んだ時:**
            赤色の棒の上に残って見える「灰色の余白」は、 **「D2 (青)」の成分そのもの** です。隙間やバグではありません。
        * **D2 (青) を選んだ時:**
            同様に、残った灰色の余白は「D1 (赤)」の成分です。
            
        ぜひ、赤と青を切り替えて、 **「2つの波を足すと、平らなノイズ(灰色)になる」** 様子を確かめてください。
        """)

    st.divider()

    # --- SCENE 2: デジタル宇宙論の視点 (The Solution) ---
    st.subheader("💻 Scene 2: デジタル宇宙論の「種明かし」")
    
    # 管理者権限モード
    admin_mode = st.checkbox("👉 **管理者権限 (Root)** でサーバーのログを見る", value=False)

    if admin_mode:
        st.success("我々は **「位置情報は最初から確定しており、DBに保存されている」** と考えます。魔法などありません。あるのは **「事後的なフィルタリング（SQL）」** だけです。")
        
        col_dig1, col_dig2 = st.columns([1, 1])
        
        with col_dig1:
            st.markdown("#### 📂 サーバー上の生ログ (Raw Data)")
            st.markdown("アカデミアには見えていない「隠れ変数（Tag）」が、最初から記録されています。")
            # データフレームを表示（ネタバレ）
            st.dataframe(df.head(10), use_container_width=True)
            # 修正箇所: num_data変数を使わず、len(df)で現在の行数を取得
            st.caption(f"... Total {len(df)} rows (Immutable Log)")

        with col_dig2:
            st.markdown("#### 🧠 実行された処理 (System Logic)")
            st.markdown(f"貴方がスイッチ **{detector}** を切り替えた時、システム内で実行されたのは以下のクエリです。")
            
            if detector == "D0 (経路不明・放置)":
                sql = "SELECT * FROM Universe_Log"
                explanation = "全データを表示しているだけです。Type_A（山）と Type_B（谷）が混ざるので、平らに見えていただけです。"
            elif detector == "D1 (経路Aを検出)":
                sql = "SELECT * FROM Universe_Log\nWHERE Hidden_Tag = 'Type_A'"
                explanation = "「Type_A」のタグがついた行だけを抽出（SELECT）しました。\n**赤色のデータは最初からそこにありました。** 新しく作られたわけではありません。"
            else:
                sql = "SELECT * FROM Universe_Log\nWHERE Hidden_Tag = 'Type_B'"
                explanation = "「Type_B」のタグがついた行だけを抽出しました。青色のデータが表示されただけです。"

            st.code(sql, language="sql")
            st.info(explanation)
    else:
        st.markdown("管理者権限を有効にすると、このパラドクスの「裏側の仕組み」が見えます。")

    st.markdown("---")
    if st.button("🔄 実験をリセット (Re-boot Universe)"):
        del st.session_state['quantum_db']
        st.rerun()