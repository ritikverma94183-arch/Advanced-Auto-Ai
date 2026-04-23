import streamlit as st

# 🚀 1. PAGE CONFIGURATIONS (Sabse upar hona zaroori hai)
st.set_page_config(page_title="Advanced Auto AI", page_icon="🏎️", layout="wide", initial_sidebar_state="collapsed")

import plotly.graph_objects as go
import pandas as pd
from fpdf import FPDF
import time
from datetime import datetime
import sqlite3

# 🚀 2. CORE IMPORTS
try:
    import auth, home, dashboard, database_page, db, compare
    from ml_engine import train_and_predict
except Exception as e:
    st.error(f"🚨 FATAL ERROR: Core files missing. Details: {e}")

# 🔥 CSS INJECTION (Hide sidebar, sleek buttons, premium wallpaper)
def inject_animations():
    css = """
    <style>
    /* 🛑 HIDE STREAMLIT SIDEBAR & TOP MENU COMPLETELY */
    [data-testid="collapsedControl"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    
    /* 🌍 BACKGROUND */
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    .stApp { background: transparent !important; }
    
    /* 🔗 SECONDARY BUTTONS -> LOOK LIKE TEXT LINKS (For Navbar/Footer) */
    button[kind="secondary"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #aaaaaa !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 0 !important;
        height: auto !important;
        min-height: 0 !important;
        line-height: normal !important;
        transition: all 0.2s ease-in-out !important;
    }
    button[kind="secondary"]:hover {
        color: #00ffcc !important;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.5) !important;
        transform: translateY(-2px) !important;
    }

    /* 🟦 PRIMARY BUTTONS (For Login & Forms) */
    button[kind="primary"] {
        background: linear-gradient(90deg, #0055ff, #00ffcc) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
    }
    button[kind="primary"]:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 5px 15px rgba(0, 255, 204, 0.4) !important;
    }

    /* 🔥 BIG DASHBOARD BUTTONS */
    .dash-btn button[kind="primary"] {
        height: 100px !important;
        font-size: 18px !important;
        background: rgba(10, 15, 25, 0.8) !important;
        border: 1px solid rgba(0, 255, 204, 0.4) !important;
        color: #00ffcc !important;
    }
    .dash-btn button[kind="primary"]:hover {
        background: rgba(0, 255, 204, 0.15) !important;
        border-color: #00ffcc !important;
    }

    /* TEXT STYLES */
    h1, h2, h3, h4, p, label, span { color: #ffffff !important; font-family: 'Segoe UI', sans-serif; }
    .glow-title { color: #00ffcc !important; font-weight: 900; text-shadow: 0 0 15px rgba(0, 255, 204, 0.5); letter-spacing: 2px; }
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div { background-color: rgba(0,0,0,0.6) !important; border: 1px solid #00ffcc !important; color: #00ffcc !important; border-radius: 8px !important; }
    .fade-in-up { animation: fadeInUp 0.8s ease-out; }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(30px); } 100% { opacity: 1; transform: translateY(0); } }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    
    # 🏎️ LUXURY SUPERCAR WALLPAPER
    full_bg_html = """
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -9999; background: #050505;">
        <img src="https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?q=80&w=1920&auto=format&fit=crop" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(0.25);" />
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.85));"></div>
    </div>
    """
    st.markdown(full_bg_html, unsafe_allow_html=True)

# ==========================================
# 🌐 TOP NAVBAR (Header)
# ==========================================
def render_navbar():
    st.markdown("<br>", unsafe_allow_html=True) 
    c1, c2, c3, c4, c5, c6 = st.columns([3, 1, 0.8, 0.8, 1, 1.2])
    
    with c1:
        st.markdown("<h3 style='margin:0; padding:0;'>🏎️ Advanced Auto <span style='color:#00ffcc;'>AI</span></h3>", unsafe_allow_html=True)
    
    with c3:
        if st.button("Home", key="nav_home", type="secondary"): st.session_state["current_page"] = "Home"; st.rerun()
    with c4:
        if st.button("About Us", key="nav_about", type="secondary"): st.session_state["current_page"] = "About"; st.rerun()
    
    if st.session_state.get("logged_in"):
        with c5:
            if st.button("Dashboard", key="nav_dash", type="secondary"): st.session_state["current_page"] = "Dashboard"; st.rerun()
        with c6:
            if st.button("Sign Out", key="nav_out", type="primary"): 
                st.session_state["logged_in"] = False
                st.session_state["current_page"] = "Home"
                st.rerun()
    else:
        with c6:
            if st.button("Sign In / Sign Up", key="nav_in", type="primary"): st.session_state["current_page"] = "Login"; st.rerun()
            
    st.markdown("<hr style='margin-top:10px; border-color:rgba(0,255,204,0.2);'>", unsafe_allow_html=True)

# ==========================================
# 🌍 BOTTOM FOOTER
# ==========================================
def render_footer():
    st.markdown("<br><br><br><hr style='border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns([5, 1.5, 1.5, 1])
    
    with f1:
        now = datetime.now().strftime("%Y")
        st.markdown(f"<p style='color:#666; font-size:13px;'>© {now} Advanced Auto AI. All Rights Reserved. | Designed for Next-Gen Dealerships</p>", unsafe_allow_html=True)
    
    with f3:
        if st.button("Contact Us", key="foot_contact", type="secondary"): st.session_state["current_page"] = "Support"; st.rerun()
    with f4:
        if st.button("Privacy Policy", key="foot_legal", type="secondary"): st.session_state["current_page"] = "Legal"; st.rerun()


# ==========================================
# 🏠 PUBLIC PAGES (Bina Login Ke)
# ==========================================
def render_landing_page():
    st.markdown("<br><br>", unsafe_allow_html=True) 
    st.markdown("""
    <div class="fade-in-up" style="text-align: center;">
        <h1 style='font-size: 5rem; color: white; font-weight: 900; margin-bottom: 0;'>Welcome to <span style='color: #00ffcc;'>Advanced Auto AI</span></h1>
        <p style='font-size: 1.3rem; color: #aaa; max-width: 800px; margin: 20px auto; line-height: 1.6;'>
            The Global Standard for Automotive Telemetry & Neural Valuation. Navigate market trends, run combat analysis, and secure your dealership with Artificial Intelligence.
        </p>
    </div>
    <hr style='border: 1px solid rgba(255,255,255,0.1); margin: 50px 0;'>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    card_style = "background: rgba(0,0,0,0.5); padding: 30px; border-radius: 15px; border: 1px solid rgba(0,255,204,0.2); text-align: center; backdrop-filter: blur(10px);"
    c1.markdown(f"<div style='{card_style}'><h2 style='color:#00ffcc; margin:0;'>99.4%</h2><p style='color:#ccc; margin-top:5px;'>Neural Engine Accuracy</p></div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='{card_style}'><h2 style='color:#00ffcc; margin:0;'>Real-Time</h2><p style='color:#ccc; margin-top:5px;'>RTO Geo-Sync</p></div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='{card_style}'><h2 style='color:#00ffcc; margin:0;'>SECURED</h2><p style='color:#ccc; margin-top:5px;'>Military-Grade Database</p></div>", unsafe_allow_html=True)

