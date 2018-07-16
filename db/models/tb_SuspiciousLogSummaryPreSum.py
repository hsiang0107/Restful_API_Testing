from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbSuspiciousLogSummaryPreSum(Base):
    __tablename__ = 'tb_SuspiciousLogSummaryPreSum'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProductGUID = Column(CHAR(36))
    InterestedIP_ID = Column(INTEGER)
    Count_H6Days = Column(INTEGER)
    Count_H13Days = Column(INTEGER)
    Count_H29Days = Column(INTEGER)
    Count_H89Days = Column(INTEGER)
    Count_M6Days = Column(INTEGER)
    Count_L6Days = Column(INTEGER)
    Count_I6Days = Column(INTEGER)
