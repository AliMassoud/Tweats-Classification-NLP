from sqlalchemy import Column, Integer, String
from Others.Classes.Database import Base

class Tweet(Base):
  __tablename__='Tweets'
  id=Column(Integer,primary_key=True)
  Email=Column(String(255))
  Emergency_Email=Column(String(80))
  text=Column(String(255))
  Prediction=Column(String(15))
  Location=Column(String(50))

  def __init__(self,YourEmail,EmeEmail,text,Prediction, Location):
    self.Email=YourEmail
    self.Emergency_Email=EmeEmail
    self.text=text
    self.Prediction = Prediction
    self.Location = Location


# class ingested_tweets(Base):
#   __tablename__='Ingested_data'
#   id=Column(Integer,primary_key=True)
#   Email=Column(String(255))
#   Emergency_Email=Column(String(80))
#   text=Column(String(255))

#   def __init__(self,YourEmail,EmeEmail,text):
#     self.Email=YourEmail
#     self.Emergency_Email=EmeEmail
#     self.text=text