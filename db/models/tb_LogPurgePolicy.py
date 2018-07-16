from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbLogPurgePolicy(Base):
    __tablename__ = 'tb_LogPurgePolicy'
    CLF_MsgLogType = Column(INTEGER, primary_key=True, nullable=False)
    LPP_EnabledAutoPurge = Column(BIT)
    LPP_MaximumLogsToKeep = Column(INTEGER, nullable=False)
    LPP_PurgeLogsPerOnce = Column(INTEGER, nullable=False)
    LPP_DaysToKeepLogs = Column(INTEGER, nullable=False)
    LPP_PurgeOffset = Column(INTEGER)
