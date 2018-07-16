from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR


class TbTotalSecurityLogByAttachmentName(Base):
    __tablename__ = 'tb_TotalSecurityLogByAttachmentName'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    Attach_name = Column(NVARCHAR(2048))
    HighSeverity = Column(INTEGER, nullable=False)
    MediumSeverity = Column(INTEGER, nullable=False)
    LowSeverity = Column(INTEGER, nullable=False)
    TotalCount = Column(INTEGER, nullable=False)
    LastDetectionTime = Column(DATETIME)
    TSC_SummaryTime = Column(DATETIME)
