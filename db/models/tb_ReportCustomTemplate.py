from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, NVARCHAR


class TbReportCustomTemplate(Base):
    __tablename__ = 'tb_ReportCustomTemplate'
    RPT_TemplateID = Column(CHAR(36), primary_key=True, nullable=False)
    RPT_TemplateName = Column(NVARCHAR(256), nullable=False)
    RPT_TemplateDescription = Column(NVARCHAR(256))
    RPT_TemplateLocation = Column(NVARCHAR(512), nullable=False)
    RPT_Creator = Column(NVARCHAR(256))
    RPT_CreatedDate = Column(DATETIME)
    RPT_ModifiedUser = Column(NVARCHAR(256))
    RPT_LastUpdatedDate = Column(DATETIME)
