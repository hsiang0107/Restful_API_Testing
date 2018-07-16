from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbVASJob(Base):
    __tablename__ = 'tb_VASJob'
    VAS_JobID = Column(INTEGER, primary_key=True, nullable=False)
    VAS_TaskID = Column(INTEGER, nullable=False)
    VAS_TaskName = Column(NVARCHAR(64))
    VAS_StartTime = Column(DATETIME, nullable=False)
    VAS_EndTime = Column(DATETIME, nullable=False)
    VAS_IssuedBy = Column(NVARCHAR(32))
    VAS_EngineVersion = Column(VARCHAR(19), nullable=False)
    VAS_TemplateNumber = Column(VARCHAR(19), nullable=False)
    VAS_Properties = Column(INTEGER, nullable=False)
    VAS_CriticalRisk = Column(INTEGER, nullable=False)
    VAS_ImportantRisk = Column(INTEGER, nullable=False)
    VAS_ModerateRisk = Column(INTEGER, nullable=False)
    VAS_LowRisk = Column(INTEGER, nullable=False)
    VAS_RiskFree = Column(INTEGER, nullable=False)
    VAS_DeployFailed = Column(INTEGER, nullable=False)
    VAS_Unsupported = Column(INTEGER, nullable=False)
    VAS_Restricted = Column(INTEGER, nullable=False)
    VAS_InProgress = Column(INTEGER, nullable=False)
    VAS_Total = Column(INTEGER, nullable=False)
