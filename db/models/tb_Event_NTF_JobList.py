from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbEventNTFJobList(Base):
    __tablename__ = 'tb_Event_NTF_JobList'
    JOBID = Column(CHAR(36), primary_key=True, nullable=False)
    USER_ID = Column(VARCHAR(38))
    Entity_ID = Column(VARCHAR(38))
    Event_ID = Column(VARCHAR(64))
    ComponentID = Column(VARCHAR(64))
    CLF_ProductType = Column(INTEGER, nullable=False)
    CLF_ProductName = Column(VARCHAR(128))
    CLF_ProductVersion = Column(VARCHAR(21))
    CLF_LogGenerationTime = Column(DATETIME)
    CLF_LogGenerationTimeZone = Column(INTEGER)
    CLF_ComputerName = Column(NVARCHAR(128))
    ELF_TrackingID = Column(CHAR(36))
    ELF_OriginalMesssage = Column(VARCHAR(128))
    ELF_StatusResult = Column(INTEGER)
    NJL_TaskState = Column(INTEGER)
    NJL_RetryTime = Column(INTEGER)
    NJL_FailMethod = Column(INTEGER)
    Result = Column(INTEGER)
    ProductInternalMessage = Column(VARCHAR(512))
    ANJ_RedAlertID = Column(CHAR(36))
    VOA_YEAR = Column(INTEGER, nullable=False)
    VOA_MONTH = Column(INTEGER, nullable=False)
    VOA_DAY = Column(INTEGER, nullable=False)
    SLF_UpdateInfo = Column(NVARCHAR(256))
    CLF_IsDayLightSaving = Column(INTEGER)
