from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np
import uvicorn

app = FastAPI()

#dla x godzin jest zdane czy nie y
X = np.array([[1], [2], [3], [6], [7], [8]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

@app.post("/predict")
def predict(request: dict):
    if "godziny" not in request:
        raise HTTPException(status_code=400, detail="Blad walidacji: Brak wymaganej cechy 'godziny'!")

    wartosc = request["godziny"]
    prediction = model.predict([[wartosc]])

    return {
        "status": "sukces",
        "wejscie": wartosc,
        "wynik": int(prediction[0])
    }

@app.get("/info")
def get_info():
    return {
        "model_type": "Logistic Regression",
        "features_count": 1,
        "features_names": ["godziny"],
        "version": "1.0"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
