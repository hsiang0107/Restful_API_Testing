from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbLogBehaviorMonitorFromChildCM(Base):
    __tablename__ = 'tb_LogBehaviorMonitor_FromChildCM'
    IDX = Column(INTEGER, primary_key=True, nullable=False)
    id = Column(INTEGER)
    MsgLogGUID = Column(UNIQUEIDENTIFIER)
    CMGuid = Column(CHAR(36))
    ProductGUID = Column(CHAR(36), nullable=False)
    LogMinorVersion = Column(SMALLINT)
    LogVersion = Column(SMALLINT)
    MsgType = Column(INTEGER, nullable=False)
    ComputerName = Column(NVARCHAR(128))
    DaylightSavingInMins = Column(INTEGER)
    TimeZoneInMins = Column(SMALLINT)
    CLF_LogReceivedTime = Column(DATETIME)
    Endpoint = Column(NVARCHAR(128))
    EndpointIP = Column(VARCHAR(256))
    LogReferenceID = Column(INTEGER)
