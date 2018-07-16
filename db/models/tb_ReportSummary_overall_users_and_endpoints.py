from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER


class TbReportSummaryoverallusersandendpoints(Base):
    __tablename__ = 'tb_ReportSummary_overall_users_and_endpoints'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SummaryTime = Column(DATETIME, nullable=False)
    TotalUserCount = Column(INTEGER, nullable=False)
    TotalEndpointCount = Column(INTEGER, nullable=False)
    TotalManagedEndpintCount = Column(INTEGER, nullable=False)
    CreateTime = Column(DATETIME, nullable=False)
