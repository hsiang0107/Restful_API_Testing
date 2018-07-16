from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, VARCHAR


class TbScheduleDownload(Base):
    __tablename__ = 'tb_ScheduleDownload'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    SD_ComponentID = Column(INTEGER)
    SD_Enable = Column(BIT)
    SD_Frequency = Column(INTEGER)
    SD_TargetTime = Column(DATETIME)
    SD_FrequencyNRange = Column(INTEGER)
    SD_FrequencyWeekday = Column(INTEGER)
    SD_AutoDeployOption = Column(INTEGER)
    SD_DeploymentPlanID = Column(VARCHAR(50))
    SD_UpdateSource = Column(VARCHAR(2048))
    SD_EnableRetry = Column(BIT)
    SD_RetryTimes = Column(INTEGER)
    SD_ReDoNeeded = Column(INTEGER)
    SD_RetryPeriod = Column(INTEGER)
    SD_UpdateSourceType = Column(INTEGER)
    SD_TaskType = Column(INTEGER)
    SD_DetailedSettings = Column(VARCHAR(1024))
    SD_RedAlertID = Column(CHAR(36))
    SD_MMPIDs = Column(INTEGER)
    SD_IsIndividual = Column(INTEGER)
    SD_PatternMask = Column(VARCHAR(1024))
    SD_SpamRuleMask = Column(VARCHAR(1024))
    SD_EngineMask = Column(VARCHAR(1024))
    SD_Language = Column(INTEGER)
    SD_Platform = Column(INTEGER)
    SD_ProductID = Column(INTEGER)
