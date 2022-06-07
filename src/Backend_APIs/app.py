# import imp
from flask import Flask
from flask import request, jsonify, json
from Others.DB_config import DB_conf
from Others.Classes.store_On_DB import Database

import pandas as pd
import numpy as np

# import 
app = Flask(__name__)

from Others.Services.predictionFunction import predicted_outcome
DB_conf = DB_conf
app.config['SQLALCHEMY_DATABASE_URI']=f"postgresql://{DB_conf['DB_USERNAME']}:{DB_conf['DB_PASSWORD']}@{DB_conf['DB_URL']}/{DB_conf['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = Database(app)






# 1- Software Architecture
# 2- Second Airflow Pipeline
# 3- History Page (or table) (Naveen)
# 4- prepare API that gets all the tweets in the DB (Chetna)


# Third Airflow
# 5- Graphana
# missing things






# class Tweet(db.db.Model):
#   __tablename__='Tweets'
#   id=db.db.Column(db.db.Integer,primary_key=True)
#   Email=db.db.Column(db.db.String(255))
#   Emergency_Email=db.db.Column(db.db.String(80))
#   text=db.db.Column(db.db.String(255))
#   Prediction=db.db.Column(db.db.String(15))

#   def __init__(self,YourEmail,EmeEmail,text,Prediction):
#     self.Email=YourEmail
#     self.Emergency_Email=EmeEmail
#     self.text=text
#     self.Prediction = Prediction


@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    temp = np.array([data['YourEmail'],data['EmeEmail'],data['text']])
    my_data = pd.DataFrame([temp], columns=['YourEmail','EmeEmail', 'text'])
    tweet_with_pred = predicted_outcome(my_data) # Pass my data to the model

    # tweet_db = Tweet(tweet_with_pred['YourEmail'][0], tweet_with_pred['EmeEmail'][0], tweet_with_pred['text'][0], tweet_with_pred['Prediction'][0])
    db.store_db_single(tweet_with_pred)
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
        db.store_db_bulk(g)
    return g_list


if __name__ == '__main__':
    app.run(debug=True)