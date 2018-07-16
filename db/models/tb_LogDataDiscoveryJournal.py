from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbLogDataDiscoveryJournal(Base):
    __tablename__ = 'tb_LogDataDiscoveryJournal'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgID = Column(CHAR(36), nullable=False)
    SLF_MsgType = Column(INTEGER)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ProductID = Column(INTEGER)
    SLF_LogVersion = Column(INTEGER)
    SLF_LogMinorVersion = Column(INTEGER)
    SLF_JobID = Column(CHAR(36), nullable=False)
    SLF_TaskID = Column(CHAR(36), nullable=False)
    SLF_TaskName = Column(NVARCHAR(256), nullable=False)
    SLF_ComputerName = Column(NVARCHAR(256))
    SLF_ComputerDomain = Column(NVARCHAR(256))
    SLF_StartTime = Column(DATETIME)
    SLF_EndTime = Column(DATETIME)
    SLF_ErrorID = Column(INTEGER)
    SLF_SecurityDestination = Column(NVARCHAR(256))
    SLF_ScheduleRunTime = Column(DATETIME)
    SLF_ClientGUID = Column(CHAR(36))
    SLF_UserName = Column(NVARCHAR(64))
    SLF_UserDomain = Column(NVARCHAR(256))
    SLF_LogGenUTCDatetime = Column(DATETIME)
    SLF_LogGenLocalDatetime = Column(DATETIME)
    SLF_TimeZoneInMins = Column(INTEGER)
    LogReceivedTime = Column(DATETIME)
    LogReceivedUTCTime = Column(DATETIME)
    LogReceivedTimeZone = Column(VARCHAR(10))
