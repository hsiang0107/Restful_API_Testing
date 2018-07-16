from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, NVARCHAR


class TbADVirtualUser(Base):
    __tablename__ = 'tb_AD_VirtualUser'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
    SAMAccountName = Column(NVARCHAR(64), nullable=False)
    Domain = Column(NVARCHAR(256), nullable=False)
    UnReferTimestamp = Column(DATETIME)
    CMGuid = Column(CHAR(36))
