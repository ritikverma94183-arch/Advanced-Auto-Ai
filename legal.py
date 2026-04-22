import streamlit as st

def show_legal():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#00ffcc; text-align:center; font-weight:900; text-shadow: 0 0 15px #00ffcc; letter-spacing: 2px;'>⚖️ LEGAL & COMPLIANCE MATRIX</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc; margin-bottom: 30px;'>System Policies, Data Handling, and Terms of Service</p>", unsafe_allow_html=True)

    # Glassmorphism container CSS
    st.markdown("""
    <style>
    .legal-box {
        background: rgba(10, 15, 25, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 255, 204, 0.4);
        border-radius: 10px;
        padding: 30px;
        color: #ddd;
        line-height: 1.8;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    .legal-box h3 { color: #00ffcc; margin-top: 0; border-bottom: 1px solid #00ffcc; padding-bottom: 10px; }
    .legal-box h4 { color: #fff; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔒 Privacy Policy", "📜 Terms & Conditions"])

    with tab1:
        st.markdown("""
        <div class="legal-box">
            <h3>Privacy Policy</h3>
            <p>Welcome to the Advanced Auto AI terminal. Your privacy is critically important to us. This policy dictates how our system handles data within the matrix.</p>
            <h4>1. Data Collection & Telemetry</h4>
            <p>When you register as a System Agent, we collect standard identification metrics (Username, Email, Date of Birth). When you scan a vehicle using our AI Engine, the hardware specifications are processed to generate market predictions but are not permanently tied to your personal identity.</p>
            <h4>2. Data Security & Encryption</h4>
            <p>All user authentication data is stored in our local, highly secure SQLite database (`secure_auth.db`). Passwords and session states are managed strictly within the application container to prevent unauthorized access.</p>
            <h4>3. Third-Party Sharing</h4>
            <p>Advanced Auto AI does not sell, rent, or share your telemetry data or valuation searches with third-party dealerships, ad networks, or external APIs. This system operates as a closed-loop environment.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="legal-box">
            <h3>Terms & Conditions</h3>
            <p>By accessing the Advanced Auto AI Command Matrix, you agree to comply with the following operational directives.</p>
            <h4>1. System Nature & Accuracy (Academic Disclaimer)</h4>
            <p><b>Notice:</b> Advanced Auto AI is built as a state-of-the-art academic/research project. The AI engine utilizes complex non-linear exponential decay algorithms and real-world RTO tax multipliers to generate predicted vehicle prices. However, these are <i>estimations</i>. The system is not a legally binding financial tool, and we do not guarantee exact real-world dealership outcomes.</p>
            <h4>2. 10/15-Year RTO Scrap Regulations</h4>
            <p>The system automatically enforces local government laws (e.g., Delhi NCR's 10-year diesel scrap policy). Users must acknowledge that regional laws can change, and the system's "Geo-Sync" logic is based on 2026 data models.</p>
            <h4>3. Authorized Use</h4>
            <p>Registered Agents are authorized to use the "Combat Analysis" and "AI Engine Core" for non-commercial, evaluation purposes only. Attempting to reverse-engineer the Core ML Matrix or manipulate the `database.csv` registry is strictly prohibited.</p>
        </div>
        """, unsafe_allow_html=True)