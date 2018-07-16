from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER


class TbLogBehaviorMonitorDetailFromChildCM(Base):
    __tablename__ = 'tb_LogBehaviorMonitorDetail_FromChildCM'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER)
    MsgLogGUID = Column(UNIQUEIDENTIFIER, primary_key=True)
    LogGenLocalDatetime = Column(DATETIME, nullable=False)
    SLF_Action = Column(INTEGER)
    TranslatedAction = Column(INTEGER)
    EventType = Column(INTEGER)
    RiskLevel = Column(INTEGER)
    PolicyID = Column(INTEGER)
    BehaviorCategory = Column(SMALLINT)
    AegisSubject = Column(NVARCHAR(1024))
    AegisOperation = Column(INTEGER)
    TranslatedAegisOperation = Column(INTEGER)
    AegisObject = Column(NVARCHAR(1024))
