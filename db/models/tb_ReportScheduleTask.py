from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbReportScheduleTask(Base):
    __tablename__ = 'tb_ReportScheduleTask'
    RPT_ReportTaskID = Column(CHAR(36), primary_key=True)
    RPT_TemplateID = Column(INTEGER)
    RPT_ScheduleCreateDate = Column(DATETIME)
    RPT_Recurrence = Column(INTEGER)
    RPT_EveryX = Column(INTEGER)
    RPT_IssueDateInX = Column(INTEGER)
    RPT_StartDate = Column(DATETIME)
    RPT_EndDate = Column(DATETIME)
    RPT_SubmitDateTime = Column(DATETIME)
    RPT_LatestSubmitTimet = Column(DATETIME)
    RPT_NextSubmitTime = Column(DATETIME)
    RPT_IssueUser = Column(NVARCHAR(256))
    RPT_CreateSchedulerUser = Column(NVARCHAR(256))
    RPT_Format = Column(INTEGER)
    RPT_ParameterTemplate = Column(IMAGE)
    RPT_NodeInfo = Column(IMAGE)
    RPT_DateRangeType = Column(INTEGER)
    RPT_LastSubmitTimeStmp = Column(DATETIME)
    RPT_IsAutoPurged = Column(INTEGER)
    RPT_AutoPurgeNumber = Column(INTEGER)
    RPT_Stop = Column(INTEGER)
    RPT_IsUseCalendarDay = Column(INTEGER)
    RPT_IP_SettingType = Column(INTEGER)
    RPT_IP_FIELD_1 = Column(VARCHAR(256))
    RPT_IP_FIELD_2 = Column(VARCHAR(256))
