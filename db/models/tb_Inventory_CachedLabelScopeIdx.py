from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbInventoryCachedLabelScopeIdx(Base):
    __tablename__ = 'tb_Inventory_CachedLabelScopeIdx'
    id = Column(INTEGER, primary_key=True, nullable=False)
    LabelID = Column(VARCHAR(64))
    UserGUID = Column(CHAR(36))
    CacheScopeStartID = Column(INTEGER)
    CacheScopeEndID = Column(INTEGER)
    LastUpdateTime = Column(DATETIME)
