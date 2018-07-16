from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR


class TbReportSubscriptionToTemplates(Base):
    __tablename__ = 'tb_ReportSubscriptionToTemplates'
    RPT_SubscriptionID = Column(CHAR(36), primary_key=True, nullable=False)
    RPT_TemplateID = Column(CHAR(36), primary_key=True, nullable=False)
