import streamlit as st
import pandas as pd
import pickle
import numpy as np


from src.predict_job_change.pipelines.data_preparation.nodes import encode_categorical_columns

model_path = "data/06_models/dt_model.pkl"
model = pickle.load(open(model_path, "rb"))

st.title("Do you change job?")


city_development_index = st.slider("City Development Index", 0.0, 1.0, 0.5, step=0.01)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
relevent_experience = st.selectbox("Relevent experience?",
                                   ["Has relevent experience", "No relevent experience"])
enrolled_university = st.selectbox("University status", ["no_enrollment", "Full time course", "Part time course"])
education_level = st.selectbox("Education level", ["Primary School", "High School", "Graduate", "Masters", "Phd"])
major_discipline = st.selectbox("Field of study",
                                ["STEM", "Business Degree", "Arts", "Humanities", "Other", "No Major"])
experience = st.selectbox("Work experience in years", [f"{i}" for i in range(1, 21)] + ["<1", ">20"])
company_size = st.selectbox("Company size",
                            ["<10", "10-49", "50-99", "100-500", "500-999", "1000-4999", "5000-9999", "10000+"])
company_type = st.selectbox("Company type", ["Private", "Public", "Startup", "NGO", "Other"])
last_new_job = st.selectbox("Time since last job change", ["Migf", "1", "2", "3", "4", ">4"])

input_data = pd.DataFrame({
    "city_development_index": [city_development_index],
    "gender": [gender],
    "relevent_experience": [relevent_experience],
    "enrolled_university": [enrolled_university],
    "education_level": [education_level],
    "major_discipline": [major_discipline],
    "experience": [experience],
    "company_size": [company_size],
    "company_type": [company_type],
    "last_new_job": [last_new_job],
})

st.write("### Your Data:")
st.dataframe(input_data)

if st.button("Predict"):

    x = encode_categorical_columns(input_data)
    y_pred = model.predict(x)

    if int(np.array(y_pred).item()) == 1:
        st.success("Model prediction: You will change job")
    else:
        st.error("Model prediction: You will not change job")
