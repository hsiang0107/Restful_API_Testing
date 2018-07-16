from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, VARCHAR


class Tbstatuslogjournalcommon(Base):
    __tablename__ = 'tb_statuslogjournalcommon'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_IPAddressList = Column(VARCHAR(1024))
    SLF_MACAddressList = Column(VARCHAR(256))
    lutontmcm = Column(DATETIME)
