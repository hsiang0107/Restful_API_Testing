from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbLogBehaviorMonitorDetail(Base):
    __tablename__ = 'tb_LogBehaviorMonitorDetail'
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
    BM_PolicyID = Column(VARCHAR(16))
    CE_FilterID = Column(VARCHAR(35))
