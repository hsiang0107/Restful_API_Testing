from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, DATETIME, INTEGER


class TbInventoryDDESRetroScanMapping(Base):
    __tablename__ = 'tb_Inventory_DDESRetroScanMapping'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EventContent_MD5 = Column(BINARY(16), nullable=False)
    RetroScanData_MD5 = Column(BINARY(16), nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
