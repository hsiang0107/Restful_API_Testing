from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSecondSuccessAccumulate(Base):
    __tablename__ = 'tb_SecondSuccessAccumulate'
    SSA_VirusName = Column(VARCHAR(64), primary_key=True)
    SSA_TotalForInstances = Column(INTEGER)
    SSA_TotalForDestinations = Column(INTEGER)
    SSA_RecordTime = Column(DATETIME)
    SSA_StartOfperiod = Column(DATETIME)
    SSA_EndOfperiod = Column(DATETIME)
    SSA_YEAR = Column(INTEGER)
    SSA_MONTH = Column(INTEGER)
    SSA_DAY = Column(INTEGER)
