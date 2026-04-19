import streamlit as st
import auth, home, dashboard, database_page, about, db, compare
import plotly.graph_objects as go
import pandas as pd
from ml_engine import train_and_predict
from fpdf import FPDF
import os

st.set_page_config(page_title="Advanced Auto AI", page_icon="🏎️", layout="wide")

# 🔥 ULTRA-ADVANCED CSS & FULL-SCREEN WALLPAPER INJECTOR
def inject_animations():
    css_animations = """
    <style>
    /* 1. Transparent Streamlit Overlays */
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    [data-testid="stAppViewBlockContainer"] { background: transparent !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    .stApp { background: transparent !important; }
    [data-testid="stSidebar"] { background-color: rgba(10, 15, 20, 0.85) !important; backdrop-filter: blur(10px); border-right: 1px solid #00ffcc; }

    /* 2. Global Text & Shadow Styling */
    h1, h2, h3, h4, h5, h6, p, label, span, div[data-testid="stMarkdownContainer"] {
        color: #ffffff !important; 
        text-shadow: 2px 2px 8px #000000, 0px 0px 5px #000000 !important; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stSelectbox label, .stNumberInput label { font-size: 16px !important; font-weight: bold !important; color: #00ffcc !important;}

    /* 3. Glowing Titles */
    .glow-title { 
        color: #00ffcc !important;
        font-weight: 900 !important;
        text-shadow: 0 0 10px #00ffcc, 0 0 30px #00ffcc, 2px 2px 10px black !important;
        letter-spacing: 2px;
    }
    .sub-title { color: #ccc !important; text-shadow: 2px 2px 8px #000000 !important; font-weight: bold; letter-spacing: 1px;}

    /* 4. 3D GLASSMORPHISM NAVIGATION BUTTONS */
    div.stButton > button {
        height: 130px;
        font-size: 24px !important;
        font-weight: 900 !important; 
        border-radius: 20px;
        background: rgba(20, 25, 35, 0.6) !important; 
        backdrop-filter: blur(10px) !important;
        border: 2px solid rgba(0, 255, 204, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        color: white !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.8), inset 0 0 15px rgba(0,255,204,0.1) !important;
        text-shadow: 2px 2px 5px black !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div.stButton > button:hover {
        transform: translateY(-12px) scale(1.03);
        background: rgba(30, 35, 45, 0.8) !important;
        border-color: #00ffcc !important;
        box-shadow: 0 20px 40px rgba(0, 255, 204, 0.6), inset 0 0 20px rgba(0,255,204,0.3) !important;
        color: #00ffcc !important;
        text-shadow: 0 0 10px #00ffcc !important;
    }
    
    /* Input Boxes Customization */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: rgba(0,0,0,0.6) !important;
        border: 1px solid #00ffcc !important;
        color: #00ffcc !important;
    }
    
    /* Smooth Load Effect */
    .fade-in-up { animation: fadeInUp 0.8s ease-out; }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(40px); } 100% { opacity: 1; transform: translateY(0); } }
    </style>
    """
    st.markdown(css_animations, unsafe_allow_html=True)
    
    # 🔥 FIX: SINGLE SEAMLESS PREMIUM WALLPAPER
    full_bg_html = """
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -9999; background: #000;">
        <img src="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1920&q=80" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(2.20);" />
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.85));"></div>
    </div>
    """
    st.markdown(full_bg_html, unsafe_allow_html=True)


