from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class Tbstatuslogjournal(Base):
    __tablename__ = 'tb_statuslogjournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ProductID = Column(INTEGER)
    SLF_ComputerName = Column(NVARCHAR(64))
    SLF_LogGenUTCDatetime = Column(DATETIME)
    SLF_LogGenLocalDatetime = Column(DATETIME)
    SLF_TimeZoneInMins = Column(INTEGER)
    SLF_DaylightSavingInMins = Column(INTEGER)
    SLF_Status = Column(INTEGER)
    SLF_UpdateAgentType = Column(INTEGER)
    SLF_LastStartupTime = Column(DATETIME)
    lutontmcm = Column(DATETIME)
    EI_DomainName = Column(NVARCHAR(64))
    EI_OS_Name = Column(NVARCHAR(128))
    EI_OS_Version = Column(VARCHAR(64))
    EI_OS_SPVersion = Column(VARCHAR(32))
    EI_OS_Language = Column(INTEGER)
    EI_OS_ContryCode = Column(VARCHAR(8))
    EI_UserGuid = Column(CHAR(36))
    EI_UserAccount = Column(NVARCHAR(32))
    EI_UserDomain = Column(NVARCHAR(256))
    EI_SystemModel = Column(SMALLINT)
    EI_ParentGuid = Column(CHAR(36))
    EI_UserMail = Column(NVARCHAR(450))
    EI_NetworkQuarantineSetting = Column(SMALLINT)
    EI_NetworkQuarantineSettingResult = Column(SMALLINT)
    EI_IsOffPremise = Column(SMALLINT)
    SLF_LastCompliantState = Column(BIGINT)
    SLF_LastLogonTime = Column(DATETIME)
    SLF_LastLogoffTime = Column(DATETIME)
    EI_IsCoExist = Column(SMALLINT)
