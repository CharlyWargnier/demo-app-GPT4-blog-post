
import streamlit as st
from src.data_loader import load_data
from src.predictor import predict
from src.analyser import analyse
from src.forecast import forecast

# Load data
data = load_data('data/large_dataset.csv')

st.title('My Streamlit App')

# Select action
action = st.selectbox(
    "Choose an action",
    ("Analyse Data", "Predict", "Forecast")
)

# Get model path
model_path = 'models/heavy_model.pkl'

if action == "Analyse Data":
    analysis_results = analyse(data)
    st.write(analysis_results)

elif action == "Predict":
    predictions = predict(data, model_path)
    st.write(predictions)

elif action == "Forecast":
    forecast_results = forecast(data, model_path)
    st.write(forecast_results)