def show_about():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>ℹ️ About Advanced Auto AI</h1>", unsafe_allow_html=True)
    
    # 🔥 YAHAN TERA ASLI DIALOGUE AA GAYA HAI BINA EXPANDER KE 🔥
    st.markdown("""
    <div class="fade-in-up" style="background: rgba(10, 15, 25, 0.85); padding: 40px; border-radius: 15px; border: 1px solid rgba(0, 255, 204, 0.3); margin: 20px auto; max-width: 900px;">
        
        <h3 style="color:#00ffcc;">Global Telemetry System</h3>
        <p style="color:#ddd; line-height:1.6; font-size:16px; margin-bottom: 20px;">
        Welcome to the next generation of automotive dealership management. This is a state-of-the-art telemetry and algorithmic valuation matrix designed for the second-hand vehicle market. By eliminating manual guesswork, our system brings enterprise-grade data science directly to the showroom floor.
        </p>

        <h3 style="color:#00ffcc;">Our Mission</h3>
        <p style="color:#ddd; line-height:1.6; font-size:16px; margin-bottom: 20px;">
        To revolutionize the second-hand vehicle market by providing an AI-driven, unbiased, and mathematically accurate valuation matrix.
        </p>
        
        <h3 style="color:#00ffcc;">System Architecture</h3>
        <p style="color:#ddd; line-height:1.6; font-size:16px;">
        Built on a Python-based neural core, the system utilizes Non-Linear Exponential Decay formulas and real-time Telemetry specifically designed for the Indian automobile sector.
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_legal():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>⚖️ Privacy Policy & Terms</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="fade-in-up" style="background: rgba(10, 15, 25, 0.8); border: 1px solid rgba(0, 255, 204, 0.2); border-radius: 10px; padding: 30px; color: #ddd; max-width: 900px; margin: 20px auto;">
        <h3 style="color: #00ffcc; border-bottom: 1px solid rgba(0,255,204,0.3); padding-bottom: 10px;">Privacy Policy</h3>
        <p>When you register as an agent, we collect standard identification metrics. All authentication data is stored locally in our highly secure database. No third-party sharing occurs.</p>
        <br>
        <h3 style="color: #00ffcc; border-bottom: 1px solid rgba(0,255,204,0.3); padding-bottom: 10px;">Terms & Conditions</h3>
        <p>Advanced Auto AI is an evaluation system. Prices are generated using non-linear decay algorithms. The AI Engine Core is restricted to authorized dealership agents only.</p>
    </div>
    """, unsafe_allow_html=True)

