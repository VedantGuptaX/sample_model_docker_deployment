from src.predict import predict_price

def test_predict():
    price = predict_price(1000, 3, 2)
    assert price > 0

