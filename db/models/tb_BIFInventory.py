from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BIT, CHAR, DATETIME, NVARCHAR


class TbBIFInventory(Base):
    __tablename__ = 'tb_BIFInventory'
    id = Column(BIGINT, primary_key=True, nullable=False)
    ViewName = Column(NVARCHAR(256))
    ResourceType = Column(NVARCHAR(256))
    IsDrillDown = Column(BIT)
    UserGuid = Column(CHAR(36))
    EventTime = Column(DATETIME)
