# import imp
from crypt import methods
from flask import Flask
from flask import request, json
import pandas as pd
import numpy as np
from Others.Services import predictionFunction
from Others.Classes import Models
from Others.Classes import Database
app = Flask(__name__)

@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    temp = np.array([data['YourEmail'],data['EmeEmail'],data['text']])
    my_data = pd.DataFrame([temp], columns=['YourEmail','EmeEmail', 'text'])
    tweet_with_pred = predictionFunction.predicted_outcome(my_data) # Pass my data to the model
    tweet_db = Models.Tweet(tweet_with_pred['YourEmail'][0], tweet_with_pred['EmeEmail'][0], tweet_with_pred['text'][0], tweet_with_pred['Prediction'][0])
    Database.store_db_single(tweet_db)

    return {
    "YourEmail": tweet_with_pred['YourEmail'][0],
    "EmeEmail": tweet_with_pred['EmeEmail'][0],
    "text": tweet_with_pred['text'][0],
    "Prediction": tweet_with_pred['Prediction'][0]
    }


@app.route('/SubmitFile', methods=["GET"])
def index():
    if request.method == 'GET':
        saved_file = request.files['data_file']
        df = pd.read_csv(saved_file)
        g_list = dict()
        g = []
        result = predictionFunction.predicted_outcome(df)
        for i in range(len(result)):
            tweet_db = Models.Tweet(result['YourEmail'][i], result['EmeEmail'][i], result['text'][i], result['Prediction'][i])
            g.append(tweet_db)
            g_list[i]= {
                'YourEmail': result['YourEmail'][i],
                'EmeEmail': result['EmeEmail'][i],
                'text': result['text'][i],
                'Prediction': result['Prediction'][i]
            }
        Database.store_db_bulk(g)
    return g_list


# @app.route('/getAllTweets', methods=['GET'])
# def get_AllTweets():
#     Database.get_all_tweets()

#     return "HEllo"


if __name__ == '__main__':
    Database.init_db()
    app.run(debug=True)



# @app.route('/IngestFile', methods=["GET"])
# def Ingest():
#     if request.method == 'GET':
#         saved_file = request.files['data_file']
#         df = pd.read_csv(saved_file)
#         g_list = dict()
#         g = []
#         for i in range(len(df)):
#             Injected_data_db = Models.ingested_tweets(df['YourEmail'][i], df['EmeEmail'][i], df['text'][i])
#             g.append(Injected_data_db)
#             g_list[i]= {
#                 'YourEmail': df['YourEmail'][i],
#                 'EmeEmail': df['EmeEmail'][i],
#                 'text': df['text'][i]
#             }
#         Database.store_db_bulk(g)
#     return g_list