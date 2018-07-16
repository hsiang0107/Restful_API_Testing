from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, TINYINT


class TbEDBDailyTrending(Base):
    __tablename__ = 'tb_EDB_DailyTrending'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Date = Column(DATETIME)
    AccountID = Column(CHAR(36))
    ScopeID = Column(CHAR(36))
    CriticalThreat_1Day = Column(INTEGER)
    CriticalThreat_7Day = Column(INTEGER)
    CriticalThreat_14Day = Column(INTEGER)
    CriticalThreat_30Day = Column(INTEGER)
    AVCompliance = Column(TINYINT)
    DLPCompliance = Column(TINYINT)
