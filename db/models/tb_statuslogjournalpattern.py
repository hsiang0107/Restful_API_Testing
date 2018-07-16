from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, SMALLINT


class Tbstatuslogjournalpattern(Base):
    __tablename__ = 'tb_statuslogjournalpattern'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36))
    SLF_DaylightSavingInMins = Column(INTEGER)
    SLF_Name = Column(INTEGER)
    SLF_Version = Column(CHAR(19))
    SLF_LastUpdateTime = Column(DATETIME)
    SLF_IsInUse = Column(SMALLINT)
    lutontmcm = Column(DATETIME)
