from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbLogBlacklistInfoJournal(Base):
    __tablename__ = 'tb_LogBlacklistInfoJournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    SLF_Action = Column(SMALLINT, nullable=False)
    SLF_Type = Column(INTEGER, nullable=False)
    SLF_Data = Column(NVARCHAR, nullable=False)
    SLF_RiskLevel = Column(INTEGER, nullable=False)
    SLF_ExpireDateTimeStamp = Column(BIGINT, nullable=False)
    ViolatedDTASPolicy = Column(VARCHAR(256))
    SourceFileSHA1 = Column(VARCHAR(64))
    Detectable = Column(SMALLINT)
    FilterCRC = Column(VARCHAR(64))
    SubmitTime = Column(DATETIME)
    AnalyzeTime = Column(DATETIME)
    FileName = Column(NVARCHAR)
    TrueFileType = Column(NVARCHAR(64))
    SubmitterProductName = Column(NVARCHAR(64))
    SubmitterHostName = Column(NVARCHAR(64))
    SubmitterIPAddress = Column(VARCHAR(128))
    DetectionName = Column(NVARCHAR(1024))
    ThreatCharacteristics = Column(NVARCHAR(128))
    SampleIdentity = Column(NVARCHAR)
    AnalyzeReportID = Column(VARCHAR(128))
    Protocol = Column(INTEGER)
    Source = Column(NVARCHAR(1024))
    Destination = Column(NVARCHAR(1024))
    RootFileSHA1 = Column(VARCHAR(128))
    DataMD5 = Column(VARCHAR(256))
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    ScanAction = Column(SMALLINT)
    SourceType = Column(SMALLINT)
    SoStatus = Column(SMALLINT)
    SOSyncFrom = Column(NVARCHAR(1024))
