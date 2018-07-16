from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbDeploymentPlansTF(Base):
    __tablename__ = 'tb_DeploymentPlansTF'
    DPTF_PlanID = Column(CHAR(36))
    DPTF_ScheduleID = Column(CHAR(36), primary_key=True, nullable=False)
    DPTF_Hour = Column(INTEGER)
    DPTF_Min = Column(INTEGER)
    DPTF_Folders = Column(NVARCHAR(450))
