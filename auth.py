import streamlit as st
import sqlite3
import datetime

# --- INITIALIZE USER DATABASE ---
def init_auth_db():
    conn = sqlite3.connect('secure_auth.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_agents 
                 (username TEXT PRIMARY KEY, email TEXT, phone TEXT, dob TEXT, password TEXT)''')
    
    # Default Admin account add karna
    c.execute("SELECT * FROM system_agents WHERE username='admin'")
    if not c.fetchone():
        c.execute("INSERT INTO system_agents VALUES ('admin', 'admin@autoai.com', '0000000000', '2000-01-01', 'admin123')")
    
    conn.commit()
    conn.close()

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        init_auth_db()  # Database initialize
        
        # 🔥 DIRECT CSS INJECTION FOR PREMIUM LUXURY CAR WALLPAPER & UI FIXES
        login_css = """
        <style>
        /* Force Streamlit App Background to Advanced Luxury Car Image */
        [data-testid="stAppViewContainer"] {
            background-color: #050505;
            background-image: url("https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?q=80&w=1920&auto=format&fit=crop");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        
        /* Transparent Header */
        [data-testid="stHeader"] {
            background-color: transparent !important;
        }

        /* Title Styling */
        .login-title {
            color: #00ffcc; font-size: 45px; font-weight: 900; text-align: center;
            text-shadow: 0 0 15px #00ffcc, 2px 2px 10px black; margin-bottom: 20px;
            letter-spacing: 3px;
        }
        
        /* Expander (About Us) Styling */
        [data-testid="stExpander"] {
            background-color: rgba(10, 15, 20, 0.85) !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid #00ffcc !important;
            border-radius: 15px !important;
            color: white !important;
        }
        [data-testid="stExpander"] p {
            color: #ddd !important;
        }
        
        /* Forms Glassmorphism */
        div[data-testid="stForm"] {
            background-color: rgba(10, 15, 25, 0.85) !important;
            backdrop-filter: blur(15px) !important;
            border: 2px solid rgba(0, 255, 204, 0.5) !important;
            border-radius: 15px !important;
            box-shadow: 0 15px 30px rgba(0,0,0,0.9) !important;
        }
        
        /* 🔥 FIX: Input Labels (Username, Password, etc.) */
        .stTextInput p, .stDateInput p {
            color: #00ffcc !important;
            font-size: 16px !important;
            font-weight: 900 !important;
            text-shadow: 1px 1px 5px black !important;
        }
        
        /* 🔥 FIX: Input Boxes & Text inside them */
        div[data-baseweb="input"], div[data-baseweb="select"] {
            background-color: rgba(0, 0, 0, 0.8) !important;
            border: 2px solid #00ffcc !important;
            border-radius: 8px !important;
        }
        div[data-baseweb="input"] input {
            color: #00ffcc !important;
            font-size: 16px !important;
            font-weight: bold !important;
            -webkit-text-fill-color: #00ffcc !important; /* Bypass browser autofill color */
        }
        
        /* 🔥 FIX: Submit Buttons */
        div[data-testid="stForm"] button {
            background: rgba(0, 0, 0, 0.8) !important;
            color: #00ffcc !important;
            border: 2px solid #00ffcc !important;
            border-radius: 10px !important;
            font-weight: 900 !important;
            font-size: 18px !important;
            padding: 10px !important;
            transition: all 0.3s ease !important;
        }
        div[data-testid="stForm"] button:hover {
            background: #00ffcc !important;
            color: #000 !important;
            box-shadow: 0 0 20px #00ffcc !important;
            transform: scale(1.02) !important;
        }
        
        /* Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            background-color: rgba(0,0,0,0.8); border-radius: 10px; padding: 5px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #ccc; font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            color: #00ffcc !important; border-bottom: 3px solid #00ffcc !important; text-shadow: 0 0 10px #00ffcc;
        }
        </style>
        """
        st.markdown(login_css, unsafe_allow_html=True)

        st.markdown("<h1 class='login-title'>🔐 SECURE TERMINAL ACCESS</h1>", unsafe_allow_html=True)
        
        # Center layout
        c1, c2, c3 = st.columns([1, 2, 1])
        
        with c2:
            # --- CLICKABLE ABOUT US SECTION (EXPANDER AT TOP) ---
            with st.expander("🌐 CLICK HERE: ABOUT ADVANCED AUTO AI", expanded=False):
                st.markdown("""
                <h3 style="color: #00ffcc; text-align: center; font-weight: 900; letter-spacing: 2px; margin-top: 0;">GLOBAL TELEMETRY SYSTEM</h3>
                <p style="color: #ddd; font-size: 15px; text-align: justify; line-height: 1.6;">
                    Welcome to the next generation of automotive dealership management. <b>Advanced Auto AI</b> is a state-of-the-art telemetry and algorithmic valuation matrix designed to revolutionize the second-hand vehicle market. By eliminating manual guesswork, our system brings enterprise-grade data science directly to the showroom floor.
                </p>
                <hr style="border-color: rgba(0,255,204,0.3);">
                <h4 style="color: white; font-size: 16px;">⚡ Core Capabilities:</h4>
                <ul style="color: #bbb; font-size: 14px; line-height: 1.8;">
                    <li><b style="color:#00ffcc;">🧠 Neural Valuation Engine:</b> Computes exact market value utilizing non-linear exponential decay mathematics.</li>
                    <li><b style="color:#ff4b4b;">🌍 Geo-Sync Intelligence:</b> Instantly adapts pricing across 28 Indian states, factoring in strict RTO scrap policies.</li>
                    <li><b style="color:#0088ff;">🔋 EV Architecture Ready:</b> Logic mapping specific to Electric Vehicle battery degradation (kWh).</li>
                    <li><b style="color:#ffc107;">📊 Live Telemetry:</b> Holographic 3D visualization of dealership net worth, fleet performance, and combat comparisons.</li>
                </ul>
                <p style="color: #888; text-align: center; font-size: 12px; margin-top: 20px;">SYSTEM BUILT FOR 2026 MARKET DYNAMICS • SECURE ACCESS ONLY</p>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True) # Space between About Us and Login Box

            # --- LOGIN & REGISTER TABS ---
            tab1, tab2 = st.tabs(["🔓 System Login", "📝 Register New"])
            
            # === TAB 1: LOGIN ===
            with tab1:
                with st.form("login_form"):
                    st.markdown("<h3 style='color: white; text-align: center; font-size: 18px; letter-spacing: 1px;'>AUTHENTICATION REQUIRED</h3>", unsafe_allow_html=True)
                    username = st.text_input("Admin ID / Username")
                    password = st.text_input("Security Passcode", type="password")
                    submit_login = st.form_submit_button("Log In", use_container_width=True)
                    
                    if submit_login:
                        conn = sqlite3.connect('secure_auth.db')
                        c = conn.cursor()
                        c.execute("SELECT * FROM system_agents WHERE username=? AND password=?", (username, password))
                        user = c.fetchone()
                        conn.close()
                        
                        if user:
                            st.session_state["logged_in"] = True
                            st.session_state["username"] = username
                            st.rerun()
                        else:
                            st.error("⚠️ Access Denied. Invalid Identity or Passcode.")

            # === TAB 2: REGISTER ===
            with tab2:
                with st.form("register_form"):
                    st.markdown("<h3 style='color: #00ffcc; text-align: center; font-size: 18px; letter-spacing: 1px;'>ENLIST NEW SYSTEM AGENT</h3>", unsafe_allow_html=True)
                    new_username = st.text_input("Choose Username *")
                    new_email = st.text_input("Email Address *")
                    new_phone = st.text_input("Mobile Number *")
                    new_dob = st.date_input("Date of Birth *", min_value=datetime.date(1950, 1, 1), max_value=datetime.date(2010, 1, 1), value=datetime.date(2000, 1, 1))
                    new_password = st.text_input("Create Passcode *", type="password")
                    submit_register = st.form_submit_button("REGISTER TO TERMINAL 🛡️", use_container_width=True)
                    
                    if submit_register:
                        if new_username and new_email and new_phone and new_password:
                            conn = sqlite3.connect('secure_auth.db')
                            c = conn.cursor()
                            try:
                                c.execute("INSERT INTO system_agents (username, email, phone, dob, password) VALUES (?, ?, ?, ?, ?)", 
                                          (new_username, new_email, new_phone, str(new_dob), new_password))
                                conn.commit()
                                st.success("✅ Registration Successful! Please switch to the 'System Login' tab to access.")
                            except sqlite3.IntegrityError:
                                st.error("⚠️ Username already exists! Choose a different one.")
                            conn.close()
                        else:
                            st.warning("⚠️ Please fill all required fields (*).")
            
        return False
    return True
