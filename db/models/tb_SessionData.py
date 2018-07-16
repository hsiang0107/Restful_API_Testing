from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbSessionData(Base):
    __tablename__ = 'tb_SessionData'
    LoginToken = Column(VARCHAR(1024), primary_key=True)
    UserID = Column(CHAR(36))
    RegTime = Column(DATETIME)
    Flag = Column(INTEGER)
    ClientGUID = Column(CHAR(36))
    LastServerConnectTime = Column(DATETIME)
    LastClientConnectTime = Column(DATETIME)
