from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbDDESTask(Base):
    __tablename__ = 'tb_DDES_Task'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CreatorGUID = Column(CHAR(36))
    TaskGUID = Column(CHAR(36))
    Status = Column(SMALLINT)
    AtRiskCnt = Column(INTEGER)
    SafeCnt = Column(INTEGER)
    PendingCnt = Column(INTEGER)
    TotalCnt = Column(INTEGER)
    RetrieveID = Column(INTEGER)
    IOC_GUID = Column(CHAR(36))
    Parameters_JSON = Column(NVARCHAR)
    InvestigateTime = Column(DATETIME)
    LastUpdateTime = Column(DATETIME)
    TriggerSource = Column(NVARCHAR)
