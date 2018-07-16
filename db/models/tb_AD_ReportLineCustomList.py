from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbADReportLineCustomList(Base):
    __tablename__ = 'tb_AD_ReportLineCustomList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    DisplayName = Column(NVARCHAR(1024))
    Color = Column(NVARCHAR(10))
    GUID = Column(CHAR(36), nullable=False)
    ParentGUID = Column(CHAR(36))
    Type = Column(SMALLINT, nullable=False)
    CreatorGuid = Column(CHAR(36))
    LastModificationTime = Column(DATETIME)
