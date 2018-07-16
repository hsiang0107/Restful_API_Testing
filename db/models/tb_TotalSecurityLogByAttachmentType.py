from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, VARCHAR


class TbTotalSecurityLogByAttachmentType(Base):
    __tablename__ = 'tb_TotalSecurityLogByAttachmentType'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    AttachType = Column(VARCHAR(80))
    HighSeverity = Column(INTEGER, nullable=False)
    MediumSeverity = Column(INTEGER, nullable=False)
    LowSeverity = Column(INTEGER, nullable=False)
    TotalCount = Column(INTEGER, nullable=False)
    LastDetectionTime = Column(DATETIME)
    TSC_SummaryTime = Column(DATETIME)
