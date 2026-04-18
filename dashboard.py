import streamlit as st
import db
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def show_dashboard():
    st.markdown("<h1 class='glow-title' style='font-size: 45px; text-align: center; margin-bottom: 5px; margin-top:20px;'>🛰️ Live Market Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title' style='text-align: center; font-size: 18px; margin-bottom: 40px;'>Real-time telemetry and dealership portfolio insights.</p>", unsafe_allow_html=True)

    df = db.get_all_cars()
    
    if df.empty:
        st.warning("⚠️ No data available in the database. Please add vehicles first.")
        return

    # --- 1. KPI METRIC CARDS ---
    total_cars = len(df)
    total_val = df['Price_INR'].sum() if 'Price_INR' in df.columns else 0
    avg_price = total_val / total_cars if total_cars > 0 else 0
    ev_count = len(df[df['Fuel_Type'] == 'Electric']) if 'Fuel_Type' in df.columns else 0

    col1, col2, col3, col4 = st.columns(4)
    box_style = "background: rgba(20,20,30,0.85); border: 2px solid #00ffcc; padding: 20px; border-radius: 15px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.6); backdrop-filter: blur(5px);"
    
    col1.markdown(f"<div class='hover-card' style='{box_style}'><h3 style='color:#ccc; margin:0; font-size:16px;'>Active Inventory</h3><h2 style='color:#00ffcc; margin:10px 0; font-size:32px; text-shadow: 0 0 10px #00ffcc;'>{total_cars}</h2></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='hover-card' style='{box_style}'><h3 style='color:#ccc; margin:0; font-size:16px;'>Portfolio Value</h3><h2 style='color:#ff4b4b; margin:10px 0; font-size:32px; text-shadow: 0 0 10px #ff4b4b;'>₹ {total_val/10000000:.2f} Cr</h2></div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='hover-card' style='{box_style}'><h3 style='color:#ccc; margin:0; font-size:16px;'>Average Price</h3><h2 style='color:#ffc107; margin:10px 0; font-size:32px; text-shadow: 0 0 10px #ffc107;'>₹ {avg_price/100000:.1f} L</h2></div>", unsafe_allow_html=True)
    col4.markdown(f"<div class='hover-card' style='{box_style}'><h3 style='color:#ccc; margin:0; font-size:16px;'>Electric Fleet (EV)</h3><h2 style='color:#0088ff; margin:10px 0; font-size:32px; text-shadow: 0 0 10px #0088ff;'>{ev_count} ⚡</h2></div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 2. VISUAL CHARTS (ROW 1) ---
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("<h3 style='color: #00ffcc; text-align: center; text-shadow: 2px 2px 5px black;'>⛽ Fuel Type Distribution</h3>", unsafe_allow_html=True)
        fuel_counts = df['Fuel_Type'].value_counts().reset_index()
        fuel_counts.columns = ['Fuel_Type', 'Count']
        
        fig1 = px.pie(fuel_counts, values='Count', names='Fuel_Type', hole=0.6, 
                      color_discrete_sequence=['#00ffcc', '#ff4b4b', '#0088ff', '#ffc107'])
        fig1.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
        fig1.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0.6)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        st.markdown("<h3 style='color: #00ffcc; text-align: center; text-shadow: 2px 2px 5px black;'>🏆 Top Brands by Volume</h3>", unsafe_allow_html=True)
        # Extract Brand from Car Name (First word)
        df['Brand'] = df['Car_Name'].apply(lambda x: str(x).split()[0])
        brand_counts = df['Brand'].value_counts().head(7).reset_index()
        brand_counts.columns = ['Brand', 'Count']
        
        fig2 = px.bar(brand_counts, x='Brand', y='Count', text='Count',
                      color='Count', color_continuous_scale=['#0088ff', '#00ffcc'])
        fig2.update_traces(textfont_size=16, textangle=0, textposition="outside", cliponaxis=False)
        fig2.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0.6)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20), xaxis_title="", yaxis_title="Number of Cars", coloraxis_showscale=False)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. VISUAL CHARTS (ROW 2) ---
    c3, c4 = st.columns(2)

    with c3:
        st.markdown("<h3 style='color: #00ffcc; text-align: center; text-shadow: 2px 2px 5px black;'>📅 Market Value vs Model Year</h3>", unsafe_allow_html=True)
        fig3 = px.scatter(df, x='Model_Year', y='Price_INR', color='Fuel_Type', size='Power_BHP', hover_name='Car_Name',
                          color_discrete_sequence=['#00ffcc', '#ff4b4b', '#0088ff', '#ffc107'], size_max=25)
        fig3.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0.6)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20), xaxis_title="Manufacturing Year", yaxis_title="Price (INR)")
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        st.markdown("<h3 style='color: #00ffcc; text-align: center; text-shadow: 2px 2px 5px black;'>⚡ Engine (CC) vs Power (BHP)</h3>", unsafe_allow_html=True)
        fig4 = px.scatter(df, x='Engine_Capacity_cc', y='Power_BHP', color='Transmission', hover_name='Car_Name',
                          color_discrete_sequence=['#ff4b4b', '#0088ff'], size='Top_Speed_kmph', size_max=20)
        fig4.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0.6)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20), xaxis_title="Engine Capacity (CC)", yaxis_title="Power (BHP)")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("<br><hr style='border: 1px solid #444;'><p style='text-align:center; color:#00ffcc; font-weight:bold; text-shadow: 0 0 5px #00ffcc;'>Live Telemetry System Active 🟢</p>", unsafe_allow_html=True)