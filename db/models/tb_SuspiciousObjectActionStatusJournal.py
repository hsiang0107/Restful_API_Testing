from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, TINYINT


class TbSuspiciousObjectActionStatusJournal(Base):
    __tablename__ = 'tb_SuspiciousObjectActionStatusJournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SourceType = Column(TINYINT, nullable=False)
    SeqID = Column(BIGINT, nullable=False)
    Date = Column(DATETIME, nullable=False)
    OldStatus = Column(TINYINT)
