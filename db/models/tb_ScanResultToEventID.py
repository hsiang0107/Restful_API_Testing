from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbScanResultToEventID(Base):
    __tablename__ = 'tb_ScanResultToEventID'
    MajorVirusType = Column(INTEGER, primary_key=True, nullable=False)
    ScanResult = Column(INTEGER, primary_key=True, nullable=False)
    EventId = Column(VARCHAR(100), primary_key=True, nullable=False)
