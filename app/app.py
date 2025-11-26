from fastapi import FastAPI
from src.predict import predict_price

app = FastAPI()

@app.get("/predict")
def predict(area: float, bedrooms: int, bathrooms: int):
    price = predict_price(area, bedrooms, bathrooms)
    return {"predicted_price": price}
