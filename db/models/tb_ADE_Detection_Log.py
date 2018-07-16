from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbADEDetectionLog(Base):
    __tablename__ = 'tb_ADE_Detection_Log'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    CLF_LogReceivedTime = Column(DATETIME, nullable=False)
    SLF_MsgType = Column(INTEGER, nullable=False)
    SLF_LogVersion = Column(INTEGER, nullable=False)
    SLF_LogMinorVersion = Column(INTEGER, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ProductID = Column(INTEGER, nullable=False)
    SLF_ComputerName = Column(NVARCHAR(128))
    SLF_ProductVersion = Column(VARCHAR(21), nullable=False)
    SLF_LogGenerationTime = Column(DATETIME, nullable=False)
    SLF_LogGenerationTimeZone = Column(INTEGER, nullable=False)
    SLF_IsDayLightSaving = Column(BIT, nullable=False)
    SLF_ClientGUID = Column(CHAR(36))
    SLF_HostName = Column(NVARCHAR(128))
    SLF_ClientIP = Column(VARCHAR(256))
    SLF_UserName = Column(NVARCHAR(128))
    SLF_InstanceID = Column(CHAR(36))
    SLF_RiskLevel = Column(INTEGER, nullable=False)
    SLF_LogLevel = Column(INTEGER, nullable=False)
    SLF_IsHidden = Column(BIT, nullable=False)
    SLF_PatternNumber = Column(VARCHAR(128))
    SLF_RuleID = Column(NVARCHAR(128), nullable=False)
    SLF_CategoryID = Column(NVARCHAR(128), nullable=False)
    SLF_HasDetailTrace = Column(INTEGER)
