from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbAVEventLog(Base):
    __tablename__ = 'tb_AVEventLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36))
    CLF_MsgLogType = Column(INTEGER)
    CLF_LogMinorVersion = Column(VARCHAR(10))
    CLF_EntityID = Column(CHAR(36))
    CLF_ManagerID = Column(CHAR(36))
    CLF_LogVersion = Column(INTEGER)
    CLF_ProductType = Column(INTEGER)
    CLF_ProductVersion = Column(VARCHAR(21))
    CLF_ProductLanguageCode = Column(INTEGER)
    CLF_LogGenerationTime = Column(DATETIME)
    CLF_LogGenerationTimeZone = Column(VARCHAR(10))
    CLF_LogReceivedTime = Column(DATETIME)
    CLF_LogReceivedTimeZone = Column(VARCHAR(10))
    CLF_ServerityCode = Column(INTEGER)
    CLF_ComponentCode = Column(INTEGER)
    CLF_LogReplicatedFlag = Column(BIT)
    CLF_ComputerName = Column(NVARCHAR(128))
    CLF_ProductPlatformCode = Column(INTEGER)
    CLF_IsDayLightSaving = Column(INTEGER)
    CLF_ReasonCode = Column(VARCHAR(64))
    CLF_ReasonCodeSource = Column(INTEGER)
    ELF_EventType = Column(INTEGER)
    ELF_CommandStatusCode = Column(INTEGER, nullable=False)
    ELF_ErrorDescription = Column(NVARCHAR(1024))
    ELF_TrackingID = Column(CHAR(36), nullable=False)
    ELF_Private_Detail = Column(IMAGE)
