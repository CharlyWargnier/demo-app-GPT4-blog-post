
def load_model(model_path):
    from sklearn.externals import joblib
    model = joblib.load(model_path)
    return model
