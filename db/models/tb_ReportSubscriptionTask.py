from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, SMALLINT


class TbReportSubscriptionTask(Base):
    __tablename__ = 'tb_ReportSubscriptionTask'
    RPT_SubscriptionID = Column(CHAR(36), primary_key=True, nullable=False)
    RPT_SubscriptionName = Column(NVARCHAR(256), nullable=False)
    RPT_TemplateVersion = Column(INTEGER, nullable=False)
    RPT_CreatedDate = Column(DATETIME)
    RPT_LastSubmittedDate = Column(DATETIME)
    RPT_NextSubmitDate = Column(DATETIME)
    RPT_EntityInfos = Column(IMAGE)
    RPT_OutputFormat = Column(INTEGER)
    RPT_Frequency = Column(INTEGER, nullable=False)
    RPT_FrequencyEveryX = Column(INTEGER, nullable=False)
    RPT_FrequencyOption = Column(INTEGER, nullable=False)
    RPT_IsUseCalendarDay = Column(SMALLINT)
    RPT_EnableAttachment = Column(SMALLINT, nullable=False)
    RPT_Recipients = Column(IMAGE)
    RPT_Issuer = Column(NVARCHAR(256), nullable=False)
    RPT_TaskStatus = Column(SMALLINT, nullable=False)
    RPT_Params = Column(IMAGE)
    RPT_Creator = Column(NVARCHAR(256), nullable=False)
    RPT_CasSendFlag = Column(INTEGER)
    RPT_CMServerID = Column(CHAR(36))
    RPT_Description = Column(NVARCHAR(256))
    RPT_LastSubmitTimeStamp = Column(DATETIME)
    RPT_NotificationSubject = Column(NVARCHAR(256))
    RPT_NotificationBody = Column(NVARCHAR(2048))
    RPT_OutputOrientation = Column(INTEGER)
