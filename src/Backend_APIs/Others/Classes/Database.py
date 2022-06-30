from sqlalchemy import create_engine, select, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Others.DB_config import DB_conf

engine = create_engine(f"postgresql://{DB_conf['DB_USERNAME']}:{DB_conf['DB_PASSWORD']}@{DB_conf['DB_URL']}/{DB_conf['DB_NAME']}")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
metadata = MetaData(bind=None)

def init_db():
    Base.metadata.create_all(bind=engine)


def store_db_single(row):
    db_session.add(row)
    db_session.commit()


def store_db_bulk(rows):
    db_session.bulk_save_objects(rows)
    db_session.commit()


def get_all_tweets():
    print("INSIDE")
    table = Table(
        'Tweets', 
        metadata, 
        autoload=True, 
        autoload_with=engine
    )
    stmt = select([table.columns])
    results = db_session.execute(stmt)
    for result in results:
        print(result)
    return results

def printt():
    return "HIIII"