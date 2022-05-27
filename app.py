<<<<<<< HEAD
from flask import Flask
from flask import request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
#import numpy as np
# import airflow
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
# {
#         "YourEmail": df1['YourEmail'],
#         "EmeEmail": df1['EmeEmail'],
#         "text": df1['text'],
#         "Prediction": df1['Prediction']
#     # }


@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    YourEmail= data['YourEmail']
    EmeEmail=data['EmeEmail']
    text=data['text']
    Prediction = predicted_outcome() # Pass my data to the model
    tweet = Tweet(YourEmail, EmeEmail, text, Prediction)
    db.session.add(tweet)
    db.session.commit()
    # print(data)
    return {
    "YourEmail": YourEmail,
    "EmeEmail": EmeEmail,
    "text": text,
    "Prediction": Prediction
    }


@app.route('/SubmitFile', methods=["GET"])
def index():
    if request.method == 'GET':
        saved_file = request.files['data_file']
        df = pd.read_csv(saved_file)
        g_list = pd.DataFrame()
        result = predicted_outcome(df)
        g_list = pd.concat([g_list,result], axis=0)
        g_list.to_sql('Tweets',db)  ##Store the dataframe to DB
    return "Hello"


if __name__ == '__main__':
=======
from flask import Flask
from flask import request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://DSPDB:PAUcwKtYQ2j0Tt0f16pe@dspdb.c7yyz4ccfsai.eu-west-2.rds.amazonaws.com/DSP_Tweeter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tweet(db.Model):
  __tablename__='Tweets'
  id=db.Column(db.Integer,primary_key=True)
  Email=db.Column(db.String(255))
  Emergency_Email=db.Column(db.String(80))
  Msg=db.Column(db.String(255))
  Prediction=db.Column(db.String(15))

  def __init__(self,YourEmail,EmeEmail,Msg,Prediction):
    self.Email=YourEmail
    self.Emergency_Email=EmeEmail
    self.Msg=Msg
    self.Prediction = Prediction


def make_predictions():
    # We add here our model code
    
    return 'Danger'


@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    YourEmail= data['YourEmail']
    EmeEmail=data['EmeEmail']
    Msg=data['Msg']
    Prediction = make_predictions() # Pass my data to the model
    tweet = Tweet(YourEmail, EmeEmail, Msg, Prediction)
    db.session.add(tweet)
    db.session.commit()
    print(data)
    return {
    "YourEmail": YourEmail,
    "EmeEmail": EmeEmail,
    "Msg": Msg,
    "Prediction": Prediction
    }


@app.route('/SubmitFile', methods=["GET"])
def index():
    if request.method == 'GET':
        saved_file = request.files['file']
        df = pd.read_csv(saved_file)
        for index, row in df.iterrows():
            print(row)
            print(type(row))
            break
    return "Hello"


if __name__ == '__main__':
>>>>>>> bea853483c019775bb8d73cc29d585e378fea51c
    app.run(debug=True)