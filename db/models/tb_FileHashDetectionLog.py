from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbFileHashDetectionLog(Base):
    __tablename__ = 'tb_FileHashDetectionLog'
    id = Column(BIGINT, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    CMGuid = Column(CHAR(36))
    SLF_LogType = Column(INTEGER, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ProductID = Column(INTEGER, nullable=False)
    SLF_LogVersion = Column(INTEGER, nullable=False)
    SLF_LogMinorVersion = Column(INTEGER, nullable=False)
    SLF_ComputerName = Column(NVARCHAR(128), nullable=False)
    SLF_ProductVersion = Column(VARCHAR(21), nullable=False)
    SLF_LogGenerationTime = Column(DATETIME, nullable=False)
    SLF_LogGenerationTimeZone = Column(INTEGER, nullable=False)
    SLF_IsDayLightSaving = Column(SMALLINT, nullable=False)
    SLF_Sender = Column(NVARCHAR(254))
    SLF_Recipient = Column(NVARCHAR)
    SLF_Subject = Column(NVARCHAR(254))
    SLF_EntryChannel = Column(INTEGER)
    SLF_ClientGUID = Column(CHAR(36))
    SLF_ClientIP = Column(VARCHAR(256))
    SLF_HostName = Column(VARCHAR(128))
    SLF_TrueFileType = Column(VARCHAR(64))
    SLF_FileSHA1 = Column(VARCHAR(64), nullable=False)
    SLF_FileSource = Column(NVARCHAR(1024))
    SLF_SourceType = Column(SMALLINT, nullable=False)
    SLF_Action = Column(SMALLINT, nullable=False)
    SLF_ActionResult = Column(SMALLINT)
    SLF_ScanType = Column(SMALLINT, nullable=False)
    SLF_LogReceivedUTCTime = Column(DATETIME, nullable=False)
    SLF_FileCreatedUTCTime = Column(DATETIME, nullable=False)
    SLF_FileModifiedUTCTime = Column(DATETIME, nullable=False)
    CE_FilterID = Column(VARCHAR(35))
    CLF_LogGenCMLocalTime = Column(DATETIME)
