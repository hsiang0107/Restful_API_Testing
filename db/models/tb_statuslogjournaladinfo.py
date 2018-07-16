from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR


class Tbstatuslogjournaladinfo(Base):
    __tablename__ = 'tb_statuslogjournaladinfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ADDomainName = Column(NVARCHAR(4000))
    SLF_ADObjectGuid = Column(CHAR(36))
    lutontmcm = Column(DATETIME)
