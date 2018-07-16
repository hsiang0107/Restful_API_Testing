from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbInventoryTagList(Base):
    __tablename__ = 'tb_Inventory_TagList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    TagID = Column(VARCHAR(16))
    TagName = Column(NVARCHAR(256), nullable=False)
    ResourceType = Column(VARCHAR(64), nullable=False)
    Creator = Column(CHAR(36), nullable=False)
    LastModifyTime = Column(DATETIME)
