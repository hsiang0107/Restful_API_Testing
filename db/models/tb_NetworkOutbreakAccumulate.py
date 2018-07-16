from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbNetworkOutbreakAccumulate(Base):
    __tablename__ = 'tb_NetworkOutbreakAccumulate'
    VLF_VirusName = Column(VARCHAR(64), primary_key=True)
    VOA_TotalForInstances = Column(INTEGER)
    VOA_TotalForDestinations = Column(INTEGER)
    VOA_RecordTime = Column(DATETIME)
    VOA_StartOfperiod = Column(DATETIME)
    VOA_EndOfperiod = Column(DATETIME)
    VOA_YEAR = Column(INTEGER)
    VOA_MONTH = Column(INTEGER)
    VOA_DAY = Column(INTEGER)
    VOA_RelayRecordTime = Column(DATETIME)
