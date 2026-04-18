import streamlit as st
import auth, home, dashboard, database_page, about, db, compare
import plotly.graph_objects as go
import pandas as pd
from ml_engine import train_and_predict
from fpdf import FPDF
import os

st.set_page_config(page_title="Advanced Car System", page_icon="🏎️", layout="wide")

# 🔥 ADVANCED FORCE ANIMATION, BOLD TEXT & FULL-SCREEN WALLPAPER INJECTOR
def inject_animations():
    css_animations = """
    <style>
    /* 1. Streamlit ki Safed Chadar ko completely transparent karna */
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    [data-testid="stAppViewBlockContainer"] { background: transparent !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    .stApp { background: transparent !important; }

    /* 2. 🔥 TEXT KO EXTRA BOLD AUR VISIBLE KARNE KA MAGIC 🔥 */
    h1, h2, h3, h4, h5, h6, p, label, span, div[data-testid="stMarkdownContainer"] {
        font-weight: 800 !important; /* Extra Bold */
        color: #ffffff !important; /* Pure White */
        text-shadow: 2px 2px 8px #000000, 0px 0px 5px #000000 !important; /* Deep Black Shadow */
    }

    /* Dropdown/Selectbox text fix */
    .stSelectbox label { font-size: 16px !important; }

    /* Neon Titles */
    .glow-title { 
        color: #00ffcc !important;
        font-weight: 900 !important;
        text-shadow: 0 0 10px #00ffcc, 0 0 25px #00ffcc, 2px 2px 10px black !important;
    }
    .sub-title {
        color: #ffffff !important;
        text-shadow: 2px 2px 8px #000000 !important;
    }

    /* 3. BIG CENTERED NAVIGATION BUTTONS */
    div.stButton > button {
        height: 120px;
        font-size: 22px !important;
        font-weight: 900 !important; /* Extra Bold Button Text */
        border-radius: 15px;
        background: rgba(20, 20, 30, 0.85) !important;
        border: 2px solid #00ffcc !important;
        transition: all 0.4s ease !important;
        color: white !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.7) !important;
        text-shadow: 2px 2px 5px black !important;
    }
    div.stButton > button:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: 0 15px 30px rgba(0, 255, 204, 0.5) !important;
        color: #00ffcc !important;
    }
    
    /* 4. Smooth Slide-Up Effect */
    .fade-in-up { animation: fadeInUp 0.8s ease-out; }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(40px); } 100% { opacity: 1; transform: translateY(0); } }
    </style>
    """
    st.markdown(css_animations, unsafe_allow_html=True)
    
    # 🔥 FULL SCREEN SPLIT WALLPAPER (Fixed format)
    full_bg_html = (
        "<div style='position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -9999; display: flex;'>"
        "<div style=\"flex: 1; background: url('https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?q=80&w=1920') center/cover no-repeat;\"></div>"
        "<div style=\"flex: 1; background: url('https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?q=80&w=1920') center/cover no-repeat;\"></div>"
        "<div style='position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85);'></div>"
        "</div>"
    )
    st.markdown(full_bg_html, unsafe_allow_html=True)


# --- PDF Generation Function ---
def generate_pdf(car_nm, year, km, fuel, trans, cond, price, battery_kwh: int = 0):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(245, 245, 245)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_font("Arial", 'B', 22)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 12, "ADVANCED AUTO AI", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, "Official Valuation Certificate", ln=True, align='C')
    pdf.ln(6)

    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(100, 8, f"Vehicle: {car_nm}")
    pdf.cell(0, 8, f"Year: {year}", ln=True)
    pdf.cell(100, 8, f"Odometer: {km:,} km")
    pdf.cell(0, 8, f"Fuel: {fuel}", ln=True)
    pdf.cell(100, 8, f"Transmission: {trans}")
    pdf.cell(0, 8, f"Condition: {cond}", ln=True)

    if isinstance(battery_kwh, (int, float)) and battery_kwh > 0:
        pdf.ln(2)
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 8, f"Battery Capacity (est): {battery_kwh} kWh", ln=True)

    pdf.ln(6)
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 110, 60)
    pdf.cell(0, 12, f"CERTIFIED MARKET VALUE: INR {price:,.0f}", ln=True, align='C')

    try: pdf.output("Valuation_Report.pdf")
    except Exception: pass


