import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "https://<api-id>.execute-api.<region>.amazonaws.com/predict"

st.set_page_config(page_title="Fraud Detection", layout="centered")
st.title("💳 Real-Time Fraud Detection")

st.subheader("Transaction Input")

input_data = {}
cols = st.columns(4)

features = ["Time"] + [f"V{i}" for i in range(1,29)] + ["Amount"]

for i, f in enumerate(features):
    with cols[i % 4]:
        input_data[f] = st.number_input(f, value=0.0)

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Predict Fraud"):
    response = requests.post(API_URL, json=input_data).json()

    prob = response["fraud_probability"]
    label = response["fraud_label"]

    st.metric("Fraud Probability", prob)
    st.success("🚨 FRAUD" if label else "✅ LEGIT")

    st.session_state.history.append(prob)

# ---- Charts ----
if st.session_state.history:
    df = pd.DataFrame({
        "Prediction #": range(1, len(st.session_state.history)+1),
        "Fraud Probability": st.session_state.history
    })

    st.subheader("Prediction History")
    fig = px.line(df, x="Prediction #", y="Fraud Probability")
    st.plotly_chart(fig, use_container_width=True)


# Feature Importance (Static Plot)

st.subheader("Feature Importance (XGBoost)")
importance = pd.read_csv("feature_importance.csv")
fig = px.bar(importance, x="importance", y="feature", orientation="h")
st.plotly_chart(fig, use_container_width=True)