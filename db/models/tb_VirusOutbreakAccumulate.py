from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbVirusOutbreakAccumulate(Base):
    __tablename__ = 'tb_VirusOutbreakAccumulate'
    VLF_VirusName = Column(VARCHAR(64), primary_key=True)
    VOA_TotalForInstances = Column(INTEGER, nullable=False)
    VOA_TotalForDestinations = Column(INTEGER, nullable=False)
    VOA_RecordTime = Column(DATETIME)
    VOA_StartOfperiod = Column(DATETIME)
    VOA_EndOfperiod = Column(DATETIME)
    VOA_YEAR = Column(INTEGER, nullable=False)
    VOA_MONTH = Column(INTEGER, nullable=False)
    VOA_DAY = Column(INTEGER, nullable=False)
    VOA_RelayRecordTime = Column(DATETIME)
