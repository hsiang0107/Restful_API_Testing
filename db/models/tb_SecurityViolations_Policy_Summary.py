from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, NVARCHAR, VARCHAR


class TbSecurityViolationsPolicySummary(Base):
    __tablename__ = 'tb_SecurityViolations_Policy_Summary'
    MsgLogID = Column(CHAR(36), primary_key=True)
    CLF_EntityID = Column(CHAR(36), nullable=False)
    CLF_LogReceivedTime = Column(DATETIME, nullable=False)
    ESV_IP = Column(VARCHAR(256), nullable=False)
    ESV_Policy = Column(NVARCHAR(64), nullable=False)
