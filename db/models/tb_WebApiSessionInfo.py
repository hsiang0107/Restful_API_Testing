from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME


class TbWebApiSessionInfo(Base):
    __tablename__ = 'tb_WebApiSessionInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SessionID = Column(CHAR(36), nullable=False)
    CreateTime = Column(DATETIME, nullable=False)
