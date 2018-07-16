from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbReportItemTracking(Base):
    __tablename__ = 'tb_ReportItemTracking'
    RPT_ItemID = Column(CHAR(36))
    RPT_CMServerID = Column(CHAR(36))
    RPT_ID = Column(CHAR(36), primary_key=True)
    RPT_TemplateID = Column(INTEGER)
    RPT_SubmitDateTime = Column(DATETIME)
    RPT_StartDateTime = Column(DATETIME)
    RPT_LatestUpdateDateTime = Column(DATETIME)
    RPT_IsComplete = Column(INTEGER)
    RPT_Name = Column(NVARCHAR(512))
    RPT_Status = Column(INTEGER)
    RPT_IssueUser = Column(NVARCHAR(512))
    RPT_Format = Column(INTEGER)
    RPT_DateFrom = Column(DATETIME)
    RPT_DateTo = Column(DATETIME)
    RPT_CasSendFlag = Column(INTEGER)
