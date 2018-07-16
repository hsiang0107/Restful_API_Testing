from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSecondFailureAccumulate(Base):
    __tablename__ = 'tb_SecondFailureAccumulate'
    SFA_VirusName = Column(VARCHAR(64), primary_key=True)
    SFA_TotalForInstances = Column(INTEGER)
    SFA_TotalForDestinations = Column(INTEGER)
    SFA_RecordTime = Column(DATETIME)
    SFA_StartOfperiod = Column(DATETIME)
    SFA_EndOfperiod = Column(DATETIME)
    SFA_YEAR = Column(INTEGER)
    SFA_MONTH = Column(INTEGER)
    SFA_DAY = Column(INTEGER)
