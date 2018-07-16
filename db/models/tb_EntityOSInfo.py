from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, SMALLINT, VARCHAR


class TbEntityOSInfo(Base):
    __tablename__ = 'tb_EntityOSInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EntityGuid = Column(CHAR(36), nullable=False)
    OS_Type = Column(VARCHAR(8))
    OS_MajorVersion = Column(SMALLINT)
    OS_MinorVersion = Column(SMALLINT)
    OS_ProductType = Column(SMALLINT)
