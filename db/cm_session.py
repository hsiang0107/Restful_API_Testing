import random
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from db.db_connection import CMConnection

Base = declarative_base()
cm_session = CMConnection().session


def all(cls, session=cm_session):
    return session.query(cls).all()


def first(cls, session=cm_session):
    return session.query(cls).first()


def rand(cls, session=cm_session):
    rand = random.randrange(0, session.query(cls).count())
    return session.query(cls).order_by(func.rand()).offset(rand).first()


def count(cls, session=cm_session):
    return session.query(cls).count()


def truncate(cls, session=cm_session):
    sql_statement = "truncate table %s" % cls.__tablename__
    session.execute(sql_statement)
    session.commit()


Base.all = classmethod(all)
Base.first = classmethod(first)
Base.rand = classmethod(rand)
Base.count = classmethod(count)
Base.truncate = classmethod(truncate)
