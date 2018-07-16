from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbCVWLog(Base):
    __tablename__ = 'tb_CVW_Log'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36))
    VLF_InfectionSource = Column(VARCHAR(254))
    VLF_InfectionDestination = Column(VARCHAR(254))
    CVW_ClientGUID = Column(CHAR(36))
    CVW_DetectedSite = Column(INTEGER)
    CVW_VirusCount = Column(INTEGER)
    CVW_FromTime = Column(DATETIME)
    CVW_ToTime = Column(DATETIME)
    CVW_LogReceivedTime = Column(DATETIME)
    VLF_VirusName = Column(NVARCHAR(256))
    CVW_DomainName = Column(NVARCHAR(128))
    CLF_EntityID = Column(CHAR(36))
    CLF_LogGenerationTimeZone = Column(INTEGER)
    CLF_IsDayLightSaving = Column(INTEGER)
    CLF_LogGenCMLocalTime = Column(DATETIME)
