import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- ページ設定 ---
st.set_page_config(
    page_title="Digital Gravity Lab",
    page_icon="🌌",
    layout="wide"
)

# --- タイトルと解説 ---
st.title("🌌 Digital Cosmology Interactive Lab")
st.markdown("""
**Kernel_03: Dual Clock Architecture & Dark Matter Verification**

この実験は、**「なぜ銀河は飛び散らずに形を保てるのか？」** という謎（銀河の回転曲線問題）に対し、2つのアプローチで挑みます。
銀河の星々は非常に高速で回転しており、本来の重力（目に見える質量）だけでは遠心力で飛び散ってしまいます。

* **👈 Left: Standard Theory (Newtonian)**
    * **Dark Matter OFF:** 目に見える物質だけの重力。星は飛び散ってしまいます。
    * **Dark Matter ON:** 「見えない質量」を大量に追加して、無理やり引き留めます（既存の解決策）。
* **👉 Right: Digital Cosmology (Time Lag)**
    * **Digital Lag:** ダークマターは使いません。**「重力情報の更新遅延（Lag）」** が発生させる「過去の位置への引力」が、強力なブレーキ（向心力）として機能します。
""")

with st.expander("🤔 なぜ左右で「動き」が違うのですか？"):
    st.markdown("""
    **1. 形の違い（Sub-structure）**
    * **左側:** 全体が一つの大きな塊になろうとします。
    * **右側:** 「小銀河（サブハロー）」がいくつも生まれ、それらが共存する**多重構造**が作られます。これは実際の宇宙の大規模構造に近い姿です。

    **2. 位置の安定性（Cosmic Friction）**
    * **左側:** 全体が画面のどこかへ流れていってしまうことがあります（慣性ドリフト）。
    * **右側:** ラグが「過去の位置への引力」として働くため、移動に対して **ブレーキ（宇宙論的摩擦）** がかかります。結果として、銀河はその場に留まり続け、非常に安定します。
    
    この **「勝手にブレーキがかかって構造が安定する」** という性質こそが、デジタル宇宙論が予言する自己安定化作用です。
    """)

# --- サイドバー: パラメータ設定 ---
st.sidebar.header("🔧 Simulation Parameters")

# 1. 共通設定
N_PARTICLES = st.sidebar.slider("Number of Stars", 100, 800, 400, step=50)
N_STEPS = st.sidebar.slider("Simulation Duration", 100, 1000, 700, step=50)

st.sidebar.markdown("---")

# 2. 標準理論の設定 (左画面)
st.sidebar.subheader("👈 Standard Theory (Left)")
USE_DARK_MATTER = st.sidebar.checkbox(
    "Enable Dark Matter",
    value=False,
    help="ONにすると、人工的な重力補正（×5.0倍）を追加し、銀河の崩壊を防ぎます。"
)

st.sidebar.markdown("---")

# 3. デジタル宇宙論の設定 (右画面)
st.sidebar.subheader("👉 Digital Theory (Right)")
LAG_INTERVAL = st.sidebar.slider(
    "Gravity Update Lag (Steps)",
    min_value=1,
    max_value=50,
    value=15,
    help="重力ポテンシャルを更新する間隔。値が大きいほど「過去の重力」に引かれる力が強くなります。"
)

# 定数
DT = 0.01
G = 1.0

# --- シミュレーションクラスの定義 ---
class Universe:
    def __init__(self, n_particles, lag_interval):
        self.lag = lag_interval
        self.n = n_particles
        
        # 初期化：銀河中心に質量集中、回転を与える
        # ランダムな配置
        r = np.random.rand(self.n) * 2.0 + 0.5 # 中心から少し離す
        theta = np.random.rand(self.n) * 2 * np.pi
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # 初速度：脱出速度より「かなり速く」設定する (1.5倍)
        # これにより、強力な重力(DM)かラグがないと飛び散る状態を作る
        v_orbital = np.sqrt(G * self.n / r) * 1.1
        
        # 回転方向の速度ベクトル
        vx = -v_orbital * np.sin(theta)
        vy = v_orbital * np.cos(theta)
        
        self.pos = np.column_stack((x, y))
        self.vel = np.column_stack((vx, vy))
        
        # 重力源（初期状態は現在位置と同じ）
        self.gravity_pos = self.pos.copy() 

    def step(self, current_step, dark_matter_factor=1.0):
        # --- Kernel_03: Lag Logic ---
        # ラグ設定がある場合、gravity_pos（引力の発生源）の更新をサボる
        # これにより、星は「過去の銀河の中心」に向かって引かれることになる
        if current_step % self.lag == 0:
            self.gravity_pos = self.pos.copy()
        
        # ターゲット（力を受ける側）：現在の位置
        xt = self.pos[:, 0:1]
        yt = self.pos[:, 1:2]
        
        # ソース（力を出す側）：ラグを考慮した位置
        xs = self.gravity_pos[:, 0:1]
        ys = self.gravity_pos[:, 1:2]
        
        # 距離ベクトル: ターゲット -> ソース (引力)
        dx = xs.T - xt
        dy = ys.T - yt
        
        # 距離の二乗 + 軟化パラメータ(Softening)
        dist_sq = dx**2 + dy**2 + 0.2
        dist = np.sqrt(dist_sq)
        
        # 力の計算 F = G * m1 * m2 / r^2
        # ダークマター係数を G に掛けることで、「見えない質量」をシミュレート
        effective_G = G * dark_matter_factor
        f_mag = effective_G / (dist_sq * dist)
        
        # 全粒子からの合力を計算
        fx = np.sum(f_mag * dx, axis=1)
        fy = np.sum(f_mag * dy, axis=1)
        
        # 速度と位置の更新 (Symplectic Euler的な簡易法)
        force = np.column_stack((fx, fy))
        self.vel += force * DT
        self.pos += self.vel * DT

