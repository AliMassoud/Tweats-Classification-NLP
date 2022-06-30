# import imp
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
    temp = np.array([data['YourEmail'],data['EmeEmail'],data['text'], data['Location']])
    my_data = pd.DataFrame([temp], columns=['YourEmail','EmeEmail', 'text', 'Location'])
    tweet_with_pred = predictionFunction.predicted_outcome(my_data) # Pass my data to the model
    print(tweet_with_pred.head())

    tweet_db = Models.Tweet(tweet_with_pred['YourEmail'][0], tweet_with_pred['EmeEmail'][0], tweet_with_pred['text'][0], tweet_with_pred['Prediction'][0], tweet_with_pred['Location'][0])
    Database.store_db_single(tweet_db)

    return {
    "YourEmail": tweet_with_pred['YourEmail'][0],
    "EmeEmail": tweet_with_pred['EmeEmail'][0],
    "text": tweet_with_pred['text'][0],
    "Location": tweet_with_pred['Location'][0],
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
            tweet_db = Models.Tweet(result['YourEmail'][i], result['EmeEmail'][i], result['text'][i], result['Prediction'][i], result['Location'][i])
            g.append(tweet_db)
            g_list[i]= {
                'YourEmail': result['YourEmail'][i],
                'EmeEmail': result['EmeEmail'][i],
                'text': result['text'][i],
                'Prediction': result['Prediction'][i],
                'Location': result['Location'][i]
            }
        Database.store_db_bulk(g)
    return g_list


@app.route('/getAllTweets', methods=['GET'])
def get_AllTweets():
    Result = Database.get_all_tweets()
    d, a = {}, []
    for rowproxy in Result:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)
    return {
        "Tweets": a
    }


if __name__ == '__main__':
    Database.init_db()
    app.run(debug=True)