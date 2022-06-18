# import sys
# sys.path.append('/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask')
# from src.Backend_APIs.app import db

from sqlalchemy import Column, Integer, String
from Others.Classes.Database import Base

class Tweet(Base):
  __tablename__='Tweets'
  id=Column(Integer,primary_key=True)
  Email=Column(String(255))
  Emergency_Email=Column(String(80))
  text=Column(String(255))
  Prediction=Column(String(15))

  def __init__(self,YourEmail,EmeEmail,text,Prediction):
    self.Email=YourEmail
    self.Emergency_Email=EmeEmail
    self.text=text
    self.Prediction = Prediction