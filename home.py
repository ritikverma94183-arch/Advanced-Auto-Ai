import streamlit as st
import db

def show_home():
    # 🔥 ULTRA-ADVANCED CSS: Hacker Grids, Scanlines, 3D Tilt & Pulsing Glows
    advanced_css = """
    <style>
    /* Live News Ticker */
    .ticker-wrap {
        width: 100%; overflow: hidden; background-color: rgba(10,10,15,0.9);
        border-top: 2px solid #00ffcc; border-bottom: 2px solid #00ffcc;
        padding: 10px 0; margin-bottom: 30px; border-radius: 5px;
        box-shadow: 0 0 20px rgba(0,255,204,0.3);
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-right: 100%;
        animation: ticker 25s linear infinite;
    }
    .ticker-item {
        display: inline-block; padding: 0 2rem; font-size: 16px; color: #00ffcc; font-weight: 900; letter-spacing: 1px;
        text-shadow: 0 0 8px #00ffcc;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* 3D Pulsing Showroom Glow Cards */
    .showroom-card {
        background: rgba(20, 20, 30, 0.6);
        backdrop-filter: blur(10px); 
        border: 1px solid rgba(0, 255, 204, 0.4); 
        border-radius: 15px; padding: 25px; text-align: center;
        transition: all 0.5s ease;
        animation: pulse-border 3s infinite alternate;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    @keyframes pulse-border {
        0% { border-color: rgba(0,255,204,0.3); box-shadow: 0 0 10px rgba(0,255,204,0.1); }
        100% { border-color: rgba(0,255,204,1); box-shadow: 0 0 25px rgba(0,255,204,0.5); }
    }
    .showroom-card:hover {
        transform: translateY(-15px) perspective(1000px) rotateX(5deg);
        background: rgba(30, 30, 45, 0.8);
        border-color: #fff; box-shadow: 0 20px 50px rgba(0,255,204,0.6);
    }

    /* 🔥 TACTICAL CYBER IMAGE CARDS */
    .cyber-image-card {
        position: relative; overflow: hidden; border-radius: 15px;
        border: 2px solid #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
        height: 280px; margin-top: 20px; background-color: #050505;
    }
    .cyber-image-bg {
        position: absolute; top: 0; left: 0;
        width: 100%; height: 100%; object-fit: cover; display: block;
        transition: 0.5s ease-in-out; filter: brightness(0.6); z-index: 0;
    }
    .cyber-image-card:hover { box-shadow: 0 0 35px rgba(0, 255, 204, 0.9); }
    .cyber-image-card:hover .cyber-image-bg {
        transform: scale(1.15);
        filter: brightness(0.4) sepia(1) hue-rotate(180deg) saturate(4);
    }
    .cyber-overlay {
        position: absolute; bottom: 15px; left: 15px; background: rgba(0,0,0,0.9);
        padding: 12px 25px; border-left: 5px solid #00ffcc; backdrop-filter: blur(8px);
        z-index: 1; transition: 0.3s;
    }
    .cyber-image-card:hover .cyber-overlay {
        border-left: 5px solid #ff4b4b;
        transform: translateX(10px); 
    }

    /* Sci-Fi Scanline Animation for Banner */
    .scanline {
        position: absolute; top: 0; left: 0; width: 100%; height: 15px;
        background: rgba(0, 255, 204, 0.6); opacity: 0.7;
        box-shadow: 0 0 25px rgba(0, 255, 204, 1);
        animation: scan 3s linear infinite; z-index: 2; pointer-events: none;
    }
    @keyframes scan {
        0% { top: -20px; }
        100% { top: 100%; }
    }
    </style>
    """
    st.markdown(advanced_css, unsafe_allow_html=True)

    # 🚨 SCROLLING NEWS TICKER
    st.markdown("""
    <div class="ticker-wrap" role="region" aria-label="Live updates">
      <div class="ticker" aria-live="polite">
        <span class="ticker-item">🔴 LIVE: Neural Network connecting to global dealership databases...</span>
        <span class="ticker-item">⚡ EV Fleet integration 100% successful. Battery metrics online.</span>
        <span class="ticker-item">🏆 HIGH DEMAND: Luxury SUVs peaking in Metro Regions.</span>
        <span class="ticker-item">📉 MARKET UPDATE: Real-time telemetry systems active and secure.</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # 🖼️ 3D VIRTUAL SHOWROOM BANNER
    banner_html = """
    <div style="position: relative; border-radius: 20px; overflow: hidden; margin-bottom: 40px; border: 2px solid #00ffcc; height: 380px; box-shadow: 0 0 30px rgba(0,255,204,0.4); background-color: #000;">
        <div class="scanline" aria-hidden="true"></div>
        <img alt="Virtual showroom" src="https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?auto=format&fit=crop&w=1920&q=80" style="position: absolute; top:0; left:0; width: 100%; height: 100%; object-fit: cover; filter: brightness(0.35); z-index: 0;" />
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; width: 100%; z-index: 3; pointer-events: none;">
            <h1 style="color: #00ffcc; font-size: 75px; margin: 0; text-shadow: 3px 3px 15px black, 0 0 40px #00ffcc; font-weight:900; letter-spacing: 4px;">VIRTUAL SHOWROOM</h1>
            <p style="color: #ffffff; font-size: 26px; text-shadow: 2px 2px 10px black; font-weight:900; letter-spacing: 4px; background: rgba(0,0,0,0.6); display: inline-block; padding: 8px 25px; border-radius: 8px; border: 1px solid #00ffcc;">SYSTEM SECURE & ONLINE</p>
        </div>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)

    # DATABASE CALCULATION
    df = db.get_all_cars()
    total_cars = len(df) if df is not None and not df.empty else 0
    total_value = df['Price_INR'].sum() if df is not None and not df.empty and 'Price_INR' in df.columns else 0

    st.markdown("<h3 style='color:white; text-shadow: 2px 2px 5px black; margin-bottom: 15px; border-bottom: 1px solid #444; padding-bottom: 10px;'>📊 Real-Time Telemetry Hub</h3>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    val_cr = total_value / 10000000 if total_cars > 0 else 0
    avg_price_l = (total_value / total_cars / 100000) if total_cars > 0 else 0

    # KPI CARDS
    c1.markdown(f"<div class='showroom-card'><h4 style='color:#ccc; letter-spacing: 1px; font-size:16px;'>TOTAL INVENTORY</h4><h1 style='color:#00ffcc; font-size: 50px; margin:0; text-shadow: 0 0 15px #00ffcc;'>{total_cars} <span style='font-size:20px; color:#fff;'>Units</span></h1></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='showroom-card'><h4 style='color:#ccc; letter-spacing: 1px; font-size:16px;'>DEALERSHIP NET WORTH</h4><h1 style='color:#ff4b4b; font-size: 50px; margin:0; text-shadow: 0 0 15px #ff4b4b;'>₹ {val_cr:,.2f} <span style='font-size:20px; color:#fff;'>Cr</span></h1></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='showroom-card'><h4 style='color:#ccc; letter-spacing: 1px; font-size:16px;'>AVG. VEHICLE VALUE</h4><h1 style='color:#ffc107; font-size: 50px; margin:0; text-shadow: 0 0 15px #ffc107;'>₹ {avg_price_l:,.1f} <span style='font-size:20px; color:#fff;'>L</span></h1></div>", unsafe_allow_html=True)

    # 🔥 ADVANCED TECHNOLOGY CARDS SECTION (URL FIX APPLIED HERE)
    st.markdown("<br><h3 style='color:white; text-shadow: 2px 2px 5px black; margin-bottom: 10px; margin-top: 15px; border-bottom: 1px solid #444; padding-bottom: 10px;'>🛰️ Advanced Fleet Modules</h3>", unsafe_allow_html=True)

    col_img1, col_img2 = st.columns(2)

    with col_img1:
        st.markdown("""
        <div class="cyber-image-card">
            <img class="cyber-image-bg" src="https://images.unsplash.com/photo-1601362840469-51e4d8d58785?auto=format&fit=crop&w=1920&q=80" />
            <div class="cyber-overlay">
                <h3 style="color:#00ffcc; margin:0; font-size: 22px; font-weight:900; text-shadow: 2px 2px 5px black;">AI Autonomous Drive</h3>
                <p style="color:#ddd; margin:0; font-size:14px; font-weight:bold; text-shadow: 1px 1px 3px black; margin-top:5px;">Neural Network Integration Ready</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_img2:
        st.markdown("""
        <div class="cyber-image-card">
            <img class="cyber-image-bg" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1920&q=80" />
            <div class="cyber-overlay">
                <h3 style="color:#00ffcc; margin:0; font-size: 22px; font-weight:900; text-shadow: 2px 2px 5px black;">Cyber-Performance Metrics</h3>
                <p style="color:#ddd; margin:0; font-size:14px; font-weight:bold; text-shadow: 1px 1px 3px black; margin-top:5px;">Real-time Telemetry & Tracking</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border:1px solid #00ffcc; box-shadow: 0 0 10px #00ffcc;'><h3 style='color:#00ffcc; text-shadow: 0 0 15px #00ffcc; text-align:center; font-weight: 900; letter-spacing: 2px;'>⚡ ALL SYSTEMS NOMINAL. STANDING BY. ⚡</h3>", unsafe_allow_html=True)
