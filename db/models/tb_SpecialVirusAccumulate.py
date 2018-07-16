from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSpecialVirusAccumulate(Base):
    __tablename__ = 'tb_SpecialVirusAccumulate'
    VLF_VirusName = Column(VARCHAR(64), primary_key=True)
    SVA_TotalInstances = Column(INTEGER, nullable=False)
    SVA_RecordTime = Column(DATETIME)
    SVA_YEAR = Column(INTEGER, nullable=False)
    SVA_MONTH = Column(INTEGER, nullable=False)
    SVA_DAY = Column(INTEGER, nullable=False)
    SVA_RelayRecordTime = Column(DATETIME)
