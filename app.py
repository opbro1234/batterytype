# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ✅ Page config MUST be first Streamlit command
st.set_page_config(page_title='Battery Type Classifier', layout='centered')

# ✅ Safe model loading (error clearly show karega)
try:
    model = joblib.load("random_forest_classifier_model.pkl")
except Exception as e:
    st.error("❌ Model load nahi ho pa raha")
    st.code(str(e))
    st.stop()

st.title('Battery Type Classification App')
st.write("Predict whether the battery is **Lead-Acid** or **Lithium-Ion**")

# ✅ number_input NEVER use value=None
Poor_Cell_Design = st.number_input('Poor Cell Design', min_value=0.0, value=0.0)
External_Abuse = st.number_input('External Abuse', min_value=0.0, value=0.0)
Poor_Battery_Design = st.number_input('Poor Battery Design', min_value=0.0, value=0.0)
Short_Circuits = st.number_input('Short Circuits', min_value=0.0, value=0.0)
Temperature = st.number_input('Temperature', min_value=0.0, value=0.0)
Overcharge_Overdischarge = st.number_input('Overcharge/Overdischarge', min_value=0.0, value=0.0)
Battery_Maintenance = st.number_input('Battery Maintenance', min_value=0.0, value=0.0)
Battery_Health = st.number_input('Battery Health', min_value=0.0, value=0.0)

if st.button('Predict'):
    input_data = np.array([[
        Poor_Cell_Design,
        External_Abuse,
        Poor_Battery_Design,
        Short_Circuits,
        Temperature,
        Overcharge_Overdischarge,
        Battery_Maintenance,
        Battery_Health
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error('🔴 Lead-Acid Battery')
    else:
        st.success('🟢 Lithium-Ion Battery')
