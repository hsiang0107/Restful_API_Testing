from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbProductSlot(Base):
    __tablename__ = 'tb_ProductSlot'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    ProductType = Column(INTEGER, nullable=False)
    ProductVersion = Column(VARCHAR(19))
    MenuVersion = Column(VARCHAR(8))
    SlotID = Column(INTEGER, nullable=False)
    CommandType = Column(INTEGER)
