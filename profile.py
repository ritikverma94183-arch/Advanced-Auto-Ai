import streamlit as st
import sqlite3

def show_profile():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#00ffcc; text-align:center; font-weight:900; text-shadow: 0 0 15px #00ffcc; letter-spacing: 2px;'>👤 AGENT IDENTITY CARD</h1>", unsafe_allow_html=True)
    
    username = st.session_state.get("username", "Unknown")
    
    # Fetch Data from DB
    conn = sqlite3.connect('secure_auth.db')
    c = conn.cursor()
    c.execute("SELECT * FROM system_agents WHERE username=?", (username,))
    user_data = c.fetchone()
    conn.close()

    if user_data:
        _, email, phone, dob, _ = user_data
    else:
        email, phone, dob = "CLASSIFIED", "CLASSIFIED", "CLASSIFIED"

    profile_html = f"""
    <div style="background: rgba(10, 15, 25, 0.85); backdrop-filter: blur(10px); border: 2px solid #00ffcc; border-radius: 15px; padding: 40px; margin: 20px auto; max-width: 600px; box-shadow: 0 0 30px rgba(0,255,204,0.2);">
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
    """
    st.markdown(profile_html, unsafe_allow_html=True)