def show_support():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>📞 Contact Support</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("contact_form"):
            st.text_input("Full Name")
            st.text_input("Registered Email")
            st.text_area("How can we help you?")
            if st.form_submit_button("Send Transmission 🚀", type="primary", use_container_width=True):
                st.success("✅ Transmission Received! Our cyber-agents will contact you soon.")


# ==========================================
# 🔒 PRIVATE DASHBOARD (Login Ke Baad)
# ==========================================
def render_private_dashboard():
    st.markdown("<h1 class='glow-title' style='text-align:center; font-size: 3rem;'>MAIN COMMAND MATRIX</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#aaa; letter-spacing:3px;'>SECURE SYSTEM ACCESS GRANTED</p><br>", unsafe_allow_html=True)
    
    st.markdown("<div class='dash-btn'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        if st.button("🔮 AI Engine Core", key="dash_ai", type="primary", use_container_width=True): st.session_state["current_page"] = "AI Price Predictions"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚔️ Combat Analysis", key="dash_combat", type="primary", use_container_width=True): st.session_state["current_page"] = "Compare Vehicles"; st.rerun()
        
    with c2:
        if st.button("🛰️ Live Telemetry", key="dash_live", type="primary", use_container_width=True): st.session_state["current_page"] = "Live Dashboard"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗄️ Global Registry", key="dash_reg", type="primary", use_container_width=True): st.session_state["current_page"] = "Database"; st.rerun()
        
    with c3:
        if st.button("👤 Agent Profile", key="dash_prof", type="primary", use_container_width=True): st.session_state["current_page"] = "Profile"; st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🏠 Showroom Overview", key="dash_home", type="primary", use_container_width=True): st.session_state["current_page"] = "Showroom Home"; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def show_profile():
    st.markdown("<br><h1 class='glow-title' style='text-align:center;'>👤 Agent Profile</h1>", unsafe_allow_html=True)
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
    <div class="fade-in-up" style="background: rgba(10, 15, 25, 0.85); border: 1px solid #00ffcc; border-radius: 15px; padding: 40px; max-width: 600px; margin: 0 auto;">
        <div style="text-align: center; border-bottom: 1px solid rgba(0,255,204,0.2); padding-bottom: 20px; margin-bottom: 20px;">
            <h2 style="color: white; margin: 0; text-transform: uppercase;">{username}</h2>
            <p style="color: #00ffcc; font-weight: bold; margin: 0;">Tier-1 Authorized Agent</p>
        </div>
        <table style="width: 100%; color: #ccc; font-size: 16px;">
            <tr><td style="padding: 10px 0;"><b>Email:</b></td><td style="text-align: right; color: white;">{email}</td></tr>
            <tr><td style="padding: 10px 0;"><b>Phone:</b></td><td style="text-align: right; color: white;">{phone}</td></tr>
            <tr><td style="padding: 10px 0;"><b>DOB:</b></td><td style="text-align: right; color: white;">{dob}</td></tr>
            <tr><td style="padding: 10px 0;"><b>Status:</b></td><td style="text-align: right; color: #00ffcc;">🟢 Online</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# --- PDF Generation ---
