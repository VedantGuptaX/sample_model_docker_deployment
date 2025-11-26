import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/housing.csv")

X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model/model.joblib")

print("Model trained and saved!")
