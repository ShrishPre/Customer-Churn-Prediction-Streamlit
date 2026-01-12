import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Customer Churn Predictor",page_icon="📉", layout="centered")

# Load model
with open("gb.pkl", "rb") as file:
    data = pickle.load(file)

model = data["model"]
features = data["features"]

st.title("📉 Customer Churn Prediction App")
st.markdown("Predict whether a customer is likely to churn or not.")

st.divider()
st.header("🧾 Customer Information")

# ===================== USER INPUTS =====================

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Has Partner", ["Yes", "No"])
Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method",["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=2000.0)

# ===================== INPUT DATAFRAME =====================

input_dict = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

input_df = pd.DataFrame([input_dict])

# One-hot encode input
input_df = pd.get_dummies(input_df)

# Add missing columns
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

# Ensure correct column order
input_df = input_df[features]


# ===================== PREDICTION =====================

if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer is likely to CHURN (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer is likely to STAY (Probability: {probability:.2f})")

# ===================== FEATURE IMPORTANCE =====================

st.header("📌 Feature Importance")

importances = model.feature_importances_
feature_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False).head(10)

st.bar_chart(feature_df.set_index("Feature"))

st.markdown("---")
st.markdown("👩‍💻 Built by **Shrishti** | Machine Learning Project")