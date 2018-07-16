from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbInventoryLabelList(Base):
    __tablename__ = 'tb_Inventory_LabelList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    LabelID = Column(VARCHAR(64))
    LabelName = Column(NVARCHAR(256))
    ItemID = Column(VARCHAR(16), nullable=False)
    ItemType = Column(SMALLINT, nullable=False)
    ResourceType = Column(VARCHAR(64), nullable=False)
    UserGuid = Column(CHAR(36), nullable=False)
    LastModifyTime = Column(DATETIME, nullable=False)
    LabelAddedBy = Column(VARCHAR(256))
