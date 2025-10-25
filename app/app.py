# app/app.py
import streamlit as st
import numpy as np
import joblib
import os

# -------------------------
# Helper: robust path loader
# -------------------------
def load_artifact(fname):
    base = os.path.dirname(__file__)            # app/ directory
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
    st.error(f"Failed to load model artifacts: {e}")
    st.stop()

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Crop Recommender", layout="centered")
st.title("🌾 Crop Recommendation System")
st.write("Enter soil and weather parameters — the model will suggest the best crop to grow.")

with st.form("input_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("Nitrogen (N)", min_value=0.0, value=90.0, step=1.0)
        P = st.number_input("Phosphorus (P)", min_value=0.0, value=42.0, step=1.0)
        K = st.number_input("Potassium (K)", min_value=0.0, value=43.0, step=1.0)
    with col2:
        temperature = st.number_input("Temperature (°C)", value=20.8, format="%.1f")
        humidity = st.number_input("Humidity (%)", value=82.0, format="%.1f")
        ph = st.number_input("pH value", min_value=0.0, max_value=14.0, value=6.5, format="%.2f")
    with col3:
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=200.0, step=1.0)
        st.markdown("**Tip:** Use realistic local values for better suggestions.")
    submit = st.form_submit_button("Predict")

if submit:
    # prepare input in same feature order used in training
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    features_scaled = scaler.transform(features)   # same scaler used in training

    # prediction + probability
    pred_int = rf.predict(features_scaled)[0]
    pred_crop = le.inverse_transform([pred_int])[0]

    # if rf supports predict_proba
    if hasattr(rf, "predict_proba"):
        proba = rf.predict_proba(features_scaled).max()
        st.success(f"Recommended crop: 🌱 **{pred_crop}** (confidence: {proba:.2%})")
    else:
        st.success(f"Recommended crop: 🌱 **{pred_crop}**")

    # small explainability: show model's feature importances and the values provided
    try:
        import pandas as pd
        fi = pd.Series(rf.feature_importances_, index=["N","P","K","temperature","humidity","ph","rainfall"])
        st.subheader("Why this crop?")
        st.write("Feature importances (overall):")
        st.bar_chart(fi.sort_values(ascending=False))

        st.write("Your input values:")
        st.table(pd.DataFrame(features, columns=["N","P","K","temperature","humidity","ph","rainfall"]))
    except Exception:
        # non-blocking: if plotting fails, ignore
        pass

st.markdown("---")
st.caption("Model trained on dataset from Kaggle. This is a suggestion system — verify with local agronomy advice.")