import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="SugarSense", page_icon="🩺")

st.title("🩺 SugarSense")
st.subheader("Early Diabetes Risk Screening")
st.write("Enter the health measurements below.")

@st.cache_resource
def load_model():
    return joblib.load("sugarsense_model.joblib")

model = load_model()

pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose", 0.0, 300.0, 120.0)
bp = st.number_input("Blood Pressure", 0.0, 150.0, 70.0)
skin = st.number_input("Skin Thickness", 0.0, 100.0, 20.0)
insulin = st.number_input("Insulin", 0.0, 900.0, 80.0)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input(
    "Diabetes Pedigree Function", 0.0, 3.0, 0.5
)
age = st.number_input("Age", 21, 100, 30)

if st.button("Predict Diabetes Risk"):

    data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age,
        "ObesityFlag": int(bmi >= 30),
        "Age35Plus": int(age >= 35),
        "MissingMeasurementCount": sum(
            value == 0 for value in
            [glucose, bp, skin, insulin, bmi]
        ),
        "GlucoseBMIInteraction": glucose * bmi
    }

    input_df = pd.DataFrame([data])

    # Match the preprocessing used during model training
    invalid_cols = [
        "Glucose", "BloodPressure",
        "SkinThickness", "Insulin", "BMI"
    ]

    input_df[invalid_cols] = input_df[invalid_cols].replace(
        0, np.nan
    )

    probability = model.predict_proba(input_df)[0][1]

    st.metric(
        "Estimated diabetes risk score",
        f"{probability * 100:.2f}%"
    )

    if probability >= 0.36:
        st.warning(
            "Higher-risk screening result. "
            "Please consult a qualified healthcare professional."
        )
    else:
        st.success(
            "Lower-risk screening result. "
            "This does not rule out diabetes."
        )

st.caption(
    "Educational project only. This tool is not a medical "
    "diagnosis and must not replace professional medical advice."
)
