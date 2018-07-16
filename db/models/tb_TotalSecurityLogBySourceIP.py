from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, VARCHAR


class TbTotalSecurityLogBySourceIP(Base):
    __tablename__ = 'tb_TotalSecurityLogBySourceIP'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    SourceIP = Column(VARCHAR(256))
    HighSeverity = Column(INTEGER, nullable=False)
    MediumSeverity = Column(INTEGER, nullable=False)
    LowSeverity = Column(INTEGER, nullable=False)
    count_mlink = Column(INTEGER, nullable=False)
    count_mattach = Column(INTEGER, nullable=False)
    TotalCount = Column(INTEGER, nullable=False)
    SLF_Country = Column(VARCHAR(128))
    SLF_City = Column(VARCHAR(128))
    LastDetectionTime = Column(DATETIME)
    TSC_SummaryTime = Column(DATETIME)
