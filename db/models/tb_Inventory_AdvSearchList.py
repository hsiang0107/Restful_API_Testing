from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbInventoryAdvSearchList(Base):
    __tablename__ = 'tb_Inventory_AdvSearchList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    AdvSearchID = Column(VARCHAR(16))
    Name = Column(NVARCHAR(256), nullable=False)
    ResourceType = Column(VARCHAR(64), nullable=False)
    Creator = Column(CHAR(36), nullable=False)
    JSONStmt = Column(NVARCHAR, nullable=False)
    SQLStmt = Column(NVARCHAR, nullable=False)
    CacheSQLStmt = Column(NVARCHAR)
    LastModifyTime = Column(DATETIME)
    IsSystemDefaultFilter = Column(INTEGER)
