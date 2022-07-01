# import pandas as pd
# from src.Backend_APIs.model_nlp.preprocess import *
# from src.Backend_APIs.model_nlp.train import build_model
# from src.Backend_APIs.model_nlp.inference import predict

# training_data_df = pd.read_csv('Data/Original_Data/train.csv')
# model_performance_dict = build_model(training_data_df)
# print(model_performance_dict)
from pprint import pformat
import great_expectations as ge
import pandas as pd

df = ge.read_csv('Data/Moved_Data_Files_Predict/Actual_train.csv')
# df = ge.read_csv(f'{final_data_path}')
https = df.expect_column_values_to_not_match_regex('text', "http\S+")
tags = df.expect_column_values_to_not_match_regex('text', '@[^\s]+')
hashtags = df.expect_column_values_to_not_match_regex('text', '#[^\s]+')
if hashtags.success is True:
    print("No hashtags in our data")
else:
    df['text'] = df['text'].str.replace(r'#[^\s]+', '').str.strip()

if tags.success is True:
    print("No Tags in our Data!")             
else:
    df['text'] = df['text'].str.replace(r'@[^\s]+', '').str.strip()

if https.success is True:
    print("No HTTPs Links in our data!")
else:
    df['text'] = df['text'].str.replace(r'http\S+', '').str.strip()
# greate Expectations (2 expects)
# COMMENT TO DIANAA
# USE THE SAME TOOLS YOU USED IN THE MODEL TO CLEAN THE TEXT
# YOU WILL USE MY MACHINE

temp = pd.DataFrame(df)
print(temp.head())
print(type(temp))
# print(https.success)
# print(tags.success)
# print(hashtags.success)
# print(numbers.success)
# print(https) 