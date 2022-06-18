import numpy as np
import pandas as pd
import sklearn 
import re
from sklearn.model_selection import train_test_split
import spacy
nlp = spacy.load('en_core_web_lg')

# Function of reading a file
def reading_dataset(path):
    data = pd.read_csv(path)
    # data = data.drop(['Id'], axis = 1)
    data = data.drop_duplicates()
    data['text'] = data['text'].apply(lambda x:x.lower())
    return data


# Function of data set split
def data_set_split(data):
    X = data.text
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    return X_train, X_test, y_train, y_test


# Function of normalize the text data
def text_normalize(text):
    text = str(text)
    text = re.sub(r'http\S+', '', text) #remove urls
    text = re.sub('#[^\s]+','',text) #remove hashtags
    text = re.sub('@[^\s]+','',text) #remove tags
    text = re.sub(r'[0-9]+','', text) #remove numbers
    text = re.sub('\s*\\b([a-z]|[a-z]{2})\\b', '', text) #remove single letters
    text = re.sub(r'[^\w\s]', '', text)
    doc = nlp(text)
    result=[]
    for token in doc:
        if(token.is_stop or token.is_space): #remove stop_words
            pass
        else:
            result.append(token.lemma_)#lemmatization
    return " ".join(result)

    #function for vectorizing the text
def vectorizer(data):
    train_vecs = np.array([nlp(text).vector for text in data])
    return train_vecs