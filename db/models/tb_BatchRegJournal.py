from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbBatchRegJournal(Base):
    __tablename__ = 'tb_BatchRegJournal'
    id = Column(INTEGER, primary_key=True, nullable=False)
    GUID = Column(CHAR(36), nullable=False)
    CmdType = Column(SMALLINT, nullable=False)
    RegReceivedTime = Column(DATETIME, nullable=False)
    ParentGUID = Column(CHAR(36))
    SLF_AgentGUID = Column(CHAR(36))
    SLF_ManagerID = Column(CHAR(36))
    SLF_DisplayName = Column(NVARCHAR(64))
    SLF_FolderPath = Column(NVARCHAR(64))
    SLF_Status = Column(INTEGER)
    SLF_IconName = Column(VARCHAR(128))
    SLF_EntityType = Column(INTEGER)
    SLF_ProductID = Column(INTEGER)
    SLF_ProductName = Column(VARCHAR(64))
    SLF_ProductVersion = Column(VARCHAR(19))
    SLF_MenuVersion = Column(VARCHAR(8))
    SLF_ProductLanguageCode = Column(INTEGER)
    SLF_ProductBuildNumber = Column(VARCHAR(24))
    SLF_ProtocolName = Column(VARCHAR(8))
    SLF_Port = Column(VARCHAR(8))
    SLF_VirtualPath = Column(VARCHAR(64))
    SLF_FQDN = Column(VARCHAR(80))
    SLF_DomainName = Column(NVARCHAR(64))
    SLF_ComputerName = Column(NVARCHAR(64))
    SLF_TimeZone = Column(VARCHAR(8))
    SLF_TimeSaving = Column(SMALLINT)
    SLF_OSName = Column(NVARCHAR(128))
    SLF_OSVersion = Column(VARCHAR(64))
    SLF_OSServicePackVersion = Column(VARCHAR(32))
    SLF_OSLanguage = Column(INTEGER)
    SLF_OSCountryCode = Column(VARCHAR(8))
    SLF_CpuType = Column(SMALLINT)
    SLF_ConfigURL = Column(VARCHAR(509))
    SLF_UrlAuthID = Column(VARCHAR(64))
    SLF_UrlAuthPasswd = Column(VARCHAR(8))
    SLF_HeartBeatFrequency = Column(INTEGER)
    SLF_PollingFrequency = Column(INTEGER)
    SLF_MACAddressList = Column(VARCHAR(256))
    SLF_IPAddressList = Column(VARCHAR(1024))
    SLF_AgentVersion = Column(VARCHAR(64))
    SLF_AgentBuildNumber = Column(INTEGER)
    RegResult = Column(VARCHAR(16))
