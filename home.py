import streamlit as st
import db

def show_home():
    # Dual Banner Section
    dual_banner_html = (
        "<div style='display: flex; position: relative; border-radius: 15px; overflow: hidden; margin-bottom: 30px; border: 1px solid #444; height: 350px;'>"
        "<div style='flex: 1; background-image: url(\"https://media.istockphoto.com/id/1208725980/photo/toyota-fortuner.jpg?s=612x612&w=0&k=20&c=wrf44J-UUcPKTCXCz0ixtWuS05yzgRGRgWHFqZZcfr0=\"); background-size: cover; background-position: center;'>"
        "<div style='width: 100%; height: 100%; background: rgba(0,0,0,0.6);'></div></div>"
        "<div style='flex: 1; background-image: url(\"https://www.hdcarwallpapers.com/walls/lamborghini_huracan_sto_lamborghini_urus_4k_8k-HD.jpg\"); background-size: cover; background-position: center;'>"
        "<div style='width: 100%; height: 100%; background: rgba(0,0,0,0.6);'></div></div>"
        "<div class='float-anim' style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; z-index: 10; width: 90%; pointer-events: none;'>"
        "<h1 class='glow-title' style='color: #00ffcc; font-size: 60px; margin-bottom: 5px; font-weight: bold; text-shadow: 3px 3px 10px black;'>Advanced Auto AI</h1>"
        "<p style='color: #ffffff; font-size: 24px; text-shadow: 2px 2px 8px black;'>The Ultimate Dealership & Valuation Command Center</p>"
        "</div></div>"
    )
    st.markdown(dual_banner_html, unsafe_allow_html=True)
    
    # Fetch Dealership Data
    df = db.get_all_cars()
    total_cars = len(df) if not df.empty else 0
    total_value = df['Price_INR'].sum() if not df.empty and 'Price_INR' in df.columns else 0
    
    st.markdown("### 📊 Real-Time Dealership Telemetry")
    
    c1, c2, c3 = st.columns(3)
    c_style = "padding:20px; border-radius:10px; background-color:#1e1e2e; text-align:center; border: 1px solid #333;"
    
    c1.markdown(f"<div class='hover-card' style='{c_style}'><h3 style='color:#888; margin:0;'>Active Inventory</h3><h1 style='color:#00ffcc; margin:10px 0;'>{total_cars}</h1><p style='color:#aaa; margin:0;'>Vehicles Loaded</p></div>", unsafe_allow_html=True)
    
    val_cr = total_value / 10000000 if total_cars > 0 else 0
    c2.markdown(f"<div class='hover-card' style='{c_style}'><h3 style='color:#888; margin:0;'>Portfolio Value</h3><h1 style='color:#ff4b4b; margin:10px 0;'>₹ {val_cr:,.2f} Cr</h1><p style='color:#aaa; margin:0;'>Dealership Asset</p></div>", unsafe_allow_html=True)
    
    avg_price_l = (total_value / total_cars / 100000) if total_cars > 0 else 0
    c3.markdown(f"<div class='hover-card' style='{c_style}'><h3 style='color:#888; margin:0;'>Inventory Avg</h3><h1 style='color:#ffc107; margin:10px 0;'>₹ {avg_price_l:,.1f} L</h1><p style='color:#aaa; margin:0;'>Average Unit Price</p></div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚙 Showroom Fleet Categories")
    pic_col1, pic_col2 = st.columns(2)
    
    with pic_col1:
        indian_card_html = (
            "<div class='hover-card' style='background-color:#1e1e2e; padding:15px; border-radius:12px; border:1px solid #3b3b4f; text-align:center; box-shadow: 0 4px 10px rgba(0,0,0,0.5);'>"
            "<h3 style='color:#ffffff; margin-bottom:10px;'>Popular Indian Fleet 🇮🇳</h3>"
            "<div class='img-container'>"
            "<img class='img-zoom' src='https://w0.peakpx.com/wallpaper/346/609/HD-wallpaper-in-pics-tata-harrier-dark-edition-launched-check-out-how-the-all-black-suv-looks-like.jpg' style='width:100%; height:250px; object-fit:cover;'>"
            "</div>"
            "<p style='color:#a0a0b0; font-size:14px;'>Top performing SUVs like TATA Harrier Dark, Toyota Fortuner, and Mahindra Thar.</p>"
            "</div>"
        )
        st.markdown(indian_card_html, unsafe_allow_html=True)
        
    with pic_col2:
        luxury_card_html = (
            "<div class='hover-card' style='background-color:#1e1e2e; padding:15px; border-radius:12px; border:1px solid #3b3b4f; text-align:center; box-shadow: 0 4px 10px rgba(0,0,0,0.5);'>"
            "<h3 style='color:#ffffff; margin-bottom:10px;'>Dream Luxury Segment 👑</h3>"
            "<div class='img-container'>"
            "<img class='img-zoom' src='https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?q=80&w=800&auto=format&fit=crop' style='width:100%; height:250px; object-fit:cover;'>"
            "</div>"
            "<p style='color:#a0a0b0; font-size:14px;'>Premium collections including Lamborghini, Porsche, BMW, and Mercedes-Benz.</p>"
            "</div>"
        )
        st.markdown(luxury_card_html, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### ⚡ Quick System Overview")
    st.info("👈 Use the **Command Center** menu on the left to navigate.")
    
    st.markdown("""
    * **🔮 AI Price Predictions:** Get market-accurate, real-time valuations & professional PDF reports.
    * **⚔️ Compare Vehicles:** Head-to-head advanced performance battle (Winner/Loser trophies 🏆).
    * **🗄️ Database (Virtual Showroom):** Style Cards view with Engine Specs & Table Data manager.
    * **🛰️ Live Dashboard:** Visual analytics and graphs of your dealership data.
    """)