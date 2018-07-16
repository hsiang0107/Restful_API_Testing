from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbTMCMWFApplicationStatusCache(Base):
    __tablename__ = 'tb_TMCMWF_ApplicationStatus_Cache'
    ServerName = Column(NVARCHAR(64), primary_key=True)
    ServerGUID = Column(CHAR(36), primary_key=True)
    ConnectionStatus = Column(INTEGER, primary_key=True)
    Number = Column(INTEGER)
    Type = Column(INTEGER)
    UpdateTime = Column(DATETIME)
