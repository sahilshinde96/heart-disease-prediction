import streamlit as st
import numpy as np
import pickle

# Load model & scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details:")

# Continuous inputs
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=0, max_value=120)
    restingBP = st.number_input("Resting Blood Pressure", min_value=0)
    cholesterol = st.number_input("Cholesterol", min_value=0)
with col2:
    maxHR = st.number_input("Max Heart Rate", min_value=0)
    oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0)
    fastingBS = st.number_input("Fasting Blood Sugar (mg/dl)", min_value=0)

# Categorical inputs
col1, col2 = st.columns(2)
with col1:
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain = st.selectbox("Chest Pain Type", ["ASY", "ATA", "NAP", "TA"])
    resting_ecg = st.selectbox("Resting ECG", ["LVH", "Normal", "ST"])
with col2:
    exercise = st.selectbox("Exercise Angina", ["No", "Yes"])
    st_slope = st.selectbox("ST Slope", ["Down", "Flat", "Up"])

# Convert categorical to one-hot encoding
sex_m = 1 if sex == "Male" else 0
exercise_y = 1 if exercise == "Yes" else 0

# One-hot encode ChestPainType (ASY is baseline)
chest_ata = 1 if chest_pain == "ATA" else 0
chest_nap = 1 if chest_pain == "NAP" else 0
chest_ta = 1 if chest_pain == "TA" else 0

# One-hot encode RestingECG (LVH is baseline)
resting_normal = 1 if resting_ecg == "Normal" else 0
resting_st = 1 if resting_ecg == "ST" else 0

# One-hot encode ST_Slope (Down is baseline)
slope_flat = 1 if st_slope == "Flat" else 0
slope_up = 1 if st_slope == "Up" else 0

# Predict button
if st.button("Predict", key="predict_btn"):
    # Create input array with all 15 features in correct order
    input_data = np.array([[
        age, restingBP, cholesterol, fastingBS, maxHR, oldpeak,
        sex_m, chest_ata, chest_nap, chest_ta,
        resting_normal, resting_st, exercise_y, slope_flat, slope_up
    ]])
    
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ High risk of Heart Disease")
    else:
        st.success("✅ Low risk of Heart Disease")