# --- AI Price Predictions Function ---
def show_ai_price_predictions():
    st.markdown("<h1 class='glow-title' style='font-size:40px; margin-top:20px;'>🔮 Enterprise Valuation Engine</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Using Real-Time Indian Market Depreciation Logic (2026 RTO Compliance).</p>", unsafe_allow_html=True)

    try:
        df_cars = db.get_all_cars()
        if not df_cars.empty: car_list = sorted(df_cars['Car_Name'].unique().tolist())
        else: car_list = ["Maruti Suzuki Swift", "Toyota Fortuner", "Lamborghini Urus"]
    except Exception:
        df_cars = pd.DataFrame()
        car_list = ["Maruti Suzuki Swift", "Toyota Fortuner", "Lamborghini Urus"]

    st.markdown("<h3 class='sub-title' style='text-align:left;'>🚘 Select Vehicle</h3>", unsafe_allow_html=True)
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
        st.markdown("#### ⚡ Fixed Engine & Performance Specs")
        c_eng1, c_eng2, c_eng3, c_eng4 , c_eng5, c_eng6 = st.columns(6)
        box_style = "padding: 10px; background-color: rgba(255,255,255,0.1); border-radius: 8px; border: 1px solid #00ffcc; color: #fff; font-size: 16px; text-align: center; font-weight: 900; text-shadow: 2px 2px 5px black;"

        c_eng1.markdown(f"<div style='font-size: 15px; margin-bottom: 5px; color: #fff;'>Engine Capacity</div><div style='{box_style}'>{def_cc} cc</div><br>", unsafe_allow_html=True)
        c_eng2.markdown(f"<div style='font-size: 15px; margin-bottom: 5px; color: #fff;'>Power</div><div style='{box_style}'>{def_bhp} BHP</div><br>", unsafe_allow_html=True)
        c_eng3.markdown(f"<div style='font-size: 15px; margin-bottom: 5px; color: #fff;'>Top Speed</div><div style='{box_style}'>{def_speed} km/h</div><br>", unsafe_allow_html=True)
        c_eng4.markdown(f"<div style='font-size: 15px; margin-bottom: 5px; color: #fff;'>Battery</div><div style='{box_style}'>{def_battery} kWh</div><br>", unsafe_allow_html=True)
        c_eng5.markdown(f"<div style='font-size: 15px; margin-bottom: 5px; color: #fff;'>Fuel Type</div><div style='{box_style}'>{def_fuel}</div><br>", unsafe_allow_html=True)
        c_eng6.markdown(f"<div style='font-size: 15px; margin-bottom: 5px; color: #fff;'>Transmission</div><div style='{box_style}'>{def_trans}</div><br>", unsafe_allow_html=True)
        
        st.markdown("#### ⚙️ Usage & Deal Parameters")
        col1, col2, col3 = st.columns(3)
        year = col1.number_input("Manufacturing Year", 1996, 2026, 2024)
        km = col2.number_input("Kilometers Driven", 0, 500000, 25000, step=1000)
        owner = col3.selectbox("Owner Type", ["First", "Second", "Third", "Fourth"])

        col4, col5 = st.columns(2)
        condition = col4.selectbox("Overall Condition", ["Mint (Like New)", "Good", "Fair", "Needs Work"], index=1)
        user_price = col5.number_input("Your Expected Price (₹)", 0, 50000000, 0, step=50000)

        submit = st.form_submit_button("Generate Professional Valuation", type="primary")

    if submit:
        with st.spinner("Calculating real-world market depreciation..."):
            price = train_and_predict(car_nm, year, km, def_fuel, owner, def_trans, def_cc, def_bhp, def_speed, battery_kwh=def_battery)
            cond_map = {"Mint (Like New)": 1.05, "Good": 1.0, "Fair": 0.85, "Needs Work": 0.65}
            price = int(price * cond_map.get(condition, 1.0))

            st.markdown("<div class='fade-in-up'>", unsafe_allow_html=True)
            st.success(f"🤖 Market Estimated Price: **₹{price:,.0f}**")

            generate_pdf(car_nm, year, km, def_fuel, def_trans, condition, price, def_battery)
            with open("Valuation_Report.pdf", "rb") as pdf_file:
                st.download_button(
                    label="📥 Download Valuation Certificate (PDF)",
                    data=pdf_file, file_name=f"{car_nm.replace(' ', '_')}_Valuation_2026.pdf", mime="application/pdf", type="secondary"
                )

            if user_price > 0:
                diff = price - user_price
                if abs(diff) < (price * 0.05): st.success("🎯 Spot on! Your expected price perfectly matches the current market.")
                elif diff > 0: st.info(f"💡 Good News! The market estimate is **₹{diff:,.0f} MORE** than your expectation. You can ask for more!")
                else: st.warning(f"⚠️ Alert! Your asking price is **₹{abs(diff):,.0f} ABOVE** the standard market value.")

            st.markdown("---")
            st.markdown(f"<h3 class='sub-title' style='text-align:left;'>📉 Live Market Trend: {car_nm}</h3>", unsafe_allow_html=True)
            
            graph_years = list(range(2010, 2027))
            graph_prices = [int(train_and_predict(car_nm, y, km, def_fuel, owner, def_trans, def_cc, def_bhp, def_speed, battery_kwh=def_battery) * cond_map.get(condition, 1.0)) for y in graph_years]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=graph_years, y=graph_prices, mode='lines+markers', name='Market Value (₹)', line=dict(color='#00ffcc', width=4), marker=dict(size=8, color='white')))
            fig.update_layout(
                template="plotly_dark", 
                xaxis_title="Manufacturing Year", 
                yaxis_title="Estimated Value (₹)", 
                height=400, 
                hovermode="x unified", 
                yaxis=dict(tickformat=",.0f"),
                paper_bgcolor='rgba(0,0,0,0.6)', 
                plot_bgcolor='rgba(0,0,0,0.6)'
            )
            st.plotly_chart(fig, use_container_width=True)
            st.balloons()
            st.markdown("</div>", unsafe_allow_html=True)


