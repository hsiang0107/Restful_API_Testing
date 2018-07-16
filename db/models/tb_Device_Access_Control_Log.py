from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbDeviceAccessControlLog(Base):
    __tablename__ = 'tb_Device_Access_Control_Log'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    SLF_MsgType = Column(INTEGER)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ClientGUID = Column(CHAR(36))
    SLF_ProductID = Column(INTEGER)
    SLF_LogVersion = Column(INTEGER)
    SLF_LogMinorVersion = Column(INTEGER)
    SLF_LogGenUTCDatetime = Column(DATETIME)
    SLF_LogGenLocalDatetime = Column(DATETIME)
    SLF_TimeZoneInMins = Column(INTEGER)
    SLF_DaylightSavingInMins = Column(INTEGER)
    LogReceivedTime = Column(DATETIME)
    LogReceivedUTCTime = Column(DATETIME)
    LogReceivedTimeZone = Column(VARCHAR(10))
    SLF_ComputerName = Column(NVARCHAR(128))
    SLF_ProcessName = Column(NVARCHAR(256))
    SLF_FileName = Column(NVARCHAR(128))
    SLF_DeviceType = Column(INTEGER)
    SLF_Permission = Column(INTEGER)
    SLF_ClientUserGUID = Column(CHAR(36))
    CLF_LogGenCMLocalTime = Column(DATETIME)
