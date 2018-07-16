from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME


class TbMDRManagedProductList(Base):
    __tablename__ = 'tb_MDR_ManagedProductList'
    GUID = Column(CHAR(36), primary_key=True)
    Enabled = Column(BIT)
    Registered = Column(BIT)
    LastModifiedTime = Column(DATETIME)
