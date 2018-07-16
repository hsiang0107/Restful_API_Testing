from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbSpywareLog(Base):
    __tablename__ = 'tb_SpywareLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MsgLogType = Column(INTEGER)
    ProductGUID = Column(CHAR(36))
    CMGuid = Column(CHAR(36))
    ClientGUID = Column(CHAR(36))
    ProductID = Column(INTEGER)
    LogVersion = Column(INTEGER)
    LogMinorVersion = Column(INTEGER)
    ComputerName = Column(NVARCHAR(128))
    LogGenUTCDatetime = Column(DATETIME)
    LogGenLocalDatetime = Column(DATETIME)
    TimeZoneInMins = Column(INTEGER)
    DaylightSavingInMins = Column(INTEGER)
    RedAlertID = Column(CHAR(36))
    LoginUser = Column(NVARCHAR(64))
    VirusName = Column(NVARCHAR(128))
    ScanType = Column(INTEGER)
    EngineType = Column(INTEGER)
    EngineVersion = Column(NVARCHAR(32))
    PatternType = Column(INTEGER)
    PatternVersion = Column(NVARCHAR(32))
    Description = Column(NVARCHAR(1024))
    LogCount = Column(INTEGER)
    LogReceivedTime = Column(DATETIME)
    LogReceivedUTCTime = Column(DATETIME)
    AggregatedUTCDatetime = Column(DATETIME)
    AggregatedLocalDatetime = Column(DATETIME)
    AggregatedCount = Column(INTEGER)
    ActionResult = Column(INTEGER)
    CE_FilterID = Column(VARCHAR(35))
    CLF_LogGenCMLocalTime = Column(DATETIME)
