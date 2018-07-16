from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbSuspiciousLogSummaryToday2(Base):
    __tablename__ = 'tb_SuspiciousLogSummaryToday_2'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Date = Column(DATETIME)
    ProductGUID = Column(CHAR(36))
    InterestedIP_ID = Column(INTEGER)
    Count_H = Column(INTEGER)
    Count_M = Column(INTEGER)
    Count_L = Column(INTEGER)
    Count_I = Column(INTEGER)
