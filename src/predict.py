import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/model.joblib")

def predict_price(area: float, bedrooms: int, bathrooms: int):
    """
    Predict house price based on inputs.
    """
    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)
    return float(prediction[0])
