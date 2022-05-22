import joblib
import sys
sys.path.append('..')
from disaster_tweets.preprocess import *
import pandas as pd

def predict(test_data):
    X = test_data.text
    X = X.apply(text_normalize)
    X_test= vectorizer(X)
    
    logistic_regression = joblib.load("../model_nlp/models/model.joblib", mmap_mode=None)
    y_pred = logistic_regression.predict(X_test)
    y_pred = ['Not Danger' if i == 0 else 'Danger' for i in y_pred]
    return y_pred

