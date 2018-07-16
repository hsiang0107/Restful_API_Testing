from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbLogIntegrityMonitor(Base):
    __tablename__ = 'tb_LogIntegrityMonitor'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MsgLogType = Column(SMALLINT, nullable=False)
    CMGuid = Column(CHAR(36), nullable=False)
    ProductGUID = Column(CHAR(36), nullable=False)
    ProductID = Column(INTEGER, nullable=False)
    LogVersion = Column(SMALLINT, nullable=False)
    LogMinorVersion = Column(SMALLINT, nullable=False)
    LogReceivedUTCTime = Column(DATETIME, nullable=False)
    LogReceivedTime = Column(DATETIME, nullable=False)
    LogReceivedTimeZone = Column(INTEGER, nullable=False)
    LogGenUTCDatetime = Column(DATETIME, nullable=False)
    LogGenLocalDatetime = Column(DATETIME, nullable=False)
    TimeZoneInMins = Column(SMALLINT, nullable=False)
    DaylightSavingInMins = Column(SMALLINT, nullable=False)
    ComputerName = Column(NVARCHAR(128), nullable=False)
    ClientGUID = Column(CHAR(36))
    EventID = Column(INTEGER)
    Status = Column(INTEGER)
    RuleID = Column(INTEGER)
    ChangeType = Column(INTEGER)
    UserName = Column(NVARCHAR(64))
    ProcessName = Column(NVARCHAR(512))
    Type = Column(VARCHAR(64))
    KeyToEntityLocation = Column(NVARCHAR(2000))
    Rank = Column(INTEGER)
    SeverityCode = Column(INTEGER)
    AssetValue = Column(INTEGER)
    ContentHashAfterChange = Column(VARCHAR(40))
    ContentHashBeforeChange = Column(VARCHAR(40))
    CLF_LogGenCMLocalTime = Column(DATETIME)