# --- PDF Generation Function ---
def generate_pdf(car_nm, year, km, fuel, trans, cond, city, price, battery_kwh: int = 0):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(240, 240, 245)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(0, 100, 200) 
    pdf.cell(0, 15, "ADVANCED AUTO AI", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Official Telemetry & Valuation Certificate", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(30, 30, 30)
    
    pdf.cell(100, 10, f"Vehicle: {car_nm}")
    pdf.cell(0, 10, f"Manufacturing Year: {year}", ln=True)
    pdf.cell(100, 10, f"Odometer: {km:,} km")
    pdf.cell(0, 10, f"Fuel Type: {fuel}", ln=True)
    pdf.cell(100, 10, f"Transmission: {trans}")
    pdf.cell(0, 10, f"Condition: {cond}", ln=True)
    pdf.cell(100, 10, f"Registration Zone: {city}")

    if isinstance(battery_kwh, (int, float)) and battery_kwh > 0:
        pdf.cell(0, 10, f"EV Battery Cap: {battery_kwh} kWh", ln=True)
    else:
        pdf.ln(10)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 18)
    pdf.set_text_color(0, 153, 76) 
    pdf.cell(0, 15, f"CERTIFIED MARKET VALUE: INR {price:,.0f}", ln=True, align='C')
    
    pdf.set_y(-30)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, 'This is a system generated report. Powered by Advanced Auto AI Dealership Engine.', 0, 0, 'C')

    try: pdf.output("Valuation_Report.pdf")
    except Exception: pass


