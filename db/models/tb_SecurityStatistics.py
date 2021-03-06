from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbSecurityStatistics(Base):
    __tablename__ = 'tb_SecurityStatistics'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36))
    CLF_MsgLogType = Column(INTEGER)
    CLF_EntityID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER)
    CLF_LogVersion = Column(INTEGER)
    CLF_LogMinorVersion = Column(VARCHAR(10))
    CLF_ManagerID = Column(CHAR(36))
    CLF_ComputerName = Column(NVARCHAR(128))
    CLF_ProductVersion = Column(VARCHAR(32))
    CLF_ProductPlatformCode = Column(INTEGER)
    CLF_ProductLanguageCode = Column(INTEGER)
    CLF_ServerityCode = Column(INTEGER)
    CLF_ComponentCode = Column(INTEGER)
    CLF_LogGenerationTime = Column(DATETIME)
    CLF_LogGenerationTimeZone = Column(VARCHAR(10))
    CLF_LogReceivedTime = Column(DATETIME)
    CLF_LogReceivedTimeZone = Column(VARCHAR(10))
    CLF_IsDayLightSaving = Column(INTEGER)
    CLF_ReasonCode = Column(VARCHAR(64))
    CLF_ReasonCodeSource = Column(INTEGER)
    CLF_ReasonCodeDescription = Column(NVARCHAR(1024))
    SVS_Name = Column(NVARCHAR(64))
    SVS_ID = Column(INTEGER)
    SVS_Violation_Count = Column(INTEGER)
