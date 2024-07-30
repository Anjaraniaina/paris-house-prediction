import streamlit as st
import pandas as pd
import build_model

model = build_model.build_model()

st.title("Simple House Price Prediction App")
st.write("Choose the attributes you want for your house and let the app give a price.")

squareMeters = st.slider("What is the total size the house in square meter?", min_value=0, max_value=100000)
numberOfRooms = st.slider("How many rooms do you want?", min_value=0, max_value=100)
hasYard = st.radio("Do you want a yard?", options=["Yes", "No"])
hasPool = st.radio("Do you want a pool?", options=["Yes", "No"])
floors = st.slider("How many floors do you want?", min_value=0, max_value=100)
numPrevOwners = st.slider("How many previous owners has the house had ?", min_value=0, max_value=100)
made = st.slider("In which year was it built ?", min_value=1970, max_value=2024)
hasStormProtector = st.radio("Do you want a storm protector?", options=["Yes", "No"])
basement = st.slider("What is the size of the basement (in square meters)?", min_value=0, max_value=10000)
attic = st.slider("What is the size of the attic (in square meters)?", min_value=0, max_value=10000)
garage = st.slider("What is the size of the garage (in square meters)?", min_value=0, max_value=1000)

hasYard = 1 if hasYard == "Yes" else 0
hasPool = 1 if hasPool == "Yes" else 0
hasStormProtector = 1 if hasStormProtector == "Yes" else 0

input_data = pd.DataFrame({
    'squareMeters': [squareMeters],
    'numberOfRooms': [numberOfRooms],
    'hasYard': [hasYard],
    'hasPool': [hasPool],
    'floors': [floors],
    'numPrevOwners': [numPrevOwners],
    'made': [made],
    'hasStormProtector': [hasStormProtector],
    'basement': [basement],
    'attic': [attic],
    'garage': [garage]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.write(f"The predicted price of the house is: ${prediction[0]:,.2f}")