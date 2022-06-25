import pandas as pd
from src.Backend_APIs.model_nlp.preprocess import *
from src.Backend_APIs.model_nlp.train import build_model
from src.Backend_APIs.model_nlp.inference import predict

training_data_df = pd.read_csv('Data/Original_Data/train.csv')
model_performance_dict = build_model(training_data_df)
print(model_performance_dict)