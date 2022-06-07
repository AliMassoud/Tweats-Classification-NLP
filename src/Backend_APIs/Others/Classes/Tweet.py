import sys
sys.path.append('/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask')
# from src.Backend_APIs.app import db

class Tweet(db.db.Model):
  __tablename__='Tweets'
  id=db.db.Column(db.db.Integer,primary_key=True)
  Email=db.db.Column(db.db.String(255))
  Emergency_Email=db.db.Column(db.db.String(80))
  text=db.db.Column(db.db.String(255))
  Prediction=db.db.Column(db.db.String(15))

  def __init__(self,YourEmail,EmeEmail,text,Prediction):
    self.Email=YourEmail
    self.Emergency_Email=EmeEmail
    self.text=text
    self.Prediction = Prediction