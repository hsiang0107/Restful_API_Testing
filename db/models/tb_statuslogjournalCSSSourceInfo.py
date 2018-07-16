from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, VARCHAR


class TbstatuslogjournalCSSSourceInfo(Base):
    __tablename__ = 'tb_statuslogjournalCSSSourceInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_CloudScanServerSourceHash = Column(BIGINT)
    SLF_CloudScanServerSource = Column(VARCHAR(2048))
    lutontmcm = Column(DATETIME)
