from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import NVARCHAR, VARCHAR


class TbInventoryTagScope(Base):
    __tablename__ = 'tb_Inventory_TagScope'
    TagID = Column(VARCHAR(16))
    ObjectID = Column(NVARCHAR(64), primary_key=True, nullable=False)
