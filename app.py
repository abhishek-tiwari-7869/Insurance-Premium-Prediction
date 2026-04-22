st.set_page_config(page_title="Insurance App")

st.title(" Insurance Premium Predictor")
st.write("Abhishek tiwari ")
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Insurance Premium Predictor")

st.write("Enter your details below:")

# Inputs
age = st.slider("Age", 18, 65)
diabetes = st.selectbox("Diabetes", [0,1])
bp = st.selectbox("Blood Pressure Problems", [0,1])
transplant = st.selectbox("Any Transplants", [0,1])
chronic = st.selectbox("Chronic Disease", [0,1])
height = st.number_input("Height (cm)", min_value=100.0)
weight = st.number_input("Weight (kg)", min_value=30.0)
allergy = st.selectbox("Allergies", [0,1])
cancer = st.selectbox("Family Cancer History", [0,1])
surgeries = st.slider("Number of Surgeries", 0, 3)

# Feature Engineering
bmi = weight / ((height/100)**2)
risk_score = diabetes + bp + transplant + chronic + surgeries

st.write(f"Calculated BMI: {bmi:.2f}")

# Prediction
if st.button("Predict Premium"):
    features = np.array([[age, diabetes, bp, transplant, chronic,
                          height, weight, allergy, cancer, surgeries,
                          bmi, risk_score]])

    prediction = model.predict(features)

    st.success(f"Estimated Premium: ₹{int(prediction[0])}")

st.success(f"Estimated Premium: ₹{int(prediction[0])}")

if risk_score >= 3:
    st.warning(" High Risk")
else:
    st.info(" Low Risk")





