from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbLogPurgeCounter(Base):
    __tablename__ = 'tb_LogPurgeCounter'
    CLF_MsgLogType = Column(INTEGER, primary_key=True, nullable=False)
    LPC_LogCounter = Column(INTEGER, nullable=False)
    LPC_IsLogPurged = Column(BIT)
    LPC_YEAR = Column(INTEGER, nullable=False)
    LPC_MONTH = Column(INTEGER, nullable=False)
    LPC_DAY = Column(INTEGER, nullable=False)
