from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR


class TbTotalSecurityLogByRecipient(Base):
    __tablename__ = 'tb_TotalSecurityLogByRecipient'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    Mail = Column(NVARCHAR(450))
    HighSeverity = Column(INTEGER, nullable=False)
    MediumSeverity = Column(INTEGER, nullable=False)
    LowSeverity = Column(INTEGER, nullable=False)
    count_mlink = Column(INTEGER, nullable=False)
    count_mattach = Column(INTEGER, nullable=False)
    TotalCount = Column(INTEGER, nullable=False)
    LastDetectionTime = Column(DATETIME)
    TSC_SummaryTime = Column(DATETIME)
