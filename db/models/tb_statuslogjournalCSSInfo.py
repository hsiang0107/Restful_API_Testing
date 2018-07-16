from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR, SMALLINT


class TbstatuslogjournalCSSInfo(Base):
    __tablename__ = 'tb_statuslogjournalCSSInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_CloudScanMode = Column(SMALLINT, nullable=False)
    SLF_CloudScanMethod = Column(SMALLINT, nullable=False)
    SLF_ScanServerSourcesHashes = Column(NVARCHAR(2048))
    lutontmcm = Column(DATETIME)
