from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbReportDelQueue(Base):
    __tablename__ = 'tb_ReportDelQueue'
    RPT_ID = Column(CHAR(36), primary_key=True)
    RPT_SubmitTime = Column(DATETIME)
    RPT_Type = Column(INTEGER)
    RPT_Status = Column(INTEGER)
