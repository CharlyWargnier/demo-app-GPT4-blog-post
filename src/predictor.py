
from .model_loader import load_model
def predict(data, model_path):
    model = load_model(model_path)
    predictions = model.predict(data)
    return predictions
