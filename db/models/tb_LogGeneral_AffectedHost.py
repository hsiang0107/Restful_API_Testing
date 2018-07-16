from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbLogGeneralAffectedHost(Base):
    __tablename__ = 'tb_LogGeneral_AffectedHost'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Date = Column(DATETIME)
    ProductGUID = Column(CHAR(36))
    InterestedIP = Column(VARCHAR(15))
    HostSeverity = Column(SMALLINT)
    ThreatEng_Detections = Column(INTEGER)
    VA_Detections = Column(INTEGER)
    PE_Count = Column(INTEGER)
    CC_Count = Column(INTEGER)
    LM_Count = Column(INTEGER)
    AD_Count = Column(INTEGER)
    DE_Count = Column(INTEGER)
    LatestDetectionTime = Column(DATETIME)
    IG_Count = Column(INTEGER)
