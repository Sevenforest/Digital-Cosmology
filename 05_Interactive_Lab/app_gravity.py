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

st.title("🌌 Digital Cosmology Interactive Lab")
st.markdown("""
**Kernel_03: Dual Clock Architecture Verification**
この実験は、**「重力情報の更新遅延（Lag）」**が銀河の形成に与える影響をシミュレーションします。
左側は通常の物理法則（ラグなし）、右側はデジタル宇宙論（ラグあり）です。
""")

# --- サイドバー: パラメータ設定 ---
st.sidebar.header("🔧 Simulation Parameters")

# 重要なパラメータ: ラグの間隔
LAG_INTERVAL = st.sidebar.slider(
    "Gravity Update Lag (Steps)",
    min_value=1,
    max_value=100,
    value=30,
    help="重力ポテンシャルを更新する間隔。1なら通常物理、大きいほどデジタル宇宙的（更新が遅い）。"
)

N_PARTICLES = st.sidebar.slider("Number of Stars", 100, 1000, 300, step=100)
N_STEPS = st.sidebar.slider("Simulation Duration", 100, 1000, 300, step=50)
DT = 0.01
G = 1.0

# --- シミュレーションクラスの定義 (修正版) ---
class Universe:
    def __init__(self, lag_interval):
        self.lag = lag_interval
        # 初期化：銀河中心に質量集中、回転を与える
        r = np.random.rand(N_PARTICLES) * 2.0 + 0.2
        theta = np.random.rand(N_PARTICLES) * 2 * np.pi
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # 初速度：脱出速度より少し速く設定（ダークマターがないと飛び散る）
        # 1.5倍だと速すぎた可能性があるので 1.2倍 に調整
        v_orbital = np.sqrt(G * N_PARTICLES / r) * 1.2 
        vx = -v_orbital * np.sin(theta)
        vy = v_orbital * np.cos(theta)
        
        self.pos = np.column_stack((x, y))
        self.vel = np.column_stack((vx, vy))
        self.gravity_pos = self.pos.copy() # 重力源（過去の幻影）

    def step(self, current_step):
        # Kernel_03: システムクロックのタイミングでのみ重力源を更新
        if current_step % self.lag == 0:
            self.gravity_pos = self.pos.copy()
        
        # --- 修正ポイント: Real vs Ghost Interaction ---
        # ターゲット（力を受ける側）：現在の位置 (self.pos)
        # ソース（力を出す側）：過去の位置 (self.gravity_pos)
        
        xt = self.pos[:, 0:1]
        yt = self.pos[:, 1:2]
        xs = self.gravity_pos[:, 0:1]
        ys = self.gravity_pos[:, 1:2]
        
        # 距離ベクトル: ソース(j) から ターゲット(i) への向き...ではなく
        # 重力は引力なので、ターゲット(i) から ソース(j) への向き
        dx = xs.T - xt
        dy = ys.T - yt
        
        dist_sq = dx**2 + dy**2 + 0.1 # 特異点回避
        dist = np.sqrt(dist_sq)
        
        # 力の計算 F = G * m / r^2
        # F_vec = F * (vec / dist) = G * vec / r^3
        f_mag = G / (dist_sq * dist)
        
        # 全ソースからの合力を計算
        fx = np.sum(f_mag * dx, axis=1)
        fy = np.sum(f_mag * dy, axis=1)
        
        # 速度と位置の更新
        force = np.column_stack((fx, fy))
        self.vel += force * DT
        self.pos += self.vel * DT

# --- メイン実行部 ---

col1, col2 = st.columns(2)
start_btn = st.sidebar.button("▶ Run Simulation", type="primary")

# プレースホルダー（アニメーション用）
with col1:
    st.subheader("Newtonian (No Lag)")
    plot_spot_std = st.empty()
with col2:
    st.subheader(f"Digital (Lag = {LAG_INTERVAL})")
    plot_spot_dig = st.empty()

if start_btn:
    # 宇宙の生成
    univ_std = Universe(lag_interval=1)          # 通常宇宙（毎回更新）
    univ_dig = Universe(lag_interval=LAG_INTERVAL) # デジタル宇宙（ラグあり）
    
    progress_bar = st.progress(0)
    
    # アニメーションループ
    for t in range(N_STEPS):
        # 物理計算
        univ_std.step(t)
        univ_dig.step(t)
        
        # 描画（パフォーマンスのため5ステップに1回描画）
        if t % 5 == 0:
            # --- 通常宇宙のプロット ---
            fig1, ax1 = plt.subplots(figsize=(5, 5))
            ax1.scatter(univ_std.pos[:,0], univ_std.pos[:,1], s=2, c='red', alpha=0.6)
            ax1.set_xlim(-6, 6); ax1.set_ylim(-6, 6)
            ax1.set_title(f"Step {t}: Scattering")
            ax1.axis('off')
            plot_spot_std.pyplot(fig1)
            plt.close(fig1) # メモリ解放
            
            # --- デジタル宇宙のプロット ---
            fig2, ax2 = plt.subplots(figsize=(5, 5))
            ax2.scatter(univ_dig.pos[:,0], univ_dig.pos[:,1], s=2, c='blue', alpha=0.6)
            ax2.set_xlim(-6, 6); ax2.set_ylim(-6, 6)
            ax2.set_title(f"Step {t}: Bound via Lag")
            ax2.axis('off')
            plot_spot_dig.pyplot(fig2)
            plt.close(fig2) # メモリ解放
        
        progress_bar.progress((t + 1) / N_STEPS)
        time.sleep(0.01) # UI応答用ウェイト

    st.success("Simulation Complete! Check the difference in galaxy shapes.")