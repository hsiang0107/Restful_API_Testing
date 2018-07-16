from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR


class TbDeploymentPlanTasks(Base):
    __tablename__ = 'tb_DeploymentPlanTasks'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    DPT_PlanID = Column(CHAR(36), nullable=False)
    DPT_CmdID = Column(INTEGER)
    DPT_Status = Column(INTEGER)
    DPT_CmdType = Column(INTEGER)
    DPT_StartupTime = Column(DATETIME)
    DPT_LUT = Column(DATETIME)
    DPT_ExtraData = Column(NVARCHAR(128))
    DPT_CmdStream = Column(IMAGE)
