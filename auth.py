import streamlit as st
import db

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""

    if st.session_state["logged_in"]:
        return True
    else:
        show_login_screen()
        return False

def show_login_screen():
    db.init_db()
    
    # Set background
    page_bg = """
    <style>
    /* 1. Main Background Wallpaper */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?q=80&w=1920&auto=format&fit=crop") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }
    
    /* 2. Safed chadar (White Background) ko transparent karna */
    [data-testid="stAppViewBlockContainer"] {
        background: transparent !important;
    }
    
    /* 3. Upar ka header transparent karna */
    [data-testid="stHeader"] { 
        background: transparent !important; 
    }
    
    /* 4. Login Box Neon Styling */
    [data-testid="stForm"] {
        background-color: rgba(20, 20, 30, 0.85) !important;
        padding: 30px !important;
        border-radius: 15px !important;
        border: 2px solid #00ffcc !important;
        box-shadow: 0px 0px 25px rgba(0, 255, 204, 0.4) !important;
    }
    
    /* 5. Force All Text to be White */
    h1, h2, p, label, span { color: white !important; }
    
    /* 6. Tabs styling */
    button[data-baseweb="tab"] { background-color: transparent !important; }
    button[data-baseweb="tab"] p { color: #aaa !important; font-size: 18px !important; }
    button[aria-selected="true"] p { color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 10px #00ffcc !important;}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)
    
    # Top Title
    st.markdown("<h1 style='color: #00ffcc !important; text-align: center; margin-bottom: 30px; text-shadow: 0 0 15px #00ffcc;'>🏎️ Advanced Auto AI</h1>", unsafe_allow_html=True)
    
    c_left, c_right = st.columns([1, 1.2])
    with c_left:
        st.markdown("<br><br><h2 style='font-size: 40px; font-weight: bold; text-shadow: 2px 2px 10px black;'>Enterprise-Level<br>Vehicle Valuation System</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#00ffcc !important; font-size: 18px; text-shadow: 1px 1px 5px black;'>Log in using dealership credentials.</p>", unsafe_allow_html=True)
        
    with c_right:
        t1, t2 = st.tabs(["🔑 Login", "➕ Register"])
        with t1:
            with st.form("login_form"):
                user = st.text_input("Username")
                pwd = st.text_input("Password", type="password")
                if st.form_submit_button("login", type="primary", use_container_width=True):
                    if db.check_user(user, pwd):
                        st.session_state.update({"logged_in": True, "username": user})
                        st.rerun()
                    else: st.error("Invalid credentials.")
        with t2:
            with st.form("reg_form"):
                n_user = st.text_input("New ID")
                n_pwd = st.text_input("Password", type="password")
                c_pwd = st.text_input("Confirm", type="password")
                if st.form_submit_button("Create Account", type="primary", use_container_width=True):
                    if n_user and n_pwd == c_pwd:
                        if db.add_user(n_user, n_pwd): st.success("Registered! Please login.")
                        else: st.error("ID exists.")
                    else: st.error("Passwords mismatch.")