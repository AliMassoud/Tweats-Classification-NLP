import sys
sys.path.append('/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask')

from flask_sqlalchemy import SQLAlchemy


# import os
# print(os.getcwd())
# print(os.listdir())src\Backend_APIs\Others\Classes\Tweet.py
from src.Backend_APIs.Others.Classes.Tweet import Tweet
class Database:
    def __init__(self, flask_app):
        self.db = SQLAlchemy(flask_app)

    def store_db_single(self, row):
        tweet_db = Tweet(row['YourEmail'], row['EmeEmail'], row['text'], row['Prediction'])
        self.db.session.add(tweet_db)
        self.db.session.commit()

    def store_db_bulk(self,rows):
        self.db.session.bulk_save_objects(rows)
        self.db.session.commit()

