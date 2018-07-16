from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbDeploymentPlanTargets(Base):
    __tablename__ = 'tb_DeploymentPlanTargets'
    DPT_CommandTrackingID = Column(CHAR(36), primary_key=True, nullable=False)
    DPT_EntityCount = Column(INTEGER)
