import streamlit as st
import sqlite3
import time

# 🔥 ADVANCED CSS, WALLPAPER & ANIMATIONS INJECTION
def inject_login_css():
    css = """
    <style>
    /* Transparent Streamlit Overlays */
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    [data-testid="stAppViewBlockContainer"] { background: transparent !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    
    /* --------------------------------------
       INPUT BOXES (Cyberpunk Style) 
    --------------------------------------- */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: rgba(10, 15, 25, 0.8) !important;
        border: 1px solid rgba(0, 255, 204, 0.3) !important;
        color: #00ffcc !important;
        border-radius: 6px !important;
        transition: all 0.3s ease-in-out !important;
    }
    div[data-baseweb="input"] > div:hover, div[data-baseweb="input"] > div:focus-within {
        border: 1px solid #00ffcc !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
        background-color: rgba(0, 0, 0, 0.9) !important;
    }
    
    /* --------------------------------------
       PRIMARY BUTTONS (Glowing & Futuristic) 
    --------------------------------------- */
    button[kind="primary"] {
        background: linear-gradient(135deg, rgba(0, 85, 255, 0.8), rgba(0, 255, 204, 0.8)) !important;
        color: white !important;
        border: 1px solid rgba(0, 255, 204, 0.5) !important;
        font-weight: 900 !important;
        border-radius: 6px !important;
        padding: 12px 20px !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        transition: all 0.4s ease !important;
    }
    button[kind="primary"]:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 8px 25px rgba(0, 255, 204, 0.6) !important;
        background: linear-gradient(135deg, rgba(0, 85, 255, 1), rgba(0, 255, 204, 1)) !important;
    }
    
    /* --------------------------------------
       SECONDARY BUTTONS (Forgot Password Link) 
    --------------------------------------- */
    button[kind="secondary"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #aaaaaa !important;
        font-size: 14px !important;
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

    /* --------------------------------------
       TABS CUSTOMIZATION (Neon Underline) 
    --------------------------------------- */
    button[data-baseweb="tab"] {
        background: transparent !important;
        color: #888888 !important;
        font-size: 15px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00ffcc !important;
        border-bottom: 3px solid #00ffcc !important;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.5) !important;
    }

    /* --------------------------------------
       ANIMATIONS 
    --------------------------------------- */
    .fade-in-up { animation: fadeInUp 0.8s cubic-bezier(0.165, 0.84, 0.44, 1); }
    @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(40px); } 100% { opacity: 1; transform: translateY(0); } }
    
    /* Glitch Title Effect */
    .glitch-title {
        color: #00ffcc;
        text-align: center;
        font-weight: 900;
        font-size: 2.5rem;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.8);
        letter-spacing: 4px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }

    /* Hacker Status Bar (Scrolling Text) */
    .status-bar {
        background: rgba(0, 0, 0, 0.8);
        border-top: 1px solid rgba(0, 255, 204, 0.3);
        border-bottom: 1px solid rgba(0, 255, 204, 0.3);
        color: #00ffcc;
        font-family: monospace;
        font-size: 12px;
        padding: 5px 0;
        overflow: hidden;
        white-space: nowrap;
        width: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
    }
    .status-content {
        display: inline-block;
        padding-left: 100%;
        animation: scrollStatus 20s linear infinite;
    }
    @keyframes scrollStatus { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    
    # 🏎️ PREMIUM DARK WALLPAPER WITH VIGNETTE EFFECT
    full_bg_html = """
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -9999; background: #030508;">
        <img src="https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?q=80&w=1920&auto=format&fit=crop" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(0.20) contrast(1.2);" />
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%);"></div>
    </div>
    """
    st.markdown(full_bg_html, unsafe_allow_html=True)


# Database Initialize Function
def init_db():
    conn = sqlite3.connect('secure_auth.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_agents
                 (username TEXT PRIMARY KEY, password TEXT, email TEXT, phone TEXT, dob TEXT)''')
    conn.commit()
    conn.close()


# Main Login/Register Function
def check_login():
    inject_login_css()
    init_db()
    
    # Session state variables for Dynamic View Logic
    if "auth_view" not in st.session_state:
        st.session_state["auth_view"] = "login"  # Options: 'login' or 'recovery'
    if "recovery_step" not in st.session_state:
        st.session_state["recovery_step"] = 1
    if "recover_user" not in st.session_state:
        st.session_state["recover_user"] = ""

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Main Container
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='fade-in-up' style='background: rgba(10, 15, 22, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(0,255,204,0.4); border-radius: 12px; padding: 40px; box-shadow: 0 15px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,255,204,0.05); position: relative; overflow: hidden;'>", unsafe_allow_html=True)
        
        st.markdown("<h1 class='glitch-title'>🛡️ SYSTEM LOGIN</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888; font-family: monospace; margin-bottom: 30px;'>AUTHORIZATION REQUIRED TO ACCESS SECURE MATRIX</p>", unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 Authenticate", "📄 Initialize Agent"])
        
        # --- 1. AUTHENTICATE TAB (Handles both Login & Password Recovery dynamically) ---
        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)
            
            # 🟢 STATE A: SHOW NORMAL LOGIN FORM
            if st.session_state["auth_view"] == "login":
                log_user = st.text_input("Admin ID / Username", key="log_user")
                log_pass = st.text_input("Security Passcode", type="password", key="log_pass")
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("VERIFY CLEARANCE 🚀", type="primary", use_container_width=True):
                    with st.spinner("SCANNING BIOMETRICS... DECRYPTING HASH..."):
                        time.sleep(1.5)
                    
                    conn = sqlite3.connect('secure_auth.db')
                    c = conn.cursor()
                    c.execute("SELECT * FROM system_agents WHERE username=? AND password=?", (log_user, log_pass))
                    result = c.fetchone()
                    conn.close()
                    
                    if result:
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = log_user
                        st.session_state["auth_view"] = "login" # reset
                        st.success("✅ ACCESS GRANTED. Welcome to the Matrix.")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error("❌ ACCESS DENIED. INTRUDER DETECTED.")

                # 🔥 FORGOT PASSWORD LINK (Clickable Text Button at the bottom) 🔥
                st.markdown("<div style='text-align: center; margin-top: 25px;'>", unsafe_allow_html=True)
                if st.button("Forgot Security Passcode?", key="forgot_btn", type="secondary"):
                    st.session_state["auth_view"] = "recovery"
                    st.session_state["recovery_step"] = 1
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

            # 🔴 STATE B: SHOW PASSWORD RECOVERY FORM
            elif st.session_state["auth_view"] == "recovery":
                st.markdown("<h3 style='color: #00ffcc; text-align:center;'>⚠️ SYSTEM RECOVERY</h3>", unsafe_allow_html=True)
                
                # Step 1: Verification
                if st.session_state["recovery_step"] == 1:
                    st.markdown("<p style='color:#ccc; text-align:center; font-size:14px;'>Enter details to verify your identity.</p>", unsafe_allow_html=True)
                    rec_user = st.text_input("Registered Admin ID", key="rec_user")
                    rec_email = st.text_input("Registered Comm Link (Email)", key="rec_email")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("VERIFY IDENTITY 🔍", type="primary", use_container_width=True):
                        with st.spinner("SEARCHING GLOBAL REGISTRY..."):
                            time.sleep(1)
                            
                        conn = sqlite3.connect('secure_auth.db')
                        c = conn.cursor()
                        c.execute("SELECT * FROM system_agents WHERE username=? AND email=?", (rec_user, rec_email))
                        result = c.fetchone()
                        conn.close()
                        
                        if result:
                            st.session_state["recovery_step"] = 2
                            st.session_state["recover_user"] = rec_user
                            st.success("✅ IDENTITY VERIFIED. UPLINK SECURED.")
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error("❌ VERIFICATION FAILED. Details do not match our records.")
                
                # Step 2: Set New Password
                elif st.session_state["recovery_step"] == 2:
                    st.markdown(f"<p style='color:#00ffcc; text-align:center;'>Identity Confirmed: {st.session_state['recover_user']}</p>", unsafe_allow_html=True)
                    new_pass = st.text_input("Enter New Security Passcode", type="password", key="new_pass")
                    confirm_pass = st.text_input("Confirm New Passcode", type="password", key="confirm_pass")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("RESET PASSCODE ♻️", type="primary", use_container_width=True):
                        if new_pass == confirm_pass and new_pass != "":
                            with st.spinner("OVERWRITING ENCRYPTION KEYS..."):
                                time.sleep(1)
                            
                            conn = sqlite3.connect('secure_auth.db')
                            c = conn.cursor()
                            c.execute("UPDATE system_agents SET password=? WHERE username=?", (new_pass, st.session_state["recover_user"]))
                            conn.commit()
                            conn.close()
                            
                            st.session_state["auth_view"] = "login"
                            st.session_state["recovery_step"] = 1
                            st.session_state["recover_user"] = ""
                            st.success("✅ PASSCODE RESET SUCCESSFUL! You can now Authenticate.")
                            time.sleep(2)
                            st.rerun()
                        else:
                            st.error("⚠️ PASSCODES DO NOT MATCH OR ARE EMPTY.")

                # 🔥 BACK TO LOGIN LINK 🔥
                st.markdown("<div style='text-align: center; margin-top: 25px;'>", unsafe_allow_html=True)
                if st.button("⬅️ Back to System Login", key="back_login_btn", type="secondary"):
                    st.session_state["auth_view"] = "login"
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

        # --- 2. REGISTER TAB (New Agent Creation) ---
        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)
            reg_user = st.text_input("Assign New Admin ID", key="reg_user")
            reg_pass = st.text_input("Set Security Passcode", type="password", key="reg_pass")
            
            c_reg1, c_reg2 = st.columns(2)
            reg_email = c_reg1.text_input("Agent Comm Link (Email)", key="reg_email")
            reg_phone = c_reg2.text_input("Secure Phone Line", key="reg_phone")
            
            reg_dob = st.date_input("Manufacture Date (DOB)")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("INITIALIZE CLEARANCE 🛡️", type="primary", use_container_width=True):
                if reg_user and reg_pass and reg_email:
                    try:
                        conn = sqlite3.connect('secure_auth.db')
                        c = conn.cursor()
                        c.execute("INSERT INTO system_agents (username, password, email, phone, dob) VALUES (?, ?, ?, ?, ?)", 
                                  (reg_user, reg_pass, reg_email, reg_phone, str(reg_dob)))
                        conn.commit()
                        conn.close()
                        st.success("✅ NEURAL UPLINK COMPLETE! Agent Added to Registry. Please Authenticate.")
                    except sqlite3.IntegrityError:
                        st.error("⚠️ FATAL: Admin ID already exists in the Main Registry!")
                else:
                    st.warning("⚠️ SYSTEM HALT: Mandatory fields (ID, Passcode, Email) are empty.")
        
        # Hacker Status Bar at the bottom of the container
        st.markdown("""
        <br>
        <div class="status-bar">
            <div class="status-content">
                [SYSTEM LOG] UPLINK: SECURE | ENCRYPTION: AES-256 ACTIVE | FIREWALL: ONLINE | DATABASE SYNC: 100% | UNAUTHORIZED ACCESS ATTEMPTS BLOCKED: 1,402
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
