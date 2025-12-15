import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.pkl")

st.markdown(
    "<h1 style='text-align: center;'>Crime Rate Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>Select Input Parameters</h3>",
    unsafe_allow_html=True
)

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

years = list(range(2020, 2030))

df = pd.read_csv("crime_dataset_india.csv")

df['Date of Occurrence'] = pd.to_datetime(df['Date of Occurrence'])
df['Year'] = df['Date of Occurrence'].dt.year
df['Month'] = df['Date of Occurrence'].dt.month

cities = sorted(df["City"].unique())
selected_city = st.selectbox("Select City", cities)

selected_month = st.selectbox("Select Month", months)

selected_year = st.selectbox("Select Year", years)

x = df[['City', 'Year', 'Month']]
x = pd.get_dummies(x, drop_first=True)

future_data = pd.DataFrame({
    'City': [selected_city],
    'Year': [selected_year],
    'Month': [selected_month]
})

future_data = pd.get_dummies(future_data)
future_data = future_data.reindex(columns=x.columns, fill_value=0)

if st.button("Predicted Crime Rate") :
    prediction = model.predict(future_data)

    st.success(
        f"Predicted Crime Rate for {selected_city}"
        f"({selected_month}, {selected_year}) : {prediction[0]:.2f}"
    )