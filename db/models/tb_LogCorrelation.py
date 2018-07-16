from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbLogCorrelation(Base):
    __tablename__ = 'tb_LogCorrelation'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgType = Column(INTEGER, nullable=False)
    ProductGUID = Column(CHAR(36), nullable=False)
    ProductID = Column(INTEGER, nullable=False)
    LogVersion = Column(SMALLINT)
    LogMinorVersion = Column(SMALLINT)
    LogGenUTCDatetime = Column(DATETIME, nullable=False)
    LogGenLocalDatetime = Column(DATETIME, nullable=False)
    LogReceivedTime = Column(DATETIME)
    TimeZoneInMins = Column(SMALLINT)
    DaylightSavingInMins = Column(INTEGER)
    ScanDirection = Column(INTEGER)
    InterestedIP = Column(VARCHAR(256))
    InterestedHostName = Column(VARCHAR(256))
    InterestedMac = Column(VARCHAR(17))
    InterestedGroup = Column(NVARCHAR(128))
    Protocol = Column(INTEGER)
    ThreatKBID = Column(INTEGER)
    ThreatTypeDescription = Column(VARCHAR(64))
    SeverityCode = Column(INTEGER)
    DetectionName = Column(VARCHAR(64))
    UserName = Column(NVARCHAR(64))
    RuleICID = Column(INTEGER)
    Description = Column(VARCHAR(256))
    UserDefineData = Column(NVARCHAR(2048))
