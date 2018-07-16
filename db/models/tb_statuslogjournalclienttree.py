from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR


class Tbstatuslogjournalclienttree(Base):
    __tablename__ = 'tb_statuslogjournalclienttree'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ClientTreePath = Column(NVARCHAR(1000))
    SLF_RealParentGuid = Column(CHAR(36))
    lutontmcm = Column(DATETIME)
