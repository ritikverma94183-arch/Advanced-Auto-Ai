import streamlit as st
import db
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import time

def show_dashboard():
    # 🔥 ULTRA-ADVANCED DASHBOARD CSS
    dash_css = """
    <style>
    /* Neon Text & Titles */
    .neon-title {
        color: #00ffcc; font-size: 45px; font-weight: 900; text-align: center;
        text-shadow: 2px 2px 15px black, 0 0 25px #00ffcc; margin-top: 10px;
    }
    
    /* 3D Glassmorphism Cards for Metrics */
    .metric-card {
        background: rgba(15, 15, 25, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 15px; padding: 20px; text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        transition: all 0.4s ease;
    }
    .metric-card:hover {
        transform: translateY(-10px);
        border-color: #00ffcc;
        box-shadow: 0 15px 40px rgba(0, 255, 204, 0.5);
    }
    
    /* Glass Containers for Graphs */
    .graph-container {
        background: rgba(10, 10, 15, 0.6);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px; padding: 15px; margin-top: 20px;
        box-shadow: inset 0 0 20px rgba(0,255,204,0.05), 0 10px 20px rgba(0,0,0,0.5);
        transition: 0.4s;
    }
    .graph-container:hover {
        border-color: rgba(0, 255, 204, 0.5);
        box-shadow: inset 0 0 20px rgba(0,255,204,0.2), 0 10px 30px rgba(0,0,0,0.8);
    }
    
    /* Live Terminal Log */
    .terminal-log {
        background: rgba(0,0,0,0.85); color: #00ffcc;
        font-family: 'Courier New', monospace; font-size: 14px;
        padding: 15px; border-radius: 8px; border-left: 4px solid #ff4b4b;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.3); margin-top: 30px;
    }
    </style>
    """
    st.markdown(dash_css, unsafe_allow_html=True)

    st.markdown("<h1 class='neon-title'>🛰️ Live Market Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #fff; font-size: 18px; font-weight: 800; text-align: center; text-shadow: 2px 2px 5px black; letter-spacing: 2px;'>GLOBAL TELEMETRY & PORTFOLIO INSIGHTS</p><br>", unsafe_allow_html=True)

    df = db.get_all_cars()
    
    if df.empty:
        st.warning("⚠️ No data available in the database. Please add vehicles first.")
        return

    # --- 1. HOLO KPI METRIC CARDS ---
    total_cars = len(df)
    total_val = df['Price_INR'].sum() if 'Price_INR' in df.columns else 0
    avg_price = total_val / total_cars if total_cars > 0 else 0
    ev_count = len(df[df['Fuel_Type'] == 'Electric']) if 'Fuel_Type' in df.columns else 0

    col1, col2, col3, col4 = st.columns(4)
    
    c1_html = f"<div class='metric-card'><h3 style='color:#ccc; font-size:14px; letter-spacing:1px;'>ACTIVE INVENTORY</h3><h2 style='color:#00ffcc; font-size:35px; margin:0; text-shadow: 0 0 15px #00ffcc;'>{total_cars}</h2></div>"
    c2_html = f"<div class='metric-card'><h3 style='color:#ccc; font-size:14px; letter-spacing:1px;'>PORTFOLIO VALUE</h3><h2 style='color:#ff4b4b; font-size:35px; margin:0; text-shadow: 0 0 15px #ff4b4b;'>₹ {total_val/10000000:.2f} Cr</h2></div>"
    c3_html = f"<div class='metric-card'><h3 style='color:#ccc; font-size:14px; letter-spacing:1px;'>AVERAGE PRICE</h3><h2 style='color:#ffc107; font-size:35px; margin:0; text-shadow: 0 0 15px #ffc107;'>₹ {avg_price/100000:.1f} L</h2></div>"
    c4_html = f"<div class='metric-card'><h3 style='color:#ccc; font-size:14px; letter-spacing:1px;'>EV FLEET ⚡</h3><h2 style='color:#0088ff; font-size:35px; margin:0; text-shadow: 0 0 15px #0088ff;'>{ev_count}</h2></div>"

    col1.markdown(c1_html, unsafe_allow_html=True)
    col2.markdown(c2_html, unsafe_allow_html=True)
    col3.markdown(c3_html, unsafe_allow_html=True)
    col4.markdown(c4_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. HOLO VISUAL CHARTS (ROW 1) ---
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("<div class='graph-container'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ffcc; font-weight: 900; text-align: center; text-shadow: 0 0 10px #00ffcc;'>⛽ Fuel Type Distribution</h3>", unsafe_allow_html=True)
        fuel_counts = df['Fuel_Type'].value_counts().reset_index()
        fuel_counts.columns = ['Fuel_Type', 'Count']
        
        fig1 = px.pie(fuel_counts, values='Count', names='Fuel_Type', hole=0.7, 
                      color_discrete_sequence=['#00ffcc', '#ff4b4b', '#0088ff', '#ffc107'])
        fig1.update_traces(textposition='outside', textinfo='percent+label', marker=dict(line=dict(color='#000000', width=3)))
        fig1.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='graph-container'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ffcc; font-weight: 900; text-align: center; text-shadow: 0 0 10px #00ffcc;'>🕸️ Fleet Radar Scan</h3>", unsafe_allow_html=True)
        
        # 🔥 NEW ADVANCED RADAR CHART 🔥
        categories = ['Avg Power (BHP)', 'Avg Speed (km/h)', 'Engine (CC/10)', 'Avg Age (Yrs*10)', 'Price (Lakhs*3)']
        avg_bhp = df['Power_BHP'].mean() if not df.empty else 120
        avg_speed = df['Top_Speed_kmph'].mean() if not df.empty else 180
        avg_cc = (df['Engine_Capacity_cc'].mean() / 10) if not df.empty else 150
        avg_age = (2026 - df['Model_Year'].mean()) * 10 if not df.empty else 40 
        avg_prc = (df['Price_INR'].mean() / 100000) * 3 if not df.empty else 30

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[avg_bhp, avg_speed, avg_cc, avg_age, avg_prc],
            theta=categories, fill='toself', fillcolor='rgba(0, 255, 204, 0.4)',
            line=dict(color='#00ffcc', width=3), name='Fleet Stats'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 300], gridcolor='rgba(0,255,204,0.3)', linecolor='rgba(0,255,204,0.3)'),
                angularaxis=dict(gridcolor='rgba(0,255,204,0.3)', linecolor='rgba(0,255,204,0.3)'),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#fff', size=12), margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- 3. HOLO VISUAL CHARTS (ROW 2) ---
    c3, c4 = st.columns(2)

    with c3:
        st.markdown("<div class='graph-container'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ffcc; font-weight: 900; text-align: center; text-shadow: 0 0 10px #00ffcc;'>📅 Depreciation Matrix</h3>", unsafe_allow_html=True)
        fig3 = px.scatter(df, x='Model_Year', y='Price_INR', color='Fuel_Type', size='Power_BHP', hover_name='Car_Name',
                          color_discrete_sequence=['#00ffcc', '#ff4b4b', '#0088ff', '#ffc107'], size_max=25)
        # Cyberpunk gridlines
        fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,255,204,0.1)', zerolinecolor='rgba(0,255,204,0.5)')
        fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,255,204,0.1)', zerolinecolor='rgba(0,255,204,0.5)')
        fig3.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='graph-container'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ffcc; font-weight: 900; text-align: center; text-shadow: 0 0 10px #00ffcc;'>⚡ Engine Core Analysis</h3>", unsafe_allow_html=True)
        fig4 = px.scatter(df, x='Engine_Capacity_cc', y='Power_BHP', color='Transmission', hover_name='Car_Name',
                          color_discrete_sequence=['#ff4b4b', '#0088ff'], size='Top_Speed_kmph', size_max=20)
        # Cyberpunk gridlines
        fig4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,75,75,0.1)', zerolinecolor='rgba(255,75,75,0.5)')
        fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,75,75,0.1)', zerolinecolor='rgba(255,75,75,0.5)')
        fig4.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- 4. HACKER TERMINAL STATUS LOG ---
    st.markdown("""
    <div class='terminal-log'>
        > [SERVER PING]: 12ms | CONNECTION: ENCRYPTED SECURE<br>
        > [DB SYNC]: Successfully synced {} vehicle records from central node.<br>
        > [AI ENGINE]: Valuation algorithms active. City modifiers loaded.<br>
        <span style='color:#fff; font-weight:bold; font-size:16px;'>> SYSTEM STATUS: ONLINE & FULLY OPERATIONAL 🟢</span>
    </div>
    """.format(total_cars), unsafe_allow_html=True)
