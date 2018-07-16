from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, SMALLINT


class TbstatuslogjournalScanningInfo(Base):
    __tablename__ = 'tb_statuslogjournalScanningInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36))
    ScanningType = Column(SMALLINT, nullable=False)
    LastUpdateUTCTime = Column(DATETIME, nullable=False)
