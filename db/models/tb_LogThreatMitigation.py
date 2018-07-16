from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbLogThreatMitigation(Base):
    __tablename__ = 'tb_LogThreatMitigation'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MsgLogType = Column(INTEGER)
    LogVersion = Column(SMALLINT)
    LogMinorVersion = Column(SMALLINT)
    SLF_ProductGUID = Column(CHAR(36))
    SLF_ProductID = Column(INTEGER)
    LogGenerationTime = Column(DATETIME)
    LogGenerationTimeZone = Column(VARCHAR(10))
    LogGenUTCDatetime = Column(DATETIME)
    LogReceivedTime = Column(DATETIME)
    LogReceivedUTCTime = Column(DATETIME)
    LogReceivedTimeZone = Column(VARCHAR(10))
    ComputerName = Column(NVARCHAR(128))
    DaylightSavingInMins = Column(INTEGER)
    CollaborationID = Column(NVARCHAR(128))
    EndpointIP = Column(NVARCHAR(256))
    Endpoint = Column(NVARCHAR(254))
    DataSource = Column(INTEGER)
    DataSourceHost = Column(NVARCHAR(254))
    ThreatDescription = Column(NVARCHAR(254))
    MitigationStatus = Column(INTEGER)
    MitigationDetails = Column(INTEGER)
