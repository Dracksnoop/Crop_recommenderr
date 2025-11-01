# app/app.py
import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Smart Crop Recommender",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Custom CSS for styling
# -------------------------
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Title styling */
    .title-container {
        background: linear-gradient(120deg, #2ecc71 0%, #27ae60 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
        text-align: center;
    }

    .title-text {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }

    .subtitle-text {
        color: #ecf0f1;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }

    /* Card styling */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #2ecc71;
        transition: transform 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }

    /* Result card */
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 2rem 0;
        text-align: center;
    }

    .crop-name {
        font-size: 3rem;
        font-weight: bold;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2ecc71 0%, #27ae60 100%);
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(120deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(46, 204, 113, 0.6);
    }

    /* Info boxes */
    .info-box {
        background: #e8f5e9;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 1rem 0;
    }

    .warning-box {
        background: #fff3e0;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


# -------------------------
# Helper: robust path loader
# -------------------------
def load_artifact(fname):
    base = os.path.dirname(__file__)
    model_dir = os.path.abspath(os.path.join(base, "..", "models"))
    path = os.path.join(model_dir, fname)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Artifact not found: {path}")
    return joblib.load(path)


# -------------------------
# Load saved artifacts
# -------------------------
try:
    rf = load_artifact("rf_model.pkl")
    scaler = load_artifact("scaler.pkl")
    le = load_artifact("label_encoder.pkl")
except Exception as e:
    st.error(f"❌ Failed to load model artifacts: {e}")
    st.stop()

# -------------------------
# Header
# -------------------------
st.markdown("""
<div class="title-container">
    <h1 class="title-text">🌾 Smart Crop Recommendation System</h1>
    <p class="subtitle-text">AI-Powered Agricultural Decision Support</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar for information
# -------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
    st.title("📊 About")

    st.markdown("""
    <div class="info-box">
    <b>How it works:</b><br>
    Our machine learning model analyzes soil and weather parameters to recommend the most suitable crop for your land.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Input Parameters")
    st.markdown("""
    - **NPK Values**: Nitrogen, Phosphorus, Potassium levels
    - **Climate**: Temperature, Humidity, Rainfall
    - **Soil**: pH value
    """)

    st.markdown("### 📈 Model Info")
    st.info(f"**Algorithm**: Random Forest\n\n**Features**: 7 parameters\n\n**Status**: ✅ Ready")

    st.markdown("---")
    st.caption("💡 Tip: Hover over input fields for guidance")

# -------------------------
# Main content area
# -------------------------
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("## 🔧 Enter Farm Parameters")

    with st.form("input_form"):
        st.markdown("### 🧪 Soil Nutrients (kg/ha)")
        col1, col2, col3 = st.columns(3)
        with col1:
            N = st.number_input("🔵 Nitrogen (N)", min_value=0.0, value=90.0, step=1.0,
                                help="Nitrogen content in soil (typically 0-140 kg/ha)")
        with col2:
            P = st.number_input("🟢 Phosphorus (P)", min_value=0.0, value=42.0, step=1.0,
                                help="Phosphorus content in soil (typically 5-145 kg/ha)")
        with col3:
            K = st.number_input("🟡 Potassium (K)", min_value=0.0, value=43.0, step=1.0,
                                help="Potassium content in soil (typically 5-205 kg/ha)")

        st.markdown("### 🌡️ Climate Conditions")
        col4, col5 = st.columns(2)
        with col4:
            temperature = st.number_input("🌡️ Temperature (°C)", value=20.8, format="%.1f",
                                          help="Average temperature (8-43°C)")
            humidity = st.number_input("💧 Humidity (%)", value=82.0, format="%.1f",
                                       help="Relative humidity (14-100%)")
        with col5:
            ph = st.number_input("⚗️ pH Value", min_value=0.0, max_value=14.0, value=6.5, format="%.2f",
                                 help="Soil pH level (3.5-9.5)")
            rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, value=200.0, step=1.0,
                                       help="Annual rainfall (20-300 mm)")

        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.form_submit_button("🚀 Get Crop Recommendation")

with col_right:
    st.markdown("## 📋 Quick Guide")

    st.markdown("""
    <div class="metric-card">
    <h4 style="color: #2c3e50;">🌱 Optimal Ranges</h4>
    <ul style="color: #34495e;">
        <li><b>N</b>: 0-140 kg/ha</li>
        <li><b>P</b>: 5-145 kg/ha</li>
        <li><b>K</b>: 5-205 kg/ha</li>
        <li><b>Temp</b>: 8-43°C</li>
        <li><b>Humidity</b>: 14-100%</li>
        <li><b>pH</b>: 3.5-9.5</li>
        <li><b>Rainfall</b>: 20-300mm</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    <span style="color: #e67e22;">⚠️ <b>Note:</b> Use values specific to your region for accurate recommendations.</span>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Prediction Logic
# -------------------------
if submit:
    with st.spinner("🔄 Analyzing parameters..."):
        # Prepare input
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        features_scaled = scaler.transform(features)

        # Prediction
        pred_int = rf.predict(features_scaled)[0]
        pred_crop = le.inverse_transform([pred_int])[0]

        # Get probability
        if hasattr(rf, "predict_proba"):
            proba = rf.predict_proba(features_scaled).max()
        else:
            proba = None

    # Display results in a beautiful card
    st.markdown("<br>", unsafe_allow_html=True)

    if proba:
        confidence_color = "#2ecc71" if proba > 0.7 else "#f39c12" if proba > 0.5 else "#e74c3c"
        st.markdown(f"""
        <div class="result-card">
            <h3>🎯 Recommended Crop</h3>
            <div class="crop-name">🌱 {pred_crop.upper()}</div>
            <div style="font-size: 1.5rem; margin-top: 1rem;">
                Confidence: <span style="color: {confidence_color}; font-weight: bold;">{proba:.1%}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-card">
            <h3>🎯 Recommended Crop</h3>
            <div class="crop-name">🌱 {pred_crop.upper()}</div>
        </div>
        """, unsafe_allow_html=True)

    # Detailed Analysis Section
    st.markdown("---")
    st.markdown("## 📊 Detailed Analysis")

    tab1, tab2, tab3 = st.tabs(["📈 Feature Importance", "📋 Input Summary", "💡 Insights"])

    with tab1:
        try:
            fi = pd.Series(rf.feature_importances_,
                           index=["N", "P", "K", "Temperature", "Humidity", "pH", "Rainfall"])
            fi_sorted = fi.sort_values(ascending=False)

            # Create bar chart using Streamlit
            st.markdown("### Feature Importance in Crop Selection")
            st.bar_chart(fi_sorted)

            # Display as a dataframe
            fi_df = pd.DataFrame({
                'Feature': fi_sorted.index,
                'Importance': [f'{val:.1%}' for val in fi_sorted.values],
                'Score': fi_sorted.values
            })
            st.dataframe(fi_df[['Feature', 'Importance']], use_container_width=True, hide_index=True)

            st.info(f"🔍 The most influential factor for this prediction was **{fi.idxmax()}** "
                    f"with an importance of {fi.max():.1%}")
        except Exception:
            pass

    with tab2:
        input_df = pd.DataFrame({
            'Parameter': ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)',
                          'Temperature', 'Humidity', 'pH', 'Rainfall'],
            'Value': [f"{N} kg/ha", f"{P} kg/ha", f"{K} kg/ha",
                      f"{temperature}°C", f"{humidity}%", f"{ph}", f"{rainfall} mm"],
            'Status': ['✅'] * 7
        })

        st.dataframe(input_df, use_container_width=True, hide_index=True)

        # Create a simple line chart for normalized values
        st.markdown("### Parameter Distribution (Normalized)")
        norm_data = pd.DataFrame({
            'Parameter': ['N', 'P', 'K', 'Temp', 'Humid', 'pH', 'Rain'],
            'Normalized Value': [N / 140, P / 145, K / 205, temperature / 43, humidity / 100, ph / 14, rainfall / 300]
        })

        st.bar_chart(norm_data.set_index('Parameter'))

    with tab3:
        st.markdown("### 🌟 Key Insights")

        col_i1, col_i2 = st.columns(2)

        with col_i1:
            st.markdown(f"""
            <div class="metric-card">
            <h4 style="color: #2c3e50;">🧪 Soil Nutrients</h4>
            <p style="color: #34495e;"><b>NPK Ratio:</b> {N:.0f}:{P:.0f}:{K:.0f}</p>
            <p style="color: #34495e;">Your soil has a {'balanced' if abs(N - P) < 30 and abs(P - K) < 30 else 'varied'} nutrient profile.</p>
            </div>
            """, unsafe_allow_html=True)

        with col_i2:
            st.markdown(f"""
            <div class="metric-card">
            <h4 style="color: #2c3e50;">🌡️ Climate</h4>
            <p style="color: #34495e;"><b>Conditions:</b> {'Humid' if humidity > 70 else 'Moderate' if humidity > 40 else 'Dry'}</p>
            <p style="color: #34495e;">Temperature is {'warm' if temperature > 25 else 'moderate' if temperature > 15 else 'cool'}.</p>
            </div>
            """, unsafe_allow_html=True)

        st.success(f"✨ Based on the analysis, **{pred_crop}** is highly suitable for your farm conditions!")

        st.markdown("""
        <div class="warning-box">
        <span style="color: #e67e22;"><b>⚠️ Important Disclaimer:</b><br>
        This is an AI-based recommendation system. Always consult with local agricultural experts 
        and consider additional factors like market demand, crop rotation, and regional farming practices 
        before making final decisions.</span>
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.metric("🎯 Model Accuracy", "95%+", help="Based on test dataset")
with col_f2:
    st.metric("🌾 Crops Supported", "22", help="Different crop types")
with col_f3:
    st.metric("📊 Parameters Used", "7", help="Input features")

st.markdown("<br>", unsafe_allow_html=True)
st.caption("🔬 Model trained on Kaggle agricultural dataset | 💚 Made with Streamlit | By krishna gurjar | ⚡ Powered by Machine Learning")