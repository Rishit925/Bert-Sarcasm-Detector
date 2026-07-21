from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI(
    title="Sarcasm Detection API",
    description="Predict whether a news headline is sarcastic using a BERT model.",
    version="1.0.0"
)

class Headline(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Sarcasm Detection API",
        "status": "Running",
        "docs": "/docs"
    }


@app.post("/predict")
def predict_headline(headline: Headline):

    prediction, confidence = predict(headline.text)

    return {
        "headline": headline.text,
        "prediction": prediction,
        "confidence": round(confidence * 100, 2)
    }