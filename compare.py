import streamlit as st
import db
import pandas as pd
import plotly.graph_objects as go
from ml_engine import train_and_predict

def show_compare():
    # 🔥 ADVANCED COMBAT ANIMATIONS CSS
    st.markdown("""
    <style>
    /* 1. Fade & Slide in for Results */
    .fade-in-up {
        animation: fadeInUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* 2. 3D Hover Effect for Spec Cards */
    .hover-combat-card {
        padding: 15px; 
        background: #1e1e1e; 
        border-radius: 12px; 
        border: 1px solid #333;
        text-align: center;
        transition: all 0.4s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .hover-combat-card:hover {
        transform: translateY(-10px) scale(1.05);
        border-color: #00ffcc !important;
        box-shadow: 0 15px 30px rgba(0, 255, 204, 0.3) !important;
        z-index: 10;
    }

    /* 3. Pulsing VS Text Animation */
    .pulse-vs {
        font-size: 24px;
        font-weight: bold;
        color: #ffc107;
        text-align: center;
        animation: pulseVS 1.5s infinite alternate;
    }
    @keyframes pulseVS {
        0% { transform: scale(1); text-shadow: 0 0 5px #ffc107; }
        100% { transform: scale(1.3); text-shadow: 0 0 20px #ffc107, 0 0 30px #ff4b4b; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("⚔️ Advanced Head-to-Head Comparison")
    st.write("Compare vehicle specs, performance, and real-time market depreciation.")

    # Database fetch karna safely
    df_cars = db.get_all_cars()
    if not df_cars.empty:
        car_list = sorted(df_cars['Car_Name'].unique().tolist())
    else:
        car_list = ["Maruti Suzuki Swift", "Toyota Fortuner", "Lamborghini Urus"]

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚙 Vehicle 1")
        car1 = st.selectbox("Select First Car", car_list, key="car1")
        
    with col2:
        st.markdown("### 🏎️ Vehicle 2")
        car2 = st.selectbox("Select Second Car", car_list, key="car2", index=min(1, len(car_list)-1))

    if st.button("Start Advanced Comparison 🚀", type="primary", use_container_width=True):
        st.markdown("---")
        
        # 🔥 SMART FETCHING LOGIC (Bugs Fixed)
        def get_car_specs(c_name):
            cc, bhp, spd = 1500, 100, 180 # Defaults
            fuel, trans = "Petrol", "Manual"
            if not df_cars.empty:
                c_df = df_cars[df_cars['Car_Name'] == c_name]
                if not c_df.empty:
                    if 'Engine_Capacity_cc' in c_df.columns: cc = int(c_df['Engine_Capacity_cc'].iloc[0])
                    if 'Power_BHP' in c_df.columns: bhp = int(c_df['Power_BHP'].iloc[0])
                    if 'Top_Speed_kmph' in c_df.columns: spd = int(c_df['Top_Speed_kmph'].iloc[0])
                    if 'Fuel_Type' in c_df.columns: fuel = str(c_df['Fuel_Type'].iloc[0])
                    if 'Transmission' in c_df.columns: trans = str(c_df['Transmission'].iloc[0])
                    if 'Battery_Capacity_kWh' in c_df.columns: battery = int(c_df['Battery_Capacity_kWh'].iloc[0])
            return cc, bhp, spd, fuel, trans, battery

        # Dono gaadiyon ka exact data nikalna
        cc1, bhp1, spd1, fuel1, trans1, battery1 = get_car_specs(car1)
        cc2, bhp2, spd2, fuel2, trans2, battery2 = get_car_specs(car2)

        # Comparison ke liye Standard Parameters (For Fair Fight)
        year, km, owner = 2024, 20000, "First"

        # AI se Market Value nikalna
        price1 = train_and_predict(car1, year, km, fuel1, owner, trans1, cc1, bhp1, spd1)
        price2 = train_and_predict(car2, year, km, fuel2, owner, trans2, cc2, bhp2, spd2)

        # 🔥 ANIMATED CONTAINER START
        st.markdown("<div class='fade-in-up'>", unsafe_allow_html=True)

        # --- 1. PRICE COMPARISON UI ---
        st.markdown("### 💰 Market Value (Assuming 2024 Model, 20k KM)")
        c1, c_vs, c2 = st.columns([2, 1, 2])
        with c1:
            st.metric(f"Current Value: {car1}", f"₹{price1:,.0f}")
        with c_vs:
            st.markdown("<br><div class='pulse-vs'>VS</div>", unsafe_allow_html=True)
        with c2:
            st.metric(f"Current Value: {car2}", f"₹{price2:,.0f}")

        # --- 2. PERFORMANCE BATTLE UI (With Trophies & Hover Animation) ---
        st.markdown("### ⚡ Specifications Battle")
        
        def colorize_winner(v1, v2, unit):
            win, lose, tie = "#00ffcc", "#ff4b4b", "#ffffff"
            if v1 > v2: return f"<span style='color:{win}; font-weight:bold;'>{v1} {unit} 🏆</span>", f"<span style='color:{lose}'>{v2} {unit}</span>"
            elif v2 > v1: return f"<span style='color:{lose}'>{v1} {unit}</span>", f"<span style='color:{win}; font-weight:bold;'>{v2} {unit} 🏆</span>"
            else: return f"<span style='color:{tie}'>{v1} {unit} 🤝</span>", f"<span style='color:{tie}'>{v2} {unit} 🤝</span>"

        cc1_str, cc2_str = colorize_winner(cc1, cc2, "cc")
        bhp1_str, bhp2_str = colorize_winner(bhp1, bhp2, "BHP")
        spd1_str, spd2_str = colorize_winner(spd1, spd2, "km/h")
        battery1_str, battery2_str = colorize_winner(battery1, battery2, "kWh")

        sc1, sc2, sc3, sc4 = st.columns(4)

        # Applied .hover-combat-card class to the boxes
        sc1.markdown(f"<div class='hover-combat-card'><b style='color:#ccc;'>Engine Capacity</b><br><br><span style='font-size:14px;'>{car1}</span><br>{cc1_str}<br><br><span style='font-size:14px;'>{car2}</span><br>{cc2_str}</div>", unsafe_allow_html=True)
        sc2.markdown(f"<div class='hover-combat-card'><b style='color:#ccc;'>Horsepower</b><br><br><span style='font-size:14px;'>{car1}</span><br>{bhp1_str}<br><br><span style='font-size:14px;'>{car2}</span><br>{bhp2_str}</div>", unsafe_allow_html=True)
        sc3.markdown(f"<div class='hover-combat-card'><b style='color:#ccc;'>Top Speed</b><br><br><span style='font-size:14px;'>{car1}</span><br>{spd1_str}<br><br><span style='font-size:14px;'>{car2}</span><br>{spd2_str}</div>", unsafe_allow_html=True)
        sc4.markdown(f"<div class='hover-combat-card'><b style='color:#ccc;'>Battery Capacity</b><br><br><span style='font-size:14px;'>{car1}</span><br>{battery1_str}<br><br><span style='font-size:14px;'>{car2}</span><br>{battery2_str}</div>", unsafe_allow_html=True)

        # --- 3. ADVANCED RADAR CHART ---
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📊 Performance Radar")
        
        max_cc, max_bhp, max_spd = max(cc1, cc2, 1), max(bhp1, bhp2, 1), max(spd1, spd2, 1)
        max_price = max(price1, price2, 1)

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[cc1/max_cc, bhp1/max_bhp, spd1/max_spd, price1/max_price, battery1/200],
            theta=['Engine (CC)', 'Power (BHP)', 'Top Speed', 'Resale Value', 'Battery Capacity (kWh)'],
            fill='toself', name=car1, line_color='#00ffcc'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=[cc2/max_cc, bhp2/max_bhp, spd2/max_spd, price2/max_price, battery2/200],
            theta=['Engine (CC)', 'Power (BHP)', 'Top Speed', 'Resale Value', 'Battery Capacity (kWh)'],
            fill='toself', name=car2, line_color='#ff4b4b'
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=False)), template="plotly_dark", height=450)
        st.plotly_chart(fig_radar, use_container_width=True)

        # --- 4. DEPRECIATION GRAPH ---
        st.markdown("### 📉 10-Year Depreciation Fight")
        years = list(range(2015, 2027))
        p1_list = [train_and_predict(car1, y, km, fuel1, owner, trans1, cc1, bhp1, spd1, battery1) for y in years]
        p2_list = [train_and_predict(car2, y, km, fuel2, owner, trans2, cc2, bhp2, spd2, battery2) for y in years]

        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=years, y=p1_list, mode='lines+markers', name=car1, line=dict(color='#00ffcc', width=3)))
        fig_line.add_trace(go.Scatter(x=years, y=p2_list, mode='lines+markers', name=car2, line=dict(color='#ff4b4b', width=3)))
        fig_line.update_layout(template="plotly_dark", height=400, hovermode="x unified", xaxis_title="Manufacturing Year", yaxis_title="Market Value (₹)")
        st.plotly_chart(fig_line, use_container_width=True)

        # 🔥 ANIMATED CONTAINER END
        st.markdown("</div>", unsafe_allow_html=True)