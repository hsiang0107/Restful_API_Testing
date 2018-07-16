from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, NVARCHAR


class TbReportLabelScopeTmp(Base):
    __tablename__ = 'tb_ReportLabelScopeTmp'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
    ResourceType = Column(NVARCHAR(64))
