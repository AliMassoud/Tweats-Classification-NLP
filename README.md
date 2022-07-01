# APIs_Flask
## DANGER TWEETS DETECTION :thinking:
### INTRODUCTION :speech_balloon:

Twitter has become an important communication channel in the terms of emergency. With the help of smartphones people announce an emergency they’re observing in real-time. Therefore, more agencies are interested in monitoring Twitter. It’s not always clear whether the tweets are actually announcing a disaster or not. In this project we build a machine learning model that predicts which tweets are danger and which one’s aren’t.

### MODEL IMPLEMENTATION
1. Data setup(load the data, train and test split)
2. Main feature preprocessing(text normalization and vectorization)
3. Model training and saving the model in the `model.joblib` file
4. Model evaluation(accurancy, precision, recall and F-score)

### CODE EXTRACTION IN PYTHON MODULES
1. For text normalization and vectorization - `preprocess.py`
2. For model building and training - `train.py`
3. For making a prediction - `inference.py`


