from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbBIFWeeklyLogInfo(Base):
    __tablename__ = 'tb_BIFWeeklyLogInfo'
    LogType = Column(VARCHAR(50), primary_key=True, nullable=False)
    Count = Column(INTEGER)
    LogDate = Column(DATETIME)
