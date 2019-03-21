# External Libraries
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class Measure(Base):
    __tablename__ = 'test_runs'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    value = Column(Integer)


class Box(Base):
    __tablename__ = 'boxes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ip = Column(String(255))
    hostname = Column(String(255))
    subnet = Column(String(255))


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True, echo=False)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
