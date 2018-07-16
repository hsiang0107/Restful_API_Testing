from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbMessageDetectionURLThreatInfo(Base):
    __tablename__ = 'tb_MessageDetectionURLThreatInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Instance_ID = Column(VARCHAR(256))
    SLF_URL = Column(NVARCHAR(512), nullable=False)
    SLF_URLSHA1 = Column(VARCHAR(64), nullable=False)
    SLF_WRSCategoryIDList = Column(VARCHAR(64))
    SLF_WRSRating = Column(INTEGER)
    SLF_SBXDetectionName = Column(VARCHAR(64))
    SLF_SBXSubmissionTime = Column(DATETIME)
    SLF_SBXSubmissionRule = Column(VARCHAR(64))
    SLF_SBXRiskLevel = Column(INTEGER)
    SLF_SBXThreatCategories = Column(NVARCHAR(128))
    SLF_Is_CCCA_Detection = Column(INTEGER)
    SLF_CCCA_DetectionSource = Column(INTEGER)
    SLF_CCCA_RiskLevel = Column(INTEGER)
