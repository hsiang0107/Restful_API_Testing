from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbReportTemplate(Base):
    __tablename__ = 'tb_ReportTemplate'
    RPT_TemplateID = Column(INTEGER, primary_key=True)
    RPT_GroupID = Column(INTEGER)
    RPT_TemplateName = Column(NVARCHAR(256))
    RPT_TemplatePathName = Column(NVARCHAR(512))
