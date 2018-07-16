from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbSecurityViolationsSummary(Base):
    __tablename__ = 'tb_SecurityViolations_Summary'
    MsgLogID = Column(CHAR(36), primary_key=True)
    CLF_EntityID = Column(CHAR(36), nullable=False)
    CLF_LogReceivedTime = Column(DATETIME, nullable=False)
    ESV_IP = Column(VARCHAR(256), nullable=False)
    ESV_MAC = Column(VARCHAR(17), nullable=False)
    ESV_Policy = Column(NVARCHAR(64), nullable=False)
    SVS_ID = Column(INTEGER, nullable=False)
    ESV_HostName = Column(NVARCHAR(256))
    ESV_UserName = Column(NVARCHAR(64))
    is_summary_mapped = Column(INTEGER)
