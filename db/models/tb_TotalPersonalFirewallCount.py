from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbTotalPersonalFirewallCount(Base):
    __tablename__ = 'tb_TotalPersonalFirewallCount'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    PFW_Accepted = Column(INTEGER)
    PFW_Dropped = Column(INTEGER)
    PFW_Rejected = Column(INTEGER)
    PFW_Reset = Column(INTEGER)
    PFW_Asked = Column(INTEGER)
    PFW_Unknown = Column(INTEGER)
    PFW_Total = Column(INTEGER)
    TVC_SummaryTime = Column(DATETIME, nullable=False)
    PFW_YEAR = Column(INTEGER, nullable=False)
    PFW_MONTH = Column(INTEGER, nullable=False)
    PFW_DAY = Column(INTEGER, nullable=False)
    CasStatus = Column(INTEGER, nullable=False)
