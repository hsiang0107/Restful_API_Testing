from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, VARCHAR


class TbSpywareDetail(Base):
    __tablename__ = 'tb_SpywareDetail'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    Filename = Column(NVARCHAR(1024))
    ScannerID = Column(INTEGER)
    ScannerSubType = Column(INTEGER)
    ThreatType = Column(INTEGER)
    RiskLevel = Column(INTEGER)
    ActionResult = Column(INTEGER)
    SLF_FileSHA1 = Column(VARCHAR(64))
    SLF_Channel = Column(INTEGER)
    SLF_CloudStorage = Column(INTEGER)
