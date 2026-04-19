import streamlit as st

def show_about():
    # 🔥 ADVANCED CSS: Hacker Terminal & Typewriter Effect
    about_css = """
    <style>
    /* Hacker Terminal Styling */
    .terminal-box {
        background-color: rgba(10, 10, 15, 0.85);
        border: 2px solid #00ffcc;
        border-radius: 15px;
        padding: 30px;
        font-family: 'Courier New', Courier, monospace;
        color: #00ffcc;
        box-shadow: 0 0 25px rgba(0,255,204,0.2) inset, 0 10px 20px rgba(0,0,0,0.8);
        margin-bottom: 40px;
    }
    
    /* Typewriter Animation */
    .typewriter-text {
        overflow: hidden; 
        white-space: nowrap; 
        border-right: .15em solid #00ffcc; 
        animation: typing 3s steps(50, end), blink-caret .75s step-end infinite;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow: 0 0 5px #00ffcc;
    }
    
    @keyframes typing { from { width: 0 } to { width: 100% } }
    @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #00ffcc; } }

    /* 3D Tech Cards */
    .tech-card {
        background: linear-gradient(145deg, #1e1e2e, #15151e);
        padding: 25px; border-radius: 15px; border: 1px solid #444;
        text-align: center; transition: all 0.4s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5); height: 240px;
    }
    .tech-card:hover {
        transform: translateY(-12px) scale(1.05);
        border-color: #00ffcc; box-shadow: 0 15px 30px rgba(0, 255, 204, 0.3); z-index: 10;
    }
    </style>
    """
    st.markdown(about_css, unsafe_allow_html=True)

    st.markdown("<h1 class='glow-title' style='text-align:center; font-size: 55px; margin-top:20px;'>🤖 System Architecture</h1>", unsafe_allow_html=True)

    # 🔥 THE HACKER BOOT TERMINAL
    st.markdown("""
    <div class="terminal-box">
        <div class="typewriter-text">> INITIALIZING SYSTEM BOOT SEQUENCE... [OK]</div>
        <div class="typewriter-text">> CONNECTING TO CENTRAL DEALERSHIP DATABASE... [CONNECTED]</div>
        <div class="typewriter-text">> LOADING AI VALUATION ENGINE (v2.6)... [ACTIVE]</div>
        <div class="typewriter-text">> BYPASSING FIREWALL... [ACCESS GRANTED]</div>
        <hr style="border-color:#00ffcc; margin: 20px 0;">
        <h2 style="color:white; font-weight:900; margin-bottom:5px;">PROJECT: ADVANCED AUTO AI</h2>
        <p style="color:#aaa; font-family:sans-serif; font-size:16px;">A highly sophisticated, AI-driven telemetry and market valuation interface designed exclusively for next-generation automobile dealerships. Engineered to calculate real-world depreciation, EV battery penalties, and region-specific RTO compliance.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:white; text-shadow: 2px 2px 5px black; margin-bottom:30px;'>⚙️ CORE TECHNOLOGIES</h2>", unsafe_allow_html=True)

    # 2x2 Grid for Tech Stack
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class='tech-card'>
            <h1 style='margin:0; font-size: 50px; text-shadow:none;'>🖥️</h1>
            <h3 style='color:#00ffcc; font-weight:900; margin-top: 10px;'>Frontend UI/UX</h3>
            <p style='color:#ccc; font-size: 15px;'>Built on <b>Streamlit</b> with custom inline CSS injection for dynamic, real-time 3D animations and holographic layouts.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='tech-card'>
            <h1 style='margin:0; font-size: 50px; text-shadow:none;'>🧠</h1>
            <h3 style='color:#00ffcc; font-weight:900; margin-top: 10px;'>Backend AI Engine</h3>
            <p style='color:#ccc; font-size: 15px;'>Custom algorithm calculating market depreciation, kilometers driven penalties, EV Battery (kWh) lifespan, and City/State modifiers.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='tech-card'>
            <h1 style='margin:0; font-size: 50px; text-shadow:none;'>📊</h1>
            <h3 style='color:#00ffcc; font-weight:900; margin-top: 10px;'>Data Visualization</h3>
            <p style='color:#ccc; font-size: 15px;'>Powered by <b>Plotly Graph Objects</b> to render animated radar charts, live market trends, and performance battle mechanics.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='tech-card'>
            <h1 style='margin:0; font-size: 50px; text-shadow:none;'>🗄️</h1>
            <h3 style='color:#00ffcc; font-weight:900; margin-top: 10px;'>Database & PDF</h3>
            <p style='color:#ccc; font-size: 15px;'>Secure <b>SQLite</b> authentication, dynamic CSV live registry, and <b>FPDF</b> for instant valuation certificate generation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
