# save this as app.py
from cgitb import text
from tempfile import tempdir
from flask import Flask
from flask import request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2

engine = psycopg2.connect(
    database="postgres",
    user="DSPDB",
    password="PAUcwKtYQ2j0Tt0f16pe",
    host="dspdb.c7yyz4ccfsai.eu-west-2.rds.amazonaws.com",
    port='5432'
)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://:@'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
# dspdb.c7yyz4ccfsai.eu-west-2.rds.amazonaws.com
class Tweet(db.Model):
  __tablename__='Tweets'
  id=db.Column(db.Integer,primary_key=True)
  Email=db.Column(db.String(255))
  Emergency_Email=db.Column(db.String(80))
  Msg=db.Column(db.String(255))

  def __init__(self,YourEmail,EmeEmail,Msg):
    self.Email=YourEmail
    self.Emergency_Email=EmeEmail
    self.Msg=Msg


@app.route("/Submit", methods=['GET'])
def submit():
    data = json.loads(request.data)
    YourEmail= data['YourEmail']
    EmeEmail=data['EmeEmail']
    Msg=data['Msg']
    # tweet = Tweet(YourEmail, EmeEmail,Msg)
    # db.session.add(tweet)
    # db.session.commit()
    print(data)
    return {
    "YourEmail": YourEmail,
    "EmeEmail": EmeEmail,
    "Msg": Msg
}


if __name__ == '__main__':
    app.run(debug=True)