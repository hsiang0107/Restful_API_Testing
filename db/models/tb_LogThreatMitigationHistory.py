from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbLogThreatMitigationHistory(Base):
    __tablename__ = 'tb_LogThreatMitigationHistory'
    MsgLogID = Column(CHAR(36), primary_key=True, nullable=False)
    Sequence = Column(INTEGER, nullable=False)
    ActiveAction = Column(INTEGER)
    ResourceType = Column(INTEGER)
    Resource = Column(NVARCHAR(254))
    ActionResult = Column(INTEGER)
    Threat = Column(NVARCHAR(254))
    ThreatType = Column(NVARCHAR(254))
