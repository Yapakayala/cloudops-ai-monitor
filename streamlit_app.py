import streamlit as st, requests

st.title("CloudOps AI Monitor")
error_count = st.slider("Error Count", 0, 100)
log_level_score = st.slider("Log Level Score", 0, 10)
event_density = st.slider("Event Density", 0, 1000)
if st.button("Predict"):
    payload = {
        "error_count": error_count,
        "log_level_score": log_level_score,
        "event_density": event_density,
    }
    response = requests.post("http://localhost:8080/predict", json=payload)
    result = response.json()
    st.write(f"Prediction: {'Anomaly' if result['prediction'] else 'Normal'}")
    st.write(f"Confidence: {round(result['confidence']*100, 2)}%")