# --- AI Price Predictions Function ---
def show_ai_price_predictions():
    st.markdown("<h1 class='glow-title' style='font-size:45px; margin-top:10px; text-align:center;'>🔮 AI Valuation Engine</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='text-align:center;'>Real-Time Depreciation Matrix & RTO Zone Compliance Scanner</p>", unsafe_allow_html=True)

    try:
        df_cars = db.get_all_cars()
        if not df_cars.empty: car_list = sorted(df_cars['Car_Name'].unique().tolist())
        else: car_list = ["Maruti Suzuki Swift", "Toyota Fortuner", "Lamborghini Urus"]
    except Exception:
        df_cars = pd.DataFrame()
        car_list = ["Maruti Suzuki Swift", "Toyota Fortuner", "Lamborghini Urus"]

    st.markdown("<br><h3 class='sub-title' style='text-align:left; color:#00ffcc !important;'>🚘 Select Target Vehicle</h3>", unsafe_allow_html=True)
    car_nm = st.selectbox("", car_list)

    def_fuel, def_trans = "Petrol", "Manual"
    def_cc, def_bhp, def_speed, def_battery = 1500, 100, 180, 0

    if not df_cars.empty:
        car_data = df_cars[df_cars['Car_Name'] == car_nm]
        if not car_data.empty:
            if 'Fuel_Type' in car_data.columns: def_fuel = str(car_data['Fuel_Type'].iloc[0])
            if 'Transmission' in car_data.columns: def_trans = str(car_data['Transmission'].iloc[0])
            if 'Engine_Capacity_cc' in car_data.columns: def_cc = int(car_data['Engine_Capacity_cc'].iloc[0])
            if 'Power_BHP' in car_data.columns: def_bhp = int(car_data['Power_BHP'].iloc[0])
            if 'Top_Speed_kmph' in car_data.columns: def_speed = int(car_data['Top_Speed_kmph'].iloc[0])
            if 'Battery_Capacity_kWh' in car_data.columns:
                try: def_battery = int(car_data['Battery_Capacity_kWh'].iloc[0])
                except Exception: def_battery = 0

    with st.form("prediction_form"):
        st.markdown("#### ⚡ Hardware Specifications (Locked)")
        c_eng1, c_eng2, c_eng3, c_eng4 , c_eng5, c_eng6 = st.columns(6)
        
        box_style = "padding: 15px 5px; background: rgba(0,0,0,0.5); backdrop-filter: blur(5px); border-radius: 10px; border: 1px solid #00ffcc; color: #00ffcc; font-size: 16px; text-align: center; font-weight: 900; text-shadow: 0 0 10px #00ffcc;"

        c_eng1.markdown(f"<div style='font-size: 13px; color: #ccc; text-align:center; margin-bottom:5px;'>Engine</div><div style='{box_style}'>{def_cc} cc</div><br>", unsafe_allow_html=True)
        c_eng2.markdown(f"<div style='font-size: 13px; color: #ccc; text-align:center; margin-bottom:5px;'>Power</div><div style='{box_style}'>{def_bhp} BHP</div><br>", unsafe_allow_html=True)
        c_eng3.markdown(f"<div style='font-size: 13px; color: #ccc; text-align:center; margin-bottom:5px;'>Max Speed</div><div style='{box_style}'>{def_speed} km/h</div><br>", unsafe_allow_html=True)
        c_eng4.markdown(f"<div style='font-size: 13px; color: #ccc; text-align:center; margin-bottom:5px;'>EV Battery</div><div style='{box_style}'>{def_battery} kWh</div><br>", unsafe_allow_html=True)
        c_eng5.markdown(f"<div style='font-size: 13px; color: #ccc; text-align:center; margin-bottom:5px;'>Fuel Core</div><div style='{box_style}'>{def_fuel}</div><br>", unsafe_allow_html=True)
        c_eng6.markdown(f"<div style='font-size: 13px; color: #ccc; text-align:center; margin-bottom:5px;'>Gearbox</div><div style='{box_style}'>{def_trans}</div><br>", unsafe_allow_html=True)
        
        st.markdown("#### ⚙️ Market & Telemetry Parameters")
        
        col1, col2, col3 = st.columns(3)
        year = col1.number_input("Manufacturing Year", 1996, 2026, 2024)
        km = col2.number_input("Kilometers Driven", 0, 500000, 25000, step=1000)
        owner = col3.selectbox("Owner Type", ["First", "Second", "Third", "Fourth"])

        col4, col5, col6 = st.columns(3)
        condition = col4.selectbox("Overall Condition", ["Mint (Like New)", "Good", "Fair", "Needs Work"], index=1)
        
        states_list = [
            "Karnataka (Bangalore)", "Kerala", "Telangana / Andhra Pradesh", 
            "Maharashtra (Mumbai / Pune)", "Tamil Nadu", "Himachal / J&K / Uttarakhand", 
            "Gujarat", "Rajasthan / Punjab / Haryana", "Uttar Pradesh / Chandigarh", 
            "Madhya Pradesh / Chhattisgarh", "Delhi NCR (10-Yr Rule)", 
            "West Bengal / Odisha", "Bihar / Jharkhand", "Assam & North East States"
        ]
        city_loc = col5.selectbox("Registration Zone", states_list, index=10)
        user_price = col6.number_input("Your Expected Price (₹)", 0, 50000000, 0, step=50000)

        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.form_submit_button("Initiate Deep Scan Valuation 🚀", type="primary", use_container_width=True)

    if submit:
        with st.spinner("Accessing satellite market data & calculating depreciation..."):
            price = train_and_predict(car_nm, year, km, def_fuel, owner, def_trans, def_cc, def_bhp, def_speed, battery_kwh=def_battery, city=city_loc)
            cond_map = {"Mint (Like New)": 1.05, "Good": 1.0, "Fair": 0.85, "Needs Work": 0.65}
            price = int(price * cond_map.get(condition, 1.0))

            st.markdown("<div class='fade-in-up'>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background: rgba(0, 255, 204, 0.1); border: 2px solid #00ffcc; padding: 20px; border-radius: 15px; text-align: center; box-shadow: 0 0 20px rgba(0, 255, 204, 0.3); margin-bottom: 20px;'>
                <h3 style='color: #fff; margin:0;'>🤖 AI CERTIFIED VALUE ({city_loc.split(' ')[0]})</h3>
                <h1 style='color: #00ffcc; font-size: 50px; margin: 10px 0; text-shadow: 0 0 20px #00ffcc;'>₹ {price:,.0f}</h1>
            </div>
            """, unsafe_allow_html=True)

            generate_pdf(car_nm, year, km, def_fuel, def_trans, condition, city_loc, price, def_battery)
            with open("Valuation_Report.pdf", "rb") as pdf_file:
                st.download_button(
                    label="📥 Download Official Terminal Report (PDF)",
                    data=pdf_file, file_name=f"{car_nm.replace(' ', '_')}_{city_loc[:5]}_Valuation_2026.pdf", mime="application/pdf", type="secondary"
                )

            if user_price > 0:
                diff = price - user_price
                if abs(diff) < (price * 0.05): st.success("🎯 SPOT ON: Your expectation matches the exact algorithm output.")
                elif diff > 0: st.info(f"💡 PROFIT DETECTED: Market estimate is **₹{diff:,.0f} HIGHER** than your expectation.")
                else: st.warning(f"⚠️ LOSS ALERT: Your asking price is **₹{abs(diff):,.0f} ABOVE** standard market tolerance.")

            st.markdown("---")
            st.markdown(f"<h3 class='sub-title' style='text-align:left;'>📉 15-Year Trajectory Analysis</h3>", unsafe_allow_html=True)
            
            graph_years = list(range(2010, 2027))
            graph_prices = [int(train_and_predict(car_nm, y, km, def_fuel, owner, def_trans, def_cc, def_bhp, def_speed, battery_kwh=def_battery, city=city_loc) * cond_map.get(condition, 1.0)) for y in graph_years]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=graph_years, y=graph_prices, mode='lines+markers', name='Market Value', 
                                     line=dict(color='#00ffcc', width=4), marker=dict(size=10, color='white', line=dict(color='#00ffcc', width=2))))
            fig.update_layout(
                template="plotly_dark", 
                xaxis_title="Manufacturing Year", yaxis_title="Estimated Value (₹)", 
                height=400, hovermode="x unified", yaxis=dict(tickformat=",.0f"),
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=True, gridcolor='rgba(0,255,204,0.1)'),
                yaxis2=dict(showgrid=True, gridcolor='rgba(0,255,204,0.1)')
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)


# --- CENTRAL HUB ---
def render_central_hub():
    st.markdown("<br><br>", unsafe_allow_html=True) 
    st.markdown("<h1 class='glow-title' style='font-size: 5.5rem; margin:0; text-align:center;'>ADVANCED AUTO AI</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='font-size: 1.5rem; letter-spacing: 4px; margin-bottom: 60px; text-align:center; color: #00ffcc !important;'>MAIN COMMAND MATRIX TERMINAL</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠\nShowroom Overview", use_container_width=True): st.session_state["current_page"] = "Home"; st.rerun()
        if st.button("⚔️\nCombat Analysis", use_container_width=True): st.session_state["current_page"] = "Compare Vehicles"; st.rerun()
    with col2:
        if st.button("🛰️\nLive Telemetry", use_container_width=True): st.session_state["current_page"] = "Live Dashboard"; st.rerun()
        if st.button("🗄️\nGlobal Registry", use_container_width=True): st.session_state["current_page"] = "Database"; st.rerun()
    with col3:
        if st.button("🔮\nAI Engine Core", use_container_width=True): st.session_state["current_page"] = "AI Price Predictions"; st.rerun()
        if st.button("ℹ️\nSystem Arch", use_container_width=True): st.session_state["current_page"] = "About"; st.rerun()


# --- MAIN ROUTING LOGIC ---
def main():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Central Hub"

    if auth.check_login():
        inject_animations()

        with st.sidebar:
            st.markdown("<h2 style='color:#00ffcc; text-shadow: 0 0 10px #00ffcc; text-align:center; letter-spacing:2px;'>[ CONTROLS ]</h2>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:center; padding:10px; background:rgba(0,255,204,0.1); border-radius:10px; margin-bottom:20px; border:1px solid #00ffcc;'><b>USER IDENTIFIED:</b><br><span style='color:#fff; font-size:18px;'>{st.session_state.get('username', 'Admin').upper()}</span></div>", unsafe_allow_html=True)
            
            if st.session_state["current_page"] != "Central Hub":
                if st.button("⬅️ RETURN TO HUB", use_container_width=True):
                    st.session_state["current_page"] = "Central Hub"
                    st.rerun()
            
            st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
            if st.button("🛑 Log Out", type="primary", use_container_width=True):
                st.session_state["logged_in"] = False
                st.session_state["current_page"] = "Central Hub"
                st.rerun()

        if st.session_state["current_page"] == "Central Hub":
            render_central_hub()
        elif st.session_state["current_page"] == "Home":
            home.show_home()
        elif st.session_state["current_page"] == "Live Dashboard":
            dashboard.show_dashboard()
        elif st.session_state["current_page"] == "Compare Vehicles":
            compare.show_compare()
        elif st.session_state["current_page"] == "AI Price Predictions":
            show_ai_price_predictions()
        elif st.session_state["current_page"] == "Database":
            database_page.show_db_page()
        elif st.session_state["current_page"] == "About":
            about.show_about()

if __name__ == "__main__":
    main()
