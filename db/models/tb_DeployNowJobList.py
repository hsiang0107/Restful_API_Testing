from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbDeployNowJobList(Base):
    __tablename__ = 'tb_DeployNowJobList'
    MS_JobID = Column(CHAR(36), primary_key=True, nullable=False)
    MS_RcvDateTime = Column(DATETIME)
    MS_EntityID = Column(CHAR(36))
    MS_DstType = Column(INTEGER)
    MS_WaitTime = Column(INTEGER)
    MS_Status = Column(INTEGER)
    MS_Token = Column(VARCHAR(255), nullable=False)
