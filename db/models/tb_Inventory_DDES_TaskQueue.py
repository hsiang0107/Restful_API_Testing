from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, INTEGER, TINYINT


class TbInventoryDDESTaskQueue(Base):
    __tablename__ = 'tb_Inventory_DDES_TaskQueue'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ScanCriteria_MD5 = Column(BINARY(16), nullable=False)
    ThreatContent_MD5 = Column(BINARY(16), nullable=False)
    ThreatType = Column(INTEGER, nullable=False)
    IsManual = Column(TINYINT)
    IsOutgoing = Column(TINYINT)
