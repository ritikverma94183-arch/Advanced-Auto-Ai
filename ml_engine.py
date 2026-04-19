import pandas as pd
import math
import warnings
import time

warnings.filterwarnings('ignore')

# =====================================================================
# 🚀 CORE NEURAL ENGINE v4.0 - TACTICAL VALUATION MATRIX
# =====================================================================

def get_brand_market_value(car_name):
    """ Classifies vehicle tier and extracts base asset value """
    name = str(car_name).lower()
    
    # [CLASS S] Ultra Luxury / Exotics
    if any(x in name for x in ['porsche', 'lamborghini', 'ferrari', 'rolls-royce']): return 25000000
    # [CLASS A] Premium Luxury
    if any(x in name for x in ['range rover', 's-class', 'defender', 'maybach']): return 15000000
    # [CLASS B] Executive Luxury
    if any(x in name for x in ['e-class', '5 series', 'q7', 'x5', 'macan']): return 8000000
    # [CLASS C] Premium
    if any(x in name for x in ['audi', 'bmw', 'mercedes', 'volvo', 'jaguar']): return 4800000
    # [CLASS D] High-End SUVs & EVs
    if any(x in name for x in ['fortuner', 'camry', 'tiguan', 'ev6', 'endeavour', 'ioniq 5']): return 4000000
    # [CLASS E] Mid-Size SUVs
    if any(x in name for x in ['innova', 'harrier', 'safari', 'xuv700', 'compass']): return 2200000
    # [CLASS F] Compact SUVs / Sedans
    if any(x in name for x in ['creta', 'seltos', 'thar', 'city', 'slavia', 'nexon ev']): return 1500000
    # [CLASS G] Hatchbacks & Micro SUVs
    if any(x in name for x in ['nexon', 'venue', 'sonet', 'brezza', 'punch']): return 1000000
    # [CLASS H] Entry Level
    if any(x in name for x in ['swift', 'baleno', 'i20', 'wagonr', 'tiago']): return 700000
    
    return 800000 # Failsafe Base Value

def train_and_predict(car_name, year, km, fuel, owner, transmission, engine_cc, power_bhp, top_speed, battery_kwh=0, city="Delhi NCR"):
    """ Advanced Multi-Variable Algorithmic Pricing Engine """
    
    # 🖥️ HACKER TERMINAL LOGS (Dikhne me awesome lagega tere VS Code me)
    print(f"\n[SYSTEM] Initializing Neural Valuation for Target: {car_name.upper()}")
    print(f"[TELEMETRY] Scanning Parameters: Model {year} | {km:,} km | Zone: {city}")
    time.sleep(0.2) # Micro-delay for terminal realism

    base_asset_value = get_brand_market_value(car_name)
    age = 2026 - year
    if age < 0: age = 0
    
    computed_price = base_asset_value
    print(f"[CALC] Base Factory Asset Value: INR {base_asset_value:,}")
    
    # 1. 📉 NON-LINEAR EXPONENTIAL DEPRECIATION ALGORITHM
    if age > 0:
        if age <= 1: 
            computed_price *= 0.85 # 15% Instant Roll-out Drop
        else:
            # Advanced Math: A = P * e^(-rt)
            depreciation_factor = max(0.20, 0.85 * math.exp(-0.085 * (age - 1)))
            computed_price = base_asset_value * depreciation_factor

    # 2. ⚙️ DYNAMIC ODOMETER PENALTY MATRIX
    expected_km = age * 11000 # Indian average standard
    if km > expected_km:
        overuse_ratio = (km - expected_km) / 10000
        computed_price *= math.pow(0.91, overuse_ratio) # 9% penalty curve
        print(f"[WARNING] Overuse detected. Applying degradation penalty.")
    elif km < expected_km and age > 0:
        computed_price *= 1.09 # Mint condition bonus

    # 3. 🚨 RTO RULE COMPLIANCE SCANNER
    if fuel == "Diesel" and age >= 10: 
        if "Delhi NCR" in city:
            computed_price *= 0.15  # 10-Yr Diesel Scrap Rule
            print("[CRITICAL ALERT] Delhi NCR 10-Year Diesel Ban Enforced. Value Decimated!")
        else:
            computed_price *= 0.40  
            
    # 4. 🔋 EV BATTERY DEGRADATION LOGIC
    if fuel == "Electric" and battery_kwh > 0:
        if battery_kwh >= 60: 
            computed_price *= 1.15  # High cap bonus
        elif battery_kwh <= 30: 
            computed_price *= 0.85  # Degradation penalty
            print("[ALERT] Low capacity EV battery detected. Adjusting lifespan value.")

    # 5. 💀 15-YEAR SCRAP DIRECTIVE
    if age >= 15: 
        if "Delhi NCR" in city: 
            print("[TERMINATION] 15-Year Rule Active. Scrap Value Applied.")
            return 50000 
        return 250000 if base_asset_value > 5000000 else 60000 

    # 6. 👤 OWNERSHIP DEVALUATION
    owner_map = {"First": 1.0, "Second": 0.82, "Third": 0.65, "Fourth": 0.50}
    computed_price *= owner_map.get(owner, 0.40)
    
    # 7. 🔥 ENTHUSIAST & PERFORMANCE MULTIPLIER
    if transmission == "Automatic": computed_price *= 1.05 
    if engine_cc >= 2000 or power_bhp >= 150:
        if age <= 6: computed_price *= 1.07 

    # 8. 🌍 REGIONAL MARKET MODIFIER (ALL 28 STATES)
    city_modifiers = {
        "Karnataka (Bangalore)": 1.15,            # Highest RTO Tax
        "Kerala": 1.12,                           
        "Telangana / Andhra Pradesh": 1.08,       
        "Maharashtra (Mumbai / Pune)": 1.05,      
        "Tamil Nadu": 1.02,                       
        "Himachal / J&K / Uttarakhand": 1.00,     # Standard
        "Gujarat": 0.98,                          
        "Rajasthan / Punjab / Haryana": 0.97,     
        "Uttar Pradesh / Chandigarh": 0.95,       
        "Madhya Pradesh / Chhattisgarh": 0.95,    
        "Delhi NCR (10-Yr Rule)": 0.92,           # Scrap Policy Drop
        "West Bengal / Odisha": 0.90,             
        "Bihar / Jharkhand": 0.90,                
        "Assam & North East States": 0.90         
    }
    regional_multiplier = city_modifiers.get(city, 1.0)
    computed_price *= regional_multiplier
    print(f"[GEO-SYNC] Applied {city} regional modifier: {regional_multiplier}x")

    final_value = int(max(computed_price, 50000))
    print(f"[SUCCESS] Core Algorithm Complete. Final Output: INR {final_value:,}\n")
    
    return final_value
