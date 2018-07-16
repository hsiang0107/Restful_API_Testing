from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER


class TbTreeLevel(Base):
    __tablename__ = 'tb_TreeLevel'
    L3Num = Column(INTEGER, primary_key=True)
    L4Num = Column(INTEGER, primary_key=True)
    L5Num = Column(INTEGER, primary_key=True)
    L6Num = Column(INTEGER, primary_key=True)
    L7Num = Column(INTEGER, primary_key=True)
    L8Num = Column(INTEGER, primary_key=True)
    L9Num = Column(INTEGER, primary_key=True)
    L10Num = Column(INTEGER)
    L11Num = Column(INTEGER)
