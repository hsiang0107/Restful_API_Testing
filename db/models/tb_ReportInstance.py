from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR


class TbReportInstance(Base):
    __tablename__ = 'tb_ReportInstance'
    RPT_InstanceID = Column(CHAR(36), primary_key=True, nullable=False)
    RPT_SubscriptionID = Column(CHAR(36), nullable=False)
    RPT_Name = Column(NVARCHAR(256), nullable=False)
    RPT_IsSchedule = Column(INTEGER, nullable=False)
    RPT_OutputFormat = Column(INTEGER, nullable=False)
    RPT_DateFrom = Column(DATETIME)
    RPT_DateTo = Column(DATETIME)
    RPT_SubmittedTime = Column(DATETIME)
    RPT_CompletedTime = Column(DATETIME)
    RPT_InstanceLocation = Column(NVARCHAR(256))
    RPT_Status = Column(INTEGER, nullable=False)
    RPT_Size = Column(INTEGER)
    RPT_TemplateInstance = Column(IMAGE)
    RPT_CasSendFlag = Column(INTEGER)
    RPT_CMServerID = Column(CHAR(36))
    RPT_OutputOrientation = Column(INTEGER)
