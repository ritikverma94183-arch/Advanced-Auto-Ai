import streamlit as st
import db
import pandas as pd
import plotly.graph_objects as go

def show_compare():
    # 🔥 ULTRA-ADVANCED CSS: Battle Arena, Neon Glows & Glassmorphism
    compare_css = """
    <style>
    .neon-title {
        color: #00ffcc; font-size: 45px; font-weight: 900; text-align: center;
        text-shadow: 2px 2px 15px black, 0 0 25px #00ffcc; margin-top: 10px;
    }
    
    /* Battle Cards */
    .battle-card-a {
        background: rgba(10, 20, 30, 0.7); backdrop-filter: blur(10px);
        border: 2px solid #00ffcc; border-radius: 15px; padding: 20px; text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.3); transition: 0.4s;
    }
    .battle-card-a:hover { transform: scale(1.05); box-shadow: 0 0 40px rgba(0, 255, 204, 0.6); }

    .battle-card-b {
        background: rgba(30, 10, 15, 0.7); backdrop-filter: blur(10px);
        border: 2px solid #ff4b4b; border-radius: 15px; padding: 20px; text-align: center;
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.3); transition: 0.4s;
    }
    .battle-card-b:hover { transform: scale(1.05); box-shadow: 0 0 40px rgba(255, 75, 75, 0.6); }

    /* Animated VS Logo */
    .vs-logo {
        font-size: 60px; font-weight: 900; color: #fff; text-align: center;
        text-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff;
        animation: pulse-vs 1.5s infinite alternate; margin-top: 50px;
    }
    @keyframes pulse-vs {
        0% { transform: scale(1); text-shadow: 0 0 10px #ff00ff; }
        100% { transform: scale(1.2); text-shadow: 0 0 30px #ff00ff, 0 0 60px #ff00ff; }
    }

    /* Spec Highlight Boxes */
    .spec-box {
        background: rgba(0,0,0,0.6); border-radius: 8px; padding: 10px;
        border-left: 3px solid #555; margin-bottom: 10px;
    }
    .win-a { border-left-color: #00ffcc; box-shadow: inset 20px 0 20px -20px rgba(0,255,204,0.5); }
    .win-b { border-left-color: #ff4b4b; box-shadow: inset 20px 0 20px -20px rgba(255,75,75,0.5); }
    </style>
    """
    st.markdown(compare_css, unsafe_allow_html=True)

    st.markdown("<h1 class='neon-title'>⚔️ Tactical Head-to-Head</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #fff; font-size: 18px; font-weight: 800; text-align: center; text-shadow: 2px 2px 5px black; letter-spacing: 2px;'>SELECT TARGETS FOR COMBAT ANALYSIS</p><br>", unsafe_allow_html=True)

    df = db.get_all_cars()
    
    if df.empty or len(df) < 2:
        st.warning("⚠️ Need at least 2 vehicles in the Database to initiate combat analysis.")
        return

    car_list = sorted(df['Car_Name'].unique().tolist())

    # Selection Row
    c_sel1, c_sel2 = st.columns(2)
    with c_sel1:
        car1_name = st.selectbox("🟦 Select Vehicle Alpha (Blue)", car_list, index=0)
    with c_sel2:
        car2_name = st.selectbox("🟥 Select Vehicle Sigma (Red)", car_list, index=1 if len(car_list) > 1 else 0)

    if car1_name == car2_name:
        st.warning("⚠️ Please select two different vehicles for comparison.")
        return

    # Fetch Data
    c1_data = df[df['Car_Name'] == car1_name].iloc[0]
    c2_data = df[df['Car_Name'] == car2_name].iloc[0]

    st.markdown("<br>", unsafe_allow_html=True)

    # --- BATTLE ARENA (CAR A vs CAR B) ---
    col1, col_vs, col2 = st.columns([1, 0.3, 1])

    with col1:
        st.markdown(f"""
        <div class='battle-card-a'>
            <h4 style='color:#ccc; letter-spacing:2px;'>VEHICLE ALPHA</h4>
            <h2 style='color:#00ffcc; text-shadow: 0 0 10px #00ffcc; font-size: 30px;'>{car1_name}</h2>
            <h1 style='color:white; margin:10px 0;'>₹ {c1_data.get('Price_INR', 0)/100000:.1f} L</h1>
            <p style='color:#00ffcc; font-weight:bold;'>{c1_data.get('Fuel_Type', 'N/A')} | {c1_data.get('Transmission', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    with col_vs:
        st.markdown("<div class='vs-logo'>VS</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='battle-card-b'>
            <h4 style='color:#ccc; letter-spacing:2px;'>VEHICLE SIGMA</h4>
            <h2 style='color:#ff4b4b; text-shadow: 0 0 10px #ff4b4b; font-size: 30px;'>{car2_name}</h2>
            <h1 style='color:white; margin:10px 0;'>₹ {c2_data.get('Price_INR', 0)/100000:.1f} L</h1>
            <p style='color:#ff4b4b; font-weight:bold;'>{c2_data.get('Fuel_Type', 'N/A')} | {c2_data.get('Transmission', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border: 1px solid #333;'>", unsafe_allow_html=True)

    # --- ADVANCED RADAR CHART (COMBAT SCAN) ---
    st.markdown("<h3 style='color: white; text-align: center; text-shadow: 0 0 10px #fff;'>🕸️ Combat Radar Scan</h3>", unsafe_allow_html=True)
    
    categories = ['Power (BHP)', 'Top Speed', 'Engine (CC/10)', 'Value (Lakhs)', 'Age Factor']
    
    # Safe data extraction
    def safe_get(data, col, default=0): return float(data.get(col, default)) if pd.notnull(data.get(col)) else default
    
    c1_stats = [
        safe_get(c1_data, 'Power_BHP', 100), safe_get(c1_data, 'Top_Speed_kmph', 150),
        safe_get(c1_data, 'Engine_Capacity_cc', 1000) / 10, safe_get(c1_data, 'Price_INR', 500000) / 100000,
        (2026 - safe_get(c1_data, 'Model_Year', 2020)) * 5
    ]
    
    c2_stats = [
        safe_get(c2_data, 'Power_BHP', 100), safe_get(c2_data, 'Top_Speed_kmph', 150),
        safe_get(c2_data, 'Engine_Capacity_cc', 1000) / 10, safe_get(c2_data, 'Price_INR', 500000) / 100000,
        (2026 - safe_get(c2_data, 'Model_Year', 2020)) * 5
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=c1_stats, theta=categories, fill='toself', name='Alpha (Blue)',
        line=dict(color='#00ffcc', width=3), fillcolor='rgba(0, 255, 204, 0.4)'
    ))
    fig.add_trace(go.Scatterpolar(
        r=c2_stats, theta=categories, fill='toself', name='Beta (Red)',
        line=dict(color='#ff4b4b', width=3), fillcolor='rgba(255, 75, 75, 0.4)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, gridcolor='rgba(255,255,255,0.2)'),
            angularaxis=dict(gridcolor='rgba(255,255,255,0.2)'),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#fff', size=14),
        margin=dict(t=40, b=40, l=40, r=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- SPEC-BY-SPEC COMPARISON BARS ---
    st.markdown("<h3 style='color: white; text-align: center; text-shadow: 0 0 10px #fff;'>⚙️ Engine Core Telemetry</h3><br>", unsafe_allow_html=True)

    def compare_row(label, val1, val2, unit="", lower_is_better=False):
        try: v1, v2 = float(val1), float(val2)
        except: v1, v2 = 0, 0
        
        # Determine winner
        if v1 == v2: win_class1 = win_class2 = "spec-box"
        elif (v1 > v2 and not lower_is_better) or (v1 < v2 and lower_is_better): 
            win_class1, win_class2 = "spec-box win-a", "spec-box"
        else: 
            win_class1, win_class2 = "spec-box", "spec-box win-b"

        c_l, c_m, c_r = st.columns([2, 1, 2])
        c_l.markdown(f"<div class='{win_class1}'><h4 style='color:#00ffcc; margin:0; text-align:right;'>{val1} {unit}</h4></div>", unsafe_allow_html=True)
        c_m.markdown(f"<div style='text-align:center; color:#ccc; padding-top:10px; font-weight:bold;'>{label}</div>", unsafe_allow_html=True)
        c_r.markdown(f"<div class='{win_class2}'><h4 style='color:#ff4b4b; margin:0; text-align:left;'>{val2} {unit}</h4></div>", unsafe_allow_html=True)

    compare_row("Power", c1_data.get('Power_BHP', 0), c2_data.get('Power_BHP', 0), "BHP")
    compare_row("Engine", c1_data.get('Engine_Capacity_cc', 0), c2_data.get('Engine_Capacity_cc', 0), "CC")
    compare_row("Top Speed", c1_data.get('Top_Speed_kmph', 0), c2_data.get('Top_Speed_kmph', 0), "km/h")
    compare_row("Model Year", c1_data.get('Model_Year', 0), c2_data.get('Model_Year', 0), "", lower_is_better=False)
    compare_row("Kilometers", c1_data.get('Kms_Driven', 0), c2_data.get('Kms_Driven', 0), "km", lower_is_better=True)

    st.markdown("<br><p style='text-align:center; color:#555;'>* Green/Red highlights indicate the superior specification.</p>", unsafe_allow_html=True)
