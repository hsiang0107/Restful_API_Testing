from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, NVARCHAR


class TbReportTempTable(Base):
    __tablename__ = 'tb_ReportTempTable'
    EntityID = Column(CHAR(36), primary_key=True)
    EntityName = Column(NVARCHAR(256))
