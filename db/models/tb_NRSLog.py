from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbNRSLog(Base):
    __tablename__ = 'tb_NRSLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MsgLogType = Column(INTEGER)
    ProductGUID = Column(CHAR(36))
    ProductID = Column(INTEGER)
    LogVersion = Column(INTEGER)
    LogMinorVersion = Column(INTEGER)
    ComputerName = Column(NVARCHAR(128))
    LogGenUTCDatetime = Column(DATETIME)
    LogGenLocalDatetime = Column(DATETIME)
    TimeZoneInMins = Column(INTEGER)
    DaylightSavingInMins = Column(INTEGER)
    NRS_BlockedIP = Column(VARCHAR(256))
    NRS_FilterType = Column(INTEGER)
    NRS_FilterAction = Column(INTEGER)
    LogReceivedTime = Column(DATETIME)
    AggregatedUTCDatetime = Column(DATETIME)
    AggregatedLocalDatetime = Column(DATETIME)
    AggregatedCount = Column(INTEGER)
    CLF_LogGenCMLocalTime = Column(DATETIME)
