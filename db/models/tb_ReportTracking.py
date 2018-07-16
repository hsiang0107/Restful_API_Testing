from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbReportTracking(Base):
    __tablename__ = 'tb_ReportTracking'
    RPT_ID = Column(CHAR(36), primary_key=True)
    RPT_CMServerID = Column(CHAR(36))
    RPT_TemplateID = Column(INTEGER)
    RPT_SubmitDateTime = Column(DATETIME)
    RPT_LatestUpdateDateTime = Column(DATETIME)
    RPT_Name = Column(NVARCHAR(512))
    RPT_IssueUser = Column(NVARCHAR(512))
    RPT_MailList = Column(IMAGE)
    RPT_Format = Column(INTEGER)
    RPT_IsSchedule = Column(INTEGER)
    RPT_IsNeedAttacheInMail = Column(INTEGER)
    RPT_DateFrom = Column(DATETIME)
    RPT_DateTo = Column(DATETIME)
    RPT_Title = Column(NVARCHAR(256))
    RPT_Description = Column(NVARCHAR(256))
    RPT_NodeInfo = Column(IMAGE(256))
    RPT_CasSendFlag = Column(INTEGER)
    RPT_IsAggReport = Column(INTEGER)
    RPT_LatestModifyTime = Column(DATETIME)
    RPT_LatestModifyUser = Column(NVARCHAR(64))
    RPT_NewTemplatesName = Column(IMAGE)
    RPT_IP_SettingType = Column(INTEGER)
    RPT_IP_FIELD_1 = Column(VARCHAR(256))
    RPT_IP_FIELD_2 = Column(VARCHAR(256))
