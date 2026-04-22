import streamlit as st

# 🚀 1. PAGE CONFIGURATIONS (Sabse upar hona zaroori hai)
st.set_page_config(page_title="Advanced Auto AI", page_icon="🏎️", layout="wide")

import plotly.graph_objects as go
import pandas as pd
from fpdf import FPDF
import time
from datetime import datetime
import sqlite3

# 🚀 2. CORE IMPORTS
try:
    import auth, home, dashboard, database_page, about, db, compare
    from ml_engine import train_and_predict
except Exception as e:
    st.error(f"🚨 FATAL ERROR: Core files missing. Details: {e}")

# 🔥 ADVANCED SLEEK CSS & FULL-SCREEN WALLPAPER INJECTOR
def inject_animations():
    css_animations = """
    <style>
    /* Transparent Streamlit Overlays */
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    [data-testid="stAppViewBlockContainer"] { background: transparent !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    .stApp { background: transparent !important; }
    [data-testid="stSidebar"] { background-color: rgba(10, 15, 20, 0.85) !important; backdrop-filter: blur(10px); border-right: 1px solid #00ffcc; }

    /* Global Text & Shadow Styling */
    h1, h2, h3, h4, h5, h6, p, label, span, div[data-testid="stMarkdownContainer"] {
        color: #ffffff !important; 
        text-shadow: 2px 2px 8px #000000, 0px 0px 5px #000000 !important; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stSelectbox label, .stNumberInput label { font-size: 16px !important; font-weight: bold !important; color: #00ffcc !important;}

    /* Glowing Titles with Pulse Animation */
    @keyframes glowPulse {
        0% { text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc; }
        50% { text-shadow: 0 0 20px #00ffcc, 0 0 40px #00ffcc, 0 0 60px #00ffcc; }
        100% { text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc; }
    }
    .glow-title { 
        color: #00ffcc !important;
        font-weight: 900 !important;
        letter-spacing: 2px;
        animation: glowPulse 3s infinite;
    }
    .sub-title { color: #ccc !important; text-shadow: 2px 2px 8px #000000 !important; font-weight: bold; letter-spacing: 1px;}

    /* 🔥 ADVANCED TECH BUTTONS (SLEEK & SHARP - PRIMARY) */
    button[kind="primary"] {
        height: 85px !important;
        font-size: 16px !important;
        font-weight: 900 !important; 
        border-radius: 12px !important;
        background: rgba(10, 15, 25, 0.8) !important; 
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(0, 255, 204, 0.5) !important;
        transition: all 0.3s ease-in-out !important;
        color: #00ffcc !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.8), inset 0 0 10px rgba(0,255,204,0.05) !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
    }
    button[kind="primary"]:hover {
        transform: translateY(-5px) scale(1.02) !important;
        background: rgba(0, 255, 204, 0.15) !important;
        border-color: #00ffcc !important;
        box-shadow: 0 10px 25px rgba(0, 255, 204, 0.5), inset 0 0 15px rgba(0,255,204,0.3) !important;
        color: #ffffff !important;
        text-shadow: 0 0 8px #00ffcc !important;
    }

    /* 🌐 WEBSITE-STYLE FOOTER BUTTONS (SECONDARY) */
    button[kind="secondary"] {
        height: 45px !important;
        font-size: 14px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        background: rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(5px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: #bbb !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        box-shadow: none !important;
    }
    button[kind="secondary"]:hover {
        border-color: #00ffcc !important;
        color: #00ffcc !important;
        background: rgba(0, 255, 204, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }

    /* SIDEBAR & FORM OVERRIDES */
    [data-testid="stSidebar"] button[kind="primary"], div[data-testid="stForm"] button[kind="primary"] {
        height: 50px !important;
        font-size: 15px !important;
        border-radius: 8px !important;
        box-shadow: 0 5px 15px rgba(0,255,204,0.2) !important;
        text-shadow: none !important;
    }

    /* Input Boxes Customization */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: rgba(0,0,0,0.6) !important;
        border: 1px solid #00ffcc !important;
        color: #00ffcc !important;
    }
    
    /* Scrolling Ticker CSS */
    .ticker-wrapper {
        background: rgba(0, 0, 0, 0.8); border-bottom: 1px solid #00ffcc; border-top: 1px solid #00ffcc;
        color: #00ffcc; font-family: monospace; font-size: 14px; padding: 5px 0; overflow: hidden; white-space: nowrap; margin-bottom: 20px;
    }
    .ticker-content { display: inline-block; padding-left: 100%; animation: ticker 20s linear infinite; }
    @keyframes ticker { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }
    
    /* Smooth Load Effect */
    .fade-in-up { animation: fadeInUp 0.8s ease-out; }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(40px); } 100% { opacity: 1; transform: translateY(0); } }
    </style>
    """
    st.markdown(css_animations, unsafe_allow_html=True)
    
    # 🔥 SEAMLESS PREMIUM WALLPAPER
    full_bg_html = """
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -9999; background: #000;">
        <img src="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1920&q=80" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(1.20);" />
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.85));"></div>
    </div>
    """
    st.markdown(full_bg_html, unsafe_allow_html=True)