# --- CENTRAL HUB LOGIC ---
def render_central_hub():
    st.markdown("<br><br>", unsafe_allow_html=True) 
    st.markdown("<h1 class='glow-title' style='font-size: 5.5rem; margin:0; text-align:center;'>ADVANCED AUTO AI</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='font-size: 1.5rem; letter-spacing: 2px; margin-bottom: 60px; text-align:center;'>THE ULTIMATE DEALERSHIP COMMAND CENTER</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠\nShowroom Overview", use_container_width=True): st.session_state["current_page"] = "Home"; st.rerun()
        if st.button("⚔️\nCompare Vehicles", use_container_width=True): st.session_state["current_page"] = "Compare Vehicles"; st.rerun()
    with col2:
        if st.button("🛰️\nLive Analytics", use_container_width=True): st.session_state["current_page"] = "Live Dashboard"; st.rerun()
        if st.button("🗄️\nFleet Database", use_container_width=True): st.session_state["current_page"] = "Database"; st.rerun()
    with col3:
        if st.button("🔮\nAI Valuations", use_container_width=True): st.session_state["current_page"] = "AI Price Predictions"; st.rerun()
        if st.button("ℹ️\nAbout System", use_container_width=True): st.session_state["current_page"] = "About"; st.rerun()


def main():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Central Hub"

    if auth.check_login():
        inject_animations()

        with st.sidebar:
            st.markdown("<h2 style='color:#00ffcc;'>🌌 Controls</h2>", unsafe_allow_html=True)
            st.markdown(f"**Dealer:** `{st.session_state.get('username', 'Admin')}`")
            st.markdown("---")
            
            if st.session_state["current_page"] != "Central Hub":
                if st.button("⬅️ Back to Hub", use_container_width=True):
                    st.session_state["current_page"] = "Central Hub"
                    st.rerun()
            
            if st.button("🛑 Logout", type="primary", use_container_width=True):
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