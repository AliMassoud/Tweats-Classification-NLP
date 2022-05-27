from flask import Flask
from flask import request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import airflow
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://DSPDB:PAUcwKtYQ2j0Tt0f16pe@dspdb.c7yyz4ccfsai.eu-west-2.rds.amazonaws.com/DSP_Tweeter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tweet(db.Model):
  __tablename__='Tweets'
  id=db.Column(db.Integer,primary_key=True)
  Email=db.Column(db.String(255))
  Emergency_Email=db.Column(db.String(80))
  text=db.Column(db.String(255))
  Prediction=db.Column(db.String(15))

  def __init__(self,YourEmail,EmeEmail,text,Prediction):
    self.Email=YourEmail
    self.Emergency_Email=EmeEmail
    self.text=text
    self.Prediction = Prediction


def predicted_outcome(df):
    df1 = pd.DataFrame(df)
    # We add here our model code
    df1['Prediction'] = 'Danger'
    return df1


@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    temp = np.array([data['YourEmail'],data['EmeEmail'],data['text']])
    my_data = pd.DataFrame([temp], columns=['YourEmail','EmeEmail', 'text'])
    tweet_with_pred = predicted_outcome(my_data) # Pass my data to the model

    tweet_db = Tweet(tweet_with_pred['YourEmail'][0], tweet_with_pred['EmeEmail'][0], tweet_with_pred['text'][0], tweet_with_pred['Prediction'][0])
    db.session.add(tweet_db)
    db.session.commit()
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
        result = predicted_outcome(df)
        for i in range(len(result)):
            tweet_db = Tweet(result['YourEmail'][i], result['EmeEmail'][i], result['text'][i], result['Prediction'][i])
            db.session.add(tweet_db)
            db.session.commit()
            g_list[i]= {
                'YourEmail': result['YourEmail'][i],
                'EmeEmail': result['EmeEmail'][i],
                'text': result['text'][i],
                'Prediction': result['Prediction'][i]
            }
    return g_list


if __name__ == '__main__':

    app.run(debug=True)