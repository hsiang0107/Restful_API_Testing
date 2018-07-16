from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, NVARCHAR


class TbRedAlert(Base):
    __tablename__ = 'tb_RedAlert'
    RA_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RA_Temporary = Column(BIT)
    RA_IssuedTime = Column(DATETIME)
    RA_CreatorName = Column(NVARCHAR(256))
    RA_TamID = Column(CHAR(36))
    RA_Closed = Column(BIT)
    RA_ClosedTime = Column(DATETIME)
    RA_ScheduleDownloadID = Column(CHAR(36))
    RA_IsAutoStop = Column(BIT)
    RA_PlannedStopTime = Column(DATETIME)
