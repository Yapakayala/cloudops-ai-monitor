from fastapi import FastAPI
from api.schema import InputMetrics
from api.inference import predict_health
from genai.explain import interpret_prediction

app = FastAPI()

@app.post("/predict")
def get_prediction(input: InputMetrics):
    return predict_health(input)

@app.post("/predict_explained")
def get_prediction_with_explanation(input: InputMetrics):
    """
    Returns both the raw prediction and a GenAI explanation.
    Falls back gracefully if API quota is exceeded.
    """
    result = predict_health(input)
    explanation = interpret_prediction(result)
    return {
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "explanation": explanation,
    }
