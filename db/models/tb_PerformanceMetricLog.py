from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbPerformanceMetricLog(Base):
    __tablename__ = 'tb_PerformanceMetricLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36))
    CLF_MsgLogType = Column(INTEGER)
    CLF_EntityID = Column(CHAR(36))
    CLF_LogVersion = Column(INTEGER)
    CLF_LogMinorVersion = Column(VARCHAR(10))
    CLF_ManagerID = Column(CHAR(36))
    CLF_ComputerName = Column(NVARCHAR(128))
    CLF_ProductType = Column(INTEGER)
    CLF_ProductVersion = Column(VARCHAR(21))
    CLF_ProductPlatformCode = Column(INTEGER)
    CLF_ProductLanguageCode = Column(INTEGER)
    CLF_ServerityCode = Column(INTEGER)
    CLF_ComponentCode = Column(INTEGER)
    CLF_LogReplicatedFlag = Column(BIT)
    CLF_LogGenerationTime = Column(DATETIME)
    CLF_LogGenerationTimeZone = Column(VARCHAR(10))
    CLF_LogReceivedTime = Column(DATETIME)
    CLF_LogReceivedTimeZone = Column(VARCHAR(10))
    CLF_IsDayLightSaving = Column(INTEGER)
    CLF_ReasonCode = Column(VARCHAR(64))
    CLF_ReasonCodeSource = Column(INTEGER)
    CLF_ReasonCodeSymbol = Column(VARCHAR(64))
    CLF_ReasonCodeDescription = Column(NVARCHAR(1024))
    CLF_RedAlertID = Column(VARCHAR(36))
    PLF_SnapshotTime = Column(DATETIME)
    PLF_ServerName = Column(NVARCHAR(64))
    PLF_MetricType = Column(INTEGER)
    PLF_MetricValue = Column(NVARCHAR(32))
