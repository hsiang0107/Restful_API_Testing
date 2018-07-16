from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbInventoryWISInfo(Base):
    __tablename__ = 'tb_Inventory_WISInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Category = Column(VARCHAR(16))
    Score = Column(SMALLINT)
    DetectionName = Column(VARCHAR(256))
    ThreatName = Column(NVARCHAR(256), nullable=False)
    LUT = Column(DATETIME, nullable=False)
