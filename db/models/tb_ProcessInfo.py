from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbProcessInfo(Base):
    __tablename__ = 'tb_ProcessInfo'
    PI_Name = Column(VARCHAR(128), primary_key=True, nullable=False)
    PI_State = Column(INTEGER, nullable=False)
    PI_FileName = Column(VARCHAR(254), nullable=False)
    PI_ListenPort = Column(INTEGER, nullable=False)
    PI_HostName = Column(VARCHAR(254), nullable=False)
    PI_IPList = Column(VARCHAR(1024))
    PI_LastAccessTime = Column(DATETIME)
