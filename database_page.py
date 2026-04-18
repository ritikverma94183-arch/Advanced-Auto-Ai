import streamlit as st
import db
import pandas as pd

def show_db_page():
    # 🔥 ADVANCED SHOWROOM ANIMATIONS CSS
    st.markdown("""
    <style>
    .fade-in-up {
        animation: fadeInUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .hover-card {
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .hover-card:hover {
        transform: translateY(-10px) scale(1.03);
        border-color: #00ffcc !important;
        box-shadow: 0 15px 30px rgba(0, 255, 204, 0.25) !important;
        z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🗄️ Premium Virtual Showroom")
    st.write("Manage your dealership inventory and view vehicles in the Virtual Showroom.")
    
    default_car_list = [
        'Maruti Suzuki Swift', 'Hyundai Creta', 'Tata Nexon', 'Toyota Fortuner', 
        'Mahindra Thar', 'Honda City', 'Kia Seltos', 'BMW 3 Series', 'Audi A4', 
        'Mercedes-Benz C-Class', 'Porsche 911', 'Lamborghini Urus', 'Range Rover'
    ]
    
    # 3 Tabs (Showroom, Table, Add Car)
    tab1, tab2, tab3 = st.tabs(["🖼️ Virtual Showroom", "📊 Data Table View", "➕ Add Custom Vehicle"])
    
    df = db.get_all_cars()

    # --- TAB 1: VIRTUAL SHOWROOM (Premium Animated Cards View) ---
    with tab1:
        if not df.empty:
            search_gal = st.text_input("🔍 Search Showroom (e.g., Audi, Fortuner, Diesel)...", key="search_gal")
            display_df = df
            if search_gal:
                # Search across all columns
                display_df = df[df.astype(str).apply(lambda x: x.str.contains(search_gal, case=False)).any(axis=1)]
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # 🔥 START ANIMATED CONTAINER
            st.markdown("<div class='fade-in-up'>", unsafe_allow_html=True)
            
            # 3 Columns ka Grid Setup
            cols = st.columns(3)
            
            for index, row in display_df.iterrows():
                # Safely fetching values
                name = row.get('Car_Name', 'Unknown Vehicle')
                price = row.get('Price_INR', 0)
                year = row.get('Model_Year', '-')
                fuel = row.get('Fuel_Type', '-')
                trans = row.get('Transmission', '-')
                cc = row.get('Engine_Capacity_cc', '-')
                bhp = row.get('Power_BHP', '-')
                km = row.get('Kilometers_Driven', 0)
                battery = row.get('Battery_Capacity_kWh', 0)
                
                # 🔥 Premium HTML Card with .hover-card Class
                card_html = f"""
                <div class="hover-card" style="background-color:#1e1e2e; padding:20px; border-radius:12px; border:1px solid #3b3b4f; margin-bottom:20px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);">
                    <h3 style="color:#00ffcc; margin-top:0px; margin-bottom:8px; font-size:20px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{name}</h3>
                    <div style="color:#a0a0b0; font-size:13px; margin-bottom:12px;">
                        🗓️ {year} &nbsp;|&nbsp; ⛽ {fuel} &nbsp;|&nbsp; ⚙️ {trans}
                    </div>
                    <h2 style="color:#ffffff; margin:0px; font-size:24px;">₹ {price:,.0f}</h2>
                    <div style="color:#7a7a8c; font-size:12px; margin-top:5px;">Driven: {km:,} km</div>
                    <hr style="border:0.5px solid #3b3b4f; margin:15px 0px;">
                    <div style="color:#cccccc; font-size:13px; display:flex; justify-content:space-between; font-weight:bold;">
                        <span>⚡ {bhp} BHP</span>
                        <span>🔧 {cc} CC</span>
                    </div>
                </div>
                """
                # Display in the correct column
                cols[index % 3].markdown(card_html, unsafe_allow_html=True)
                
            st.markdown("</div>", unsafe_allow_html=True) # End Animated Container
            
            if display_df.empty:
                st.warning("No vehicles match your search criteria.")
        else:
            st.info("No cars in the showroom yet! Add some from the 'Add Custom Vehicle' tab.")

    # --- TAB 2: DATA TABLE VIEW ---
    with tab2:
        if not df.empty:
            search_tab = st.text_input("🔍 Filter Table Data...", key="search_tab")
            display_df_tab = df
            if search_tab:
                display_df_tab = df[df.astype(str).apply(lambda x: x.str.contains(search_tab, case=False)).any(axis=1)]
                
            st.dataframe(display_df_tab, use_container_width=True)
            
            st.markdown("---")
            st.markdown("### 🗑️ Remove Vehicle from Database")
            del_col1, del_col2 = st.columns([3, 1])
            delete_idx = del_col1.selectbox("Select Index Number (from left side of table) to Delete:", display_df_tab.index.tolist())
            
            if del_col2.button("🗑️ Delete Selected Record", type="primary"):
                if db.delete_car(delete_idx):
                    st.success(f"✅ Record successfully removed from database!")
                    st.rerun()
        else:
            st.error("Database CSV file not found or empty! Please add a car from the next tab.")
            
    # --- TAB 3: ADD CUSTOM VEHICLE ---
    with tab3:
        st.markdown("### ➕ Add a New Vehicle to Showroom")
        
        existing_cars = []
        if not df.empty and 'Car_Name' in df.columns:
            existing_cars = df['Car_Name'].unique().tolist()
        final_dropdown_list = sorted(list(set(existing_cars + default_car_list)))
        
        with st.form("add_car_form"):
            col1, col2 = st.columns(2)
            new_name = col1.selectbox("Car Brand/Model", final_dropdown_list)
            new_year = col2.number_input("Model Year", 1996, 2026, 2024)

            col3, col4 = st.columns(2)
            new_km = col3.number_input("Kilometers Driven", 0, 500000, 5000)
            new_price = col4.number_input("Set Custom Deal Price (₹)", 10000, 500000000, 1500000, step=50000)

            # --- Specs & Details (fixed/non-editable) ---
            # Determine sensible defaults from the existing DB row if available
            default_cc, default_bhp, default_speed = 1500, 120, 180
            default_fuel, default_trans, default_battery = "Petrol", "Manual", 0
            if not df.empty and 'Car_Name' in df.columns:
                match = df[df['Car_Name'] == new_name]
                if not match.empty:
                    r = match.iloc[0]
                    try:
                        if 'Engine_Capacity_cc' in r and r['Engine_Capacity_cc'] is not None:
                            default_cc = int(r['Engine_Capacity_cc'])
                    except Exception:
                        pass
                    try:
                        if 'Power_BHP' in r and r['Power_BHP'] is not None:
                            default_bhp = int(r['Power_BHP'])
                    except Exception:
                        pass
                    try:
                        if 'Top_Speed_kmph' in r and r['Top_Speed_kmph'] is not None:
                            default_speed = int(r['Top_Speed_kmph'])
                    except Exception:
                        pass
                    try:
                        if 'Fuel_Type' in r and r['Fuel_Type']:
                            default_fuel = r['Fuel_Type']
                    except Exception:
                        pass
                    try:
                        if 'Transmission' in r and r['Transmission']:
                            default_trans = r['Transmission']
                    except Exception:
                        pass
                    try:
                        if 'Battery_Capacity_kWh' in r and r['Battery_Capacity_kWh'] is not None:
                            default_battery = int(r['Battery_Capacity_kWh'])
                    except Exception:
                        pass

            st.markdown("#### Specs & Details (fixed)")
            col_sp1, col_sp2, col_sp3 = st.columns(3)
            col_sp1.number_input("Engine (CC)", 800, 8000, value=default_cc, disabled=True)
            col_sp2.number_input("Power (BHP)", 50, 1500, value=default_bhp, disabled=True)
            col_sp3.number_input("Top Speed (km/h)", 100, 400, value=default_speed, disabled=True)

            col5, col6, col7, col8 = st.columns(4)
            # Fuel and Transmission are fixed (non-editable)
            fuel_options = ["Petrol", "Diesel", "Electric", "CNG"]
            fuel_index = fuel_options.index(default_fuel) if default_fuel in fuel_options else 0
            col5.selectbox("Fuel Type", fuel_options, index=fuel_index, disabled=True)

            # Owner remains selectable
            new_owner = col6.selectbox("Owner Type", ["First", "Second", "Third", "Fourth"])

            trans_options = ["Manual", "Automatic"]
            trans_index = trans_options.index(default_trans) if default_trans in trans_options else 0
            col7.selectbox("Transmission", trans_options, index=trans_index, disabled=True)

            col8.number_input("Battery Capacity (kWh, if Electric)", 0, 200, value=default_battery, disabled=True)

            submit_car = st.form_submit_button("➕ Save to Inventory", type="primary")

            if submit_car:
                new_data = {
                    'Car_Name': new_name, 'Model_Year': new_year, 'Owner_Type': new_owner,
                    'Kilometers_Driven': new_km, 'Fuel_Type': default_fuel, 'Transmission': default_trans,
                    'Price_INR': new_price, 'Engine_Capacity_cc': default_cc,
                    'Power_BHP': default_bhp, 'Top_Speed_kmph': default_speed,
                    'Battery_Capacity_kWh': default_battery
                }
                if db.add_new_car(new_data):
                    st.success(f"✅ {new_name} added to showroom successfully!")
                    st.balloons()