from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbTotalSpywareCount(Base):
    __tablename__ = 'tb_TotalSpywareCount'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    TSC_ActionResult = Column(INTEGER, nullable=False)
    TSC_Total = Column(INTEGER, nullable=False)
    TSC_YEAR = Column(INTEGER, nullable=False)
    TSC_MONTH = Column(INTEGER, nullable=False)
    TSC_DAY = Column(INTEGER, nullable=False)
    TSC_SummaryTime = Column(DATETIME)
    CasStatus = Column(INTEGER)