def generate_pdf(car_nm, year, km, fuel, trans, cond, city, price, battery_kwh: int = 0):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 15, "ADVANCED AUTO AI", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 8, "Official Valuation Certificate", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, f"Vehicle: {car_nm}"); pdf.cell(0, 10, f"Year: {year}", ln=True)
    pdf.cell(100, 10, f"Odometer: {km:,} km"); pdf.cell(0, 10, f"Fuel: {fuel}", ln=True)
    pdf.cell(100, 10, f"Condition: {cond}"); pdf.cell(0, 10, f"Zone: {city}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 18)
    pdf.set_text_color(0, 153, 76)
    pdf.cell(0, 15, f"MARKET VALUE: INR {price:,.0f}", ln=True, align='C')
    try: pdf.output("Valuation_Report.pdf")
    except: pass

# --- AI Price Predictions Function ---
def show_ai_price_predictions():
    st.markdown("<h1 class='glow-title'>🔮 AI Valuation Engine</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#aaa; margin-bottom:30px;'>Real-Time Depreciation Matrix & Compliance Scanner</p>", unsafe_allow_html=True)

    try:
        df_cars = db.get_all_cars()
        if not df_cars.empty: car_list = sorted(df_cars['Car_Name'].unique().tolist())
        else: car_list = ["Maruti Suzuki Swift", "Toyota Fortuner", "Lamborghini Urus"]
    except Exception:
        df_cars = pd.DataFrame()
        car_list = ["Maruti Suzuki Swift", "Toyota Fortuner"]

    car_nm = st.selectbox("🚘 Select Target Vehicle", car_list)

    def_fuel, def_trans, def_cc, def_bhp, def_speed, def_battery = "Petrol", "Manual", 1500, 100, 180, 0
    if not df_cars.empty:
        car_data = df_cars[df_cars['Car_Name'] == car_nm]
        if not car_data.empty:
            if 'Fuel_Type' in car_data.columns: def_fuel = str(car_data['Fuel_Type'].iloc[0])
            if 'Transmission' in car_data.columns: def_trans = str(car_data['Transmission'].iloc[0])
            if 'Engine_Capacity_cc' in car_data.columns: def_cc = int(car_data['Engine_Capacity_cc'].iloc[0])
            if 'Power_BHP' in car_data.columns: def_bhp = int(car_data['Power_BHP'].iloc[0])

    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        year = col1.number_input("Manufacturing Year", 1996, 2026, 2024)
        km = col2.number_input("Kilometers Driven", 0, 500000, 25000, step=1000)
        owner = col3.selectbox("Owner Type", ["First", "Second", "Third", "Fourth"])

        col4, col5, col6 = st.columns(3)
        condition = col4.selectbox("Condition", ["Mint (Like New)", "Good", "Fair", "Needs Work"], index=1)
        city_loc = col5.selectbox("Zone", ["Delhi NCR (10-Yr Rule)", "Maharashtra (Mumbai / Pune)", "Karnataka (Bangalore)", "Kerala", "Other"], index=0)
        user_price = col6.number_input("Expected Price (₹)", 0, 50000000, 0, step=50000)

        submit = st.form_submit_button("Scan & Calculate Value 🚀", type="primary", use_container_width=True)

    if submit:
        with st.spinner("Processing satellite data..."):
            time.sleep(1)
            price = train_and_predict(car_nm, year, km, def_fuel, owner, def_trans, def_cc, def_bhp, def_speed, battery_kwh=def_battery, city=city_loc)
            cond_map = {"Mint (Like New)": 1.05, "Good": 1.0, "Fair": 0.85, "Needs Work": 0.65}
            price = int(price * cond_map.get(condition, 1.0))

            st.markdown(f"""
            <div class='fade-in-up' style='background: rgba(0, 255, 204, 0.05); border-left: 5px solid #00ffcc; padding: 20px; border-radius: 8px; margin-top: 20px;'>
                <h4 style='color: #ccc; margin:0;'>AI CERTIFIED VALUE</h4>
                <h1 style='color: #00ffcc; font-size: 45px; margin: 5px 0;'>₹ {price:,.0f}</h1>
            </div>
            """, unsafe_allow_html=True)
            generate_pdf(car_nm, year, km, def_fuel, def_trans, condition, city_loc, price, def_battery)
            with open("Valuation_Report.pdf", "rb") as pdf_file:
                st.download_button(label="📥 Download Report", data=pdf_file, file_name="Valuation.pdf", mime="application/pdf")


# ==========================================
# 🚀 MAIN APP ROUTING ENGINE
# ==========================================
def main():
    if "current_page" not in st.session_state: st.session_state["current_page"] = "Home"
    if "logged_in" not in st.session_state: st.session_state["logged_in"] = False

    inject_animations()
    
    # 1. TOP NAVBAR (Agar Login page par nahi hain to Navbar dikhega)
    if st.session_state["current_page"] != "Login":
        render_navbar()

    # 2. PAGE CONTENT RENDERING
    page = st.session_state["current_page"]

    # Public Pages
    if page == "Home": render_landing_page()
    elif page == "About": show_about()
    elif page == "Support": show_support()
    elif page == "Legal": show_legal()
    
    # Authentication Page (Login/Sign Up)
    elif page == "Login":
        # 🔥 YAHAN TERA BACK TO HOME AUR T&C AA GAYA 🔥
        colA, colB, colC = st.columns([1, 2, 1])
        with colA:
            st.markdown("<br><br>", unsafe_allow_html=True)
            if st.button("⬅️ Back to Home", key="back_to_home_login", type="secondary"):
                st.session_state["current_page"] = "Home"
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Original Login Form call
        auth.check_login()

        # Login hone ke baad direct dashboard
        if st.session_state.get("logged_in"):
            st.session_state["current_page"] = "Dashboard"
            st.rerun()

        # Auth form ke niche Terms & Conditions
        st.markdown("<hr style='border-color:rgba(255,255,255,0.1); margin-top:40px; max-width: 600px; margin-left:auto; margin-right:auto;'>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#888; font-size:13px;'>By signing in, you agree to our System Policies.</p>", unsafe_allow_html=True)
        colX, colY, colZ = st.columns([1, 1, 1])
        with colY:
            if st.button("Read Terms & Conditions", key="login_terms_btn", type="secondary", use_container_width=True):
                st.session_state["current_page"] = "Legal"
                st.rerun()

    # Protected Pages (Only if logged in)
    elif page in ["Dashboard", "AI Price Predictions", "Compare Vehicles", "Live Dashboard", "Database", "Profile", "Showroom Home"]:
        if not st.session_state["logged_in"]:
            st.error("🚨 ACCESS DENIED: Please Sign In to access the Advanced Auto AI Matrix.")
        else:
            if page == "Dashboard": render_private_dashboard()
            elif page == "Profile": show_profile()
            elif page == "Showroom Home": home.show_home()
            elif page == "AI Price Predictions": show_ai_price_predictions()
            elif page == "Compare Vehicles": compare.show_compare()
            elif page == "Live Dashboard": dashboard.show_dashboard()
            elif page == "Database": database_page.show_db_page()

    # 3. BOTTOM FOOTER (Agar Login page par nahi hain to Footer dikhega)
    if st.session_state["current_page"] != "Login":
        render_footer()

if __name__ == "__main__":
    main()
