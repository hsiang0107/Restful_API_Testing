from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbTotalWebSecurityCount(Base):
    __tablename__ = 'tb_TotalWebSecurityCount'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    TVC_SummaryTime = Column(DATETIME)
    BT_YEAR = Column(INTEGER, nullable=False)
    BT_MONTH = Column(INTEGER, nullable=False)
    BT_DAY = Column(INTEGER, nullable=False)
    CasStatus = Column(INTEGER)
    SLF_BlockingType = Column(INTEGER)
    BT_Count = Column(INTEGER)
    SLF_ObjectNameURL = Column(NVARCHAR(1024))
