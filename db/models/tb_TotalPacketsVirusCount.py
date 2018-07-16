from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbTotalPacketsVirusCount(Base):
    __tablename__ = 'tb_TotalPacketsVirusCount'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    SA_Pass = Column(INTEGER, nullable=False)
    SA_Drop = Column(INTEGER, nullable=False)
    SA_Quarantine = Column(INTEGER, nullable=False)
    SA_Total = Column(INTEGER, nullable=False)
    TVC_SummaryTime = Column(DATETIME)
    SA_YEAR = Column(INTEGER, nullable=False)
    SA_MONTH = Column(INTEGER, nullable=False)
    SA_DAY = Column(INTEGER, nullable=False)
    CasStatus = Column(INTEGER)
