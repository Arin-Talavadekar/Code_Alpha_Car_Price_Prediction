import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('car_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')


# App title
st.title("🚘 Car Price Prediction App")

# Sidebar input fields
st.sidebar.header("Input Car Details")

year = st.sidebar.number_input("Year of Purchase", 2000, 2025, 2017)
present_price = st.sidebar.number_input("Present Ex-Showroom Price (in Lakhs)", 0.0, 50.0, 9.85)
kms_driven = st.sidebar.number_input("Kilometers Driven", 0, 100000, 6900)
fuel_type = st.sidebar.selectbox("Fuel Type", ("Petrol", "Diesel", "CNG"))
selling_type = st.sidebar.selectbox("Seller Type", ("Dealer", "Individual"))
transmission = st.sidebar.selectbox("Transmission", ("Manual", "Automatic"))
owner = st.sidebar.selectbox("Owner", (0, 1, 2, 3))

# Encode categorical variables same as your training process
if fuel_type == "Petrol":
    fuel = 1
elif fuel_type == "Diesel":
    fuel = 0
else:
    fuel = 2

selling = 0 if selling_type == "Dealer" else 1
trans = 1 if transmission == "Manual" else 0

# Create dataframe for prediction
input_df = pd.DataFrame({
    'Year': [year],
    'Present_Price': [present_price],
    'Driven_kms': [kms_driven],
    'Fuel_Type': [fuel],
    'Selling_type': [selling],
    'Transmission': [trans],
    'Owner': [owner]
})

# Predict button
if st.sidebar.button("Predict Price"):
    input_df = input_df[model_columns]  
    prediction = model.predict(input_df)
    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")
