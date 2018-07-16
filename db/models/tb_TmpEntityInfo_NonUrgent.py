from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BIT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbTmpEntityInfoNonUrgent(Base):
    __tablename__ = 'tb_TmpEntityInfo_NonUrgent'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Entity_SeqID = Column(INTEGER, nullable=False)
    EI_EntityID = Column(CHAR(36), nullable=False)
    EI_ProductType = Column(INTEGER)
    EI_ProductVersion = Column(VARCHAR(19))
    EI_MenuVersion = Column(VARCHAR(8))
    EI_ProductLanguage = Column(INTEGER)
    EI_ProductBuildNumber = Column(VARCHAR(24))
    EI_ADObjectGuid = Column(UNIQUEIDENTIFIER)
    EI_ClientTreePath = Column(NVARCHAR(1000))
    EI_RealParentGuid = Column(CHAR(36))
    EI_UpdateAgentType = Column(INTEGER)
    RTSSetting = Column(SMALLINT)
    PFWSetting = Column(SMALLINT)
    LastScheduleScanUTC = Column(DATETIME)
    LastManualScanUTC = Column(DATETIME)
    LastScanNowScanUTC = Column(DATETIME)
    Ext_DirtyRecord = Column(BIT)
    EI_IsOffPremise = Column(SMALLINT)
    EI_LastCompliantState = Column(BIGINT)
    EI_IsCoExist = Column(SMALLINT)
