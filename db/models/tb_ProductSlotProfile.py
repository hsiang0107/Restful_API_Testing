from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, VARCHAR


class TbProductSlotProfile(Base):
    __tablename__ = 'tb_ProductSlotProfile'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    ProductCode = Column(VARCHAR(2), nullable=False)
    APName = Column(VARCHAR(2), nullable=False)
    OSVersion = Column(VARCHAR(2), nullable=False)
