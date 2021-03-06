from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbApplicationControlEvent(Base):
    __tablename__ = 'tb_ApplicationControlEvent'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    LogReceivedTime = Column(DATETIME)
    LogReceivedUTCTime = Column(DATETIME)
    LogReceivedTimeZone = Column(VARCHAR(10))
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_MsgType = Column(INTEGER)
    SLF_ClientGUID = Column(CHAR(36), nullable=False)
    SLF_ProductID = Column(SMALLINT)
    SLF_LogVersion = Column(SMALLINT, nullable=False)
    SLF_LogMinorVersion = Column(SMALLINT, nullable=False)
    SLF_ComputerName = Column(NVARCHAR(128))
    SLF_LogGenUTCDatetime = Column(DATETIME, nullable=False)
    SLF_LogGenLocalDatetime = Column(DATETIME, nullable=False)
    SLF_TimeZoneInMins = Column(SMALLINT, nullable=False)
    SLF_DaylightSavingInMins = Column(SMALLINT, nullable=False)
    SLF_ClientHostName = Column(NVARCHAR(64))
    SLF_ProductServerPatternVersion = Column(VARCHAR(64))
    SLF_ClientUserGUID = Column(CHAR(36))
    SLF_ClientUserName = Column(NVARCHAR(64))
    SLF_ClientUserDomain = Column(NVARCHAR(256))
    SLF_ClientUserDepartment = Column(NVARCHAR(256))
    SLF_ClientIPAddressList = Column(VARCHAR(256))
    SLF_ClientMachineArchitecture = Column(VARCHAR(64))
    SLF_ClientNotficationMessage = Column(NVARCHAR(256))
    SLF_ClientNotficationMessageUTCDatetime = Column(DATETIME)
    SLF_ClientSynchronizationUTCDatetime = Column(DATETIME(2))
    SLF_ClientPolicyChangedUTCDatetime = Column(DATETIME)
    SLF_ClientStatus = Column(SMALLINT)
    SLF_ApplicationFileHash = Column(VARCHAR(64))
    SLF_ApplicationFileName = Column(NVARCHAR(256))
    SLF_ApplicationFileCreatedUTCDatetime = Column(DATETIME)
    SLF_ApplicationFileModifiedUTCDatetime = Column(DATETIME)
    SLF_ApplicationFileOwner = Column(NVARCHAR(256))
    SLF_ApplicationPath = Column(NVARCHAR(512))
    SLF_ApplicationDriveType = Column(SMALLINT)
    SLF_ApplicationProcessName = Column(NVARCHAR(256))
    SLF_ApplicationProcessCommandline = Column(NVARCHAR(1024))
    SLF_ApplicationProcessOwner = Column(NVARCHAR(256))
    SLF_ApplicationExecutionEnvironment = Column(NVARCHAR(64))
    SLF_ApplicationGRIDCategory = Column(NVARCHAR(256))
    SLF_RuleContent = Column(NVARCHAR(256))
    SLF_RuleName = Column(NVARCHAR(256))
    SLF_RuleGUID = Column(CHAR(36))
    SLF_RuleType = Column(SMALLINT)
    SLF_PolicyName = Column(NVARCHAR(256))
    SLF_PolicyGUID = Column(CHAR(36))
    SLF_PolicyInfo = Column(NVARCHAR(256))
    SLF_PolicyAction = Column(SMALLINT)
    SLF_PolicyActionTriggerCount = Column(INTEGER)
    CE_FilterID = Column(VARCHAR(35))
    CLF_LogGenCMLocalTime = Column(DATETIME)
    SLF_ApplicationFileHashType = Column(SMALLINT)
    SLF_MatchedRuleMethod = Column(SMALLINT)
    SLF_Signer = Column(NVARCHAR(128))
