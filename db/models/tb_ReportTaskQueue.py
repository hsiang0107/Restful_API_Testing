from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbReportTaskQueue(Base):
    __tablename__ = 'tb_ReportTaskQueue'
    RPT_ID = Column(CHAR(36), primary_key=True)
    RPT_GenDate = Column(DATETIME)
    RPT_IssueUser = Column(NVARCHAR(256))
    RPT_RetryCount = Column(INTEGER)
    RPT_LoginToken = Column(VARCHAR(1024))
    RPT_NodeInfo = Column(IMAGE)
    RPT_ParameterTemplate = Column(IMAGE)
    RPT_MailList = Column(IMAGE)
    RPT_IsNeedAttacheInMail = Column(INTEGER)
