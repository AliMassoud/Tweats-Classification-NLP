# import sys
# sys.path.append('/mnt/c/Users/user/Desktop/DSP_Project_APIs/APIs_Flask')
# from app import app
# db = SQLAlchemy(appp)

def store_db_single(db, row):
    db.session.add(row)
    db.session.commit()

def store_db_bulk(db,rows):
    db.session.bulk_save_objects(rows)
    db.session.commit()