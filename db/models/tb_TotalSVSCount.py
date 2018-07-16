from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbTotalSVSCount(Base):
    __tablename__ = 'tb_TotalSVSCount'
    SVS_ID = Column(INTEGER, primary_key=True)
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    SVS_Violation_Count = Column(INTEGER)
    TVC_SummaryTime = Column(DATETIME)
    CasStatus = Column(INTEGER)
