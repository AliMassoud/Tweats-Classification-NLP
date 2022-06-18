import joblib
# import os
# print(os.getcwd())
from model_nlp.preprocess import *
import pandas as pd
def predict(test_data):
    X = test_data.text
    X = X.apply(text_normalize)
    X_test= vectorizer(X)
    model_path = "src/Backend_APIs/model_nlp/models/model.joblib"
    logistic_regression = joblib.load(model_path, mmap_mode=None)
    y_pred = logistic_regression.predict(X_test)
    y_pred = ['Not Danger' if i == 0 else 'Danger' for i in y_pred]
    return y_pred