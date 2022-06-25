# import imp
from flask import Flask
from flask import request, json
import pandas as pd
import numpy as np
from Others.Services.predictionFunction import predicted_outcome
from Others.Classes.Models import Tweet
from Others.Classes.Database import init_db,store_db_single,store_db_bulk

app = Flask(__name__)

@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    temp = np.array([data['YourEmail'],data['EmeEmail'],data['text']])
    my_data = pd.DataFrame([temp], columns=['YourEmail','EmeEmail', 'text'])
    tweet_with_pred = predicted_outcome(my_data) # Pass my data to the model

    tweet_db = Tweet(tweet_with_pred['YourEmail'][0], tweet_with_pred['EmeEmail'][0], tweet_with_pred['text'][0], tweet_with_pred['Prediction'][0])
    store_db_single(tweet_db)
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
        df = pd.read_csv(saved_file, encoding='UTF-8')
        g_list = dict()
        g = []
        result = predicted_outcome(df)
        for i in range(len(result)):
            tweet_db = Tweet(result['YourEmail'][i], result['EmeEmail'][i], result['text'][i], result['Prediction'][i])
            g.append(tweet_db)
            g_list[i]= {
                'YourEmail': result['YourEmail'][i],
                'EmeEmail': result['EmeEmail'][i],
                'text': result['text'][i],
                'Prediction': result['Prediction'][i]
            }
        store_db_bulk(g)
    return g_list

if __name__ == '__main__':
    init_db()
    app.run(debug=True)