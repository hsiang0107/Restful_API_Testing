from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbAVVirusLog(Base):
    __tablename__ = 'tb_AVVirusLog'
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
    CLF_LogReceivedUTCTime = Column(DATETIME)
    CLF_LogReceivedTimeZone = Column(VARCHAR(10))
    CLF_ServerityCode = Column(INTEGER)
    CLF_ComponentCode = Column(INTEGER)
    CLF_LogReplicatedFlag = Column(BIT)
    CLF_ComputerName = Column(NVARCHAR(128))
    CLF_ProductPlatformCode = Column(INTEGER)
    CLF_IsDayLightSaving = Column(INTEGER)
    CLF_ReasonCode = Column(VARCHAR(64))
    CLF_ReasonCodeSource = Column(INTEGER)
    VLF_VirusLogType = Column(INTEGER)
    VLF_VirusName = Column(NVARCHAR(64))
    VLF_IsMoreThanOneVirus = Column(BIT)
    VLF_FunctionCode = Column(INTEGER)
    VLF_FirstAction = Column(INTEGER)
    VLF_SecondAction = Column(INTEGER)
    VLF_FirstActionResult = Column(INTEGER)
    VLF_SecondActionResult = Column(INTEGER)
    VLF_FileName = Column(NVARCHAR(254))
    VLF_FilePath = Column(NVARCHAR(254))
    VLF_FileNameInCompressedFile = Column(NVARCHAR(254))
    VLF_InfectionSource = Column(NVARCHAR(254))
    VLF_InfectionDestination = Column(NVARCHAR(254))
    VLF_EngineType = Column(VARCHAR(19))
    VLF_EngineVersion = Column(VARCHAR(19))
    VLF_PatternType = Column(INTEGER)
    VLF_PatternNumber = Column(VARCHAR(19))
    SIC_RuleName = Column(NVARCHAR(64))
    MVL_Protocol = Column(VARCHAR(32))
    MVL_DeliverTime = Column(DATETIME)
    MVL_StorageGroup = Column(NVARCHAR(64))
    MVL_DataBaseName = Column(NVARCHAR(64))
    MVL_FolderName = Column(NVARCHAR(256))
    MVL_MessageID = Column(NVARCHAR(38))
    DVL_ClientIPAddress = Column(VARCHAR(256))
    DVL_ResultCode = Column(INTEGER)
    FVL_InfectTarget = Column(NVARCHAR(32))
    FVL_LoginUser = Column(NVARCHAR(32))
    MVL_Subject = Column(NVARCHAR(512))
    DCS_JobID = Column(INTEGER)
    DCS_TaskID = Column(INTEGER)
    VLF_MajorVirusType = Column(INTEGER)
    VLF_SubVirusType = Column(INTEGER)
    VLF_PrivateAttribute = Column(IMAGE)
    VLF_ClientGUID = Column(CHAR(36))
    AggregatedCount = Column(INTEGER)
    AggregatedLocalToTime = Column(DATETIME)
    AggregatedUTCToTime = Column(DATETIME)
    SourceIP = Column(VARCHAR(256))
    DestIP = Column(VARCHAR(256))
    UserGroupName = Column(NVARCHAR(128))
    SLF_FileSHA1 = Column(VARCHAR(64))
    SLF_CloudStorage = Column(INTEGER)
    CE_FilterID = Column(VARCHAR(35))
    SLF_Channel = Column(INTEGER)
    CLF_LogGenCMLocalTime = Column(DATETIME)
