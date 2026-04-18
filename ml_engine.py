import pandas as pd
import datetime
import warnings
warnings.filterwarnings('ignore')

# --- Market Intelligence: Real Base Prices (New Car Price in 2026) ---
def get_brand_market_value(car_name):
    name = str(car_name).lower()
    if any(x in name for x in ['porsche', 'lamborghini', 'ferrari', 'rolls-royce', 'bentley']): return 25000000
    if any(x in name for x in ['range rover', 's-class', '7 series', 'defender', 'maybach']): return 15000000
    if any(x in name for x in ['e-class', '5 series', 'a6', 'xc90', 'q7', 'x5', 'gle', 'macan']): return 8000000
    if any(x in name for x in ['audi', 'bmw', 'mercedes', 'volvo', 'jaguar']): return 4800000
    if any(x in name for x in ['fortuner', 'camry', 'kodiaq', 'tiguan', 'gloster', 'ev6', 'ioniq 5', 'endeavour']): return 4000000
    if any(x in name for x in ['innova', 'hector', 'harrier', 'safari', 'xuv700', 'compass', 'octavia', 'scorpio']): return 2200000
    if any(x in name for x in ['creta', 'seltos', 'thar', 'city', 'civic', 'verna', 'slavia', 'virtus', 'taigun', 'kushaq', 'grand vitara']): return 1500000
    if any(x in name for x in ['nexon', 'venue', 'sonet', 'brezza', 'xuv300', 'bolero', 'punch', 'fronx', 'ecosport']): return 1000000
    if any(x in name for x in ['swift', 'baleno', 'i20', 'wagonr', 'tiago', 'ignis', 'altroz', 'dzire']): return 700000
    
    return 800000 # Default fallback

# Main Prediction Engine
def train_and_predict(car_name, year, km, fuel, owner, transmission, engine_cc=1500, power_bhp=100, top_speed=180, battery_kwh=0, state="", city=""):
    current_year = 2026 
    base_price = get_brand_market_value(car_name)
    
    # 1. Age Calculation
    age = current_year - year
    if age < 0: age = 0
    
    # Pehle saal 15% drop, uske baad linear drop
    depreciated_price = base_price
    if age > 0:
        if age <= 1:
            depreciated_price *= 0.85
        else:
            factor = 0.85 - (0.08 * (age - 1))
            if factor < 0.20: factor = 0.20 
            depreciated_price = base_price * factor

    # 🔥 STRICT KILOMETER DEPRECIATION 
    expected_km = age * 10000
    if km > expected_km:
        extra_km = km - expected_km
        km_penalty = (0.90) ** (extra_km / 10000)
        depreciated_price *= km_penalty
    elif km < expected_km and age > 0:
        depreciated_price *= 1.10

    # 2. RTO & Fuel Policy
    if fuel == "Diesel" and age >= 10:
        depreciated_price *= 0.40 # 10 saal Diesel ban policy
        
    if age >= 15:
        # Scrap value after 15 years
        if base_price > 5000000:
            return 250000 
        else:
            return 60000 

    # 3. Owner & Transmission Factors
    owner_map = {"First": 1.0, "Second": 0.85, "Third": 0.70, "Fourth": 0.55}
    depreciated_price *= owner_map.get(owner, 0.50)
    
    if transmission == "Automatic":
        depreciated_price *= 1.05 

    # 4. Engine Specs Factors (Background logic)
    if engine_cc > 2500 or power_bhp > 180:
        if age < 5: depreciated_price *= 1.05 

    # 5. Electric vehicle / Battery adjustment
    # If the vehicle is electric, the battery pack represents a material portion of value.
    # Heuristic: per-kWh replacement value (INR); battery health degrades ~3%/year, floor at 50%.
    try:
        bk = float(battery_kwh or 0)
    except Exception:
        bk = 0.0

    if str(fuel).lower() == 'electric' and bk > 0:
        # Choose a conservative per-kWh value (INR). Adjust if you want more/less sensitivity.
        per_kwh_value = 25000.0  # INR per kWh (heuristic)

        # Battery health factor: degrade ~3% per year, min 0.5 (50% health)
        health_factor = max(0.5, 1.0 - 0.03 * age)

        # Estimated remaining battery value
        battery_value = bk * per_kwh_value * health_factor

        # Add a portion of battery value to depreciated price (buyer values used battery but not full replacement cost)
        depreciated_price += battery_value * 0.75

        # Additional policy: older EVs (>8y) see steeper battery anxiety discounts
        if age >= 8:
            depreciated_price *= 0.85

    # 6. Location/State & City adjustments (India-specific heuristics)
    # The user requested per-location pricing sensitivity. We apply a conservative
    # multiplier by state and a small city-level tweak for well-known metros.
    try:
        st = str(state).strip()
    except Exception:
        st = ""

    # Basic buckets: metros (higher prices), standard (no change), lower-tier states (slight discount)
    metros = {"Delhi", "Maharashtra", "Karnataka", "Tamil Nadu", "West Bengal", "Gujarat"}
    lower_tier = {"Bihar", "Jharkhand", "Chhattisgarh", "Odisha", "Assam", "Nagaland", "Manipur", "Mizoram", "Tripura", "Meghalaya"}

    state_factor = 1.0
    if st in metros:
        state_factor = 1.08
    elif st in lower_tier:
        state_factor = 0.93
    else:
        state_factor = 1.00

    # City-level micro-adjustments for big metros when the city name contains known terms
    city_factor = 1.0
    try:
        ct = str(city).lower()
    except Exception:
        ct = ""

    if any(x in ct for x in ["mumbai", "bombay", "delhi", "bangalore", "bengaluru", "kolkata", "chennai", "gurgaon", "noida", "hyderabad"]):
        city_factor = 1.02

    depreciated_price = depreciated_price * state_factor * city_factor

    scrap_value = 50000 if base_price < 2000000 else 150000

    return int(max(depreciated_price, scrap_value))
