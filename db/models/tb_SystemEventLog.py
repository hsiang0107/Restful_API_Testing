from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR


class TbSystemEventLog(Base):
    __tablename__ = 'tb_SystemEventLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Time = Column(DATETIME, nullable=False)
    EventType = Column(INTEGER, nullable=False)
    Result = Column(INTEGER, nullable=False)
    Description = Column(NVARCHAR(1024))
