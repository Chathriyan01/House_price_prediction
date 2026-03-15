# 🏠 House Price Prediction App (Streamlit)

A simple Machine Learning web application built with **Streamlit** to predict house prices in **INR** using features like area, bedrooms, bathrooms, parking, and home amenities.

## Features
- Clean and interactive Streamlit UI  
- Auto-generated input fields  
- Loads a pre-trained ML model (`house_price_model.jb`)  
- Provides instant house price predictions  

## Project Files
- `app.py` — Streamlit application  
- `house_price_model.jb` — Trained model file  
- `app.ipynb` — Notebook used for model training  

## How to Run
```bash
pip install streamlit pandas numpy matplotlib scikit-learn joblib
streamlit run app.py
