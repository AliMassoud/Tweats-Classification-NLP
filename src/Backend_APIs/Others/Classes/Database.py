from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Others.DB_config import DB_conf

engine = create_engine(f"postgresql://{DB_conf['DB_USERNAME']}:{DB_conf['DB_PASSWORD']}@{DB_conf['DB_URL']}/{DB_conf['DB_NAME']}")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import Models
    Base.metadata.create_all(bind=engine)


def store_db_single(row):
    db_session.add(row)
    db_session.commit()


def store_db_bulk(rows):
    db_session.bulk_save_objects(rows)
    db_session.commit()