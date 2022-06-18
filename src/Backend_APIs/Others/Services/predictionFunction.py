import pandas as pd

import sys
sys.path.append("..")
from model_nlp.inference import predict
def predicted_outcome(df):
    df1 = pd.DataFrame(df)
    # We added here our model code
    predictions = predict(df1)
    df1['Prediction'] = predictions
    return df1