from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbNetworkContentInspectionEngineLog(Base):
    __tablename__ = 'tb_Network_Content_Inspection_Engine_Log'
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
    SLF_SourceIP = Column(VARCHAR(256))
    SLF_SourcePort = Column(INTEGER)
    SLF_DestinationIP = Column(VARCHAR(256))
    SLF_DestinationPort = Column(INTEGER)
    SLF_Action = Column(INTEGER)
    SLF_Direction = Column(INTEGER)
    SLF_PatternType = Column(INTEGER)
    SLF_Is_CCCA_Detection = Column(INTEGER)
    SLF_CCCA_DetectionSource = Column(INTEGER)
    SLF_CCCA_RiskLevel = Column(INTEGER)
    NCIE_ThreatName = Column(NVARCHAR(64))
    CE_FilterID = Column(VARCHAR(35))
    SLF_DestinationDomain = Column(NVARCHAR(256))
    CLF_LogGenCMLocalTime = Column(DATETIME)
