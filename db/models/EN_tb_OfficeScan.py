from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class ENtbOfficeScan(Base):
    __tablename__ = 'EN_tb_OfficeScan'
    RID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_LogGenerationTime = Column(DATETIME)
    SLF_LogGenerationTimeZone = Column(INTEGER)
    SLF_IsDayLightSaving = Column(INTEGER)
    CLF_LogReceivedTime = Column(DATETIME)
    CLF_LogReceivedTimeZone = Column(INTEGER)
    EntityID = Column(CHAR(36), nullable=False)
    HostName = Column(NVARCHAR(64))
    OSName = Column(NVARCHAR(64))
    IPAddress = Column(VARCHAR(256))
    GroupName = Column(NVARCHAR(64))
    PatternNumber = Column(VARCHAR(19))
    InternalPatternNumber = Column(VARCHAR(19))
    EngineVersion = Column(VARCHAR(19))
    EngineType = Column(INTEGER)
    ProgramVersion = Column(VARCHAR(19))
    Status = Column(INTEGER)