# --- 🚀 NEW EMBEDDED ADVANCED PAGES (FIX FOR THE 3 BUTTONS) ---

def show_legal():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>⚖️ LEGAL & COMPLIANCE MATRIX</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='text-align:center;'>System Policies, Data Handling, and Terms of Service</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔒 Privacy Policy", "📜 Terms & Conditions"])
    box_css = "background: rgba(10, 15, 25, 0.8); border: 1px solid rgba(0, 255, 204, 0.4); border-radius: 10px; padding: 30px; color: #ddd; box-shadow: 0 10px 30px rgba(0,0,0,0.8);"
    with tab1:
        st.markdown(f"""
        <div style="{box_css}">
            <h3 style="color: #00ffcc; border-bottom: 1px solid #00ffcc; padding-bottom: 10px;">Privacy Policy</h3>
            <h4>1. Data Collection & Telemetry</h4>
            <p>When you register as a System Agent, we collect standard identification metrics (Username, Email, Date of Birth). Telemetry is securely processed within the matrix.</p>
            <h4>2. Data Security & Encryption</h4>
            <p>All user authentication data is stored in our local, highly secure database (`secure_auth.db`).</p>
        </div>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown(f"""
        <div style="{box_css}">
            <h3 style="color: #00ffcc; border-bottom: 1px solid #00ffcc; padding-bottom: 10px;">Terms & Conditions</h3>
            <h4>1. System Nature & Accuracy</h4>
            <p>Advanced Auto AI is built as a state-of-the-art AI evaluation project. The system generates predicted vehicle prices using non-linear exponential decay algorithms.</p>
            <h4>2. Authorized Use</h4>
            <p>Registered Agents are authorized to use the Combat Analysis and AI Engine Core for non-commercial evaluation purposes only.</p>
        </div>
        """, unsafe_allow_html=True)

def show_support():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>📞 HELPDESK & SYSTEM FAQ</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='text-align:center;'>Resolve Queries & Contact System Administrators</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["❓ Frequently Asked Questions", "📨 Contact Support"])
    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🤖 How does the Neural Valuation Engine calculate prices?"):
            st.write("Our engine uses a complex non-linear exponential decay formula. It analyzes base factory value, deducts depreciation, and factors in 28-state RTO tax multipliers.")
        with st.expander("🔋 Does the system support Electric Vehicles (EVs)?"):
            st.write("Yes! We have a dedicated algorithm for EVs based on Battery Capacity (kWh) and lifespan degradation.")
    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.form("support_ticket"):
            st.markdown("<h3 style='color: #00ffcc;'>Submit a Support Ticket</h3>", unsafe_allow_html=True)
            st.selectbox("Issue Category", ["Valuation Error", "Database Update Request", "Account Issue", "Other"])
            st.text_area("Describe your issue in detail...")
            if st.form_submit_button("SEND TRANSMISSION 🚀", type="primary"):
                st.success("✅ Transmission Received! Our cyber-agents will contact your registered email.")

def show_profile():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>👤 AGENT IDENTITY CARD</h1>", unsafe_allow_html=True)
    username = st.session_state.get("username", "Unknown")
    
    try:
        conn = sqlite3.connect('secure_auth.db')
        c = conn.cursor()
        c.execute("SELECT email, phone, dob FROM system_agents WHERE username=?", (username,))
        user_data = c.fetchone()
        conn.close()
        if user_data: email, phone, dob = user_data
        else: email, phone, dob = "CLASSIFIED", "CLASSIFIED", "CLASSIFIED"
    except Exception:
        email, phone, dob = "CLASSIFIED", "CLASSIFIED", "CLASSIFIED"

    st.markdown(f"""
    <div class="fade-in-up" style="background: rgba(10, 15, 25, 0.85); backdrop-filter: blur(10px); border: 2px solid #00ffcc; border-radius: 15px; padding: 40px; margin: 20px auto; max-width: 600px; box-shadow: 0 0 30px rgba(0,255,204,0.2);">
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/8682/8682333.png" width="100" style="filter: drop-shadow(0px 0px 10px #00ffcc);">
            <h2 style="color: white; margin-top: 10px; text-transform: uppercase;">{username}</h2>
            <p style="color: #00ffcc; font-weight: bold; letter-spacing: 2px;">CLEARANCE LEVEL: TIER-1 ADMIN</p>
        </div>
        <hr style="border-color: rgba(0, 255, 204, 0.3);">
        <table style="width: 100%; color: #ccc; font-size: 18px;">
            <tr><td style="padding: 10px 0;"><b>📧 Comm Link (Email):</b></td><td style="text-align: right; color: white;">{email}</td></tr>
            <tr><td style="padding: 10px 0;"><b>📱 Secured Line (Phone):</b></td><td style="text-align: right; color: white;">{phone}</td></tr>
            <tr><td style="padding: 10px 0;"><b>📅 Manufacture Date (DOB):</b></td><td style="text-align: right; color: white;">{dob}</td></tr>
            <tr><td style="padding: 10px 0;"><b>🟢 Status:</b></td><td style="text-align: right; color: #00ffcc; font-weight: bold;">ACTIVE / ONLINE</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)


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
        with st.spinner("Establishing secure connection to satellite database..."):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01) 
                progress_bar.progress(percent_complete + 1)
            
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
                elif diff > 0: 
                    st.info(f"💡 PROFIT DETECTED: Market estimate is **₹{diff:,.0f} HIGHER** than your expectation.")
                    st.balloons() 
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


