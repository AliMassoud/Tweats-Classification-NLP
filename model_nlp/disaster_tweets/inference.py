import joblib
from preprocess import *
import pandas as pd
import os
def predict(test_data):
    X = test_data.text
    X = X.apply(text_normalize)
    X_test= vectorizer(X)
    model_path = "/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask/model_nlp/models/model.joblib"
    logistic_regression = joblib.load(model_path, mmap_mode=None)
    y_pred = logistic_regression.predict(X_test)
    y_pred = ['Not Danger' if i == 0 else 'Danger' for i in y_pred]
    return y_pred