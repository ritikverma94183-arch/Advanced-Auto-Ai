import streamlit as st

def show_about():
    # 🔥 ADVANCED ABOUT PAGE ANIMATIONS & EFFECTS
    about_css = """
    <style>
    /* Fade In Effect */
    .fade-in { animation: fadeIn 1s ease-in; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

    /* Neon Gradient Title */
    .gradient-text {
        background: linear-gradient(45deg, #00ffcc, #0088ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }

    /* 🏎️ MOVING CAR ANIMATION TRACK */
    .track {
        width: 100%;
        height: 60px;
        background: #15151e;
        border-bottom: 3px dashed #00ffcc;
        position: relative;
        overflow: hidden;
        border-radius: 10px;
        margin: 30px 0;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.8);
    }
    .car-anim {
        font-size: 45px;
        position: absolute;
        top: 0px;
        animation: drive 5s linear infinite;
    }
    @keyframes drive {
        0% { left: -15%; }
        100% { left: 110%; }
    }

    /* 3D Hover Cards for Tech Stack */
    .tech-box {
        background: #1e1e2e;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #3b3b4f;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 5px 15px rgba(0,0,0,0.4);
        margin-bottom: 20px;
        height: 220px;
    }
    .tech-box:hover {
        transform: translateY(-12px) scale(1.05);
        border-color: #00ffcc;
        box-shadow: 0 15px 30px rgba(0, 255, 204, 0.25);
        z-index: 10;
    }
    </style>
    """
    st.markdown(about_css, unsafe_allow_html=True)

    # Start Container
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    # Header section
    st.markdown("<h1 class='gradient-text'>🚀 About Advanced Auto AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc; font-size:18px;'>Next-Generation Dealership & Valuation Command Center</p>", unsafe_allow_html=True)

    # 🔥 The Moving Car Animation
    st.markdown("""
    <div class='track'>
        <div class='car-anim'>🏎️💨</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌟 Project Vision")
    st.info("This application is designed to revolutionize the automobile industry by bringing **Real-Time AI Market Valuations**, **Live Inventory Telemetry**, and **Advanced Combat-style Comparisons** into a single, high-performance dashboard.")

    st.markdown("---")
    st.markdown("<h3 style='text-align:center; margin-bottom: 30px; color:white;'>⚙️ Core Technologies Under The Hood</h3>", unsafe_allow_html=True)

    # 2x2 Grid for Tech Stack
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class='tech-box'>
            <h1 style='margin:0; font-size: 50px;'>🖥️</h1>
            <h3 style='color:#00ffcc; margin-top: 10px;'>Frontend UI/UX</h3>
            <p style='color:#aaa; font-size: 14px;'>Built exclusively on <b>Streamlit</b> with custom CSS injection for dynamic, real-time 3D animations and interactive layouts.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='tech-box'>
            <h1 style='margin:0; font-size: 50px;'>🧠</h1>
            <h3 style='color:#00ffcc; margin-top: 10px;'>Backend AI Engine</h3>
            <p style='color:#aaa; font-size: 14px;'>Custom logic algorithms to calculate real-world market depreciation, kilometers driven penalties, and condition modifiers.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='tech-box'>
            <h1 style='margin:0; font-size: 50px;'>📊</h1>
            <h3 style='color:#00ffcc; margin-top: 10px;'>Data Visualization</h3>
            <p style='color:#aaa; font-size: 14px;'>Powered by <b>Plotly Graph Objects & Express</b> to render animated radar charts, live market trends, and performance battle mechanics.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='tech-box'>
            <h1 style='margin:0; font-size: 50px;'>🗄️</h1>
            <h3 style='color:#00ffcc; margin-top: 10px;'>Database Management</h3>
            <p style='color:#aaa; font-size: 14px;'>Secure data handling utilizing <b>SQLite</b> for user authentication and dynamic <b>CSV integration</b> for the live vehicle registry.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🔒 Compliance & Certification")
    st.success("PDF Generation integrated natively via **FPDF** for downloading official, shareable vehicle valuation certificates instantly.")

    # End Container
    st.markdown("</div>", unsafe_allow_html=True)