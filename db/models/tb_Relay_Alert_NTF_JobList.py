from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbRelayAlertNTFJobList(Base):
    __tablename__ = 'tb_Relay_Alert_NTF_JobList'
    JOBID = Column(CHAR(36), primary_key=True, nullable=False)
    JobID2 = Column(UNIQUEIDENTIFIER)
    ANJ_RedAlertID = Column(CHAR(36))
    USER_ID = Column(VARCHAR(38))
    Entity_ID = Column(VARCHAR(38))
    Event_ID = Column(VARCHAR(64))
    ComponentID = Column(VARCHAR(64))
    CLF_ProductType = Column(INTEGER, nullable=False)
    CLF_ProductName = Column(VARCHAR(128))
    CLF_ProductVersion = Column(VARCHAR(21))
    CLF_LogGenerationTime = Column(DATETIME)
    CLF_LogGenerationTimeZone = Column(INTEGER)
    CLF_ComputerName = Column(NVARCHAR(128))
    VLF_VirusName = Column(VARCHAR(64))
    VLF_VirusCount = Column(INTEGER, nullable=False)
    VLF_InfectionSource = Column(NVARCHAR(254))
    VLF_InfectionDestination = Column(NVARCHAR(254))
    VLF_FileName = Column(NVARCHAR(254))
    VLF_FilePath = Column(NVARCHAR(254))
    VLF_EngineVersion = Column(VARCHAR(19))
    VLF_PatternNumber = Column(VARCHAR(19))
    VOA_RecordTime = Column(DATETIME)
    VOA_StartOfperiod = Column(DATETIME)
    VOA_EndOfperiod = Column(DATETIME)
    NJL_TaskState = Column(INTEGER)
    NJL_RetryTime = Column(INTEGER)
    NJL_FailMethod = Column(INTEGER)
    Result = Column(INTEGER)
    VOA_YEAR = Column(INTEGER, nullable=False)
    VOA_MONTH = Column(INTEGER, nullable=False)
    VOA_DAY = Column(INTEGER, nullable=False)
    GS_ScanAction = Column(INTEGER)
    VLF_FunctionCode = Column(INTEGER)
    LoginUser = Column(NVARCHAR(254))
    CLF_ProductServer = Column(NVARCHAR(128))
    CLF_IsDayLightSaving = Column(INTEGER)
