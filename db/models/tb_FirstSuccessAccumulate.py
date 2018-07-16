from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbFirstSuccessAccumulate(Base):
    __tablename__ = 'tb_FirstSuccessAccumulate'
    FSA_VirusName = Column(VARCHAR(64), primary_key=True)
    FSA_TotalForInstances = Column(INTEGER)
    FSA_TotalForDestinations = Column(INTEGER)
    FSA_RecordTime = Column(DATETIME)
    FSA_StartOfperiod = Column(DATETIME)
    FSA_EndOfperiod = Column(DATETIME)
    FSA_YEAR = Column(INTEGER)
    FSA_MONTH = Column(INTEGER)
    FSA_DAY = Column(INTEGER)