# --- CENTRAL HUB (ADVANCED UI UPGRADE) ---
def render_central_hub():
    # 🔥 ADVANCED FEATURE: Scrolling Live Ticker
    st.markdown("""
    <div class='ticker-wrapper'>
        <div class='ticker-content'>
            [SYSTEM ALERT] SECURE SATELLITE UPLINK ESTABLISHED... ENCRYPTED CONNECTION: STABLE... NEURAL ENGINE ACCURACY: 99.4%... RTO DATABASE SYNCED: 28 STATES... ACTIVE FIREWALL: ENGAGED...
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='glow-title' style='font-size: 4.5rem; margin:0; text-align:center;'>ADVANCED AUTO AI</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='font-size: 1.2rem; letter-spacing: 4px; margin-bottom: 20px; text-align:center; color: #00ffcc !important;'>MAIN COMMAND MATRIX TERMINAL</p>", unsafe_allow_html=True)
    
    # 🔥 ADVANCED FEATURE: Holographic System Metrics
    m1, m2, m3 = st.columns(3)
    metric_css = "background: rgba(0,0,0,0.6); border: 1px solid #00ffcc; border-radius: 10px; padding: 15px; text-align: center; color: white; margin-bottom: 30px; box-shadow: inset 0 0 10px rgba(0,255,204,0.2);"
    m1.markdown(f"<div style='{metric_css}'><p style='margin:0; font-size:12px; color:#ccc;'>GLOBAL NODES</p><h2 style='margin:0; color:#00ffcc;'>1,402 ACTIVE</h2></div>", unsafe_allow_html=True)
    m2.markdown(f"<div style='{metric_css}'><p style='margin:0; font-size:12px; color:#ccc;'>AI ACCURACY SCORE</p><h2 style='margin:0; color:#00ffcc;'>99.4 %</h2></div>", unsafe_allow_html=True)
    m3.markdown(f"<div style='{metric_css}'><p style='margin:0; font-size:12px; color:#ccc;'>DB REGISTRY STATUS</p><h2 style='margin:0; color:#00ffcc;'>SECURED</h2></div>", unsafe_allow_html=True)

    # 1. CORE MODULES
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Showroom Overview", use_container_width=True, type="primary"): st.session_state["current_page"] = "Home"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚔️ Combat Analysis", use_container_width=True, type="primary"): st.session_state["current_page"] = "Compare Vehicles"; st.rerun()
    with col2:
        if st.button("🛰️ Live Telemetry", use_container_width=True, type="primary"): st.session_state["current_page"] = "Live Dashboard"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗄️ Global Registry", use_container_width=True, type="primary"): st.session_state["current_page"] = "Database"; st.rerun()
    with col3:
        if st.button("🔮 AI Engine Core", use_container_width=True, type="primary"): st.session_state["current_page"] = "AI Price Predictions"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ℹ️ System Arch", use_container_width=True, type="primary"): st.session_state["current_page"] = "About"; st.rerun()

    # 2. WEBSITE STYLE NAVBAR
    st.markdown("<hr style='border: 1px solid rgba(0, 255, 204, 0.3); margin: 30px 0 20px 0;'>", unsafe_allow_html=True)
    
    web1, web2, web3 = st.columns(3)
    with web1:
        if st.button("👤 Agent Profile", use_container_width=True, type="secondary"): st.session_state["current_page"] = "Profile"; st.rerun()
    with web2:
        if st.button("📞 Support & FAQ", use_container_width=True, type="secondary"): st.session_state["current_page"] = "Support"; st.rerun()
    with web3:
        if st.button("⚖️ Legal & Policies", use_container_width=True, type="secondary"): st.session_state["current_page"] = "Legal"; st.rerun()


# --- MAIN ROUTING LOGIC ---
def main():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Central Hub"

    # Call auth.check_login() once to avoid creating the same login form multiple times
    logged_in = auth.check_login()

    # 🔥 ADVANCED FEATURE: Welcome Toast Login Notification
    if "toast_shown" not in st.session_state and logged_in:
        st.toast(f"Welcome Agent {st.session_state.get('username', '')}. Matrix is Online.", icon='🟢')
        st.session_state["toast_shown"] = True

    if logged_in:
        inject_animations()

        with st.sidebar:
            st.markdown("<h2 style='color:#00ffcc; text-shadow: 0 0 10px #00ffcc; text-align:center; letter-spacing:2px;'>[ CONTROLS ]</h2>", unsafe_allow_html=True)
            
            # Live Hacker System Clock
            now = datetime.now().strftime("%d-%m-%Y | %H:%M")
            st.markdown(f"<p style='text-align:center; color:#00ffcc; font-family:monospace; margin-top:-10px; font-size:14px;'>SYS.TIME: {now}</p>", unsafe_allow_html=True)

            st.markdown(f"<div style='text-align:center; padding:10px; background:rgba(0,255,204,0.1); border-radius:10px; margin-bottom:20px; border:1px solid #00ffcc;'><b>USER IDENTIFIED:</b><br><span style='color:#fff; font-size:18px;'>{st.session_state.get('username', 'Admin').upper()}</span></div>", unsafe_allow_html=True)
            
            # 🔥 ADVANCED FEATURE: Sidebar Diagnostics Loop
            st.markdown("""
            <div style='background:rgba(0,0,0,0.6); padding:10px; border-radius:8px; border:1px solid #333; margin-bottom:20px;'>
                <p style='color:#00ffcc; font-size:12px; margin:0; text-align:center;'>CORE DIAGNOSTICS</p>
                <div style='height:4px; background:#00ffcc; margin:5px 0; width:80%;'></div>
                <div style='height:4px; background:#ff4b4b; margin:5px 0; width:45%;'></div>
            </div>
            """, unsafe_allow_html=True)

            if st.session_state["current_page"] != "Central Hub":
                if st.button("⬅️ RETURN TO HUB", use_container_width=True, type="secondary"):
                    st.session_state["current_page"] = "Central Hub"
                    st.rerun()
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            if st.button("🛑 Log Out", type="primary", use_container_width=True):
                st.session_state["logged_in"] = False
                st.session_state["current_page"] = "Central Hub"
                if "toast_shown" in st.session_state: del st.session_state["toast_shown"]
                st.rerun()
                
            # Global Copyright Footer
            st.markdown("""
            <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(0,255,204,0.2);">
                <p style="color: #666; font-size: 12px; font-family: monospace;">
                    © 2026 ADVANCED AUTO AI.<br>All Rights Reserved.<br>
                    <span style="color: #00ffcc;">System Core v4.0 Active</span>
                </p>
            </div>
            """, unsafe_allow_html=True)

        # FIXED ROUTING
        current = st.session_state["current_page"]
        if current == "Central Hub": render_central_hub()
        elif current == "Home": home.show_home()
        elif current == "Live Dashboard": dashboard.show_dashboard()
        elif current == "Compare Vehicles": compare.show_compare()
        elif current == "AI Price Predictions": show_ai_price_predictions()
        elif current == "Database": database_page.show_db_page()
        elif current == "About": about.show_about()
        elif current == "Legal": show_legal()
        elif current == "Support": show_support()
        elif current == "Profile": show_profile()

if __name__ == "__main__":
    main()