# --- メイン実行部 ---

col1, col2 = st.columns(2)

# レイアウト枠の作成
with col1:
    st.subheader("Standard (Newtonian)")
    status_std = st.empty()
    plot_spot_std = st.empty()

with col2:
    st.subheader(f"Digital (Lag = {LAG_INTERVAL})")
    status_dig = st.empty()
    plot_spot_dig = st.empty()

start_btn = st.sidebar.button("▶ Run Simulation", type="primary")

if start_btn:
    # 宇宙の生成 (同じ初期条件にするためシード固定も検討可能だが、今回はランダム)
    # 左：ラグなし (Lag=1)
    univ_std = Universe(N_PARTICLES, lag_interval=1)          
    # 右：ラグあり (Lag=ユーザー設定)
    univ_dig = Universe(N_PARTICLES, lag_interval=LAG_INTERVAL) 
    
    # ステータス表示
    if USE_DARK_MATTER:
        status_std.info("🛡️ **Dark Matter: ON** (Gravity x 5.0)")
        dm_factor = 5.0
    else:
        status_std.warning("⚠️ **Dark Matter: OFF** (Gravity x 1.0)")
        dm_factor = 1.0
        
    status_dig.success(f"⏳ **Lag Mode** (Update every {LAG_INTERVAL} steps)")

    progress_bar = st.progress(0)
    
    # アニメーションループ
    for t in range(N_STEPS):
        # 物理計算
        univ_std.step(t, dark_matter_factor=dm_factor) # 左はDM係数を適用
        univ_dig.step(t, dark_matter_factor=1.0)       # 右はDMなし（Lagのみ）
        
        # 描画（パフォーマンスのため、数ステップに1回描画）
        if t % 4 == 0:
            # 範囲設定（共通）
            LIM = 8
            
            # --- 左：通常宇宙 ---
            fig1, ax1 = plt.subplots(figsize=(4, 4))
            # 背景を黒っぽく
            fig1.patch.set_facecolor('#0e1117')
            ax1.set_facecolor('#0e1117')
            
            # 星の描画
            ax1.scatter(univ_std.pos[:,0], univ_std.pos[:,1], s=1, c='#ff4b4b', alpha=0.8)
            ax1.set_xlim(-LIM, LIM); ax1.set_ylim(-LIM, LIM)
            ax1.set_title(f"Step {t}", color='white')
            ax1.axis('off')
            plot_spot_std.pyplot(fig1)
            plt.close(fig1) # メモリ解放
            
            # --- 右：デジタル宇宙 ---
            fig2, ax2 = plt.subplots(figsize=(4, 4))
            fig2.patch.set_facecolor('#0e1117')
            ax2.set_facecolor('#0e1117')
            
            # 星の描画
            ax2.scatter(univ_dig.pos[:,0], univ_dig.pos[:,1], s=1, c='#00ccff', alpha=0.8)
            ax2.set_xlim(-LIM, LIM); ax2.set_ylim(-LIM, LIM)
            ax2.set_title(f"Step {t}", color='white')
            ax2.axis('off')
            plot_spot_dig.pyplot(fig2)
            plt.close(fig2) # メモリ解放
        
        progress_bar.progress((t + 1) / N_STEPS)
        # time.sleep(0.001) # 最速で回すためコメントアウト（必要なら調整）

    st.success("Simulation Complete.")