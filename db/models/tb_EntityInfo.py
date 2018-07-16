from sqlalchemy import Column
from sqlalchemy import and_
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR
from db import L10NTMCM


class TbEntityInfo(Base):
    __tablename__ = 'tb_EntityInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EI_EntityID = Column(CHAR(36), nullable=False)
    EI_AgentID = Column(CHAR(36), nullable=False)
    EI_ParentID = Column(CHAR(36), nullable=False)
    EI_ManagerID = Column(CHAR(36), nullable=False)
    EI_State = Column(INTEGER)
    EI_Type = Column(INTEGER)
    EI_SerialNumber = Column(VARCHAR(60))
    EI_ProductType = Column(INTEGER, nullable=False)
    EI_ProductVersion = Column(VARCHAR(19))
    EI_ProductLanguage = Column(INTEGER)
    EI_SetupTime = Column(DATETIME)
    EI_LastRegistrationTime = Column(DATETIME)
    EI_LastLogonTime = Column(DATETIME)
    EI_LastLogoffTime = Column(DATETIME)
    EI_CacheToken = Column(VARCHAR(256))
    EI_UpdateSourceID = Column(CHAR(36))
    EI_MenuVersion = Column(VARCHAR(8))
    EI_ProductBuildNumber = Column(VARCHAR(24))
    EI_LastStartupTime = Column(DATETIME)
    EI_PatternNumber = Column(VARCHAR(19))
    EI_PatternLastUpdateTime = Column(DATETIME)
    EI_SpamRuleNumber = Column(VARCHAR(8))
    EI_SpamRuleLastUpdateTime = Column(DATETIME)
    EI_SpamRuleFilename1 = Column(VARCHAR(16))
    EI_SpamRule1LastUpdateTime = Column(DATETIME)
    EI_SpamRuleFilename2 = Column(VARCHAR(16))
    EI_SpamRule2LastUpdateTime = Column(DATETIME)
    EI_DCTNumber = Column(VARCHAR(19))
    EI_DCTLastUpdateTime = Column(DATETIME)
    EI_OS_Name = Column(NVARCHAR(128))
    EI_OS_Version = Column(VARCHAR(64))
    EI_OS_SPVersion = Column(VARCHAR(32))
    EI_OS_Language = Column(INTEGER)
    EI_OS_ContryCode = Column(VARCHAR(8))
    EI_OS_MachineName = Column(NVARCHAR(64))
    EI_IPAddressList = Column(VARCHAR(1024))
    EI_MACAddressList = Column(VARCHAR(256))
    EI_DomainName = Column(NVARCHAR(64))
    EI_PrivateAttribute = Column(IMAGE)
    EI_Timezone = Column(VARCHAR(8))
    EI_LastNotifyTime = Column(DATETIME)
    EI_AgentVersion = Column(VARCHAR(64))
    EI_CAVRule = Column(VARCHAR(19))
    EI_CAVRuleUpdateTime = Column(DATETIME)
    EI_Pattern2Version = Column(VARCHAR(19))
    EI_Pattern2VersionUpdateTime = Column(DATETIME)
    EI_VATVersion = Column(VARCHAR(19))
    EI_VATVersionUpdateTime = Column(DATETIME)
    EI_VIVersion = Column(VARCHAR(19))
    EI_VIVersionUpdateTime = Column(DATETIME)
    EI_SpywareVersion = Column(VARCHAR(19))
    EI_SpywareLastUpdateTime = Column(DATETIME)
    EI_CFWVersion = Column(VARCHAR(19))
    EI_CFWLastUpdateTime = Column(DATETIME)
    EI_SpyCleanUpVersion = Column(VARCHAR(19))
    EI_SpyCleanUpLastUpdateTime = Column(DATETIME)
    EI_GroupName = Column(NVARCHAR(64))
    EI_ASpyVersion = Column(VARCHAR(19))
    EI_ASpyLastUpdateTime = Column(DATETIME)
    EI_AgentBuild = Column(INTEGER)
    EI_CloudScanMode = Column(SMALLINT)
    EI_CloudScanMethod = Column(SMALLINT)
    LUTonTMCM = Column(DATETIME)
    ADDomainID = Column(INTEGER)
    EI_ADObjectGuid = Column(UNIQUEIDENTIFIER)
    EI_ClientTreePath = Column(NVARCHAR(1000))
    EI_RealParentGuid = Column(CHAR(36))
    LogReceivedTime = Column(DATETIME)
    EI_PATTERN_TMA_SSA = Column(VARCHAR(19))
    EI_PATTERN_TMA_SSALastUpdateTime = Column(DATETIME)
    EI_UpdateAgentType = Column(INTEGER)
    EI_FQDN = Column(VARCHAR(80))
    EI_PolicyID = Column(UNIQUEIDENTIFIER)
    EI_PolicyFlag = Column(INTEGER)
    RTSSetting = Column(SMALLINT)
    PFWSetting = Column(SMALLINT)
    LastScheduleScanUTC = Column(DATETIME)
    LastManualScanUTC = Column(DATETIME)
    LastScanNowScanUTC = Column(DATETIME)
    EI_OS_Type = Column(VARCHAR(16))
    EI_Platform_Type = Column(VARCHAR(16))
    EI_MachineID = Column(CHAR(36))
    EI_UserGuid = Column(VARCHAR(36))
    EI_UserAccount = Column(NVARCHAR(32))
    EI_UserDomain = Column(NVARCHAR(256))
    EI_UserMail = Column(NVARCHAR(450))
    EI_SystemModel = Column(SMALLINT)
    EI_AD_DomainName = Column(NVARCHAR(64))
    EI_NetworkQuarantineSetting = Column(SMALLINT)
    EI_NetworkQuarantineAction = Column(SMALLINT)
    EI_NetworkQuarantineActionStatus = Column(SMALLINT)
    EI_NetworkQuarantineSettingResult = Column(SMALLINT)
    EI_IsOffPremise = Column(SMALLINT)
    EI_LastCompliantState = Column(BIGINT)
    EI_IsSaaSMode = Column(SMALLINT)
    EI_IsCoExist = Column(SMALLINT)
    EI_ServerCommunicationPort_HTTP = Column(INTEGER)
    EI_ServerCommunicationPort_HTTPS = Column(INTEGER)

    @classmethod
    def find_by_entityid(cls, entityid):
        return cm_session.query(cls).filter(cls.EI_EntityID == entityid).first()

    @classmethod
    def _get_server_type(cls, category, symbolic1, symbolic2, guid):
        statement = 'SELECT EI_EntityID FROM tb_EntityInfo WITH(NOLOCK) where EI_ProductType > (SELECT idmap FROM ' \
                    'L10NTMCM WHERE category = {0} AND symbolic = \'{1}\') and EI_ProductType < (SELECT idmap FROM ' \
                    'L10NTMCM WHERE category = {0} AND symbolic = \'{2}\') and EI_Type < 2 and EI_EntityID = \'{3}\''
        return cm_session.execute(statement.format(category, symbolic1, symbolic2, guid)).fetchone()

    @classmethod
    def is_wsi_server(cls, guid):
        server = cls._get_server_type('196', 'SLF_PRODUCT_START', 'SLF_PRODUCT_END', guid)
        return True if server else False

    @classmethod
    def is_saas_server(cls, guid):
        server = cls._get_server_type('195', 'SLF_PRODUCT_SCOSTART', 'SLF_PRODUCT_SCOEND', guid)
        return True if server else False

    @classmethod
    def find_by_machine_name(cls, name):
        return cm_session.query(cls).filter(cls.EI_OS_MachineName == name).first()
