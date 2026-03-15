import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("house_price_model.jb")

# ---------------------------
# 1. Create list of input features
# ---------------------------
input_features = [
    'area', 'bedrooms', 'bathrooms', 'stories',
    'mainroad', 'guestroom', 'basement', 'hotwaterheating',
    'airconditioning', 'parking', 'prefarea'
]

st.title("🏠 House Price Prediction (INR)")
st.write("Enter the details below to predict the house price")

# ---------------------------
# 2. Create a dictionary to store all user inputs
# ---------------------------
user_data = {}

# Numeric Inputs
numeric_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

# Yes/No Categorical Inputs
yes_no_features = [
    'mainroad', 'guestroom', 'basement',
    'hotwaterheating', 'airconditioning', 'prefarea'
]


st.subheader("Enter House Details")

# ---------------------------
# 3. Auto-generate UI based on input list
# ---------------------------
for feature in input_features:

    # Numeric fields
    if feature in numeric_features:
        user_data[feature] = st.number_input(feature.capitalize(), min_value=0)

    # Yes/No dropdown fields
    elif feature in yes_no_features:
        val = st.selectbox(f"{feature.capitalize()} (Yes/No)", ["Yes", "No"])
        user_data[feature] = 1 if val == "Yes" else 0


# ---------------------------
# 4. Convert input to DataFrame
# ---------------------------
input_df = pd.DataFrame([user_data])

# ---------------------------
# 5. Predict
# ---------------------------
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"🏡 **Predicted House Price: ₹ {prediction:,.2f}**")