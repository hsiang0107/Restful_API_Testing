from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbInventoryCachedLabelScope(Base):
    __tablename__ = 'tb_Inventory_CachedLabelScope'
    id = Column(INTEGER, primary_key=True, nullable=False)
    GUID = Column(CHAR(36))
    ResourceType = Column(VARCHAR(64), nullable=False)
