from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, INTEGER, VARCHAR


class TbManualDownload(Base):
    __tablename__ = 'tb_ManualDownload'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    MD_SelectedComponents = Column(INTEGER)
    MD_AutoDeployOption = Column(INTEGER)
    MD_DeploymentPlanID = Column(VARCHAR(50))
    MD_UpdateSource = Column(VARCHAR(2048))
    MD_EnableRetry = Column(BIT)
    MD_RetryTimes = Column(INTEGER)
    MD_RetryPeriod = Column(INTEGER)
    MD_UpdateSourceType = Column(INTEGER)
    MD_MMPIDs = Column(INTEGER)
    MD_PatternMask = Column(VARCHAR(64))
    MD_SpamRuleMask = Column(VARCHAR(64))
    MD_EngineMask = Column(VARCHAR(64))
