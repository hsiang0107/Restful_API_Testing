from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, IMAGE, NVARCHAR


class TbDeploymentPlans(Base):
    __tablename__ = 'tb_DeploymentPlans'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    DP_PlanName = Column(NVARCHAR(64), nullable=False)
    DP_TimeFolder = Column(IMAGE)
