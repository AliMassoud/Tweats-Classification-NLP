import pandas as pd

# import sys
# sys.path.append("../../")
# from model_nlp.inference import predict
from model_nlp import inference
def predicted_outcome(df):
    df1 = pd.DataFrame(df)
    # We added here our model code
    predictions = inference.predict(df1)
    df1['Prediction'] = predictions
    return df1