import pandas as pd


import sys
sys.path.append("/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask/model_nlp/disaster_tweets")
from inference import predict
def predicted_outcome(df):
    df1 = pd.DataFrame(df)
    # We added here our model code
    predictions = predict(df1)
    df1['Prediction'] = predictions
    return df1